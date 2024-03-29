# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCanCommentafterreacting():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_canCommentafterreacting(self):
    self.driver.get("https://postemote.pythonanywhere.com/")
    self.driver.set_window_size(943, 1400)
    self.driver.find_element(By.CSS_SELECTOR, ".happy-button3bcd2ef0-5a6a-4f41-9527-b024d7186a6b").click()
    self.driver.find_element(By.ID, "comment3bcd2ef0-5a6a-4f41-9527-b024d7186a6b").click()
    self.driver.find_element(By.ID, "comment3bcd2ef0-5a6a-4f41-9527-b024d7186a6b").send_keys("Hello world")
    self.driver.find_element(By.ID, "comment3bcd2ef0-5a6a-4f41-9527-b024d7186a6b").send_keys(Keys.ENTER)
  
