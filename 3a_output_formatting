"""Emotion detection application using Watson NLP."""

import json
import requests


def emotion_detector(text_to_analyse):
    """Call Watson NLP and return all emotion scores plus the dominant emotion."""
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    myobj = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=myobj, headers=headers)
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }
    res = json.loads(response.text)
    formatted_response = res["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(formatted_response, key=lambda emotion: formatted_response[emotion])
    formatted_response["dominant_emotion"] = dominant_emotion
    return formatted_response
