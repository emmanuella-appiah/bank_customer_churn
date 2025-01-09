import requests

url = "http://127.0.0.1:8501/predict"
data = {
    'credit_score': 619,
    'country': 'France',
    'Gender': 'Female',
    'age': 42,
    'tenure': 2,
    'balance': 0,
    'products_number': 1,
    'credit_card': 1,
    'active_member': 1,
    'estimated_salary': 101348
}

response = requests.post(url, json=data)

print("Response Status Code:", response.status_code)
print(response.json())

if response.json()['prediction'] == 0:
    print('Customer has not churned (not left the bank)')
else:
    print('Customer has churned (left the bank)')


# docker build -t ai-project .
# docker run -p 8501:8501 ai-project



