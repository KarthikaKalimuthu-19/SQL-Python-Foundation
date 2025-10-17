import sys
sys.path.append(r'C:\Users\ELCOT\Desktop\Finance')

from entity.Users import Users
from entity.Product import Product
from entity.Electronics import Electronics
from entity.Clothing import Clothing
from entity.OrderItems import OrderItems
from entity.Orders import Orders
from dao.OrderProcessor import OrderProcessor
from exception.UserNotFoundException import UserNotFoundException


def main():
    processor = OrderProcessor()
    

    while True:
        print("\n------ Order Management Menu ------")
        print("1. Create Order")
        print("2. Get Orders by User")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                user_id = int(input("Enter User ID: "))
                username = input("Enter Username: ")
                password = input("Enter Password: ")
                role = input("Enter Role (Admin/User): ")

                user = Users(user_id, username, password, role)

                product_count = int(input("How many products to order? "))
                products = []

                for i in range(product_count):
                    print(f"\nEnter details for Product #{i+1}")
                    product_id = int(input("Product ID: "))
                    product_name = input("Product Name: ")
                    description = input("Description: ")
                    price = float(input("Price: "))
                    quantity = int(input("Quantity in Stock: "))
                    product_type = input("Type (Electronics/Clothing): ")

                    if product_type == 'Electronics':
                        brand=input('Enter brand: ')
                        warranty_period=int(input('Enter warranty period: '))

                        product=Electronics(product_id,product_name,description,price,quantity,brand,warranty_period)

                    elif product_type == 'Clothing':
                        size=input('Enter size: ')
                        color=input('Enter color: ')

                        product=Clothing(product_id,product_name,description,price,quantity,size,color)

                    else:
                        print('Invalid product type')
                        continue
                    
                    products.append(product)

                processor.createOrder(user, products)

            except Exception as e:
                print("Error during order creation:", e)

        elif choice == "2":
            try:
                user_id = int(input('Enter User ID to view orders: '))
                username = input('Enter Username: ')
                password = input('Enter password: ')
                role = input('Enter role(Admin/User): ')
                user = Users(user_id,username,password,role)

                processor.getOrderByUser(user)

            except UserNotFoundException as ue:
                print(ue)

            except Exception as e:
                print("Error fetching orders:", e)

        elif choice == "3":
            print("Exiting Order Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__=='__main__':
    main()
