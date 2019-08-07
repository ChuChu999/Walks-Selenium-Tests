# Walks-Selenium-Tests
Automated tests that simulate the checkout process for https://www.takewalks.com and https://www.walksofitaly.com

## Dependencies
**Python**
- `brew install python` to install Python
- `python3 --version` to check version and confirm a successful installation

**Selenium**
- `pip install selenium` to install the Selenium package for Python

**ChromeDriver**
- Download [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) according to your system's version of Google Chrome (find your Chrome version through Help -> About Google Chrome)
- Move the extracted chromedriver file to `/usr/local/bin`

**Additional Information**
- Reference the [Selenium with Python Documentation](https://selenium-python.readthedocs.io/installation.html) for more information on how to install the Selenium package for Python

## How to Run
- Open `test_tw.py` or `test_woi.py` in a text editor
- Modify the `test_name` parameter to select which test to run
- Modify the `environment` parameter to set the environment for the test
- `python3 [file_name]` in root directory to run the test
