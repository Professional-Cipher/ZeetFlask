from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from werkzeug.wrappers import response

app = Flask(__name__)


@app.route('/mybot', methods=['POST'])
def mybot():
    incoming_msg = request.values.get('Body', '').lower()

    resp = MessagingResponse()

    msg = resp.message()

    responded = False

    if 'hi' in incoming_msg:
        msg.body('Hello , I am your bot')
        responded = True

    if 'quote' in incoming_msg:
        r = request.get('http://api.quotable.io/random')

        if r.status_code == 200:
            data = r.json()
            quote = f"{data['content']} ({data['author']})"
        else:
            quote = 'Sorry, I am not able to get the quote'

        msg.body(quote)
        responded = True

    if not responded:
        msg.body("Hi, sorry unable to understand")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
