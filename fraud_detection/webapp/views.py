from django.shortcuts import render
import joblib
import os
import numpy as np

def home(request):
    return render(request, 'webapp/home.html')

def prediction(request):
    if request.method == 'POST':
        try:
            # Load model
            model_path = os.path.join(os.path.dirname(__file__), 'model/fraud_model.pkl')
            model = joblib.load(model_path)

            # Collect all 28 inputs
            input_data = []
            for i in range(1, 29):  # input1 to input28
                field_value = float(request.POST.get(f'input{i}', 0))  # default to 0 if not found
                input_data.append(field_value)

            features = np.array([input_data])
            prediction = model.predict(features)[0]

            result = "⚠️ Fraud Detected!" if prediction == 1 else "✅ Legitimate Transaction"
            return render(request, 'webapp/result.html', {'result': result})

        except FileNotFoundError:
            return render(request, 'webapp/result.html', {'result': "❌ Model file not found!"})

        except Exception as e:
            return render(request, 'webapp/result.html', {'result': f"Error: {str(e)}"})

    return render(request, 'webapp/prediction.html')
