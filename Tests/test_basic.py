import unittest
from Tests.send_message import Facebook
from BotLib.utility.tag import Tags
from BotLib.utility.util import Utility
import random
import time


class TestBasic(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.facebook = Facebook()
        self.test_user = "1475588502509679"
        self.utility = Utility()

    @classmethod
    def tearDownClass(self):
        del self.facebook

    def test_typing_on(self):
        waiting_period = random.uniform(0.1, 20.1)
        typing_payload = self.utility.typing_on(
            self.test_user, waiting_period=waiting_period)
        status_code = self.facebook.send_message(typing_payload)
        self.assertEqual(status_code, 200, "Better be 200 Saul!")

        text = "test_typing_on - Test 1 - waiting for {} -- {}".format(
            waiting_period, random.randint(0, 10000000000000))
        echo_payload = self.utility.basic_text_reply_payload(
            self.test_user, text)
        status_code = self.facebook.send_message(echo_payload)
        self.assertEqual(status_code, 200, "Better be 200 Saul!")

    def test_echo_back(self):
        text = "test_echo_back - Test 1 -- {}".format(
            random.randint(0, 10000000000000))
        echo_payload = self.utility.basic_text_reply_payload(
            self.test_user, text)
        status_code = self.facebook.send_message(echo_payload)
        self.assertEqual(status_code, 200, "Better be 200 Saul!")

        waiting_period = random.uniform(0.1, 20.1)
        typing_payload = self.utility.typing_on(
            self.test_user, waiting_period=waiting_period)
        status_code = self.facebook.send_message(typing_payload)
        self.assertEqual(status_code, 200, "Better be 200 Saul!")
        time.sleep(waiting_period)

        text = "test_echo_back - waiting for {} - Test 2 -- {}".format(
            waiting_period, random.randint(0, 10000000000000))
        echo_payload = self.utility.basic_text_reply_payload(
            self.test_user, text)
        status_code = self.facebook.send_message(echo_payload)
        self.assertEqual(status_code, 200, "Better be 200 Saul!")

        text = "Test 3 - {}".format('x' * 20000)
        echo_payload = self.utility.basic_text_reply_payload(
            self.test_user, text)
        status_code = self.facebook.send_message(echo_payload)
        self.assertEqual(status_code, 400, "Better be 400 Saul!")

    def test_marked_seen(self):
        mark_seen_payload = self.utility.marked_seen(self.test_user)
        status_code = self.facebook.send_message(mark_seen_payload)
        self.assertEqual(status_code, 200, "Better be 200 Saul!")
