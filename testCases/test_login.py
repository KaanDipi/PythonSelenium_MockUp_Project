# Test case for Login page

# ----------importing plugs
import pytest
import os
from selenium import webdriver

# ----------importing classes
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig



class Test_001_Login:

#  getting common data from file,
#  called by its name directly thanks to @staticmethod, otherswise we have to create object
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()

#    password = ReadConfig.getPassword()
#  OR -- without using  @staticmethod, we can use like this through creating an object
    password1 = ReadConfig()
    password = password1.getPassword()

#  called by its name directly thanks to @staticmethod, otherwise we have to create object
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_homePageTitle(self,setup):
# setup is in conftest.py, returning a driver, can be called directly W/o importing folder because of @pytest.fixture()


        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")

        self.driver=setup

        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)  # getting the webpage


        act_title=self.driver.title

        if act_title == "Your store. Login1":
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            assert True

        else:
            self.logger.error("**** Home page title test failed****")

# ---------  changing the directory to save the file in specific folder

#             path = os.path.dirname(os.getcwd())
#             os.chdir(path + '\\Screenshots')
#             print(os.getcwd())
#             self.driver.get_screenshot_as_file(os.getcwd() + "\\HomePageTitle_Error.png")

            print("**********************************test_homePage" + os.getcwd()) # previous  directory
            #print("2 ----: "+os.path.dirname(os.getcwd())) # checking where we are
            print("----")
            #os.chdir(os.path.dirname(os.getcwd())) # moving to main directory
            self.driver.get_screenshot_as_file(os.getcwd() + '\\Screenshots' + "\\HomePageTitle_Error.png")
            print("**********************************test_homePage"+os.getcwd()) # checking where we are
# -------------
            self.driver.close()
            assert False


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
# setup is in conftest.py, returning a driver, can be called directly W/o importing folder because of @pytest.fixture()

        self.logger.info("****Started Login Test****")
        self.driver=setup
        self.logger.info("****Opening URL****")

        self.driver.get(self.baseURL)

#  creating LoginPage object
        self.lp=LoginPage(self.driver)  # invoke the constructor

# accessing LoginPage actions & perform the actions
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("****Login test passed ****")
            self.driver.close()
            assert True

        else:
            self.logger.error("****Login test failed ****")

#   changing the directory to save the file in specific folder
#            print("**********************************test_login1" + os.getcwd())
#            os.chdir(os.path.dirname(os.getcwd()))  # moving to main directory
#            print("**********************************test_login1" + os.getcwd())
            self.driver.get_screenshot_as_file(os.getcwd() + '\\Screenshots' + "\\Login_Error.png")

            self.driver.close()
            assert False




