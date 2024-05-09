from django.test import SimpleTestCase
from main.forms import CreateNewUser

class TestForms(SimpleTestCase):

    def test_CreateNewUser_valid_data(self):
        form = CreateNewUser(data={
            'username':'James',
            'email': 'james@gmail.com',
            'password1': 'spinningmonkeys',
            'password2': 'spinningmonkeys'
        })

        self.assertTrue(form.is_valid())

    def test_CreateNewUser_no_data(self):
        form = CreateNewUser(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)