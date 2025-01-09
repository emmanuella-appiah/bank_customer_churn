from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('churn_model.pkl', 'rb'))


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)
        input_data = pd.DataFrame([data])
        prediction = model.predict(input_data)
        model_prediction = int(prediction[0])
        return jsonify({'prediction': model_prediction})

    except KeyError as e:
        return jsonify({'error': f'Missing key in input data: {str(e)}'}), 400

    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8501)
