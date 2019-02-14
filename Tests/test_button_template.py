import unittest
from BotLib.template.button_template import ButtonTemplate
from BotLib.utility.button import Button
from Tests.send_message import Facebook

class TestButtonTemplate(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.button = Button()
        self.facebook = Facebook()
        self.template = ButtonTemplate("1475588502509679")
    
    @classmethod
    def tearDownClass(self):
        del self.button
        del self.facebook
        del self.template

    def test_button_template_with_web_url(self):
        buttons = list()
        for _ in range(0, 3):
            title = "Test 1 - {}".format(_)
            url = "https://adventures.is/wp-content/uploads/2017/06/eyjafjallajokull-glacier-volcano-iceland1.jpg"
            buttons.append(self.button.create_url_button(title, url))
        title_text = "test_button_template_with_web_url - Test 1 - {}".format(_)
        button_payload = self.template.button_template(title_text, buttons)
        status_code = self.facebook.send_message(button_payload)
        self.assertEqual(status_code, 200, "First run worked?")