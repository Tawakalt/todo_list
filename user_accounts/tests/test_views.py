from django.test import TestCase


class SendLoginEmailViewTest(TestCase):

    def test_redirects_to_home_page(self):
        response = self.client.post(
            '/user_accounts/send_login_email',
            data = {'email': 'olaniyitawakalt95test@gmail.com'}
        )
        self.assertRedirects(response, '/')
