import unittest
from bizarro_lib.template.list_template import ListTemplate
from bizarro_lib.utility.button import Button
from bizarro_lib.utility.button_validation import ButtonValidation
from Tests.send_message import Facebook

class TestListTemplate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.list_template = ListTemplate('1475588502509679')
        cls.bttn = Button()
        cls.btn_validation = ButtonValidation()
        cls.facebook = Facebook()
        cls.url = "https://adventures.is/wp-content/uploads/2017/06/eyjafjallajokull-glacier-volcano-iceland1.jpg"

    @classmethod
    def tearDownClass(cls):
        del cls.list_template
        del cls.bttn
        del cls.btn_validation

    def test_one(self):
        buttons = list()
        buttons.append(self.bttn.create_url_button("Hello_Test_One", self.url))
        list_payload = list()

        for _ in range(0, 2):
            list_payload.append(self.list_template.create_list_element("Hello Test 1_{}".format(_), 'Subtitle_one', self.url, buttons=buttons))     
        payload = self.list_template.list_template_payload(list_payload)
        print(payload)
        self.assertNotEqual(type(payload), type(None), "None type!")
        status_code = self.facebook.send_message(list_payload)
        self.assertEqual(status_code, 200, "Come on man!")

