#Imports
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui as pag
import time




def  main():
  url =  "http://linkedin.com/"
  network_url =  "http://linkedin.com/mynetwork/"
  driver = webdriver.Chrome("/Users/test/Downloads/chromedriver")
  start_bot(driver,url,network_url)

def login_to_linkedin(driver):
  username = driver.find_element_by_id("session_key")
  username.send_keys("chaseleffers1@gmail.com")
  password = driver.find_element_by_id("session_password")
  password.send_keys("11621162")
  driver.find_element_by_class_name("sign-in-form__submit-button").click()

def  goto_network_page(driver,network_url):
    driver.get(network_url)
"""
def  send_requests_to_users(driver):
    #WebDriverWait(driver, 60) #.until(EC.presence_of_element_located((By.CLASS_NAME, "class name of an element")))
    time.sleep(3)
    javaScript =  "window.scrollBy(0,2000);"
    driver.execute_script(javaScript)
    n =  4
    pag.click(1142, 256)
    #ph2 artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view
    #driver.find_element_by_class_name("artdeco-button--tertiary").click()
    #driver.find_elements_by_css_selector("[aria-label=See all People you may know from Northeastern University]").click()
    #driver.find_elements_by_css_selector("button[class*='ph2 artdeco-button artdeco-button--secondary']").click()
    time.sleep(.5)
    #WebDriverWait(driver, 60)
    for j in range(0, 4):
        #for i in  range(0, n):
        #    pag.click((360 + i*180), (530))
        pag.click(500, 500)
        javaScript =  "window.scrollBy(0,500);" #295
        driver.execute_script(javaScript)
    print("Done !")
    input()
"""

def  accept_invitations_from_users(driver):
  javaScript =  "window.scrollBy(0,0);"
  driver.execute_script(javaScript)
  element_exists =  True
  while element_exists:
    try:
      #driver.find_element_by_class_name("invitation-card__action-btn") #aria-label
      driver.find_element_by_class_name("full-width artdeco-button artdeco-button--2 artdeco-button--full artdeco-button--secondary ember-view")
    except NoSuchElementException:
      element_exists =  False
    finally :
      if element_exists:
        driver.find_element_by_class_name("full-width artdeco-button artdeco-button--2 artdeco-button--full artdeco-button--secondary ember-view").click()


def  start_bot(driver,url,network_url):
  driver.get(url)
  login_to_linkedin(driver)
  goto_network_page(driver, network_url)
  #send_requests_to_users(driver)
  send_requests_to_users_refresh(driver)
  #accept_invitations_from_users(driver)


def  send_requests_to_users_refresh(driver):
    time.sleep(3)
    javaScript =  "window.scrollBy(0,2000);"
    driver.execute_script(javaScript)
    n = 12
    pag.click(1197, 295)
    for z in range(0,n):
        for j in range(0, 2):
            for i in  range(0, 4):
                pag.click((503 + i*180), (547))
            javaScript =  "window.scrollBy(0,290);"
            driver.execute_script(javaScript)
        driver.get("http://linkedin.com/mynetwork/")
        time.sleep(3.5)
        #driver.execute_script("window.scrollBy(0,-4000);")
        driver.execute_script("window.scrollBy(0,2000);")
    print("Done !")
    input()


if __name__ == "__main__":
    main()



"""
<button aria-label="See all People you may know from Northeastern University" id="ember238" class="ph2 artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view" type="button"><!---->
<span class="artdeco-button__text">
    See all
</span></button>



<span class="artdeco-button__text">
    See all
</span>
"""