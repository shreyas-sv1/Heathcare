"""
Healthcare Application - File Generation Verification Script
Checks if all required files were created successfully
"""

import os
from pathlib import Path

def check_file(filepath, description):
    """Check if a file exists"""
    exists = os.path.exists(filepath)
    status = "✓" if exists else "✗"
    print(f"{status} {description:50} {'OK' if exists else 'MISSING'}")
    return exists

def main():
    print("""
╔══════════════════════════════════════════════════════════════╗
║        Healthcare Application - Verification Report         ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    base_java = "src/main/java/com/healthcare/app"
    base_test = "src/test/java/com/healthcare/app"
    
    all_ok = True
    
    # Core Configuration Files
    print("\n📋 Core Configuration Files:")
    all_ok &= check_file("build.gradle", "Build configuration")
    all_ok &= check_file("settings.gradle", "Project settings")
    all_ok &= check_file("src/main/resources/application.properties", "Application properties")
    all_ok &= check_file(f"{base_java}/HealthcareApplication.java", "Main application class")
    
    # Enums
    print("\n📝 Enum Classes (4):")
    enums = ["Role", "AppointmentStatus", "Gender", "RecordType"]
    for enum in enums:
        all_ok &= check_file(f"{base_java}/enums/{enum}.java", enum)
    
    # Entities
    print("\n🗃️  Entity Classes (7):")
    entities = ["User", "DoctorProfile", "PatientProfile", "Appointment", 
                "Prescription", "PrescriptionItem", "MedicalRecord"]
    for entity in entities:
        all_ok &= check_file(f"{base_java}/entity/{entity}.java", entity)
    
    # Repositories
    print("\n💾 Repository Interfaces (6):")
    repos = ["UserRepository", "DoctorProfileRepository", "PatientProfileRepository",
             "AppointmentRepository", "PrescriptionRepository", "MedicalRecordRepository"]
    for repo in repos:
        all_ok &= check_file(f"{base_java}/repository/{repo}.java", repo)
    
    # Security
    print("\n🔐 Security Classes (3):")
    security = ["JwtUtil", "JwtFilter", "UserDetailsServiceImpl"]
    for sec in security:
        all_ok &= check_file(f"{base_java}/security/{sec}.java", sec)
    
    # Configuration
    print("\n⚙️  Configuration Classes (2):")
    configs = ["SecurityConfig", "SwaggerConfig"]
    for config in configs:
        all_ok &= check_file(f"{base_java}/config/{config}.java", config)
    
    # Exceptions
    print("\n❌ Exception Classes (5):")
    exceptions = ["ResourceNotFoundException", "BadRequestException", 
                  "UnauthorizedException", "DuplicateResourceException",
                  "GlobalExceptionHandler"]
    for exc in exceptions:
        all_ok &= check_file(f"{base_java}/exception/{exc}.java", exc)
    
    # Request DTOs
    print("\n📨 Request DTOs (8):")
    requests = ["RegisterRequest", "LoginRequest", "UpdatePatientProfileRequest",
                "CreateDoctorRequest", "BookAppointmentRequest", 
                "UpdateAppointmentStatusRequest", "CreatePrescriptionRequest",
                "PrescriptionItemRequest"]
    for req in requests:
        all_ok &= check_file(f"{base_java}/dto/request/{req}.java", req)
    
    # Response DTOs
    print("\n📬 Response DTOs (10):")
    responses = ["AuthResponse", "UserResponse", "DoctorResponse", 
                 "PatientProfileResponse", "AppointmentResponse",
                 "PrescriptionResponse", "PrescriptionItemResponse",
                 "MedicalRecordResponse", "DashboardResponse", "ErrorResponse"]
    for resp in responses:
        all_ok &= check_file(f"{base_java}/dto/response/{resp}.java", resp)
    
    # Services
    print("\n🔧 Service Interfaces (6):")
    services = ["AuthService", "PatientService", "DoctorService",
                "AppointmentService", "PrescriptionService", "AdminService"]
    for svc in services:
        all_ok &= check_file(f"{base_java}/service/{svc}.java", svc)
    
    print("\n🛠️  Service Implementations (6):")
    for svc in services:
        all_ok &= check_file(f"{base_java}/service/impl/{svc}Impl.java", f"{svc}Impl")
    
    # Controllers
    print("\n🎮 Controller Classes (6):")
    controllers = ["AuthController", "PatientController", "DoctorController",
                   "AppointmentController", "AdminController", "PublicController"]
    for ctrl in controllers:
        all_ok &= check_file(f"{base_java}/controller/{ctrl}.java", ctrl)
    
    # Tests
    print("\n🧪 Test Classes (3):")
    tests = ["AppointmentServiceTest", "AuthServiceTest", "PrescriptionServiceTest"]
    for test in tests:
        all_ok &= check_file(f"{base_test}/service/{test}.java", test)
    
    # Database Files
    print("\n🗄️  Database Scripts (4):")
    db_files = ["schema.sql", "seed.sql", "drop_all.sql", "verify.sql"]
    for db_file in db_files:
        all_ok &= check_file(f"database/{db_file}", db_file)
    
    # Frontend Files
    print("\n🌐 Frontend Files (7):")
    frontend_files = [
        "styles.css",
        "index.html",
        "register.html",
        "login.html",
        "patient-dashboard.html",
        "doctor-dashboard.html",
        "admin-dashboard.html"
    ]
    for fe_file in frontend_files:
        all_ok &= check_file(f"frontend/{fe_file}", fe_file)
    
    # Summary
    print("\n" + "="*70)
    if all_ok:
        print("✓ SUCCESS: All files generated correctly!")
        print("\nNext Steps:")
        print("1. Update application.properties with MySQL credentials")
        print("2. Run: mysql -u root -p healthcare_db < database/schema.sql")
        print("3. Run: mysql -u root -p healthcare_db < database/seed.sql")
        print("4. Run: gradlew.bat bootRun")
        print("5. Open: http://localhost:8080/swagger-ui.html")
    else:
        print("✗ WARNING: Some files are missing!")
        print("\nTroubleshooting:")
        print("1. Re-run: python build_all.py")
        print("2. Check for error messages above")
        print("3. Verify Python is installed: python --version")
        print("4. Try running individual scripts manually")
    print("="*70)
    
    return 0 if all_ok else 1

if __name__ == "__main__":
    import sys
    sys.exit(main())
