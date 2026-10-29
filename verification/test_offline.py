"""Offline verification; not a substitute for the five live course tests."""
import json
import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector
from server import app


class OfflineChecks(unittest.TestCase):
    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_nested_watson_scores(self, post):
        for dominant in ("anger", "disgust", "fear", "joy", "sadness"):
            with self.subTest(dominant=dominant):
                scores = dict.fromkeys(("anger", "disgust", "fear", "joy", "sadness"), 0.025)
                scores[dominant] = 0.9
                response = Mock(status_code=200)
                response.text = json.dumps({"emotionPredictions": [{"emotion": scores}]})
                post.return_value = response
                result = emotion_detector("example")
                self.assertEqual(result, {**scores, "dominant_emotion": dominant})
        self.assertEqual(post.call_args.kwargs["json"], {"raw_document": {"text": "example"}})

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_http_400(self, post):
        post.return_value = Mock(status_code=400)
        result = emotion_detector("")
        self.assertEqual(len(result), 6)
        self.assertTrue(all(value is None for value in result.values()))

    def test_interface_and_blank_input(self):
        with app.test_client() as client:
            self.assertEqual(client.get("/").status_code, 200)
            for text in ("", "   "):
                response = client.get("/emotionDetector", query_string={"textToAnalyze": text})
                self.assertEqual(response.text, "Invalid Input! Please try again.")

    @patch("server.emotion_detector")
    def test_rendered_emotions(self, detector):
        detector.return_value = dict(anger=.9, disgust=.025, fear=.025, joy=.025,
                                     sadness=.025, dominant_emotion="anger")
        with app.test_client() as client:
            response = client.get("/emotionDetector", query_string={"textToAnalyze": "angry"})
            self.assertIn("The dominant emotion is anger.", response.text)
            for name in ("anger", "disgust", "fear", "joy", "sadness"):
                self.assertIn(f"'{name}':", response.text)


if __name__ == "__main__":
    unittest.main()
