import os
import unittest

from flask import Flask, Request, request
from io import StringIO
from io import BytesIO


from app import app


class TestConfig(unittest.TestCase):

       # def setUp(self):
    #     pass

    # def tearDown(self):
    #     pass

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    # home page renders correctly
    def test_rendered_home(self):
        response = self.app.get('/', content_type='html/text')
        self.assertTrue(b'Mr. Acme' in response.data)

    def test_upload(self):

        class FileObj(StringIO):

            def close(self):
                global RESULT
                RESULT = True

        class MyRequest(Request):
            def _get_file_stream(self, *args, **kwargs):
                return FileObj()

        app = Flask(__name__)
        app.debug = True
        app.request_class = MyRequest

        @app.route("/upload", methods=['POST'])
        def upload():
            client = app.test_client()
            resp = client.post(
                '/upload',
                data={
                    'file': (BytesIO(b'my file contents'), 'hello world.jpg'),
                }
            )
            self.assertEqual(
                'ok',
                resp.data,
            )
            global RESULT
            self.assertTrue(RESULT)


if __name__ == '__main__':
    unittest.main()
