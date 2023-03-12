if the code not work then check the Google Chrome version,  if needed then update chromedriver.exe file as per GoogleChrome version
--------------------------
Methods to run the project

1-
right click on python testcase file --> open in terminal --> pytest -v -s test_login.py

2-
right click on python testcase file --> open in terminal --> pytest -s -v  --html=Reports\report_login.html test_login.py

3-
right click on python testcase file --> open in terminal --> pytest -s -v -m "sanity" --html=./Reports/marker_tests.html testCases/ --browser chrome
(run the specific test case which is sanity test method)

4-
double click on run.bat file

-----------------------
