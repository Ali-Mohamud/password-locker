import unittest
from user import User
from credential import Credential


class TestUser(unittest.TestCase):

    def setUp(self):

        self.new_user = User("ahmed","ali")


    def tearDown(self):

        User.user_list = []

    def test_init(self):

        self.assertEqual( self.new_user.user_name, "ahmed" )
        self.assertEqual( self.new_user.user_password, "ali" )

    def test_save_user(self):

        self.new_user.save_user()

        self.assertEqual( len(User.user_list), 1 )

    def test_save_multiple_users(self):

        self.new_user.save_user()

        test_user = User("mary","david")

        test_user.save_user()

        self.assertEqual( len(User.user_list), 2)

#     def test_find_credential(self):

#         self.new_user.save_user()

#         test_user = User("mary","david")

#         test_user.save_user()

#         found_credential = User.find_credential("moo")

#         self.assertEqual( found_credential, False )

#     def test_log_in(self):
#         self.new_user.save_user()

#         test_user = User("mary","david")

#         test_user.save_user()

#         found_credential = User.log_in("mary", "david")

#         self.assertEqual( found_credential,  Credential.credential_list )   
    
#     def test_display_user(self):
        
        
#         self.assertEqual( User.display_user() , User.user_list )
        
#     def test_user_exist(self):
        

#         self.new_user.save_user()

#         test_user = User("mary","david")

#         test_user.save_user()
        
#         user_exists = User.user_exist("mary")
        
#         self.assertTrue(user_exists)


# if __name__ == '__main__':
#     unittest.main()