"""A modular API for interacting
with the RouteSMS HTTP API
"""
import requests


class RouteSMS(object):
    """Interact with the RouteSMS HTTP API"""

    def __init__(self, username, password):
        """
        Class constructor
        :param username:
        :param password:
        :return:
        """
        self.username = username
        self.password = password

    def send_message(self, recipient, sender, message):
        """
        Accepts the message details and sends SMS
        :param recipient:
        :param sender:
        :param message:
        :return:
        """
        recipient = str(recipient)
        url = "http://smsplus3.routesms.com:8080/bulksms/bulksms?"
        credentials = "username=" + self.username + "&password=" + self.password
        msg_type = "&type=0&dlr=1"
        msg_format = "&destination=" + recipient + "&source=" + \
                     sender + "&message=" + message

        final = url + credentials + msg_type + msg_format

        try:
            result = requests.get(final)
            status = result.text.split("|")
            if status[0] == "1701" and status[1] == recipient:
                return True
            else:
                return False
        except requests.ConnectionError:
            return False

