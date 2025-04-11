@echo off
REM copy module folder and main.py to test folder
echo Copying modules...
xcopy /E /Y "..\module" "module\" >nul
echo Copying main.py...
echo F | xcopy /Y "..\main.py" "main.py" >nul

REM run test
echo Running tests...
python main.py
pause