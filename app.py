from flask import Flask, render_template, request
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Load the trained model
model = joblib.load('model/random_forest_model5.pkl')

features_order = ['Gender', 'Age', 'Height', 'Weight', 'family_history_with_overweight', 
                  'FAVC', 'FCVC', 'NCP', 'CAEC', 'SMOKE', 'CH2O', 'SCC', 
                  'FAF', 'TUE', 'CALC', 'MTRANS', 'BMI']

# Initialize label encoders for categorical variables
label_encoders = {
    'Gender': LabelEncoder(),
    'family_history_with_overweight': LabelEncoder(),
    'FAVC': LabelEncoder(),
    'CAEC': LabelEncoder(),
    'SMOKE': LabelEncoder(),
    'SCC': LabelEncoder(),
    'CALC': LabelEncoder(),
    'MTRANS': LabelEncoder()
}

# Fit label encoders on the original categories as per training data
label_encoders['Gender'].fit(['Male', 'Female'])
label_encoders['family_history_with_overweight'].fit(['yes', 'no'])
label_encoders['FAVC'].fit(['yes', 'no'])
label_encoders['CAEC'].fit(['no', 'Sometimes', 'Frequently', 'Always'])
label_encoders['SMOKE'].fit(['yes', 'no'])
label_encoders['SCC'].fit(['yes', 'no'])
label_encoders['CALC'].fit(['no', 'Sometimes', 'Frequently', 'Always'])
label_encoders['MTRANS'].fit(['Automobile', 'Bike', 'Motorbike', 'Public_Transportation', 'Walking'])

# Create a mapping from prediction
prediction_mapping = {
    0: ('Underweight', 'You are underweight. It is important to consult a healthcare provider to determine the cause and receive guidance on achieving a healthy weight.'),
    1: ('Normal_Weight', 'Your weight is normal. Continue maintaining a balanced diet and regular physical activity to stay healthy.'),
    2: ('Overweight_Level_I', 'You are slightly overweight. Consider increasing your physical activity and monitoring your diet to manage your weight.'),
    3: ('Obesity_Type_I', 'You have Obesity Type I. It is advisable to consult with a healthcare professional to develop a plan that includes diet, exercise, and potentially other treatments.'),
    4: ('Obesity_Type_II', 'You have Obesity Type II. This increases your risk of severe health issues like heart disease and diabetes. Please consult a healthcare provider for a comprehensive weight management plan.'),
    5: ('Obesity_Type_III', 'You have Obesity Type III, also known as severe or morbid obesity. Immediate medical intervention is recommended to manage your weight and reduce health risks.'),
    6: ('Overweight_Level_II', 'You are moderately overweight. Engaging in regular exercise and adopting a healthier diet can help manage your weight effectively.')
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            data = {
                'Gender': request.form['Gender'],
                'family_history_with_overweight': request.form['family_history_with_overweight'],
                'FAVC': request.form['FAVC'],
                'CAEC': request.form['CAEC'],
                'SMOKE': request.form['SMOKE'],
                'SCC': request.form['SCC'],
                'CALC': request.form['CALC'],
                'MTRANS': request.form['MTRANS'],
                'Age': float(request.form['Age']),
                'Height': float(request.form['Height']),
                'Weight': float(request.form['Weight']),
                'FCVC': float(request.form['FCVC']),
                'NCP': float(request.form['NCP']),
                'CH2O': float(request.form['CH2O']),
                'FAF': float(request.form['FAF']),
                'TUE': float(request.form['TUE'])
            }

            # Encode categorical features using fitted label encoders
            for feature, encoder in label_encoders.items():
                data[feature] = encoder.transform([data[feature]])[0]
                
            data['BMI'] = data['Weight'] / (data['Height'] ** 2)

            # Convert data into a DataFrame
            input_data = pd.DataFrame([data])

            # Reorder the DataFrame columns to match the training feature order
            input_data = input_data[features_order]

            # Predict using the trained model
            prediction_num = model.predict(input_data)[0]

            # Convert the numerical prediction to a text label and additional message
            prediction_label, health_message = prediction_mapping[prediction_num]

            return render_template('index.html', prediction_text=f'Predicted Obesity Risk Level: {prediction_label}', health_message=health_message)

        except KeyError as e:
            return f"Missing form field: {e}", 400
        except Exception as e:
            return str(e), 500

if __name__ == '__main__':
    app.run(debug=True)
