import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector


class EmotionDetectorTests(unittest.TestCase):
    @staticmethod
    def response_for(dominant):
        scores = {
            "anger": 0.1, "disgust": 0.1, "fear": 0.1,
            "joy": 0.1, "sadness": 0.1,
        }
        scores[dominant] = 0.9
        response = Mock(status_code=200)
        response.text = '{"emotionPredictions": [{"emotion": ' + str(scores).replace("'", '"') + '}]}'
        return response

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_anger(self, post):
        post.return_value = self.response_for("anger")
        self.assertEqual(emotion_detector("test")["dominant_emotion"], "anger")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_disgust(self, post):
        post.return_value = self.response_for("disgust")
        self.assertEqual(emotion_detector("test")["dominant_emotion"], "disgust")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_fear(self, post):
        post.return_value = self.response_for("fear")
        self.assertEqual(emotion_detector("test")["dominant_emotion"], "fear")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy(self, post):
        post.return_value = self.response_for("joy")
        self.assertEqual(emotion_detector("test")["dominant_emotion"], "joy")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sadness(self, post):
        post.return_value = self.response_for("sadness")
        self.assertEqual(emotion_detector("test")["dominant_emotion"], "sadness")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_bad_request(self, post):
        post.return_value = Mock(status_code=400)
        self.assertIsNone(emotion_detector("bad input")["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
