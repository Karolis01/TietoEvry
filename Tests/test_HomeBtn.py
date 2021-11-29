from Config.config import TestData
from Pages.LinksButtons import LinksButtons
from Tests.test_base import BaseTest


class TestHomeBtn(BaseTest):

    def test_service_link(self):
        self.linksButtons = LinksButtons(self.driver)
        self.linksButtons.service_link("services")
        service_title = self.linksButtons.get_page_title(TestData.SERVICE_TITLE)
        assert service_title == self.linksButtons.get_page_title(TestData.SERVICE_TITLE)
        self.linksButtons.home_btn()
        home_title = self.linksButtons.get_page_title(TestData.HOME_PAGE_TITLE)
        assert home_title == TestData.HOME_PAGE_TITLE

    def test_isg_future_of_work(self):
        self.linksButtons = LinksButtons(self.driver)
        self.linksButtons.isg_future_of_work("isg future of work")
        isg_title = self.linksButtons.get_page_title(TestData.FUTURE_OF_WORK_TITLE)
        assert isg_title == self.linksButtons.get_page_title(TestData.FUTURE_OF_WORK_TITLE)
        self.linksButtons.home_btn()
        home_title = self.linksButtons.get_page_title(TestData.HOME_PAGE_TITLE)
        assert home_title == TestData.HOME_PAGE_TITLE

    def test_industries_link(self):
        self.linksButtons = LinksButtons(self.driver)
        self.linksButtons.industries_link("industries")
        industries_title = self.linksButtons.get_page_title(TestData.INDUSTRIES_TITLE)
        assert industries_title == self.linksButtons.get_page_title(TestData.INDUSTRIES_TITLE)
        self.linksButtons.home_btn()
        home_title = self.linksButtons.get_page_title(TestData.HOME_PAGE_TITLE)
        assert home_title == TestData.HOME_PAGE_TITLE

    def test_all_news_link(self):
        self.linksButtons = LinksButtons(self.driver)
        self.linksButtons.all_news("all news")
        all_news_title = self.linksButtons.get_page_title(TestData.ALL_NEWS_TITLE)
        assert all_news_title == self.linksButtons.get_page_title(TestData.ALL_NEWS_TITLE)
        self.linksButtons.home_btn()
        home_title = self.linksButtons.get_page_title(TestData.HOME_PAGE_TITLE)
        assert home_title == TestData.HOME_PAGE_TITLE

    def test_success_stories_link(self):
        self.linksButtons = LinksButtons(self.driver)
        self.linksButtons.success_stories("success stories")
        success_stories_title = self.linksButtons.get_page_title(TestData.SUCCESS_STORIES_TITLE)
        assert success_stories_title == self.linksButtons.get_page_title(TestData.SUCCESS_STORIES_TITLE)
        self.linksButtons.home_btn()
        home_title = self.linksButtons.get_page_title(TestData.HOME_PAGE_TITLE)
        assert home_title == TestData.HOME_PAGE_TITLE
