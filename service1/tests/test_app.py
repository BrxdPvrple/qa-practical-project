import unittest
from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app

class TestBase(TestCase):
    def create_app(self):

        return app


class TestFrontEnd(TestBase):
  
    def test_home(self):
        # Mock Values
        genre = 'Classical'
        instrument = 'Guitar'
        video = 'https://www.youtube.com/embed/1SuUe4HC0T4?start=114'

        with requests_mock.Mocker() as m:
            m.get('http://genres:5001/genre', text=genre)
            m.get('http://instruments:5002/instrument', text=instrument)
            m.post('http://backend:5003/video', text=video)
            response = self.client.get(url_for('home'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'https://www.youtube.com/embed/1SuUe4HC0T4?start=114', response.data)


