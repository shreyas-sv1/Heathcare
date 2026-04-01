# Java Source Files Generation Instructions

## Problem
PowerShell 7 (pwsh) is not installed on this system, which prevents automated script execution.

## Solution - Two Options

### Option 1: Install PowerShell 7 (Recommended)
1. Install PowerShell 7:
   ```
   winget install --id Microsoft.Powershell --source winget
   ```
   Or download from: https://aka.ms/powershell

2. Restart your terminal

3. Run:
   ```
   cd C:\Users\Arunkumar\Desktop\hc
   python setup_dirs.py
   python generate_files_part1.py
   ```

### Option 2: Use Batch File (Quick)
1. Double-click the file: `generate_java_files.bat`
   
   OR

2. Open Command Prompt and run:
   ```
   cd C:\Users\Arunkumar\Desktop\hc
   generate_java_files.bat
   ```

This will:
- Create all necessary directories
- Generate all 34 Java source files:
  - 6 Repository interfaces
  - 3 Security classes
  - 2 Configuration classes
  - 5 Exception classes
  - 8 Request DTOs
  - 10 Response DTOs

### Option 3: Run Python Script Directly
If Python is installed:
```
cd C:\Users\Arunkumar\Desktop\hc
python generate_all_java_files.py
```

### Option 4: Run Node.js Script Directly
If Node.js is installed:
```
cd C:\Users\Arunkumar\Desktop\hc
node generate_all_java_files.js
```

## Files Generated
After running any of the above options, you will have all Java source files in:
- `src/main/java/com/healthcare/app/repository/` (6 files)
- `src/main/java/com/healthcare/app/security/` (3 files)
- `src/main/java/com/healthcare/app/config/` (2 files)
- `src/main/java/com/healthcare/app/exception/` (5 files)
- `src/main/java/com/healthcare/app/dto/request/` (8 files)
- `src/main/java/com/healthcare/app/dto/response/` (10 files)

## Verification
After generation, verify the files were created:
```
dir /s /b src\main\java\com\healthcare\app\*.java
```

## Next Steps
1. Complete database setup (see QUICKSTART.txt)
2. Build the project: `gradlew.bat build`
3. Run the application: `gradlew.bat bootRun`

## Note
The generate_all_java_files.js and generate_all_java_files.py scripts have been created
and are ready to use. Both do exactly the same thing - use whichever runtime you have available.
