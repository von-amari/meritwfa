import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from flask import Flask
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


@app.route('/id/<proj_id>', methods=['GET'])
def running(proj_id):
    got_text = ""
    return_dict = {}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

    # browser = webdriver.Chrome(executable_path='C:/bin/chromedriver.exe')
    # service = Service(executable_path=ChromeDriverManager().install())
    # browser = webdriver.Chrome(service=service)

    url = 'https://merit3d.makeros.com/login'
    browser.get(url)
    secure_url = 'https://merit3d.makeros.com'
    email = "blake.merrell@merit3d.com",
    password = "Dustless1"
    project_url = "https://merit3d.makeros.com/projects/show/" + proj_id + "/billing"
    browser.find_element(by=By.ID, value="email").send_keys(email)
    browser.find_element(by=By.ID, value="password").send_keys(password)
    time.sleep(2)
    browser.find_element(by=By.CLASS_NAME, value="btn").click()
    time.sleep(2)
    browser.get(project_url)
    time.sleep(2)
    # browser.find_element(by=By.CLASS_NAME, value="project-title").click()
    # time.sleep(2)
    # browser.find_element(by=By.CLASS_NAME, value="bill").click()
    # time.sleep(2)
    parts = browser.find_element(by=By.CLASS_NAME, value="parts-content")
    time.sleep(2)
    icon_qty = parts.find_element(by=By.CLASS_NAME, value="parts-icon")
    return_dict["qty"] = icon_qty.text
    part_text = parts.find_elements(by=By.CLASS_NAME, value="parts-text")

    for i in range(len(part_text)):
        if i == 0:
            return_dict["name"] = part_text[i].text
        if i == 1:
            part_text[i].click()
            time.sleep(1)
            got_text = got_text + part_text[i].text
            return_dict["details"] = part_text[i].text
            print(got_text)
        if i == 2:
            return_dict["price"] = part_text[i].text
        if i == 3:
            return_dict["create_date"] = part_text[i].text
    # return json.dumps(data)

    print(return_dict)
    return return_dict

