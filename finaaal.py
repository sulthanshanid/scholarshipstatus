from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from seleniumwire import webdriver as wiredriver
from seleniumwire import webdriver as wiredriver
import mysql.connector
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium import webdriver
import requests
from selenium.webdriver.chrome.service import Service
import base64
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from lxml.html import soupparser
from selenium.webdriver.common.keys import Keys
from PIL import Image
import io
import mysql.connector
from Screenshot import Screenshot
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumwire import webdriver as wiredriver
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import shutil
import easyocr
import requests
from selenium import webdriver
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import selenium
from selenium import webdriver

# Replace with the path to your WebDriver executable (e.g., chromedriver for Chrome)
webdriver_path = 'C:\chromedriver.exe'
geckodriver_path = 'C:\geckodriver.exe'

# Start a browser session with Selenium Wire
options = {
    'proxy': {
        'http': 'http://localhost:8080',  # Replace with your proxy server
        'https': 'http://localhost:8080'
    }
}

# Disable GPU acceleration

# Start a browser session
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType

# Set up the proxy configuration
'''
proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = "http://127.0.0.1:8080"  # Replace with your Burp Proxy address and port
proxy.ssl_proxy = "http://127.0.0.1:8080"

# Configure the Selenium WebDriver to use the proxy
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--proxy-server=http://127.0.0.1:8080")  # Same proxy address as above
# Path to your Chrome WebDriver executable
  # Replace with the actual path

# Create a WebDriver instance with the proxy settings
driver = webdriver.Chrome(executable_path=webdriver_path, options=chrome_options)
'''
# Navigate to a website
# Replace with your target URL

# You can now interact with the webpage using Selenium
# For example, you can find elements, click buttons, or extract data.

# Remember to close the WebDriver when you're done


driver = webdriver.Chrome(executable_path=webdriver_path)
# service = Service(executable_path=geckodriver_path)

# Create Firefox WebDriver with the specified service
# driver = webdriver.Firefox(service=service)
'''
proxy = '127.0.0.1:8080'
os.environ['http_proxy'] = proxy
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy
os.environ['REQUESTS_CA_BUNDLE'] = "C:\\Users\\User\\Desktop\\cacert.pem"
'''
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="sch"
)

ob = Screenshot.Screenshot()
cursor = conn.cursor()

# SQL query to retrieve APPLID and PASSWORD from the User table
query = "SELECT APPLID, PASSWORD,NAME  FROM User "

# Execute the query
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()
# Print the results
for result in results:
    try:
        passed = 0
        applid, password, name = result

        print(f"NAME: {name} ,APPLID: {applid}, PASSWORD: {password}  ")
        applicationid = applid
        passwordd = password
        scheme = applicationid[2:6]


        while (passed == 0):

            driver.get('https://scholarships.gov.in/payl/loginPage.action')
            cookies = driver.get_cookies()

            # Create a session using the requests library
            session = requests.Session()
            for cookie in cookies:
                session.cookies.set(cookie['name'], cookie['value'])

            # Use the requests session for making HTTP requests

            select = Select(driver.find_element(By.ID, 'academicYear1'))
            select.select_by_index(1)
            if (scheme == "2022"):
               radioButtons = driver.find_element(By.CSS_SELECTOR, "input[value='F']")
            if (scheme == "2021"):
                radioButtons = driver.find_element(By.CSS_SELECTOR, "input[value='R']")
            radioButtons.click()

            inputElement = driver.find_element(By.XPATH,
                                               '/html/body/center/main/table/tbody/tr/td/div/div[2]/form/table/tbody/tr[3]/td[2]/input')
            inputElement.send_keys(applicationid)
            inputElement = driver.find_element(By.XPATH,
                                               '/html/body/center/main/table/tbody/tr/td/div/div[2]/form/table/tbody/tr[4]/td[2]/input')
            inputElement.send_keys(passwordd)
            captcha_image = driver.find_element(By.XPATH,
                                                '/html/body/center/main/table/tbody/tr/td/div/div[2]/form/table/tbody/tr[5]/td[2]/img[1]')  # Replace with the actual element locator

            # Get the image source URL
            captcha_image_url = captcha_image.get_attribute('src')

            # Open the image URL directly in the browser

            # Switch to the new tab

            image_content = session.get(captcha_image_url).content

            # Get the image content from the browser

            # Convert the image content to a Pillow image
            pillow_image = Image.open(io.BytesIO(image_content))

            # Save the image to a file
            pillow_image.save('captcha_image.png')

            # print('CAPTCHA image saved successfully')

            # Open the second website in the new tab
            # Replace with the URL of the second website

            # Close the new tab
            image_path = r'C:\Users\User\PycharmProjects\pythonProject\captcha_image.png'
            '''
            captchaurl = 'https://lens.google.com/upload?ep=ccm&s=csp&st=1653142987619'
            encoded_image = {'encoded_image': open(image_path, 'rb')}
            burp0cap_headers = {"Cache-Control": "max-age=0", "Upgrade-Insecure-Requests": "1",
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
                                "Origin": "null",
                                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                                "Sec-Gpc": "1", "Sec-Fetch-Site": "none",
                                "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1",
                                "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate",
                                "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}
            rlens = requests.post(captchaurl, files=encoded_image, headers=burp0cap_headers,
                                  allow_redirects=True)
            DATA000 = str(rlens.content)
            # print(DATA000)
            root = soupparser.fromstring(DATA000)
            result_url = root.xpath('//meta[@http-equiv="refresh"]/@content')
            result_url = str(result_url[0])
            url2 = result_url.split('URL=')
            finalurl = str(url2[1])
            # print(finalurl)
            r2 = requests.get(finalurl)
            r3 = str(r2.text)
            ty = "[[[[[[["
            res = r3.partition(ty)[2]
            resfinal = res[1:7]
            print(resfinal)
            '''


            def capture_full_page_screenshot() -> bytes:
                """Gets full page screenshot of the current window as a binary data."""
                metrics = driver.execute_cdp_cmd("Page.getLayoutMetrics", {})
                return base64.b64decode(
                    driver.execute_cdp_cmd(
                        "Page.captureScreenshot",
                        {
                            "clip": {
                                "x": 0,
                                "y": 0,
                                "width": metrics["contentSize"]["width"],
                                "height": metrics["contentSize"]["height"],
                                "scale": 1,
                            },
                            "captureBeyondViewport": True,
                        },
                    )["data"]
                )


            # Switch back to the original tab
            import easyocr

            # Create an OCR reader instance
            reader = easyocr.Reader(['en'])  # Specify the language(s) you want to use, e.g., 'en' for English

            # Load an image from file (replace 'image.png' with your image file)

            try:
                # Perform OCR on the image
                image = Image.open(image_path)

                # Display the image (opens with the default image viewer)

                result = reader.readtext(image_path)

                # Initialize an empty list to store the extracted text
                extracted_text = []

                # Extract text from the OCR result
                for detection in result:
                    text = detection[1]
                    text_without_spaces = text.replace(' ', '')
                    text_without_spaces = text.replace(' ', '')
                    # Remove spaces
                    extracted_text.append(text_without_spaces)

                # Combine the extracted text into a single string (if needed)
                extracted_text_str = ' '.join(extracted_text)

                # Print the extracted text
                print("Extracted text:", extracted_text_str)

            except Exception as e:
                print(f"An error occurred: {str(e)}")

            # Don't forget to close the reader when you're done

            resfinal = extracted_text_str.replace(' ', '')
            print(resfinal)

            driver.find_element(By.XPATH,
                                '//*[@id="chkCaptcha"]').send_keys(
                resfinal)

            js_code = """
                                    function test() {
                                        var capVal = document.getElementById("chkCaptcha").value;
                                        var url = "checkcaptcha.java?getCaptcha=" + capVal;
                                    
                                        var xmlHttp = new XMLHttpRequest();
                                        xmlHttp.withCredentials = true;
                                        xmlHttp.open("POST", url, false);  // Use synchronous (blocking) request
                                        xmlHttp.send(null);
                                    
                                        var captchaTest = xmlHttp.responseText;
                                    
                                        if (captchaTest > 0) {
                                            return '1';  // Return '1' if the test passes
                                        } else {
                                            return '0';  // Return '0' if the test fails
                                        }
                                    }
                                    
                                    return test();"""
            result = driver.execute_script(js_code)

            if result == '1':
                print("Pass")
            else:
                print("Fail")
                driver.close()
                driver = webdriver.Chrome(executable_path=webdriver_path)

            # Retrieve the result from local storage

            print(result)

            if (result == '1'):
                print("hi")
                passed = 1

        driver.execute_script('validatefrm();')
        time.sleep(10)
        screenshot_path = r'C:\Users\User\Documents\SCHOLARSHIP_FILES\SS\\' + applicationid + name+'.png'

        IMG = r"C:\Users\User\Documents\SCHOLARSHIP_FILES\SS\\" + applicationid + name+".png"
        STATUS = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/center/main/div/div/div/div[2]/div/center/main/div/div/div/div[1]/table/tbody/tr[3]/td[2]').text
        print(STATUS)
        if(scheme=="2022"):
          MERIT=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/center/main/div/div/div/div[2]/div/center/main/div/div/div/div[2]/div/table/tbody/tr[6]/td[2]").text
          if(MERIT!='No' ):

              print("Selected for Merit LIST"+MERIT)

              FRESHPAYMENT = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/center/main/div/div/div/div[2]/div/center/main/div/div/div/div[2]/div/table/tbody/tr[7]/td[2]").text
              print("Payment Processed "+FRESHPAYMENT)

              FRESHTOKEN=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/center/main/div/div/div/div[2]/div/center/main/div/div/div/div[4]/table/tbody/tr[2]/td[2]/b").text
              print("PFMS TOKEN "+FRESHTOKEN)


              FRESHAMOUNT=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/center/main/div/div/div/div[2]/div/center/main/div/div/div/div[4]/table/tbody/tr[2]/td[2]/b").text
              print("AMOUNT " +FRESHAMOUNT)

              FRESHPAYMENTSTATUS=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/center/main/div/div/div/div[2]/div/center/main/div/div/div/div[9]/table/tbody/tr[2]/td[2]").text
              print("PAYMENT STATUS "+FRESHPAYMENTSTATUS)
              sql = 'UPDATE User SET SELECTED = %s, PAYMENT_PROCCESSED = %s ,PFMSTOKEN= %s,AMOUNT= %s,PAYMENT_STATUS= %s WHERE APPLID = %s'
              val = (MERIT, FRESHPAYMENT,FRESHTOKEN,FRESHAMOUNT,FRESHPAYMENTSTATUS, applicationid)

              mycursor = conn.cursor()
              mycursor.execute(sql, val)
              conn.commit()
        if(scheme=="2021"):
            RENEWALPAYMENT=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/center/main/div/div/div/div[2]/div/center/main/div/div/div/div[2]/div/table/tbody/tr[5]/td[2]").text
            if(RENEWALPAYMENT!="No"):
                print("Payment Processed " + RENEWALPAYMENT)

                RENEWALTOKEN=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/center/main/div/div/div/div[2]/div/center/main/div/div/div/div[4]/table/tbody/tr[2]/td[2]/b").text
                print("PFMS TOKEN " + RENEWALTOKEN)

                RENEWALAMOUNT=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/center/main/div/div/div/div[2]/div/center/main/div/div/div/div[4]/table/tbody/tr[3]/td[2]").text
                print("AMOUNT " + RENEWALAMOUNT)
                RENEWALPAYMENTSTATUS=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div/center/main/div/div/div/div[2]/div/center/main/div/div/div/div[9]/table/tbody/tr[2]/td[2]/b").text
                print("PAYMENT STATUS " + RENEWALPAYMENTSTATUS)
                sql = 'UPDATE User SET  PAYMENT_PROCCESSED = %s ,PFMSTOKEN= %s,AMOUNT= %s,PAYMENT_STATUS= %s WHERE APPLID = %s'
                val = ( RENEWALPAYMENT, RENEWALTOKEN, RENEWALAMOUNT, RENEWALPAYMENTSTATUS, applicationid)
            # driver.save_full_page_screenshot(screenshot_path)
        screenshot_data = capture_full_page_screenshot()
        with open(screenshot_path, "wb") as screenshot_file:
            screenshot_file.write(screenshot_data)
        print(STATUS)
        sql = 'UPDATE User SET STATUS = %s, IMG = %s WHERE APPLID = %s'
        val = (STATUS, IMG, applicationid)

        mycursor = conn.cursor()
        mycursor.execute(sql, val)
        conn.commit()
    except Exception as e:
        print(f"An exception occurred for APPLID: {applid}, PASSWORD: {password}")
        print(f"Exception details: {str(e)}")
        continue

    # Close the browser session
driver.quit()