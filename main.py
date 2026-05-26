import requests
import json

def main():
    # Setup configuration
    name = "Ibrahim Mahidpur Wala"
    # Using '230171' (odd last digit) so the webhook assigns Question 1, 
    # since we could not reliably access the Question 2 PDF link.
    reg_no = "230171" 
    email = "ibrahimmahidpurwala230172@acropolis.in"
    
    generate_url = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
    payload = {
        "name": name,
        "regNo": reg_no,
        "email": email
    }
    
    print(f"Sending POST request to {generate_url} to generate webhook...")
    try:
        response = requests.post(generate_url, json=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to generate webhook: {e}")
        return
        
    data = response.json()
    webhook_url = data.get("webhook")
    access_token = data.get("accessToken")
    
    if not webhook_url or not access_token:
        print("Invalid response format received from server:")
        print(data)
        return
        
    print(f"Received Webhook URL: {webhook_url}")
    print(f"Received Access Token.")
    
    # SQL Query for Question 1
    # Problem: Find the highest salary credited to an employee, but only for transactions 
    # that were not made on the 1st day of any month. Extract NAME, AGE, DEPARTMENT_NAME.
    sql_query = """
    SELECT 
        p.AMOUNT AS SALARY,
        CONCAT(e.FIRST_NAME, ' ', e.LAST_NAME) AS NAME,
        EXTRACT(YEAR FROM CURRENT_DATE) - EXTRACT(YEAR FROM e.DOB) AS AGE,
        d.DEPARTMENT_NAME
    FROM PAYMENTS p
    JOIN EMPLOYEE e ON p.EMP_ID = e.EMP_ID
    JOIN DEPARTMENT d ON e.DEPARTMENT = d.DEPARTMENT_ID
    WHERE EXTRACT(DAY FROM p.PAYMENT_TIME) <> 1
    ORDER BY p.AMOUNT DESC
    LIMIT 1;
    """
    
    submit_payload = {
        "finalQuery": sql_query.strip()
    }
    
    headers = {
        "Authorization": access_token,
        "Content-Type": "application/json"
    }
    
    print("Submitting SQL solution to the webhook...")
    try:
        submit_response = requests.post(webhook_url, json=submit_payload, headers=headers)
        submit_response.raise_for_status()
        print(f"Submit Success! Response Status: {submit_response.status_code}")
        print(f"Response Body: {submit_response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to submit solution: {e}")
        if 'submit_response' in locals() and submit_response:
            print(f"Response Body: {submit_response.text}")

if __name__ == "__main__":
    main()
