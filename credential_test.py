
import unittest
from credential import Credential

class TestCredential(unittest.TestCase):
   

    def setUp(self):
        

        
        self.new_credential = Credential("ali","moo","4545")

    def tearDown(self):
        
        Credential.credential_list = []

    def test_init(self):
       
        self.assertEqual( self.new_credential.user_password, "ali")
        self.assertEqual( self.new_credential.credential_name, "moo" )
        self.assertEqual( self.new_credential.credential_password, "4545" )

    def test_save_credential(self):
      

        self.new_credential.save_credential()

        self.assertEqual( len(Credential.credential_list), 1 )

    def test_save_multiple_credentials(self):
        

        
        self.new_credential.save_credential()

        test_credential = Credential("liin","lenovo","4646")

        test_credential.save_credential()

        self.assertEqual( len(Credential.credential_list), 2)

    def test_generate_password(self):
       
        
        generated_password = self.new_credential.generate_password()

        self.assertEqual( len(generated_password), 8 )   
    
    def test_display_credential(self):
       

        
        self.new_credential.save_credential()

        test_credential = Credential("liin","lenovo","4646")

        test_credential.save_credential()

        test_credential = Credential("liin","moo","4545")

        test_credential.save_credential()
        
        self.assertEqual( len(Credential.display_credential("liin")) , 2 )
        
    def test_credential_exist(self):
        
        

        
        self.new_credential.save_credential()

        test_credential = Credential("liin","lenovo","4646")

        test_credential.save_credential()
        
        
        credential_exists = Credential.credential_exist("lenovo")
        
        self.assertTrue(credential_exists)
        

# if __name__ == '__main__':
#     unittest.main()