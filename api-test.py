#!/usr/bin/python

from api import app
import unittest
import json

class ApiTestCase(unittest.TestCase):
    # Using the unittest library, to call the 2 resources (HelloWorld, PiDecimal)
    # calling the URL as expected, and checking that the
    # returned value matches the expected result
    def test_hello(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        # Check that the body is {'hello' : 'world'}
        self.assertEqual(json.loads(response.data), {'hello': 'world'})

    def test_pi(self):
        tester = app.test_client(self)
        response = tester.get('/10')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"10 Decimals": "3.1415926536"})

    # This tests will purposely fail
    # We are checking that the responses are not the values we have provided
    # ie NOT {'hello' : 'Badi'} for HelloWorld
    # and NOT the value we shall provide for Pi to 5 decimal places
    def test_hello_fail(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'hello': 'Badi'})

    def test_pi_fail(self):
        tester = app.test_client(self)
        response = tester.get('/5')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {"5 Decimals": "3.14"})

if __name__ == '__main__':
    unittest.main()
