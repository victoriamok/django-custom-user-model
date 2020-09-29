from django.test import TestCase
from django.contrib.auth import get_user_model


class UserManagersTests(TestCase):

    def test_create_user(self, **extra_fields):
        User = get_user_model()
        user = User.objects.create_user(
            email='normal@user.com', first_name='Ross', last_name='Geller', password='foo', **extra_fields
        )
        self.assertEqual(user.email, 'normal@user.com')
        # self.assertEqual(user.first_name, 'Ross')
        # self.assertEqual(user.last_name, 'Geller')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', first_name='', last_name='', password='foo')

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@user.me', password='foo')
        self.assertEqual(admin_user.email, 'super@user.me')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.me', password='foo', is_superuser=False)
