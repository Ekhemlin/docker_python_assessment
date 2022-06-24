from flask import Flask, request
import utils

app = Flask(__name__)

@app.route('/detect_intent', methods = ['POST'])
def detectIntent():
    try:
        request_body = request.get_json(force=True) 
        if("message" in request_body):
            message = request_body["message"]
            intent = utils.getIntentFromSentence(message)
            body = {"Intent" : intent}
            status = 200
        else:
            body = {"Error" : "Missing argument 'message' in request body"}
            status = 422
        payload = utils.formatReturnPayload(body, status)
        return payload
    except Exception as e:
        body = {"Error" : str(e), "Message" : "Internal server error while detecting intent"}
        payload = utils.formatReturnPayload(body, 500)
        return(payload)

@app.route('/health')
def requestCustomerData():
    response = utils.formatReturnPayload({"Message" : "Service is functional"}, 200)
    return(response)


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8080)