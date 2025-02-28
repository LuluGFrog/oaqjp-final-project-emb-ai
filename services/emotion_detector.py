from watson_nlp import EmotionDetection

def emotion_detector(text_to_analyze):
    # Import necessary libraries


    # Initialize the Emotion Detection service
    emotion_service = EmotionDetection()

    # Analyze the text
    response = emotion_service.analyze(text_to_analyze)

    # Return the text attribute of the response
    return response.text