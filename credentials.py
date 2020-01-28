class Credentials:
    """
    Class that generates new instances of credentials.
    """
    credentials_list = [] # Empty credentials list
    def __init__(self,login_username,password):
        # docstring removed for simplicity
        self.login_username = login_username
        self.password = password
    def save_credentials(self):
        '''
        save_credentials method saves credentials into the list
        '''
        Credentials.credentials_list.append(self)
    def delete_credentials(self):
        '''
        delete_credentials deletes credentials that is saved in the credentials_list
        '''
        Credentials.credentials_list.remove(self)
    @classmethod
    def find_by_password(cls,password):
        '''
        Method that takes in password and display the user that matches the password
        '''
        for credentials in cls.credentials_list:
            if credentials.password == password:
                return credentials
    @classmethod
    def credentials_exist(cls,password):
        '''
        Method that checks if the credentials exist in the credentials_list
        '''
        for credentials in cls.credentials_list:
            if credentials.password == password:
                return True
        return False
    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list