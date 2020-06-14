import json
import logging

from flask import Flask, request, jsonify
from flask_api import status
from decouple import config

app = Flask(__name__)


class Facebook:

    # This is a test suite for facebook messenger service.
    def __init__(self):
        self.__reply_url = config("facebook_graph_api_url") + \
            config("page_access_token")

    def send_message(self, payload: dict = None):
        """
        A strip down function to check if everything went well with the payload generation.
        """
        try:
            import requests
            if payload is None:
                response = requests.get(self.__reply_url)
            else:
                response = requests.post(self.__reply_url, json=payload)
            logging.debug(response.content)
            return response.status_code
        except Exception as error:
            logging.exception("Error occurred {}".format(error))
            return None


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        if str(request.args.get(key='hub.verify_token', default='no_verify_token')) == config('messenger_access_token'):
            return request.args.get('hub.challenge'), status.HTTP_200_OK
        else:
            return jsonify(
                status='Access Restricted',
                status_code=status.HTTP_401_UNAUTHORIZED,
            )
    elif request.method == 'POST':
        incoming_message = json.loads((request.data).decode("utf-8"))
        for entry in incoming_message["entry"]:
            if "messaging" in entry:
                for message in entry["messaging"]:
                    if "message" in message:
                        if "is_echo" in message["message"]:
                            return '', status.HTTP_200_OK
                        elif "quick_reply" in message["message"]:
                            return '', status.HTTP_200_OK
                        elif "text" in message["message"]:
                            sender_id = message["sender"]["id"]
                            if 'message' in message:
                                user_message = message['message']['text'] if 'text' in message['message'] else None
                            else:
                                user_message = None
                            if user_message is None:
                                user_message = "Hello"

                            def __custom_basic_payload(sender_id, user_message):
                                """
                                created a custom function to avoid dependencies on chatbot. 
                                It does not have any validation like the original function. 
                                """
                                return {
                                    "recipient": {
                                        "id": sender_id
                                    },
                                    "message": {
                                        "text": user_message
                                    }
                                }

                            payload = __custom_basic_payload(
                                sender_id, user_message)
                            Facebook().send_message(payload)

                            text = "Received a message from user: {}".format(
                                sender_id)
                            payload = __custom_basic_payload(
                                sender_id, text)
                            Facebook().send_message(payload)
                            return '', status.HTTP_200_OK
                        elif "read" in message["message"]:
                            return '', status.HTTP_200_OK
                        else:
                            return '', status.HTTP_200_OK
                    elif "delivery" in message:
                        return '', status.HTTP_200_OK
                    elif "read" in message:
                        return '', status.HTTP_200_OK
                    elif "postback" in message:
                        return '', status.HTTP_200_OK
                    else:
                        return '', status.HTTP_200_OK
            elif "standby" in entry:
                return '', status.HTTP_200_OK
            else:
                return '', status.HTTP_200_OK
    else:
        return jsonify(
            status='Access Restricted',
            status_code=status.HTTP_401_UNAUTHORIZED,
        )
