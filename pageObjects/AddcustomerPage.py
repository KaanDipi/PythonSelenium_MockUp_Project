# A class that contains Adding a New Customer objects for test cases.

import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class AddCustomer:

# Web elements of add customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"

    txtcustomerRoles_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemForumModerators_xpath="//li[contains(text(),'Forum Moderators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"

    drpmgrOfVendor_xpath = "//select[@id='VendorId']"

    rdMaleGender_xpath = "//input[@id='Gender_Male']"
    rdFeMaleGender_xpath = "//input[@id='Gender_Female']"

    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"


# this is a constructor
    def __init__(self, driver):
        self.driver = driver

# action methods for web elements/locators
    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH,self.btnAddnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self,role):# CustomerRoles element contains list element but to select it we need to do something different
        self.driver.find_element(By.XPATH,self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role=='Administrators':
            listitem=self.driver.find_element(By.XPATH,self.lstitemAdministrators_xpath)
        elif role=='Guests':
            # Here user can be Registered( or) Guest, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        elif role=='Registered':
            listitem = self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)
        elif role=='Vendors':
            listitem = self.driver.find_element(By.XPATH,self.lstitemVendors_xpath)
        else:
            listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)
        time.sleep(3)
#self.listitem.click() --> sometime click action not work, use below one instead. this element is different..
        self.driver.execute_script("arguments[0].click();", listitem)

    def setManagerOfVendor(self,value): # Vendor element contains SELECT tag name..
        drp=Select(self.driver.find_element(By.XPATH,self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element(By.XPATH,self.rdMaleGender_xpath).click()
        elif gender=='Female':
            self.driver.find_element(By.XPATH,self.rdFeMaleGender_xpath).click()
        else:
            self.driver.find_element(By.XPATH,self.rdMaleGender_xpath).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.XPATH,self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.XPATH,self.txtLastName_xpath).send_keys(lname)

    def setDob(self, dob):
        self.driver.find_element(By.XPATH,self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH,self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()