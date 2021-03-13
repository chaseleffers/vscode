#Imports
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui as pag
import time


class Botbase: 


    def login(self, username ="chaseleffers1@gmail.com", password ="11621162" , html_sign_butt = "sign-in-form__submit-button", sesh_key = "session_key", el_id = "session_password"):
        self.username = self.driver.find_element_by_id(sesh_key)
        self.username.send_keys(username)
        self.password = self.driver.find_element_by_id(el_id)
        self.password.send_keys(password)
        self.driver.find_element_by_class_name(html_sign_butt).click()

    def scroll_by(self, y, x=0):
        self.javaScript =  "window.scrollBy(0,{0});".format(x)
        self.driver.execute_script(self.javaScript)

    def click_element(self, html_name, reps = 1, wait = 10000):
        #self.wait_until_found(html_name, wait)
        time.sleep(3)
        for x in range(0, reps):
            try:
                #self.driver.find_element_by_css_selector(html_name)
                #self.driver.find_element_by_css_selector(html_name).click()
                driver.find_element_by_css_selector("button.artdeco-button--secondary").click()
            except:
                print("error")
                break
                    
    
    def mouse_click(self, x, y):
        pag.click(x, y)


    def initialize_bot(self):
        self.driver = webdriver.Chrome("/Users/test/Downloads/chromedriver")

    def go_to(self, url):
        self.driver.get(url)

    def wait_until_found(self, element, max_wait = 1000):
        count = 0
        while True:
            try: 
                self.driver.find_element_by_css_selector(element)
                break
            except:
                count += 1
            if count == 10000:
                print("Error Finding Element")
                break




if __name__ == "__main__":
    print("window.scrollBy(0, {0});".format(2000))
    
    bot = Botbase()
    bot.initialize_bot()
    bot.go_to("http://linkedin.com/")
    bot.login()
    bot.go_to("http://linkedin.com/mynetwork/")
    time.sleep(3)
    bot.scroll_by(2000)
    bot.click_element("[aria-label~='to connect']")
    

# find_element_by_css_selector("[aria-label~='to connect']")
# driver.find_element_by_xpath("//button[@aria-label='invite']")
# driver.find_element_by_xpath("//button[@aria-label='invite']/div[@class='mn-hd-txt'][text()='Any time']");

"""
class="full-width artdeco-button artdeco-button--2 artdeco-button--full artdeco-button--secondary ember-view"
"""