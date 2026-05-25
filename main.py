import requests
import sys

# ─────────────────────────────────────────────
#  UPDATE THESE THREE VALUES BEFORE RUNNING
# ─────────────────────────────────────────────
NAME   = "Ibrahim Mahidpur Wala"           # Your full name
REG_NO = "REG12347"           # Your registration number
EMAIL  = "ibrahmmahidpurwala230172@acropolis.in"   # Your email
# ─────────────────────────────────────────────

GENERATE_WEBHOOK_URL = "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON"
SUBMIT_URL           = "https://bfhldevapigw.healthrx.co.in/hiring/testWebhook/PYTHON"


# ── SQL Queries ───────────────────────────────────────────────────────────────
#
# Q1 (Odd last digit of regNo):
#   Find the 2nd highest salary among all employees.
#   Return NULL if it doesn't exist.
#   Table: WORKERS  columns: WORKER_ID, FIRST_NAME, LAST_NAME, SALARY, JOINING_DATE, DEPARTMENT
#
SQL_QUERY_ODD = """
SELECT MAX(SALARY) AS SecondHighestSalary
FROM WORKERS
WHERE SALARY < (SELECT MAX(SALARY) FROM WORKERS)
""".strip()

#
# Q2 (Even last digit of regNo):
#   For each department, find employees whose salary is >= the department average.
#   Return: DEPARTMENT, FIRST_NAME, SALARY, sorted by DEPARTMENT ASC, SALARY DESC.
#   Tables: WORKERS (same as above)
#
SQL_QUERY_EVEN = """
SELECT W.DEPARTMENT, W.FIRST_NAME, W.SALARY
FROM WORKERS W
JOIN (
    SELECT DEPARTMENT, AVG(SALARY) AS AVG_SALARY
    FROM WORKERS
    GROUP BY DEPARTMENT
) D ON W.DEPARTMENT = D.DEPARTMENT
WHERE W.SALARY >= D.AVG_SALARY
ORDER BY W.DEPARTMENT ASC, W.SALARY DESC
""".strip()


def get_last_digit(reg_no: str) -> int:
    """Extract the last numeric digit from a registration number string."""
    digits = [ch for ch in reg_no if ch.isdigit()]
    if not digits:
        raise ValueError(f"No digit found in regNo: {reg_no!r}")
    return int(digits[-1])


def step1_generate_webhook() -> tuple[str, str]:
    """POST to generateWebhook and return (webhook_url, access_token)."""
    print(f"\n[1] Calling generateWebhook API...")
    print(f"    name={NAME!r}  regNo={REG_NO!r}  email={EMAIL!r}")

    payload = {"name": NAME, "regNo": REG_NO, "email": EMAIL}
    try:
        resp = requests.post(GENERATE_WEBHOOK_URL, json=payload, timeout=30)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"    [X] HTTP error: {e}")
        print(f"    Response body: {resp.text}")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"    [X] Request failed: {e}")
        sys.exit(1)

    data = resp.json()
    print(f"    [OK] Response: {data}")

    webhook   = data.get("webhook") or data.get("webhookUrl") or data.get("url")
    token     = data.get("accessToken") or data.get("token") or data.get("access_token")

    if not webhook or not token:
        print(f"    [X] Could not parse webhook/token from response: {data}")
        sys.exit(1)

    print(f"    webhook      = {webhook}")
    print(f"    accessToken  = {token[:20]}...")
    return webhook, token


def step2_submit_answer(webhook_url: str, access_token: str, sql_query: str) -> None:
    """POST the final SQL query to the webhook URL."""
    print(f"\n[2] Submitting SQL answer to webhook...")
    print(f"    URL: {webhook_url}")
    print(f"    Query:\n{sql_query}\n")

    headers = {
        "Authorization": access_token,
        "Content-Type":  "application/json",
    }
    payload = {"finalQuery": sql_query}

    try:
        resp = requests.post(webhook_url, json=payload, headers=headers, timeout=30)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f"    [X] HTTP error: {e}")
        print(f"    Response body: {resp.text}")
        sys.exit(1)
    except requests.exceptions.RequestException as e:
        print(f"    [X] Request failed: {e}")
        sys.exit(1)

    print(f"    [OK] Status code : {resp.status_code}")
    try:
        print(f"    [OK] Response    : {resp.json()}")
    except Exception:
        print(f"    [OK] Response    : {resp.text}")


def main():
    # ── Determine which question applies ─────────────────────────────────────
    last_digit = get_last_digit(REG_NO)
    is_odd     = last_digit % 2 != 0
    question   = "Q1 (Odd)" if is_odd else "Q2 (Even)"
    sql_query  = SQL_QUERY_ODD if is_odd else SQL_QUERY_EVEN

    print("=" * 60)
    print("  BFHL Qualifier 1 - Python Submission")
    print("=" * 60)
    print(f"  regNo last digit : {last_digit}  ->  {question}")

    # ── Step 1: Get webhook + token ───────────────────────────────────────────
    webhook_url, access_token = step1_generate_webhook()

    # ── Step 2: Submit SQL answer ─────────────────────────────────────────────
    step2_submit_answer(webhook_url, access_token, sql_query)

    print("\n[OK] Done! Check the response above for confirmation.")


if __name__ == "__main__":
    main()
