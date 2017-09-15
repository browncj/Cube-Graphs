import unittest

from test_settings import TEST_URL, TestBrowser


class SiteVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = TestBrowser()

    def tearDown(self):
        self.browser.quit()

    def test_can_access_home_page(self):
        self.browser.get(TEST_URL)
        self.assertIn('solve', self.browser.title.lower())
