from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.op

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import time
import pandas as pd

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.asianpaints.com/catalogue/colour-catalogue.html')

a=1
c_va=[]
while a<9:
    time.sleep(0.3)
    try:
        btn=driver.find_element_by_css_selector("button.color-catalogue-revamp-list--loadMoreBtn")
        driver.execute_script("arguments[0].click();", btn)
        a=a+1
        print(a)
        print('clicked')
        # rgb_value=driver.find_element_by_class_name('color-catalogue-revamp-list--card').value_of_css_property('background-color')
        # c_va.append(rgb_value)
    except NoSuchElementException:
        print('exist')
        break
rgb_value=driver.find_element_by_class_name('color-catalogue-revamp-list--card').value_of_css_property('background-color')
print(rgb_value)
color_name=driver.find_elements_by_class_name('color-catalogue-revamp-list--colorName')
color_code=driver.find_elements_by_class_name('color-catalogue-revamp-list--colorCode')
print(c_va)
source=driver.page_source

for i,j in zip(color_name,color_code):
    print(i.text,j.text)
# job_details_df = pd.DataFrame(jobdetails)
# job_details_df.columns = ['title', 'company', 'location', 'summary', 'publish_date']
print(source)