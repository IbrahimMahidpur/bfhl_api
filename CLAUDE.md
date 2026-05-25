# BFHL Qualifier 1 - Python Task

## Your Job
Run `main.py` with your actual credentials. It will:
1. Call the generateWebhook API with your details
2. Auto-detect which SQL question you get (odd/even regNo)
3. Submit the correct SQL query to the webhook
4. Print the final response

## Setup & Run

```bash
pip install requests
python main.py
```

## Customize Before Running
Open `main.py` and update these 3 fields at the top:

```python
NAME   = "Your Full Name"       # e.g. "Ravi Kumar"
REG_NO = "REG12347"             # your actual registration number
EMAIL  = "you@example.com"      # your actual email
```

## What Happens Automatically
- The script reads the last digit of your `REG_NO`
- **Odd digit** → submits the Q1 SQL (nth highest salary problem)
- **Even digit** → submits the Q2 SQL (department-wise salary analysis)
- Authorization token from step 1 is automatically passed to step 2

## Files
- `main.py` — the only file you need to run
- `CLAUDE.md` — this file
