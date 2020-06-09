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
    else:
        return '', status.HTTP_200_OK
