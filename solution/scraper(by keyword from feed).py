import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import date, datetime
from selenium.common.exceptions import NoSuchElementException

import time
import os
import pandas as pd
import csv

#Set personal info to use on linkedin.
email = 'superMark2058@gmail.com'
password = 'ToTo20000508'
#Set keyword id to scraping.

if __name__ == '__main__':
    driver = uc.Chrome(driver_executable_path=ChromeDriverManager().install())

    #Sign in linkedin with email address and password.
    driver.get('https://www.linkedin.com/checkpoint/lg/sign-in-another-account')
    input_email = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]'))).send_keys(email)
    input_password = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys(password)
    signin = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="organic-div"]/form/div[3]/button'))).click()
    time.sleep(1)



    
    driver.get('https://www.linkedin.com/posts/thomasdussud_please-explain-your-motivations-for-applying-activity-7100144420817129472-vl2A/?utm_source=share&utm_medium=member_desktop')
    time.sleep(3)
    # write search windows
    # WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="global-nav-typeahead"]/input'))).send_keys(keyword)
    # press enter
    # WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="global-nav-typeahead"]/input'))).send_keys(Keys.ENTER)

    # WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, f"//div[@class='scaffold-finite-scroll__content']/div[{lump}]/div/ul/li[{k}]/div/div/div/div[2]/a/div[3]/span[1]/span[1]/span[1]"))).text
    for i in range(0, 10):
        WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, '/html/body'))).send_keys(Keys.END)
        try:
            button_text = "Load more comments"  # Replace with the text of the button you want to find
            xpath_expression = f"//span[text()='{button_text}']"
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, xpath_expression))).click()
            print("pressed")
        except:
            print("cant find load more button")
        time.sleep(1)
    
    all_name_list = driver.find_elements(By.CLASS_NAME, 'comments-post-meta__name-text')
    # Define the data-attribute-index value you want to match
    js_script = '''
        mail_list=[]
        elements=document.querySelectorAll('a[href^="mailto:"]');
        elements.forEach(element=>{
            mail_list.push(element.textContent);
        });
        return mail_list;
    '''
    all_email_list = driver.execute_script(js_script)
    print(len(all_name_list))
    print(len(all_email_list))
    for i in range(0, len(all_name_list)):
        temp_name = all_name_list[i].text()
        temp_email = all_email_list[i].text()
        print(temp_name, temp_email)
        with open("result.txt", "a") as fp:
            fp.write(temp_name + " : " + temp_email)
            fp.write("\n")