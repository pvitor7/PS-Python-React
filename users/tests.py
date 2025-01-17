from .models import User
from django.test import TestCase
from django.db.utils import IntegrityError, DataError

class UserTestCase(TestCase):
    def setUp(self):
        self.valid_user_data = {
            "username": "User1",
            "password": "vsb972761",
            "email": "user1@mail.com",
            "cellphone": "021992248141"
        }

    def test_create_user_with_valid_data(self):
        user = User.objects.create_user(**self.valid_user_data)
        self.assertEqual(user.username, self.valid_user_data["username"])
        self.assertEqual(user.email, self.valid_user_data["email"])
        self.assertEqual(user.cellphone, self.valid_user_data["cellphone"])
    
    def test_create_user_with_duplicate_email(self):
        User.objects.create_user(**self.valid_user_data)
        with self.assertRaises(IntegrityError):
            User.objects.create_user(**self.valid_user_data)

    def test_create_user_with_duplicate_cellphone(self):
        User.objects.create_user(**self.valid_user_data)
        with self.assertRaises(IntegrityError):
            User.objects.create_user(**self.valid_user_data)
            
    def test_username_unique(self):
        User.objects.create_user(**self.valid_user_data)
        self.valid_user_data['email'] = 'janedoe@example.com'
        with self.assertRaises(IntegrityError):
            User.objects.create_user(**self.valid_user_data)
        
    def test_email_unique(self):
        User.objects.create_user(**self.valid_user_data)
        self.valid_user_data['username'] = 'janedoe'
        with self.assertRaises(IntegrityError):
            User.objects.create_user(**self.valid_user_data)
        
    def test_cellphone_unique(self):
        User.objects.create_user(**self.valid_user_data)
        self.valid_user_data['email'] = 'janedoe@example.com'
        with self.assertRaises(IntegrityError):
            User.objects.create_user(**self.valid_user_data)

    def test_username_max_length(self):
        self.valid_user_data['username'] = 'a' * 49
        with self.assertRaises(DataError):
            User.objects.create(**self.valid_user_data)
            
