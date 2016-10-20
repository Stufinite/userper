import urllib.request
import json


class Userper():

    def __init__(self, location):
        self.location = location

    def get_user(self, session_id=''):
        r = urllib.request.urlopen(
            'http://' + self.location + '/auth/get_user/' + session_id)
        text = bytes.decode(r.readline())
        return text if text == 'None' else json.loads(text)

    def get_username(self, session_id=''):
        r = urllib.request.urlopen(
            'http://' + self.location + '/auth/get_username/' + session_id)
        return bytes.decode(r.readline())
