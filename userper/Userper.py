import urllib.request
from urllib.error import HTTPError
import json


class Userper():

    def __init__(self, location):
        self.location = location

    def get(self, session_id=''):
        user = self._get_user(session_id)
        if user != 'None':
            self.username = user['username']
            self.email = user['email']
            self.name = user['name']
            self.grade = user['grade']
            self.major = user['major']
            self.second_major = user['second_major']
            self.career = user['career']
        else:
            raise HTTPError(self.location, "404", "Page not found", None, None)

    def get_test(self, session_id=''):
        user = {
            'username': 'root',
            'email': 'root@mail.stufinite.faith',
            'name': 'root',
            'grade': '2',
            'major': '資訊科學與工程學系學士班',
            'second_major': '',
            'career': 'U',
        }
        if user != 'None':
            self.username = user['username']
            self.email = user['email']
            self.name = user['name']
            self.grade = user['grade']
            self.major = user['major']
            self.second_major = user['second_major']
            self.career = user['career']

    def _get_user(self, session_id=''):
        req = urllib.request.Request('https://' + self.location + '/auth/get_user/' + session_id,
                                     headers={'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"})
        r = urllib.request.urlopen(req)
        text = bytes.decode(r.readline())
        return text if text == 'None' else json.loads(text)

    def _get_username(self, session_id=''):
        req = urllib.request.Request('https://' + self.location + '/auth/get_username/' + session_id,
                                     headers={'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36"})
        r = urllib.request.urlopen(req)
        return bytes.decode(r.readline())
