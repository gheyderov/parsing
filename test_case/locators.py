from selenium.webdriver.common.by import By

# for keeping locators in one place

class MainPageLocators(object):
    TITLE = (By.TAG_NAME, "h1")
    PARENT_SECTION = (By.XPATH, "../..")