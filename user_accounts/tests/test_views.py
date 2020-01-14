from django.test import TestCase
from unittest.mock import patch, call
from user_accounts.models import Token

class SendLoginEmailViewTest(TestCase):

    def test_redirects_to_home_page(self):
        response = self.client.post(
            '/user_accounts/send_login_email',
            data = {'email': 'olaniyitawakalt95test@gmail.com'}
        )
        self.assertRedirects(response, '/')

    @patch('user_accounts.views.send_mail')
    def test_sends_mail_to_address_from_post(self, mock_send_mail):
        self.client.post(
            '/user_accounts/send_login_email',
            data = {'email': 'olaniyitawakalt95test@gmail.com'}
        )

        self.assertEqual(mock_send_mail.called, True)
        (subject, body, from_email, to_list), kwargs = mock_send_mail.call_args
        self.assertEqual(subject,  'Your login link for Superlists')
        self.assertEqual(from_email,  'noreply@superlists')
        self.assertEqual(to_list,  ['olaniyitawakalt95test@gmail.com'])

    def test_adds_success_message(self):
        response = self.client.post(
            '/user_accounts/send_login_email',
            data = {'email': 'olaniyitawakalt95test@gmail.com'},
            follow = True
        )

        message = list(response.context['messages'])[0]
        self.assertEqual(
            message.message,
            "Check your email, we've sent you a link you can use to log in."
        )
        self.assertEqual(message.tags, "success")

    @patch('user_accounts.views.messages')
    def test_adds_success_message_with_mocks(self, mock_messages):
        response = self.client.post(
            '/user_accounts/send_login_email',
            data = {'email': 'olaniyitawakalt95test@gmail.com'}
        )

        expected = "Check your email, we've sent you a link you can use to log in."

        self.assertEqual(
            mock_messages.success.call_args,
            call(response.wsgi_request, expected),
        )


class LoginViewTest(TestCase):

    def test_redirects_to_home_page(self):
        response = self.client.get('/user_accounts/login?token=abcd123')
        self.assertRedirects(response, '/')

    def test_creates_token_associated_with_email(self):
        self.client.post(
            '/user_accounts/send_login_email',
            data = {'email': 'olaniyitawakalt95test@gmail.com'}
        )
        token = Token.objects.first()
        self.assertEqual(token.email, 'olaniyitawakalt95test@gmail.com')

    @patch('user_accounts.views.send_mail')
    def test_send_link_to_login_using_token_uid(self, mock_send_mail):
        self.client.post(
            '/user_accounts/send_login_email',
            data = {'email': 'olaniyitawakalt95test@gmail.com'}
        )

        token = Token.objects.first()
        expected_url = f'http://testserver/user_accounts/login?token={token.uid}'
        (subject, body, from_email, to_list), kwargs = mock_send_mail.call_args
        self.assertIn(expected_url, body)

    @patch('user_accounts.views.auth')
    def test_calls_authenticate_with_uid_from_get_request(self, mock_auth):
        self.client.get('/user_accounts/login?token=abcd123')
        self.assertEqual(
            mock_auth.authenticate.call_args,
            call(uid='abcd123')
        )
