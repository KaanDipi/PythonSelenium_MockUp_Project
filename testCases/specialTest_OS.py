# testing the os function
import os

# print(os.getcwd())
#
# path=os.path.dirname(os.getcwd())
# print(path)
# os.chdir(path)
# print(os.getcwd())
# print(os.listdir())
# os.chdir(path+'\\Logs')
# print(os.getcwd())
# print(os.listdir())

# # -------------------------

print(os.getcwd()) # cofig
print("----")
print(os.path.dirname(os.getcwd())) # main
print("----")
print(os.chdir(os.path.dirname(os.getcwd()))) # main
print("test")
print(os.getcwd()) # main