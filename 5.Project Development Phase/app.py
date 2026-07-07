import numpy as np
import joblib
import os
from flask import Flask, request, render_template

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, 'models', 'model.pkl'))
scale = joblib.load(os.path.join(BASE_DIR, 'models', 'scaler.pkl'))


@app.route('/')  # rendering the html template
def home():
    return render_template('home.html')


@app.route('/predict', methods=["POST", "GET"])  # rendering the html template
def predict():
    return render_template('predict.html')


@app.route('/submit', methods=["POST", "GET"])  # route to show the predictions in a web UI
def submit():
    # reading the inputs given by the user
    input_feature = [float(x) for x in request.form.values()]
    input_feature = np.array(input_feature).reshape(1, -1)

    # scaling the input using the same scaler fit during training
    data_scaled = scale.transform(input_feature)

    # predictions using the loaded model file
    prediction = model.predict(data_scaled)
    print(prediction)
    prediction = int(prediction[0])
    print(type(prediction))

    if prediction == 0:
        return render_template("submit.html", result="Loan will Not be Approved")
    else:
        return render_template("submit.html", result="Loan will be Approved")
        # showing the prediction results in a UI


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 7860))
    app.run(host='0.0.0.0', port=port, debug=False)
