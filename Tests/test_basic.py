import random
import time
import unittest

from decouple import config
from messenger_bot.utility.util import MessengerUtility

from Tests.send_message import Facebook


class TestBasic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.facebook = Facebook()
        cls.test_user = config("test_facebook_user", None)
        cls.utility = MessengerUtility()

        if cls.test_user is None:
            print("*$#" * 20)
            print("*$#" * 20)
            print("*$#" * 20)
            print("None Env Variable")
            print("*$#" * 20)
            print("*$#" * 20)
            print("*$#" * 20)

    @classmethod
    def tearDownClass(cls):
        del cls.facebook

    def test_typing_on(self):
        """
        This function test the typing on functionality. 
        There are two test cases. 
        """
        waiting_period = random.uniform(0.1, 20.1)
        typing_payload = self.utility.typing_on(
            self.test_user, waiting_period=waiting_period)
        status_code = self.facebook.send_message(typing_payload)
        self.assertEqual(status_code, 200, "test_typing_on typing_on")

        text = "test_typing_on - Test 1 - waiting for {} -- {}".format(
            waiting_period, random.randint(0, 10000000000000))
        echo_payload = self.utility.basic_text_reply_payload(
            self.test_user, text)
        status_code = self.facebook.send_message(echo_payload)
        self.assertEqual(status_code, 200,
                         "test_typing_on - Test 1")

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
                         "test_echo_back - Test 1")

        waiting_period = random.uniform(0.1, 20.1)
        typing_payload = self.utility.typing_on(
            self.test_user, waiting_period=waiting_period)
        status_code = self.facebook.send_message(typing_payload)
        self.assertEqual(
            status_code, 200, "test_echo_back - Test 1")
        time.sleep(waiting_period)

        text = "test_echo_back - waiting for {} - Test 2 -- {}".format(
            waiting_period, random.randint(0, 10000000000000))
        echo_payload = self.utility.basic_text_reply_payload(
            self.test_user, text)
        status_code = self.facebook.send_message(echo_payload)
        self.assertEqual(status_code, 200,
                         "test_echo_back - Test 2")

        text = "Test 3 - {}".format('x' * 20000)
        echo_payload = self.utility.basic_text_reply_payload(
            self.test_user, text)
        status_code = self.facebook.send_message(echo_payload)
        self.assertEqual(status_code, 400,
                         "test_echo_back Test 3 -> 400")

    def test_marked_seen(self):
        """
        basic tests for marked seen. 
        There is only one basic test case here
        """
        mark_seen_payload = self.utility.marked_seen(self.test_user)
        status_code = self.facebook.send_message(mark_seen_payload)
        self.assertEqual(status_code, 200, "test_marked_seen 200")
