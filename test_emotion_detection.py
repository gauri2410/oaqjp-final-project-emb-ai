import unittest
from unittest.mock import Mock, patch

from EmotionDetection.emotion_detection import emotion_detector


class EmotionDetectorTests(unittest.TestCase):
    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy_is_dominant(self, post):
        response = Mock(status_code=200)
        response.json.return_value = {"emotionPredictions": [{"emotion": {
            "anger": 0.01, "disgust": 0.01, "fear": 0.01, "joy": 0.9, "sadness": 0.07
        }}]}
        post.return_value = response
        result = emotion_detector("I am glad")
        self.assertEqual(result["dominant_emotion"], "joy")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_bad_request_returns_empty_result(self, post):
        post.return_value = Mock(status_code=400)
        result = emotion_detector(" ")
        self.assertIsNone(result["dominant_emotion"])

    def test_all_required_keys_are_present(self):
        self.assertEqual(
            set(emotion_detector(" ") ),
            {"anger", "disgust", "fear", "joy", "sadness", "dominant_emotion"},
        )


if __name__ == "__main__":
    unittest.main()
