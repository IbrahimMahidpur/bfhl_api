import os
import requests
from dotenv import load_dotenv

load_dotenv()

USER_NAME = os.getenv('USER_NAME')
REG_NO = os.getenv('REG_NO')
USER_EMAIL = os.getenv('USER_EMAIL')
API_BASE_URL = os.getenv('API_BASE_URL')

if not all([USER_NAME, REG_NO, USER_EMAIL, API_BASE_URL]):
    raise RuntimeError('Missing required environment variables')

payload = {
    "name": USER_NAME,
    "reg_no": REG_NO,
    "email": USER_EMAIL,
    "message": "Hello from BFHL Qualifier"
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(f"{API_BASE_URL}/generateWebhook/PYTHON", json=payload, headers=headers)

if response.status_code == 200:
    data = response.json()
    print('Success:', data)
else:
    print('Error:', response.status_code, response.text)
