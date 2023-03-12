# Test case for adding a new customer

import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random
import os
from selenium.webdriver.common.by import By


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()

#    password = ReadConfig.getPassword()
#  OR -- without using  @staticmethod, we can use like this through creating an object
    password1 = ReadConfig()
    password = password1.getPassword()

    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Add Customer Test **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()

        self.logger.info("************* Providing customer info **********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Kaan")
        self.addcust.setLastName("Dipi")
        self.addcust.setDob("7/05/1985")  # Format: D / MM / YYY
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is for testing.........")
        time.sleep(10)
        self.addcust.clickOnSave()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

#  getting whatever message is displayed on the webpage and convert it into text format to check it
        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
#        print(self.msg)

        if 'customer has been added successfully.1' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:

#   changing the directory to save the file in specific folder
            #os.chdir(os.path.dirname(os.getcwd()))  # moving to main directory
            print("**********************************test_addCustomer" + os.getcwd())
            self.driver.get_screenshot_as_file(os.getcwd() + '\\Screenshots' + "\\AddCustomer_error.png")

            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))