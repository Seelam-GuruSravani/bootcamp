import unittest
import json
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Happy path test cases

    def test_ping(self):
        response = self.app.get('/ping')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), '200 OK')

    def test_healthz(self):
        response = self.app.get('/healthz')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertIn('cpu_percent', data)
        self.assertIn('memory_percent', data)


    def test_run(self):
        # Ensure that the Flask application is running and can handle requests
        with app.test_client() as client:
            response = client.get('/ping')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data.decode(), '200 OK')

            response = client.get('/healthz')
            self.assertEqual(response.status_code, 200)
            data = json.loads(response.data.decode())
            self.assertIn('cpu_percent', data)
            self.assertIn('memory_percent', data)


    # Sad path test cases

    def test_invalid_endpoint(self):
        response = self.app.get('/invalid')
        self.assertEqual(response.status_code, 404)

    def test_invalid_method_ping(self):
        response = self.app.post('/ping')
        self.assertEqual(response.status_code, 405)

    def test_invalid_method_healthz(self):
        response = self.app.post('/healthz')
        self.assertEqual(response.status_code, 405)

if __name__ == '__main__':
    unittest.main()
