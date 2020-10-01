from django.contrib.auth import SESSION_KEY
from django.test import RequestFactory, TestCase

from users.models import CustomUser
from users.views import registration_view, account_view


class ViewsTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = CustomUser.objects.create_user(first_name='Richie',
                                                   last_name='Rich',
                                                   email='richie@rich.com',
                                                   password='sybvEv-ravgi0-mopkov')

    def test_register(self):
        request = self.factory.get('/customer/details')
        request.user = self.user
        # request.user = AnonymousUser()
        response = registration_view(request)
        self.assertEqual(response.status_code, 200)

    def test_login(self, email='richie@rich.com', password='sybvEv-ravgi0-mopkov'):
        response = self.client.post('/login/', {
            'email': email,
            'password': password,
        })
        self.assertIn(SESSION_KEY, self.client.session)
        return response

    def test_logout(self):
        response = self.client.get('/logout/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(SESSION_KEY, self.client.session)

    def test_remove_user(self, email='richie@rich.com'):
        response = self.client.post('/delete_account/', {
            'email': email
        })
        self.assertEqual(response.status_code, 302)

    def test_account(self):
        request = self.factory.get('/customer/details')
        request.user = self.user
        response = account_view(request)
        self.assertEqual(response.status_code, 200)