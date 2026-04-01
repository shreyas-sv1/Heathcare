@echo off
echo ========================================================
echo Healthcare Application - Complete Build System
echo ========================================================
echo.
echo This will generate all source files for your application.
echo.
echo Requirements:
echo - Python 3.7+ installed
echo - Internet connection (not required)
echo.
pause

python build_all.py

echo.
echo ========================================================
echo Build process completed!
echo ========================================================
echo.
echo Press any key to close...
pause >nul
