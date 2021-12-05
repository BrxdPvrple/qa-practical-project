import unittest
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from app import app


# Tests app flask app is inititalised
class TestBase(TestCase):
    def create_app(self):
        return app


# Test for genre view in genre.py
class TestGenre(TestBase):
    def test_genre(self):
        with patch('random.choice') as r:
            r.return_value = 'Jazz'
            response = self.client.get(url_for('genre'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Jazz', response.data)
