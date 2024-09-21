# Import necessary libraries
import joblib
from flask import Flask, request, jsonify
from flask import request, Flask, redirect
from flask import render_template


# Create a Flask web app
# app = Flask(__name__)
app = Flask(__name__, template_folder='templates')


# Load the trained KNN model
# load project model here with proper path 
model = joblib.load('C:\\Users\\jadha\\OneDrive\\Desktop\\MLproject\\finalheart_disease.pkl')

# Define a route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
         # Get input data from the POST request
        data = request.get_json()
        age = data['age']
        sex = data['sex']
        cp = data['cp']
        trestbps = data['trestbps']
        chol = data['chol']
        fbs = data['fbs']
        restecg = data['restecg']
        thalach = data['thalach']
        exang = data['exang']
        oldpeak = data['oldpeak']
        slope = data['slope']
        ca = data['ca']
        thal = data['thal']

        # Make a prediction using the loaded model
        new_data = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
        prediction = model.predict(new_data)
       # prediction = model.predict(new_data)

        # Return the prediction as JSON
        return jsonify({'prediction': int(prediction[0])})

    except Exception as e:
        return jsonify({'error': str(e)})

# Define a home route for testing
# @app.route('/')
# def home():
#      return app.send_static_file('C:\\Users\\jadha\\OneDrive\\Desktop\\MLproject\\index.html')

@app.route('/')
def home():
    return render_template('index.html',homeIsActive=True,addNoteIsActive=False)
    #return "hello world"

    

port = 3000
# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True,port =3000)
