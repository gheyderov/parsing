import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from test_case.page import MainPage


class HepsiburadaPrice(unittest.TestCase):
    
        def setUp(self):
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            self.driver.get("https://www.hepsiburada.com/skechers-claw-hammer-erkek-siyah-outdoor-ayakkabi-51595-bkgy-p-HBV000007I88B")
    
        def test_title(self):
            title = MainPage(self.driver).get_title()
            self.assertEqual(title, "Skechers Claw Hammer Erkek Siyah Outdoor Ayakkabı 51595 Bkgy")
    
        def tearDown(self):
            self.driver.close()