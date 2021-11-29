from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage


class LinksButtons(BasePage):
    HOME = (By.LINK_TEXT, 'Home')
    SEARCH = (By.XPATH, "//body/nav[1]/div[3]/ul[1]/li[1]/form[1]/div[1]/button[1]/*[1]")
    SEARCH_FIELD = (By.XPATH, "//div[@class='search expandable']//input[@placeholder='Type to search']")
    SERVICE_LINK = (By.XPATH, "//a[@href='https://www.tietoevry.com/en/services/']//div[@class='title']//span[@class='keyword'][normalize-space()='Services']")
    INDUSTRIES_LINK = (By.XPATH, "//a[@href='https://www.tietoevry.com/en/industries/']//div[@class='title']//span[@class='keyword'][normalize-space()='Industries']")
    ALL_NEWS_LINK = (By.XPATH, "//a[@href='https://www.tietoevry.com/en/newsroom/all-news-and-releases/']//div[@class='title']")
    ISG_FUTURE_OF_WORK = (By.XPATH, "//div[@class='container-fluid']//a[1]//div[1][1]//span[2]")
    SUCCESS_STORIES_LINK = (By.XPATH, "//div[@class='title']//span[@class='keyword'][normalize-space()='Success stories']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_page_title(self, title):
        return self.get_title(title)

    def home_btn(self):
        self.do_click(self.HOME)

    def service_link(self, services):
        self.do_click(self.SEARCH)
        self.do_send_keys(self.SEARCH_FIELD, services)
        self.do_click(self.SERVICE_LINK)

    def industries_link(self, industries):
        self.do_click(self.SEARCH)
        self.do_send_keys(self.SEARCH_FIELD, industries)
        self.do_click(self.INDUSTRIES_LINK)

    def all_news(self, news):
        self.do_click(self.SEARCH)
        self.do_send_keys(self.SEARCH_FIELD, news)
        self.do_click(self.ALL_NEWS_LINK)

    def isg_future_of_work(self, isg):
        self.do_click(self.SEARCH)
        self.do_send_keys(self.SEARCH_FIELD, isg)
        self.do_click(self.ISG_FUTURE_OF_WORK)

    def success_stories(self, success):
        self.do_click(self.SEARCH)
        self.do_send_keys(self.SEARCH_FIELD, success)
        self.do_click(self.SUCCESS_STORIES_LINK)
