import unittest
from flask import url_for
from flask_testing import TestCase
from app import app


# Tests app flask app is inititalised
class TestBase(TestCase):
    def create_app(self):
        return app


# Test for video view in genre.py
class TestVideo(TestBase):
    def test_video(self):
        response = self.client.post(url_for('video'), json={'genre':'Classical', 'instrument': 'Guitar'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"https://www.youtube.com/embed/1SuUe4HC0T4?start=114", response.data)
