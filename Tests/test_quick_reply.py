import unittest
from BotLib.quick_reply.quick_re import QuickReply
from .send_message import Facebook


class TestQuickReply(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.facebook = Facebook()
        self.test_user = "1475588502509679"

    @classmethod
    def tearDownClass(self):
        del self.facebook

    def test_quick_reply(self):
        q_reply = QuickReply(self.test_user)

        # ---------------------------------------
        # Test Phase 1 & 2
        # ---------------------------------------
        test_1_payload = q_reply.quick_reply_create("text", "Hello_World")
        self.assertEqual(test_1_payload, {},
                         "Its suppose to be an empty dictionary here!")
        test_2_payload = q_reply.quick_reply_create(
            "text", "Hello_World", "123456", "")

        test_1_quick_reply_payload = q_reply.quick_reply(
            "Title_text", [test_1_payload])
        test_2_quick_reply_payload = q_reply.quick_reply(
            "Title_text", [test_2_payload])

        self.assertNotEqual(type(test_1_quick_reply_payload), dict,
                            "Test_1_You shall not PASSSSSSSS")
        self.assertEqual(type(test_2_quick_reply_payload), dict,
                         "Test_2_This is suppose to be a dictionary to be passed!")
        status_code = self.facebook.send_message(test_2_quick_reply_payload)
        self.assertEqual(status_code, 200, "This better be 200!")

        # ---------------------------------------
        # Test phase 3:
        # ---------------------------------------
        # Run All Text based - 11 in total. All goes normal. Nothing changei changei
        test_3_payload = list()
        for _ in range(0, 11):
            title_text = "Humbda Dumda"
            payload = "123123dfjf"
            image_url = "https://developers.facebook.com/docs/messenger-platform/reference/send-api/quick-replies/"
            test_3_payload.append(q_reply.quick_reply_create(
                "text", title_text=title_text, payload=payload, image_url=image_url))
        test_3_quick_reply_payload = q_reply.quick_reply(
            "Title Text", test_3_payload)
        self.assertEqual(type(test_3_quick_reply_payload), dict, "Oh Crap!")
        status_code = self.facebook.send_message(test_3_quick_reply_payload)
        self.assertEqual(status_code, 200, "This better be 200!")
