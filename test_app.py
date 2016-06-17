from app import app
import unittest

class FlaskAppTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        #generate test client
        self.app = app.test_client()
        #passes exceptions in the line to the test client.
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_status_code(self):
        #send GET to root
        result = self.app.get("/")
        #check that result matches as expected
        self.assertEqual(result.status_code, 200)

    def test_home_data(self):
        #sends
        result = self.app.get("/")
        #assert the response data
        self.assertEqual(result.data, "Hi!  I\'m a Flask Application. Now I\'m inside a Docker container.")
