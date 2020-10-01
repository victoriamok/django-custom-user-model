from django.test import TestCase
from users.forms import CustomUserCreationForm


class UserCreationFormTest(TestCase):

    def test_registration_form(self):
        form = CustomUserCreationForm(data={'email': 'richie@rich.com',
                                            'first_name': 'Richie',
                                            'last_name': 'Rich',
                                            'password1': 'sybvEv-ravgi0-mopkov',
                                            'password2': 'sybvEv-ravgi0-mopkov'})
        self.assertTrue(form.is_valid())

        form = CustomUserCreationForm(data={'email': 'richie@rich',
                                            'first_name': 'Richie',
                                            'last_name': 'Rich',
                                            'password1': 'sybvEv-ravgi0-mopkov',
                                            'password2': 'sybvEv-ravgi0-mopkov'})
        self.assertFalse(form.is_valid())

        form = CustomUserCreationForm(data={'email': 'richie@rich.com',
                                            'first_name': '',
                                            'last_name': 'Rich',
                                            'password1': 'sybvEv-ravgi0-mopkov',
                                            'password2': 'sybvEv-ravgi0-mopkov'})
        self.assertFalse(form.is_valid())

        form = CustomUserCreationForm(data={'email': 'richie@rich.com',
                                            'first_name': 'Richie',
                                            'last_name': '',
                                            'password1': 'sybvEv-ravgi0-mopkov',
                                            'password2': 'sybvEv-ravgi0-mopkov'})
        self.assertFalse(form.is_valid())

        form = CustomUserCreationForm(data={'email': 'richie@rich',
                                            'first_name': 'Richie',
                                            'last_name': 'Rich',
                                            'password1': 'sybvEv',
                                            'password2': 'sybvEv'})
        self.assertFalse(form.is_valid())

        form = CustomUserCreationForm(data={'email': 'richie@rich',
                                            'first_name': 'Richie',
                                            'last_name': 'Rich',
                                            'password1': 'sybvEv-ravgi0-mopkov',
                                            'password2': 'sybvEv-ravgi0-mopkog'})
        self.assertFalse(form.is_valid())

