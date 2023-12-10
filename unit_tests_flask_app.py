import unittest
from flask_app import app
import json
import base64


class TestGenerateArrayEndpoint(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.valid_input = {'sentence': 'This is a test sentence.'}
        self.invalid_input = {}  # Missing 'sentence' key
        # Sending a valid authentication request
        self.login_response = self.app.post('/login',
                                            headers={'Authorization': 'Basic ' + base64.b64encode(
                                                b'arun:CJpassword64').decode(
                                                'utf-8')})
        self.data = self.login_response.get_json()
        self.access_token = self.data['access_token']

    def test_login(self):

        # Check if the response status code is 200 OK
        self.assertEqual(self.login_response.status_code, 200)

        # Check if the response contains an access token
        self.assertIn('access_token', self.data)

    def test_valid_input(self):
        # Testing with valid input
        response = self.app.post('/generate_array', json=self.valid_input,
                                 headers={'Authorization': 'Bearer {}'.format(self.access_token)})
        data = response.get_json()
        print(data, '')
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', data)  # data is a dictionary object
        self.assertEqual(len(data['result']), 500)  # Checking for 500-dimensional array

    def test_invalid_input(self):
        # Testing with invalid input
        response = self.app.post('/generate_array', json=self.invalid_input,
                                 headers={'Authorization': 'Bearer {}'.format(self.access_token)})
        data = response.get_json()

        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)
        self.assertEqual(data['error'], 'Invalid input')


if __name__ == '__main__':
    unittest.main()
