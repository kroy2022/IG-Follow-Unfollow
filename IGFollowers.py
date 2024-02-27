from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium import webdriver

class HomePage:
    def __init__(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
        self.browser = webdriver.Firefox()
        self.browser.get('https://www.instagram.com/')
        self.login()
    
    def login(self):
        username_input = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_input = self.browser.find_element(By.NAME, "password")

        username_input.clear()  
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        login_button = self.browser.find_element(By.XPATH, "//button[contains(., 'Log in')]")        
        login_button.click()

        sleep(5)
        self.profile()

    def profile(self):
        profile_button = self.browser.find_element(By.XPATH, "//span[contains(text(), 'Profile')]")
        profile_button.click()

        sleep(3)

        followers_button = self.browser.find_element(By.CSS_SELECTOR, "li.xl565be.x1m39q7l.x1uw6ca5.x2pgyrj > a.x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._alvs._a6hd")
        following_button = self.browser.find_element(By.CSS_SELECTOR, "a.x1i10hfl.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._alvs._a6hd")

        followers_button.click()
        print("clicked follower button")

        
        followers_list = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "._aano > div:nth-child(1) > div:nth-child(1)"))
        )
        print("after follower list")
        followers = []

        follower_elements = followers_list.find_elements(By.CSS_SELECTOR, "div.x1dm5mii")

        print("after follower elements")
        for follower_element in followers_list:
            username_span = follower_element.find_element(By.CSS_SELECTOR, "span._ap3a._aaco._aacw._aacx._aad7._aade")
            username = username_span.text
            print(username)
            followers.append(username)

        for username in followers:
            print(username)

home = HomePage()