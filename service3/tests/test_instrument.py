import unittest
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from instrument import app


# Tests app flask app is inititalised
class TestBase(TestCase):
    def create_app(self):
        return app


# Test for instrument view in genre.py
class TestInstrument(TestBase):
    def test_instrument(self):
        with patch('random.choice') as r:
            r.return_value = 'Guitar'
            response = self.client.get(url_for('instrument'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Guitar', response.data)
