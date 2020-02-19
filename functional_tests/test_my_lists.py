from .base import FunctionalTest
from .server_tools import create_session_on_server


class MyListTest(FunctionalTest):

    def test_loggesd_in_users_lists_are_saved_as_my_lists(self):
        email = 'olaniyitawakalt95test@gmail.com'
        self.browser.get(self.live_server_url)
        self.wait_to_be_logged_out(email)

        # Edith is a logged in user
        self.create_pre_authenticated_session(email)
        self.browser.get(self.live_server_url)
        self.wait_to_be_logged_in(email)

    def test_logged_in_users_list_are_saved_as_my_list(self):
        # Edith is a logged in user
        self.create_pre_authenticated_session('ab@c.com')
        # She goes to the home page and starts a list
        self.browser.get(self.live_server_url)
        self.add_list_item("Take a course")
        self.add_list_item("Take a vacation")
        first_list_url = self.browser.current_url
        # She notices a "My List" link, for the first time.
        self.browser.find_element_by_link_text('My Lists').click()
        # She sees that her list is in there,
        # named according to its first list item
        self.wait_for(
            lambda: self.browser.find_element_by_link_text("Take a course")
        )
        self.browser.find_element_by_link_text("Take a course").click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, first_list_url)
        )
        # She decides to start another list just to see
        self.browser.get(self.live_server_url)
        self.add_list_item("Make dinner")
        second_list_url = self.browser.current_url
        # Under "My lists" her new list appears
        self.browser.find_element_by_link_text('My Lists').click()
        self.wait_for(
            lambda: self.browser.find_element_by_link_text("Make dinner")
        )
        self.browser.find_element_by_link_text("Make dinner").click()
        self.wait_for(
            lambda: self.assertEqual(self.browser.current_url, second_list_url)
        )
        # She logs out. The "My Lists" optin disappears
        self.browser.find_element_by_link_text('Log out').click()
        self.wait_for(lambda: self.assertFalse(
            'My Lists' in self.browser.page_source
        ))
