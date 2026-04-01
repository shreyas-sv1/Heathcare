@echo off
echo ========================================
echo Healthcare App - Java Files Generator
echo ========================================
echo.
echo Creating directory structure...
mkdir src\main\java\com\healthcare\app\repository 2>nul
mkdir src\main\java\com\healthcare\app\security 2>nul
mkdir src\main\java\com\healthcare\app\config 2>nul
mkdir src\main\java\com\healthcare\app\exception 2>nul
mkdir src\main\java\com\healthcare\app\dto\request 2>nul
mkdir src\main\java\com\healthcare\app\dto\response 2>nul
echo Directory structure created!
echo.
echo Now generating Java files...
node generate_all_java_files.js
echo.
echo ========================================
echo DONE! All Java source files created.
echo ========================================
pause
