from flask import Flask, Request, request
from app import app
import unittest
from io import BytesIO, StringIO


class FlaskTestCase(unittest.TestCase):

    # ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # home page renders correctly
    def test_rendered_home(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Mr. Acme' in response.data)


if __name__ == '__main__':
    unittest.main()
