import unittest
from Tests.send_message import Facebook
from messenger_bot.utility.util import MessengerUtility
import random
import time
from decouple import config


class TestBasic(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.facebook = Facebook()
        self.test_user = config("test_facebook_user", None)
        self.utility = MessengerUtility()

    @classmethod
    def tearDownClass(self):
        del self.facebook

    def test_typing_on(self):
        """
        This function test the typing on functionality. 
        There are two test cases. 
        """
        waiting_period = random.uniform(0.1, 20.1)
        typing_payload = self.utility.typing_on(
            self.test_user, waiting_period=waiting_period)
        status_code = self.facebook.send_message(typing_payload)
        self.assertEqual(status_code, 200, "typing_payload -> 200")

        text = "test_typing_on - Test 1 - waiting for {} -- {}".format(
            waiting_period, random.randint(0, 10000000000000))
        echo_payload = self.utility.basic_text_reply_payload(
            self.test_user, text)
        status_code = self.facebook.send_message(echo_payload)
        self.assertEqual(status_code, 200,
                         "test_typing_on - Test 1 -> 200")

    def test_echo_back(self):
        """
        This functions test tbe basic text reply payload settings
        There are four test cases. 
        """
        text = "test_echo_back - Test 1 -- {}".format(
            random.randint(0, 10000000000000))
        echo_payload = self.utility.basic_text_reply_payload(
            self.test_user, text)
        status_code = self.facebook.send_message(echo_payload)
        self.assertEqual(status_code, 200,
                         "test_echo_back - Test 1 -> 200")

        waiting_period = random.uniform(0.1, 20.1)
        typing_payload = self.utility.typing_on(
            self.test_user, waiting_period=waiting_period)
        status_code = self.facebook.send_message(typing_payload)
        self.assertEqual(
            status_code, 200, "test_echo_back - Test 1 -> 200")
        time.sleep(waiting_period)

        text = "test_echo_back - waiting for {} - Test 2 -- {}".format(
            waiting_period, random.randint(0, 10000000000000))
        echo_payload = self.utility.basic_text_reply_payload(
            self.test_user, text)
        status_code = self.facebook.send_message(echo_payload)
        self.assertEqual(status_code, 200,
                         "test_echo_back - Test 2 -> 200")

        text = "Test 3 - {}".format('x' * 20000)
        echo_payload = self.utility.basic_text_reply_payload(
            self.test_user, text)
        status_code = self.facebook.send_message(echo_payload)
        self.assertEqual(status_code, 400,
                         "test_echo_back Test 3 -> 400")

    def test_marked_seen(self):
        mark_seen_payload = self.utility.marked_seen(self.test_user)
        status_code = self.facebook.send_message(mark_seen_payload)
        self.assertEqual(status_code, 200, "test_marked_seen 200")
