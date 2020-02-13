#!/usr/bin/env python3.6
from user import User
from credentials import Credentials
def create_user(uname,fname,phone,email,password):
    '''
    Function to create a new user
    '''
    new_user = User(uname,fname,phone,email,password)
    return new_user
def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()
def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()
def find_user(password):
    '''
    Function that finds a user by password and returns the user
    '''
    return User.find_by_password(password)
def check_existing_user(password):
    '''
    Function that check if a contact exists with that number and return a Boolean
    '''
    return User.user_exist(password)
def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def main():
    print("Hello welcome to password locker. What is your name?")
    user_name = input()
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')
    while True:
                    print("Use these short codes : cc - create a new account, du - display user, fu -find a user, ex -exit the credentials list ")
                    short_code = input().lower()
                    if short_code == 'cc':
                            print("New User")
                            print("-"*10)
                            print ("User name ....")
                            u_name = input()
                            print("First name ...")
                            f_name = input()
                            print("Phone number ...")
                            p_number = input()
                            print("Email address ...")
                            e_address = input()
                            print("Password ...")
                            password = input()

                            save_user(create_user(u_name,f_name,p_number,e_address,password))
                            print ('\n')
                            print(f"New User {u_name} {f_name} created")
                            print ('\n')
                    elif short_code == 'du':
                            if display_users():
                                    print("Here is a list of all your users")
                                    print('\n')
                                    for user in display_users():
                                            print(f"{user.user_name} {user.first_name} .....{user.phone_number}")
                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any users saved yet")
                                    print('\n')
                    elif short_code == 'fu':
                            print("Enter the password")
                            search_password = input()
                            if check_existing_user(search_password):
                                    search_user = find_user(search_password)
                                    print(f"{search_user.user_name} {search_user.first_name}")
                                    print('-' * 20)
                                    print(f"Password.......{search_user.password}")
                                    print(f"Email address.......{search_user.email}")
                            else:
                                    print("That user does not exist")
                    elif short_code == "ex":
                            print("Thank you for your attempt")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':
    main()
