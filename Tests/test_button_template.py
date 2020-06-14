import unittest

from decouple import config
from messenger_bot.buttons.button_generator import Button
from messenger_bot.template.template_button import ButtonTemplate
from messenger_bot.utility.util import MessengerUtility

from Tests.send_message import Facebook


class TestButtonTemplate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.button = Button()
        cls.facebook = Facebook()
        cls.template = ButtonTemplate(config("test_facebook_user", None))
        cls.url = config("test_url", None)
        cls.postback_payload = "TestButtonTemplate-3"

    @classmethod
    def tearDownClass(cls):
        del cls.button
        del cls.facebook
        del cls.template

    def test_button_template_with_web_url(self):
        """
        Button Template test with Web URL buttons with default. 
        """
        buttons = list()
        for _ in range(0, 3):
            title = "Test 1 - {}".format(_)
            buttons.append(self.button.create_url_button(title, self.url))
        title_text = "test_button_template_with_web_url - Test 1 - {}".format(
            _)
        button_payload = self.template.button_template(title_text, buttons)
        status_code = self.facebook.send_message(button_payload)
        self.assertEqual(status_code, 200,
                         "test_button_template - web_url - Test 1")

    def test_2_button_template_with_web_url(self):
        """
        Button Template test with Web URL buttons with messenger_extension TRUE
        This function tests the default_action option with Button Template.
        """
        buttons = list()
        """
        TODO: whitelisting format changed!
        TODO: There has to be a good function for this feature!
        For this test, domain has been whitelisted from the page settings
        """
        # whitelist_payload = MessengerUtility.whitelist_domain(self.url)
        # status_code = self.facebook.send_message(whitelist_payload)
        # self.assertEqual(status_code, 200,
        #                  "test2_button_template web_url whitelist")

        title = "Test 2 - {}".format(1)
        buttons.append(self.button.create_url_button(
            title, self.url, messenger_extensions=True, fallback_url=self.url))
        title_text = "test_button_template_with_web_url - Test 2 - {}".format(
            1)
        button_payload = self.template.button_template(title_text, buttons)
        status_code = self.facebook.send_message(button_payload)
        self.assertEqual(status_code, 200, "test2_button_template web_url")

    def test_3_button_template_with_web_url(self):
        """
        ButtonTemplate WebURL test 3
        This test case wouldn't work.
        """
        buttons = list()
        title = "Test 3 - {}".format(1)
        buttons.append(self.button.create_url_button(title, None))
        self.assertEqual(type(buttons[0]), type(None), "Must be None")

        title_text = "test_button_template_with_web_url - Test 3 - {}".format(
            1)
        button_payload = self.template.button_template(title_text, buttons)
        status_code = self.facebook.send_message(button_payload)
        self.assertEqual(status_code, 400,
                         "test_button_template_with_web_url - Test 3 -> 400")

    def test_4_button_template_with_web_url(self):
        """
        ButtonTemplate test 4 with WEB_URL 
        It has multiple test cases. 
        """
        buttons = list()
        title = "Test 4 - {}".format(1)
        _ = "A" * 640
        _another = "A" * 40
        title += _another
        buttons.append(self.button.create_url_button(title, self.url))
        self.assertEqual(type(buttons[0]), type(dict()), "Must nt block")

        title_text = "test_button_template_with_web_url - Test 4 - {} --- {}".format(
            1, _)
        button_payload = self.template.button_template(title_text, buttons)
        status_code = self.facebook.send_message(button_payload)
        self.assertEqual(status_code, 400, "DO NOT work again!")

        for _ in range(0, 3):
            title = "Test 4 - {}".format(_)
            buttons.append(self.button.create_url_button(title, self.url))

        title_text = "test_button_template_with_web_url - Test 4 - {}".format(
            2)
        button_payload = self.template.button_template(title_text, buttons)
        status_code = self.facebook.send_message(button_payload)
        self.assertEqual(status_code, 400, "DO NOT work again!")

    def test_5_button_template_with_web_url(self):
        buttons = list()
        title = "Test 5 - {}".format(1)
        _another = "A" * 40
        title += _another
        buttons.append(self.button.create_url_button(title, self.url))
        self.assertEqual(type(buttons[0]), type(dict()), "Must nt block")
        title_text = "test_button_template_with_web_url - Test 5 - {}".format(
            1)
        button_payload = self.template.button_template(title_text, buttons)
        status_code = self.facebook.send_message(button_payload)
        self.assertEqual(status_code, 200, "Suppose to work again!")

    def test_6_button_template_with_postback(self):
        buttons = list()
        title = "Test 6 - {}".format(1)
        buttons.append(self.button.create_postback_button(
            title, self.postback_payload))
        self.assertEqual(type(buttons[0]), type(dict()), "Must nt block")
        title_text = "test_button_template_with_postback - Test 6 - {}".format(
            1)
        button_payload = self.template.button_template(title_text, buttons)
        status_code = self.facebook.send_message(button_payload)
        self.assertEqual(status_code, 200, "Suppose to work again!")

    def test_7_button_template_with_postback(self):
        buttons = list()
        title = "Test 7 - {}".format(1)
        title += ("A" * 20)
        buttons.append(self.button.create_postback_button(
            title, self.postback_payload))
        self.assertEqual(type(buttons[0]), type(dict()), "Must nt block")
        title_text = "test_button_template_with_postback - Test 7 - {}".format(
            1)
        button_payload = self.template.button_template(title_text, buttons)
        status_code = self.facebook.send_message(button_payload)
        self.assertEqual(status_code, 200, "Suppose to work again!")

    def test_8_button_template_with_postback(self):
        buttons = list()
        title = "Test 8 - {}".format(1)
        _postback_payload = self.postback_payload + ("A" * 2000)
        buttons.append(self.button.create_postback_button(
            title, _postback_payload))
        self.assertEqual(type(buttons[0]), type(None), "Must nt block")
        title_text = "test_button_template_with_postback - Test 8 - {}".format(
            1)
        button_payload = self.template.button_template(title_text, buttons)
        status_code = self.facebook.send_message(button_payload)
        self.assertEqual(status_code, 400, "Suppose to NOT work again!")

    def test_9_button_template_with_postback_and_web_url(self):
        buttons = list()
        title = "Test 9 Postback - {}".format(1)
        buttons.append(self.button.create_postback_button(
            title, self.postback_payload))
        self.assertEqual(type(buttons[0]), type(dict()), "Must nt block")
        for _ in range(0, 2):
            title = "Test 9 WebURL - {}".format(_)
            buttons.append(self.button.create_url_button(title, self.url))

        title_text = "test_button_template_with_postback - Test 9 - {}".format(
            1)
        button_payload = self.template.button_template(title_text, buttons)
        status_code = self.facebook.send_message(button_payload)
        self.assertEqual(status_code, 200, "Suppose to work again!")

    def test_10_button_template_with_call_button(self):
        buttons = list()
        title = "Test 10 Call button - {}".format(1)
        buttons.append(self.button.create_call_button(title, "+8801723130852"))
        self.assertEqual(type(buttons[0]), type(dict()), "Must nt block")

        title_text = "test_button_template_with_call_button - Test 10 - {}".format(
            1)
        button_payload = self.template.button_template(title_text, buttons)
        status_code = self.facebook.send_message(button_payload)
        self.assertEqual(status_code, 200, "Suppose to work again!")

    def test_11_button_template_with_call_button(self):
        buttons = list()
        title = "Test 11 Call button - {}".format(1)
        buttons.append(self.button.create_call_button(title, "01723130852"))
        self.assertEqual(type(buttons[0]), type(None), "Must block")

        title_text = "test_button_template_with_call_button - Test 11 - {}".format(
            1)
        button_payload = self.template.button_template(title_text, buttons)
        status_code = self.facebook.send_message(button_payload)
        self.assertEqual(status_code, 400, "Suppose to NOT work again!")

        buttons = list()
        title = "Test 11 Call button - {}".format(1)
        buttons.append(self.button.create_call_button(title, ""))
        self.assertEqual(type(buttons[0]), type(None), "Must block")

        title_text = "test_button_template_with_call_button - Test 11 - {}".format(
            1)
        button_payload = self.template.button_template(title_text, buttons)
        status_code = self.facebook.send_message(button_payload)
        self.assertEqual(status_code, 400, "Suppose to NOT work again!")

    def test_12_button_template_with_call_button(self):
        buttons = list()
        title = "Test 11 Call button - {}".format(1)
        buttons.append(self.button.create_call_button(title, "+8801723130852"))
        self.assertEqual(type(buttons[0]), type(dict()), "Must nt block")

        title = "Test 12 PostBack - {}".format(1)
        buttons.append(self.button.create_postback_button(
            title, self.postback_payload))
        self.assertEqual(type(buttons[1]), type(dict()), "Must nt block")

        title_text = "test_button_template_with_call_button - Test 12 - {}".format(
            1)
        button_payload = self.template.button_template(title_text, buttons)
        status_code = self.facebook.send_message(button_payload)
        self.assertEqual(status_code, 200, "Suppose to work again!")
