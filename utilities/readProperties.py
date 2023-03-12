# to read config.ini file
# used for reading common data and re-usability

#  to read data from .ini file, we need to set up some settings
import configparser
import os


config = configparser.RawConfigParser()
config.read((os.getcwd() + "\\Configurations\\config.ini"))
print("*********************test_readProperties"+os.getcwd())

class ReadConfig:

    # thanks to staticmethod, we can access the methods(getApplicationURL etc.)
    # directly by using class name and without creating an object, no need self
    # have a look at test_login> Test_001_Login
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'useremail')
        return username
#  -------
    # @staticmethod
    # def getPassword():
    #     password = config.get('common info', 'password')
    #     return password
    def getPassword(self):
        password = config.get('common info', 'password')
        return password


