#--exception for invalid user

class UserNotFoundException(Exception):
    def __init__(self,message='User ID not found in the database'):
        super().__init__(message)
