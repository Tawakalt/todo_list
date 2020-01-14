from django.test import TestCase
from unittest.mock import patch

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

