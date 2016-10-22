import urllib.request
import json


class Userper():

    def __init__(self, location):
        self.location = location

    def get(self, session_id=''):
        user = self._get_user(session_id)
        if user != None:
            self.username = user['username']
            self.email = user['email']
            self.name = user['name']
            self.grade = user['grade']
            self.major = user['major']

    def get_test(self, session_id=''):
        user = {
            'username': 'root',
            'email': 'root@mail.stufinite.faith',
            'name': 'root'
            'grade': 1,
            'major': 'CS'
        }
        if user != None:
            self.username = user['username']
            self.email = user['email']
            self.last_name = user['last_name']
            self.first_name = user['first_name']
            self.grade = user['grade']
            self.major = user['major']

    def _get_user(self, session_id=''):
        r = urllib.request.urlopen(
            'http://' + self.location + '/auth/get_user/' + session_id)
        text = bytes.decode(r.readline())
        return text if text == 'None' else json.loads(text)

    def _get_username(self, session_id=''):
        r = urllib.request.urlopen(
            'http://' + self.location + '/auth/get_username/' + session_id)
        return bytes.decode(r.readline())
