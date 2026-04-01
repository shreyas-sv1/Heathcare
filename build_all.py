"""
Healthcare Application - Master Build Script
Executes all generation scripts in the correct order
"""

import subprocess
import sys
import os

def run_script(script_name, description):
    """Run a Python script and report status"""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"Script: {script_name}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(
            [sys.executable, script_name],
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        if result.stderr:
            print(f"Warnings: {result.stderr}")
        print(f"✓ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error running {script_name}:")
        print(e.stdout)
        print(e.stderr)
        return False
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return False

def main():
    """Execute all generation scripts"""
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║      Healthcare Application - Complete Build System         ║
    ║                                                              ║
    ║  This script will generate ALL source files for the         ║
    ║  Healthcare Management System                               ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    # Check if we're in the right directory
    if not os.path.exists('build.gradle'):
        print("ERROR: Please run this script from the project root directory")
        print("Expected: C:\\Users\\Arunkumar\\Desktop\\hc")
        sys.exit(1)
    
    scripts = [
        ("setup_dirs.py", "Create Directory Structure"),
        ("create_database_files.py", "Generate Database SQL Scripts"),
        ("generate_all_java_files.py", "Generate Core Java Files (Entities, Enums, Repos)"),
        ("generate_services.py", "Generate Service Layer"),
        ("generate_controllers.py", "Generate Controller Layer"),
        ("generate_tests.py", "Generate Unit Tests"),
        ("generate_frontend.py", "Generate Frontend Files"),
    ]
    
    results = []
    for script, description in scripts:
        if not os.path.exists(script):
            print(f"\n⚠ Warning: {script} not found, skipping...")
            results.append((description, False))
            continue
        
        success = run_script(script, description)
        results.append((description, success))
    
    # Print summary
    print("\n" + "="*60)
    print("BUILD SUMMARY")
    print("="*60)
    
    all_success = True
    for description, success in results:
        status = "✓ SUCCESS" if success else "✗ FAILED"
        print(f"{status:12} - {description}")
        if not success:
            all_success = False
    
    print("="*60)
    
    if all_success:
        print("""
    ✓ ALL GENERATION COMPLETED SUCCESSFULLY!
    
    Next steps:
    1. Update src/main/resources/application.properties with your MySQL credentials
    2. Create MySQL database: CREATE DATABASE healthcare_db;
    3. Run database schema: mysql -u root -p healthcare_db < database/schema.sql
    4. Run seed data: mysql -u root -p healthcare_db < database/seed.sql
    5. Build project: gradlew.bat build
    6. Run application: gradlew.bat bootRun
    7. Open http://localhost:8080/swagger-ui.html
    8. Open frontend/index.html in browser
    
    Default login:
    - Admin: admin@healthcare.com / admin123
    - Doctor: doctor1@healthcare.com / doctor123
    - Patient: patient1@healthcare.com / patient123
        """)
    else:
        print("""
    ⚠ SOME STEPS FAILED
    
    Please check the error messages above and fix any issues.
    You can run individual scripts manually:
    - python setup_dirs.py
    - python create_database_files.py
    - etc.
        """)
    
    return 0 if all_success else 1

if __name__ == "__main__":
    sys.exit(main())
