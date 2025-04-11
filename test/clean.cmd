@echo off
REM switch to script folder
cd /d %~dp0

REM delete test files
for %%F in (*) do (
    if /i not "%%~nxF" == "config.json" (
        if /i not "%%~nxF" == "test.cmd" (
            if /i not "%%~nxF" == "clean.cmd" (
                del /q "%%F" 2>nul
            )
        )
    )
)

REM delete all child folder
for /d %%D in (*) do (
    rd /s /q "%%D" 2>nul
)

echo Clean completed.
pause