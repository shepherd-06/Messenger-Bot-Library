import logging
import unittest

from decouple import config
from messenger_bot.buttons.button_generator import Button
from messenger_bot.buttons.button_validator import ButtonValidation
from messenger_bot.template.template_list import ListTemplate

from Tests.send_message import Facebook


class TestListTemplate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.list_template = ListTemplate(config("test_facebook_user", None))
        cls.button = Button()
        cls.btn_validation = ButtonValidation()
        cls.facebook = Facebook()
        cls.url = config("test_url", None)
        logging.info("List Template has been deprecated on July 29, 2019")

    @classmethod
    def tearDownClass(cls):
        del cls.list_template
        del cls.button
        del cls.btn_validation

    def test_one(self):
        """
        Only test functions for List template
        There are two test cases here.
        """
        buttons = list()
        buttons.append(self.button.create_url_button(
            "Hello_Test_One", self.url))
        list_payload = list()

        for _ in range(0, 2):
            list_payload.append(self.list_template.create_list_element(
                "Hello Test 1_{}".format(_), 'Subtitle_one', self.url, buttons=buttons))
        payload = self.list_template.list_template_payload(list_payload)
        self.assertNotEqual(type(payload), type(
            None), "test_one - list_template - payload test")

        status_code = self.facebook.send_message(payload)
        self.assertEqual(status_code, 400, "test_one - list_template -> 400")
        logging.critical(
            "Deprecation Warning! List Template has been depcreated on July 29, 2019")
