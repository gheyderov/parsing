from test_case.locators import MainPageLocators

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    
class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.hepsiburada.com/skechers-claw-hammer-erkek-siyah-outdoor-ayakkabi-51595-bkgy-p-HBV000007I88B"
        self.title = MainPageLocators.TITLE
        self.parent_section = MainPageLocators.PARENT_SECTION
        self.driver.get(self.url)
        self.driver.implicitly_wait(5)

    def get_title(self):
        return self.driver.find_element(*self.title).text

    def get_parent_section(self):
        return self.driver.find_element(*self.parent_section)