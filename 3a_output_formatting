"""Emotion detection client for the Watson NLP service."""

import requests


SERVICE_URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"
EMPTY_RESULT = {
    "anger": None,
    "disgust": None,
    "fear": None,
    "joy": None,
    "sadness": None,
    "dominant_emotion": None,
}


def emotion_detector(text_to_analyse):
    """Return five emotion scores and the dominant emotion."""
    if not text_to_analyse or not str(text_to_analyse).strip():
        return EMPTY_RESULT.copy()

    response = requests.post(
        SERVICE_URL,
        json={"raw_document": {"text": text_to_analyse}},
        headers={"grpc-metadata-mm-model-id": MODEL_ID},
        timeout=30,
    )
    if response.status_code == 400:
        return EMPTY_RESULT.copy()
    response.raise_for_status()

    emotions = response.json()["emotionPredictions"][0]["emotion"]
    result = {emotion: emotions.get(emotion) for emotion in EMPTY_RESULT if emotion != "dominant_emotion"}
    result["dominant_emotion"] = max(result, key=lambda emotion: result[emotion])
    return result
