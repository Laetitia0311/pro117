# import the necessary modules
from flask import Flask , render_template , request , jsonify

# importing sentiment_analysis file as sa
import sentiment_analysis as sa

app = Flask(__name__)

# app route for index page
@app.route('/')
def home():
    return render_template('index.html')

# Write a route for POST requests
@app.route('/analyze', methods=['POST'])
def analyze_review():
    # Extract the customer_review from the request data
    data = request.get_json()
    review = data.get('customer_review')

    # Check if the customer_review is empty; return an error if it is
    if not review:
        return jsonify({'status': 'error', 'message': 'Empty response'})

    # If the review is not empty, pass it through the 'predict' function
    sentiment, emoticon_path = sa.predict(review)

    # Return sentiment and emoticon path as JSON response
    return jsonify({'sentiment': sentiment, 'emoticon_path': emoticon_path})

    # predict function returns 2 things : sentiment and path of image in static folder
    # example : Positive , ./static/assets/emoticons/positive.png

    else:

        _ , _ = sa.predict(review)

        return jsonify({'':'' , '':''})


if __name__  ==  "__main__":
    app.run(debug = True)