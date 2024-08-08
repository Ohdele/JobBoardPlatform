import requests

url = 'http://127.0.0.1:5000/login'
payload = {'username': 'testuser', 'password': 'testpassword'}

try:
    response = requests.post(url, json=payload)
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    response_json = response.json()
    print(f"Response JSON: {response_json}")
except requests.exceptions.RequestException as e:
    print(f"Request Exception: {e}")
except ValueError as e:
    print(f"JSON Decode Exception: {e}")
