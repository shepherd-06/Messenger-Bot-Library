import unittest
from BotLib.quick_reply.quick_re import QuickReply

class TestQuickReply(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()

    def test_quick_reply(self):
        quick_reply = QuickReply("test_run_1234")
        test_1_payload = quick_reply.quick_reply_create("text", "Hello_World")
        self.assertEqual(test_1_payload, {}, "Its suppose to be an error here!")
