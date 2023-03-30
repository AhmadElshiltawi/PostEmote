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

class TestSadReact():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_sadReact(self):
    self.driver.get("https://postemote.pythonanywhere.com/")
    self.driver.set_window_size(943, 1400)
    self.driver.find_element(By.CSS_SELECTOR, ".sad-button3bcd2ef0-5a6a-4f41-9527-b024d7186a6b").click()
    element = self.driver.find_element(By.LINK_TEXT, "Post an image")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
  