import sys
sys.path.append(r'C:\Users\ELCOT\Desktop\Order_management')

from dao.IOrderManagementRepository import IOrderManagementRepository
from entity.Users import Users
from entity.Product import Product
from entity.Orders import Orders
from entity.OrderItems import OrderItems
from entity.Electronics import Electronics
from entity.Clothing import Clothing
from exception.UserNotFoundException import UserNotFoundException
from utill.DBConnUtil import DBConnUtil

class OrderProcessor(IOrderManagementRepository):
    def __init__(self):
        self.connection = DBConnUtil.get_connection()

    def createOrder(self,user: Users, products: list[Product]):
        cursor=self.connection.cursor()
        
        try:
            cursor.execute('select * from Users where user_id=?',(user.user_id))
            if not cursor.fetchone():
                print('User not found. Creating user...')

                cursor.execute('select isnull(max(user_id),0) from Users')
                max_user_id=cursor.fetchone()[0]
                user_id=max_user_id+1
                
                cursor.execute('insert into Users (user_id, username, password, role) values(?,?,?,?)',(user.user_id, user.username, user.password, user.role))

            cursor.execute('select isnull(max(order_id),0) from Orders')
            max_id=cursor.fetchone()[0]
            order_id=max_id+1
            
            cursor.execute('insert into Orders (order_id,user_id) values (?,?)',(order_id,user.user_id))

            
            for product in products:
                cursor.execute('select 1 from Product where productid=?',(product.productid))
                if cursor.fetchone():
                    print('product Id is already exist. Assiging new ID.')
                    cursor.execute('select isnull(max(user_id),0) from Users')
                    product.productid=cursor.fetchone()[0]+1
                
                cursor.execute('insert into Product(productid,productName,description,price,quantityInStock,type) values(?,?,?,?,?,?)',(product.productid,product.productName,product.description,product.price,product.quantityInStock,product.type))
                if isinstance(product, Electronics):
                    cursor.execute('insert into Electronics (productid,brand,warranty_period) values (?,?,?)',(product.productid,product.brand,product.warranty_period))
                elif isinstance(product, Clothing):
                    cursor.execute('insert into Clothing(productid,size,color) values (?,?,?)',(product.productid,product.size,product.color))

                cursor.execute('select isnull(max(order_item_id),0) from OrderItems')
                max_order_item_id=cursor.fetchone()[0]
                order_item_id=max_order_item_id+1

                cursor.execute('insert into OrderItems (order_item_id,order_id,productid) values (?,?,?)',(order_item_id,order_id,product.productid))
                

            self.connection.commit()
            print(f'Order {order_id} created for user ID {user.user_id}')

        except Exception as e:
            print('Error in creating order: ',e)


    def getOrderByUser(self,user: Users):
        cursor=self.connection.cursor()

        try:
            cursor.execute('select * from Users where user_id=?',(user.user_id))
            if not cursor.fetchone():
                raise UserNotFoundException ('User not found.')

            cursor.execute('select p.productid,p.productName,p.description,p.price,p.quantityInStock,p.type from Orders as o join OrderItems as oi on o.order_id=oi.order_id join Product as p on oi.productid=p.productid where o.user_id=?',
                        (user.user_id))
            rows=cursor.fetchall()
            if not rows:
                print(f'No orders found for User ID {user.user_id}')
            else:
                print('Product ordered: ')
                
                for p in rows:
                    print(f'Product ID: {p[0]}, Name: {p[1]}, Type: {p[5]}, Price: {p[3]}')


        except UserNotFoundException as ue:
            print(ue)

        except Exception as e:
            print(e)
                
    
    
