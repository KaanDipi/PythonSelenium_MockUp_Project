REM : comment for .bat file
REM to run this file, double click it


REM testCases/ --> RUN ALL TEST CASES WHICH ARE IN tesCases folder
REM testCases/test_login.py --> RUN ONLY test_login.py file which is in testCases

REM pytest -s -v -m "sanity" --html=Reports\report_sanity.html testCases/
REM pytest -s -v -m "regression" --html=Reports\report_sanity.html testCases/
REM pytest -s -v -m "sanity and regression" --html=Reports\report_sanity.html testCases/
REM pytest -s -v -m "sanity or regression" --html=Reports\report_sanity.html testCases/
pytest -s -v -m "sanity " --html=Reports\report_sanity_test.html testCases/test_login.py