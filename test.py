import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=r'/home/acm/Downloads/geckodriver')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        print driver.title
        self.assertIn("Python", driver.title)
    def test_search_in_python_org1(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
    def test_search_in_python(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("JAVA", driver.title)
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()