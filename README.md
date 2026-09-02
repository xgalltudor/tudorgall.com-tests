# Test Automation for www.tudorgall.com

Automated regression tests for [www.tudorgall.com](https://www.tudorgall.com), covering three frameworks — all written in Python.

| Framework | Folder | Runner |
|---|---|---|
| Selenium + Pytest | `SeleniumTests/` | `python SeleniumTests/run.py` |
| Playwright + Pytest | `PlaywrightTests/` | `python PlaywrightTests/run.py` |
| Robot Framework | `RobotFrameworkTests/` | `robot RobotFrameworkTests/Tests/*.robot` |

Each framework covers the same 5 test modules:
- **TC001** — Navigate directly to each page
- **TC002** — Navigate between pages via header/footer links
- **TC003** — Inner element interaction (CTA buttons, social media links, contact info)
- **TC004** — CV PDF download link validation
- **TC005** — Contact form submission (empty, gradual, required fields only)

## Prerequisites

- Python 3.8+
- pip
- ChromeDriver (Selenium only — must match your installed Chrome version)

## Installation

Clone the repository, then install dependencies for whichever framework(s) you want to run.

### Selenium
```bash
pip install -r SeleniumTests/requirements.txt
```

### Playwright
```bash
pip install -r PlaywrightTests/requirements.txt
playwright install chromium
```

### Robot Framework
```bash
pip install -r RobotFrameworkTests/requirements.txt
```

## Running the tests

### Selenium
```bash
python SeleniumTests/run.py
```

### Playwright
```bash
python PlaywrightTests/run.py
```

### Robot Framework
```bash
robot RobotFrameworkTests/Tests/*.robot
```

## Contact

Tudor Gall — [xgalltudor@yahoo.com](mailto:xgalltudor@yahoo.com)
