from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

from users import views
from users.forms import CustomUserCreationForm


# Create your tests here.

class CustomUserTests(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='TestUser',
            email='email@email.com',
            password='password'
        )
        self.assertEqual(user.username,'TestUser')
        self.assertEqual(user.email,'email@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username = 'superadmin',
            email = 'example@email.com',
            password='password'
        )
        self.assertEqual(admin_user.username, 'superadmin')
        self.assertEqual(admin_user.email,'example@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class CustomUserTests(TestCase):
    class SignupPageTests(TestCase):
        def setUp(self):
            url = reverse('signup')
            self.response = self.client.get(url)

        def test_signup_template(self):
            self.assertEqual(self.response, 'signup.html')
            self.assertContains(self.response, 'Sign Up')
            self.assertNotContains(
                self.response, 'Hi there! I should not be on the page'
            )
        def test_signup_form(self):
            form = self.response.context.get('form')
            self.assertIsInstance(form, CustomUserCreationForm)
            self.assertContains(self.response, 'csrfmiddlewaretoken')

        def test_signup_view(self):
            view = resolve('/accounts/signup/')
            self.assertEqual(
                view.func.__name__,
                views.SignupPageView.as_view().__name__
            )