import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'  # URL of the sentiment analysis service

    
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed


    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}  # Set the headers required for the API request


    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers

    # we need the label and score from the response.text

    # return response.text  # Return the response text from the API

    # Convert the text to dictionary format
    json_reponse=json.loads(response.text)

    label=formatted_response['documentSentiment']['label']
    score=formatted_response['documentSentiment']['score']

    score_label_dict={
        'label' : label,
        'score' : score
    }

    return score_label_dict



sentiment_analyzer("I love this new technology")