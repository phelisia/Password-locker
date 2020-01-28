class User:
    """
    Class that generates new instances of users.
    """

    user_list = []

    def __init__(self,user_name,first_name,number,email,password):

      # docstring removed for simplicity

        self.user_name = user_name
        self.first_name = first_name
        self.phone_number = number
        self.email = email
        self.password = password
        user_list = [] # Empty user list
 # Init method up here
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)
    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)
    @classmethod
    def find_by_password(cls,password):
        '''
        Method that takes in a password and returns a user that matches that password.

        Args:
            password: password to search for
        Returns :
            User that matches the password.
             '''

        for user in cls.user_list:
            if user.password == password:
                return user
    @classmethod
    def user_exist(cls,password):
        '''
        Method that checks if a user exists from the user_list.
        Args:
            password: password to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.users_list:
            if user.password == password:
                    return True

        return False  
    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list
     
