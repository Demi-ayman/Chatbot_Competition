from chat import get_response
from flask import Flask,render_template,request,jsonify


app =Flask(__name__)

@app.get("/")
def index_get():
    return render_template("base.html") 

@app.route("/predict", methods=["POST"])
def predict():
    text = request.get_json().get("message")

    # Error handling (optional):
    if not text:
        return jsonify({"error": "Please enter a message."}), 400  # Bad request

    response = get_response(text)  # Call your chatbot logic

    return jsonify({"answer": response})
if __name__ == "__main__":
    app.run(debug=True)

#from flask_cors import CORS
#CORS(app, origins=['http://127.0.0.1:5000/predict'])
#@app.route("/")
#def home():
#    return render_template("base.html")


#
#def predict():
#    text = request.get_json().get("message")

    # Error handling (optional):
#    if not text:
#        return jsonify({"error": "Please enter a message."}), 400  # Bad request

#    response = get_response(text)  # Call your chatbot logic

#    return jsonify({"answer": response})

#def get_response():
#    userText = request.args.get("msg")
#    return str(get_response(userText))