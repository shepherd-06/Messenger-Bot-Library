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

    def test_generic_template_three(self):
        buttons = list()
        for _ in range(0, 4):
            title = "Test 3 - {}".format(_)
            buttons.append(self.button.create_url_button(title, self.url))
        
        payload = list()
        payload.append(self.generic_template.create_single_generic_elements(
            "test_generic_template_three", subtitle= "Gello Hello - Two", image_url=self.url, buttons=buttons))
        self.assertEqual(payload[0], None, "None returned!")

        generic_payload = self.generic_template.generic_template(payload)

        self.assertEqual(generic_payload, None, "Generic Payload is None! Crap!")
        status_code = self.facebook.send_message(generic_payload)
        self.assertEqual(status_code, 400, "Status code is not 200! Whaaaaaaaaaaaat!")
    
    def test_generic_template_four(self):
        buttons = list()
        for _ in range(0, 3):
            title = "Test 4 - {} ".format(_)
            title += "A" * 100
            buttons.append(self.button.create_url_button(title, self.url))
        
        payload = list()
        payload_title = "test_generic_template_four" + " " + "A" * 500
        payload_subtitle = "Gello Hello - 4 " + "A" * 500
        payload.append(self.generic_template.create_single_generic_elements(
            payload_title, subtitle= payload_subtitle, image_url=self.url, buttons=buttons))
        self.assertNotEqual(payload[0], None, "None returned!")

        generic_payload = self.generic_template.generic_template(payload)

        self.assertNotEqual(generic_payload, None, "Generic Payload is None! Crap!")
        status_code = self.facebook.send_message(generic_payload)
        self.assertEqual(status_code, 200, "Status code is not 200! Whaaaaaaaaaaaat!")


    
    def test_generic_template_five(self):
        buttons = list()
        for _ in range(0, 3):
            title = "Test 5 - {} ".format(_)
            buttons.append(self.button.create_url_button(title, self.url))
        
        payload = list()
        payload_title = "test_generic_template_five"
        payload_subtitle = "Gello Hello - 5"
        for _ in range (0, 12):
            payload.append(self.generic_template.create_single_generic_elements(
                payload_title + str(_), subtitle= payload_subtitle, image_url=self.url, buttons=buttons))

        generic_payload = self.generic_template.generic_template(payload)
        self.assertEqual(generic_payload, None, "Generic Payload is None! Crap!")
        status_code = self.facebook.send_message(generic_payload)
        self.assertEqual(status_code, 400, "Status code is not 200! Whaaaaaaaaaaaat!")

    
    def test_generic_template_six(self):
        buttons = list()
        for _ in range(0, 3):
            title = "Test 6 - {} ".format(_)
            buttons.append(self.button.create_url_button(title, self.url))
        
        payload = list()
        payload_title = "test_generic_template_six "
        payload_subtitle = "Gello Hello - 6"
        for _ in range (0, 10):
            payload.append(self.generic_template.create_single_generic_elements(
                payload_title + str(_), subtitle= payload_subtitle, image_url=self.url, buttons=buttons))

        generic_payload = self.generic_template.generic_template(payload)
        self.assertNotEqual(generic_payload, None, "Generic Payload is None! Crap!")
        status_code = self.facebook.send_message(generic_payload)
        self.assertEqual(status_code, 200, "Status code is not 200! Whaaaaaaaaaaaat!")

    
    def test_generic_template_seven(self):
        default_action = self.button.create_url_button("", self.url, is_default_action = True)
        buttons = list()
        for _ in range(0, 3):
            title = "Test 7 - {} ".format(_)
            buttons.append(self.button.create_url_button(title, self.url))
        
        payload = list()
        payload_title = "test_generic_template_seven "
        payload_subtitle = "Gello Hello - 7"
        for _ in range (0, 10):
            payload.append(self.generic_template.create_single_generic_elements(
                payload_title + str(_), subtitle= payload_subtitle, image_url=self.url, buttons=buttons, default_action=default_action))

        generic_payload = self.generic_template.generic_template(payload, shareable= True, image_aspect_ratio="square")
        self.assertNotEqual(generic_payload, None, "Generic Payload is None! Crap!")
        status_code = self.facebook.send_message(generic_payload)
        self.assertEqual(status_code, 200, "Status code is not 200! Whaaaaaaaaaaaat!")

    
    def test_generic_template_eight(self):
        default_action = self.button.create_url_button("", self.url, is_default_action = True)
        buttons = list()
        for _ in range(0, 3):
            title = "Test 7 - {} ".format(_)
            buttons.append(self.button.create_url_button(title, self.url))
        
        payload = list()
        payload_title = "test_generic_template_eight "
        payload_subtitle = "Gello Hello - 8"
        payload.append(self.generic_template.create_single_generic_elements(
                payload_title, subtitle= payload_subtitle, image_url=self.url, buttons=buttons, default_action=default_action))
        generic_payload = self.generic_template.generic_template(payload, shareable= True, image_aspect_ratio="vertical")
        self.assertEqual(generic_payload, None, "Generic Payload is None! Crap!")
        status_code = self.facebook.send_message(generic_payload)
        self.assertEqual(status_code, 400, "Status code is not 200! Whaaaaaaaaaaaat!")

    
    def test_generic_template_nine(self):
        default_action = self.button.create_url_button("", self.url, is_default_action = True)
        buttons = list()
        for _ in range(0, 3):
            title = "Test 7 - {} ".format(_)
            buttons.append(self.button.create_url_button(title, self.url))
        
        payload = list()
        payload_title = "test_generic_template_nine "
        payload_subtitle = "Gello Hello - 9"
        payload.append(self.generic_template.create_single_generic_elements(
                payload_title, subtitle= payload_subtitle, image_url=self.url, buttons=buttons, default_action=default_action))
        generic_payload = self.generic_template.generic_template(payload, shareable= True)
        self.assertNotEqual(generic_payload, None, "Generic Payload is None! Crap!")
        status_code = self.facebook.send_message(generic_payload)
        self.assertEqual(status_code, 200, "Status code is not 200! Whaaaaaaaaaaaat!")