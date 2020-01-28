import unittest
from credentials import Credentials
class TestUser(unittest.TestCase):
     '''
     Test class that defines test cases for the Credentials class behaviour
     Args:
         unittest.Testcase: TestCase class that helps in creating test cases
     '''
     def setUp(self):
         '''
         Set up method to run before each test cases.
         '''
         self.new_credentials = Credentials("Pj","private")
     def test_init(self):
         '''
         test_init test case to test if the object is properly initialized
         '''
         self.assertEqual(self.new_credentials.login_username,"Pj")
         self.assertEqual(self.new_credentials.password,"private")
     def test_save_credentials(self):
         '''
         test_save_credentials test case to test if credentials object can be saved into the credentials list
         '''
         self.new_credentials.save_credentials()
         self.assertEqual(len(Credentials.credentials_list),1)
     def tearDown(self):
         '''
         tearDown method that does clean up after each test case has run.
         '''
         Credentials.credentials_list = []
     def test_save_multiple_credentials(self):
         '''
         test_save_multiple_credentials to test if we can save a variety of credentials objects to the credentials_list
         '''
         self.new_credentials.save_credentials()
         test_credentials = Credentials("Pj", "private")
         test_credentials.save_credentials()
         self.assertEqual(len(Credentials.credentials_list),2)
     def test_delete_credentials(self):
         '''
         test_delete_credentials to test if we can remove credentials from a credential_list
         '''
         self.new_credentials.save_credentials()
         test_credentials = Credentials("Pj", "private")
         test_credentials.save_credentials()
         self.new_credentials.delete_credentials()
         self.assertEqual(len(Credentials.credentials_list),1)
     def test_find_user_by_password(self):
         '''
         Test to see if we can find a user by password and display information
         '''
         self.new_credentials.save_credentials()
         test_credentials = Credentials("Pj", "private")
         test_credentials.save_credentials()
         found_credentials = Credentials.find_by_password("private")
         self.assertEqual(found_credentials.login_username, test_credentials.login_username)
     def test_credentials_exists(self):
         '''
         test to check if we can return a boolean if credentials doesn't exist
         '''
         self.new_credentials.save_credentials()
         test_credentials = Credentials("Pj", "private")
         test_credentials.save_credentials()
         credentials_exists = Credentials.credentials_exist("private")
         self.assertTrue(credentials_exists)
     def test_display_all_credentials(self):
         '''
         method that returns a list of all credentials saved
         '''
         self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
if __name__ == '__main__':
     unittest.main()