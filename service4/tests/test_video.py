import unittest
from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase
from video import app


# Tests app flask app is inititalised
class TestBase(TestCase):
    def create_app(self):
        return app


# Test for video view in genre.py
class TestVideo(TestBase):
    def test_video(self):
        with patch('random.choice') as r:
            r.return_value = "https://www.youtube.com/embed/1SuUe4HC0T4?start=114"
            response = self.client.post(url_for('video'))
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"https://www.youtube.com/embed/1SuUe4HC0T4?start=114", response.data)
















    # def test_piano(self):
    #     with patch('random.choice') as r:
    #         r.return_value = "https://www.youtube.com/embed/GS2Y_CkaXP0?start=114"
    #         response = self.client.post(url_for('video'))
    #         self.assertEqual(response.status_code, 200)
    #         self.assertIn(b"https://www.youtube.com/embed/GS2Y_CkaXP0?start=114", response.data)


    # def test_saxophone(self):
    #     with patch('random.choice') as r:
    #         r.return_value = "https://www.youtube.com/embed/hiZp8bTAWbU"
    #         response = self.client.post(url_for('video'))
    #         self.assertEqual(response.status_code, 200)
    #         self.assertIn(b"https://www.youtube.com/embed/hiZp8bTAWbU", response.data)


    # def test_violin(self):
    #     with patch('random.choice') as r:
    #         r.return_value = "https://www.youtube.com/embed/ysOITu9GukE"
    #         response = self.client.post(url_for('video'))
    #         self.assertEqual(response.status_code, 200)
    #         self.assertIn(b"https://www.youtube.com/embed/ysOITu9GukE", response.data)

