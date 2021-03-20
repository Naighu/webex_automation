from requests.api import request
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import requests


class WebexAutomation:
    def __init__(self, url):
        self.driver = webdriver.Chrome(r"chromedriver.exe")
        self.url = url

    def _connect(self):
        try:
            self.driver.get(self.url)
        except:
            raise requests.exceptions.ConnectTimeout

    def joinMeeting(self, name, email):
        try:
            self._connect()
            # join in browser button
            WebDriverWait(self.driver, 8).until(EC.presence_of_element_located((
                By.XPATH, "/html/body/div[1]/div[3]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[3]/a")))
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div[3]/div/div[1]/div/div[2]/div[1]/div[2]/div[2]/div[3]/a").click()
            frame_xpath = "/html/body/div[2]/iframe"

            # switching i frame
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((
                By.XPATH, frame_xpath)))
            frame = self.driver.find_element_by_xpath(frame_xpath)
            self.driver.switch_to.frame(frame)
            time.sleep(2)

            # name text feild
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[2]/input").send_keys(name)

            # email id textfeild
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[3]/input").send_keys(email)

            # next button
            self.driver.find_element_by_xpath(
                "/html/body/div[1]/div/div[2]/div[4]/button").click()

            # # got it button
            # got_it_button = "/html/body/div[4]/div[2]/div/div/div/div/div[1]/button"
            # WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((
            #     By.XPATH, got_it_button)))
            # self.driver.find_element_by_xpath(
            #     got_it_button).click()

            # join meeting
            join = "/html/body/div[1]/div/div[3]/div[2]/span/button"
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((
                By.XPATH, join)))
            self.driver.find_element_by_xpath(
                join).click()

            return True,""
        except requests.exceptions.ConnectTimeout:
            return False,"Something went wrong check your internetConnection and tryagain"
        except requests.exceptions.ConnectionError:
            return  False,  "Something went wrong check your internetConnection and tryagain"
        except Exception as e:
            print(str(e))
            return  False,"Something went wrong"

    def close_meeting(self):
        # close meeting
        print("closing the connection")
        self.driver.close()

    def message(self, msg):
        try:
            chatBtn = "/html/body/div[3]/div[18]/div[2]/div[2]/div/button[2]/span[1]/i"
            WebDriverWait(self.driver, 8).until(
                EC.presence_of_element_located((By.XPATH, chatBtn)))
            self.driver.find_element_by_xpath(chatBtn).click()
            text_area = "/html/body/div[3]/div[4]/div/div/div/div[8]/div/div/div[3]/textarea"
            text_area_box = self.driver.find_element_by_xpath(text_area)
            text_area_box.send_keys(msg, Keys.ENTER)
            return True, "message"
        except Exception as e:
            print(str(e))
            return False, str(e)
