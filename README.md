# Login Page Automation Project

This project demonstrates a login page test automation setup using:
- Python
- Playwright
- Pytest
- Page Object Model (POM)

It includes:
- base page object
- login page object
- browser and page fixtures
- login happy-path and invalid-login tests

## Tech Stack
- Python 3.10+
- Playwright
- Pytest
- pytest-playwright (via Playwright Python package)

## Project Structure

```text
.
├── .gitignore
├── README.md
├── pytest.ini
├── requirements.txt
├── conftest.py
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   └── login_page.py
└── tests/
    └── test_login.py
```

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
python -m playwright install
```

3. Run tests:

```bash
pytest -q
```

## Example Login Page Used

This project uses the public demo login page from SauceDemo:

- URL: https://www.saucedemo.com/
- Standard user: `standard_user`
- Password: `secret_sauce`

## Notes

- POM keeps the UI selectors and actions separate from the test logic.
- Fixtures centralize browser creation and page setup.
- The sample tests verify both successful and unsuccessful login flows.
