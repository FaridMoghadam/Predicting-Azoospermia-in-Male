# Imports
import pickle
import numpy as np
from flask import Flask, request, jsonify, render_template 

# Load model
model = pickle.load(open("model.pkl","rb")) 

# Create app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    
    # Get data from form
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    
    # Make prediction
    prediction = model.predict(final_features)

    # Map prediction to output labels
    output = "non-obstructive" if prediction[0] == 0 else "obstructive"


    return render_template('index.html', 
                           prediction_text="This Person is {}".format(output))

if __name__ == "__main__":
    app.run(debug=True)





    #1-1-1
    #1-1111-111
    #111-1111-1111