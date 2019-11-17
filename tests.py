#!/usr/bin/env python
import app
import json
import unittest


class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(json.loads(rv.data), {"message": "Hello World"})


if __name__ == '__main__':
    unittest.main()
