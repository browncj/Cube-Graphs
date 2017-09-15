import unittest
import time

from test_settings import TEST_URL, TestBrowser


class SiteVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = TestBrowser()

    def tearDown(self):
        self.browser.quit()

    def test_can_access_home_page(self):
        self.browser.get(TEST_URL)
        self.assertIn('solve', self.browser.title.lower())


    def test_charts_redirects_to_login(self):
        self.browser.get(TEST_URL + '/track/charts')
        self.assertIn('login', self.browser.page_source.lower())


    def test_can_start_timer_and_view_results_then_delete(self):
        self.browser.get(TEST_URL + '/timer')
        self.assertNotIn('00:01', self.browser.page_source)
        self.browser.find_element_by_id('main').click()
        time.sleep(1.1)
        self.browser.find_element_by_id('main').click()
        self.assertIn('00:01', self.browser.page_source)
        self.browser.find_element_by_id('delete').click()
        self.assertNotIn('00:01', self.browser.page_source)


    def test_scramble_updates_after_solve(self):
        self.browser.get(TEST_URL + '/timer')
        scramble1 = self.browser.find_element_by_class_name('scramble').text.strip()
        self.browser.find_element_by_id('main').click()
        self.browser.find_element_by_id('main').click()
        time.sleep(0.05)
        scramble2 = self.browser.find_element_by_class_name('scramble').text.strip()
        self.assertNotEqual(scramble1, scramble2)
