# ---------
# this file is created for a purpose that is valid every test cases

# if there is any pre-conditions script for any multiple test cases, called it as @pytest.fixture()
# it makes sense to create a file which is called as conftest..
# then we can invoke those parameters(duplication in multiple test cases) to make code look simple& clean
# avoid duplication
# ---------

import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#  changing the directory to choose driver
print(os.getcwd())
os.chdir(os.path.dirname(os.getcwd()))  # moving to main directory
print("**********************************test_Conftest"+os.getcwd())
Serv_obj=Service(os.getcwd() + '\\Drivers' + "\\chromedriver.exe")



# this is pre-condition that is used for many test cases. @pytest.fixture() is run first. then other test cases method
@pytest.fixture()
def setup(browser):

        if browser == 'chrome':
            driver = webdriver.Chrome(service=Serv_obj)
            print("Launching chrome browser.........")
        elif browser == 'firefox':
            driver = webdriver.Chrome(service=Serv_obj)  # u should convert it into .Firefox() for real project
            print("Launching firefox browser.........")
        else:
            driver = webdriver.Chrome(service=Serv_obj)  # for default browser would be internet expolor. should convert it into .Ie() for real project
        return driver


def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


########### pytest HTML Report ################

#  pytest -s -v -n=2 --html=Reports\report.html testCases/test_login.py --browser chrome


# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Kaan'

# It is hook for delete/Modify Environment info to HTML Report
@ pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)