import unittest
from BotLib.template.generic_template import GenericTemplate
from BotLib.utility.button import Button
from Tests.send_message import Facebook


class TestGenericTemplate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.generic_template = GenericTemplate("1475588502509679")
        cls.button = Button()
        cls.facebook = Facebook()
        cls.url = "https://adventures.is/wp-content/uploads/2017/06/eyjafjallajokull-glacier-volcano-iceland1.jpg"

    @classmethod
    def tearDownClass(cls):
        del cls.generic_template
        del cls.button
        del cls.facebook
        del cls.url

    def test_generic_template_one(self):
        default_action = self.button.create_url_button("Boshe achi eka", self.url, is_default_action = True)
        payload = list()
        payload.append(self.generic_template.create_single_generic_elements(
            "test_generic_template_one", subtitle= "Subtitle", image_url=self.url, default_action=default_action))
        self.assertNotEqual(payload[0], None, "None returned!")

        generic_payload = self.generic_template.generic_template(payload)

        self.assertNotEqual(generic_payload, None, "Generic Payload is None! Crap!")
        status_code = self.facebook.send_message(generic_payload)
        self.assertEqual(status_code, 200, "Status code is not 200! Whaaaaaaaaaaaat!")

    def test_generic_template_two(self):
        default_action = self.button.create_url_button(title = "", url= self.url, is_default_action = True)
        buttons = list()
        for _ in range(0, 3):
            title = "Test 2 - {}".format(_)
            buttons.append(self.button.create_url_button(title, self.url))
        payload = list()
        payload.append(self.generic_template.create_single_generic_elements(
            "test_generic_template_two", subtitle= "Gello Hello - Two", image_url=self.url, default_action=default_action, buttons=buttons))
        self.assertNotEqual(payload[0], None, "None returned!")

        generic_payload = self.generic_template.generic_template(payload)

        self.assertNotEqual(generic_payload, None, "Generic Payload is None! Crap!")
        status_code = self.facebook.send_message(generic_payload)
        self.assertEqual(status_code, 200, "Status code is not 200! Whaaaaaaaaaaaat!")