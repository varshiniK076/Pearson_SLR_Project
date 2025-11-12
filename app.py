from flask import Flask, render_template, request
import numpy as np
import pickle  

app = Flask(__name__)

# Load your trained model
model = pickle.load(open('Pearson.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    try:
        father_height = float(request.form['Father'])
        prediction = model.predict([[father_height]])[0]
        output = f"Predicted Son's Height: {prediction:.2f} inches"
        return render_template('index.html', prediction_text=output)
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
