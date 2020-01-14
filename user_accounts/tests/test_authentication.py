from django.contrib.auth import get_user_model
from django.test import TestCase
from user_accounts.authentication import PasswordlessAuthenticationBackend
from user_accounts.models import Token

User = get_user_model()


class AuthenticateTest(TestCase):

    def test_returns_None_if_no_such_token(self):
        result = PasswordlessAuthenticationBackend().authenticate(
            'no-such-token'
        )
        self.assertIsNone(result)

    def test_returns_new_user_with_correct_email_if_token_extists(self):
        email = 'olaniyitawakalt95test@gmail.com'
        token = Token.objects.create(email=email)
        user = PasswordlessAuthenticationBackend().authenticate(token.uid)
        new_user = User.objects.get(email=email)
        self.assertEqual(user, new_user)

    def test_returns_existing_user_with_correct_email_if_user_exists(self):
        email = 'olaniyitawakalt95test@gmail.com'
        existing_user = User.objects.create(email=email)
        token = Token.objects.create(email=email)
        user = PasswordlessAuthenticationBackend().authenticate(token.uid)
        self.assertEqual(user, existing_user)


class GetUserTest(TestCase):

    def test_gets_user_by_email(self):
        User.objects.create(email='a@b.com')
        desired_user = User.objects.create(email='olaniyitawakalt95test@gmail.com')
        found_user = PasswordlessAuthenticationBackend().get_user(
            'olaniyitawakalt95test@gmail.com'
        )
        self.assertEqual(found_user, desired_user)

    def test_returns_None_if_no_user_with_that_email(self):
        self.assertIsNone(
            PasswordlessAuthenticationBackend().get_user('olaniyitawakalt95test@gmail.com')
        )