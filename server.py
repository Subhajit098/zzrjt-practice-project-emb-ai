"""Executing this module initiates the application of sentiment
analysis to be executed over the Flask channel and deployed on
localhost:5000.
"""
# Import necessary modules from Flask and the sentiment analyzer
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# Initiate the Flask app
app = Flask(__name__)

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """This endpoint receives text from the HTML interface and 
    runs sentiment analysis over it using the sentiment_analyzer
    function. The output returned shows the label and its confidence 
    score for the provided text.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = sentiment_analyzer(text_to_analyze)

    label = response.get('label')
    score = response.get('score')

    if label is None:
        return "Invalid input! Try again"
    return f"The given text has been identified as {label} with a score of {score}"

@app.route("/")
def render_index_page():
    """This function renders the main application page."""
    return render_template("index.html")

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000 '''
    app.run(host="0.0.0.0", port=8000)
