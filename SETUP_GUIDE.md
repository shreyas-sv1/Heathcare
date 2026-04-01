# HEALTHCARE APPLICATION - COMPLETE SETUP GUIDE

## 📋 OVERVIEW
This is a complete Patient Appointment & Health Records System built with Spring Boot 3, MySQL 8, and Vanilla JavaScript.

---

## 🚀 QUICK START (3 Steps)

### Step 1: Generate All Source Files
```batch
# Double-click BUILD.bat
# OR run in command prompt:
python build_all.py
```

This creates:
- All Java source files (Entities, Services, Controllers, Security, DTOs)
- Database SQL scripts
- Frontend HTML/CSS/JS files
- Unit tests

### Step 2: Setup Database
```sql
# Login to MySQL
mysql -u root -p

# Create database and run scripts
CREATE DATABASE healthcare_db;
USE healthcare_db;
source C:/Users/Arunkumar/Desktop/hc/database/schema.sql
source C:/Users/Arunkumar/Desktop/hc/database/seed.sql

# Verify
SELECT COUNT(*) FROM users;
```

### Step 3: Configure & Run
```batch
# Edit application.properties with your MySQL credentials
# Then run:
gradlew.bat bootRun
```

**Access:**
- API: http://localhost:8080
- Swagger: http://localhost:8080/swagger-ui.html
- Frontend: Open `frontend/index.html` in browser

---

## 📁 PROJECT STRUCTURE

```
healthcare-app/
├── src/main/java/com/healthcare/app/
│   ├── HealthcareApplication.java      # Main class
│   │
│   ├── entity/                         # JPA Entities
│   │   ├── User.java
│   │   ├── DoctorProfile.java
│   │   ├── PatientProfile.java
│   │   ├── Appointment.java
│   │   ├── Prescription.java
│   │   ├── PrescriptionItem.java
│   │   └── MedicalRecord.java
│   │
│   ├── repository/                     # Data Access
│   │   ├── UserRepository.java
│   │   ├── DoctorProfileRepository.java
│   │   ├── PatientProfileRepository.java
│   │   ├── AppointmentRepository.java
│   │   ├── PrescriptionRepository.java
│   │   └── MedicalRecordRepository.java
│   │
│   ├── service/                        # Business Logic
│   │   ├── AuthService.java
│   │   ├── PatientService.java
│   │   ├── DoctorService.java
│   │   ├── AppointmentService.java
│   │   ├── PrescriptionService.java
│   │   ├── AdminService.java
│   │   └── impl/                       # Implementations
│   │       ├── AuthServiceImpl.java
│   │       ├── PatientServiceImpl.java
│   │       ├── DoctorServiceImpl.java
│   │       ├── AppointmentServiceImpl.java
│   │       ├── PrescriptionServiceImpl.java
│   │       └── AdminServiceImpl.java
│   │
│   ├── controller/                     # REST APIs
│   │   ├── AuthController.java
│   │   ├── PatientController.java
│   │   ├── DoctorController.java
│   │   ├── AppointmentController.java
│   │   ├── AdminController.java
│   │   └── PublicController.java
│   │
│   ├── dto/                           # Data Transfer Objects
│   │   ├── request/                   # Request DTOs
│   │   │   ├── RegisterRequest.java
│   │   │   ├── LoginRequest.java
│   │   │   ├── UpdatePatientProfileRequest.java
│   │   │   ├── CreateDoctorRequest.java
│   │   │   ├── BookAppointmentRequest.java
│   │   │   ├── UpdateAppointmentStatusRequest.java
│   │   │   ├── CreatePrescriptionRequest.java
│   │   │   └── PrescriptionItemRequest.java
│   │   │
│   │   └── response/                  # Response DTOs
│   │       ├── AuthResponse.java
│   │       ├── UserResponse.java
│   │       ├── DoctorResponse.java
│   │       ├── PatientProfileResponse.java
│   │       ├── AppointmentResponse.java
│   │       ├── PrescriptionResponse.java
│   │       ├── PrescriptionItemResponse.java
│   │       ├── MedicalRecordResponse.java
│   │       ├── DashboardResponse.java
│   │       └── ErrorResponse.java
│   │
│   ├── security/                      # Security & JWT
│   │   ├── JwtUtil.java              # Token generation/validation
│   │   ├── JwtFilter.java            # Request filter
│   │   └── UserDetailsServiceImpl.java
│   │
│   ├── config/                        # Configuration
│   │   ├── SecurityConfig.java       # Spring Security
│   │   └── SwaggerConfig.java        # API documentation
│   │
│   ├── exception/                     # Exception Handling
│   │   ├── ResourceNotFoundException.java
│   │   ├── BadRequestException.java
│   │   ├── UnauthorizedException.java
│   │   ├── DuplicateResourceException.java
│   │   └── GlobalExceptionHandler.java
│   │
│   └── enums/                         # Enumerations
│       ├── Role.java                 # PATIENT, DOCTOR, ADMIN
│       ├── AppointmentStatus.java    # SCHEDULED, CONFIRMED, etc.
│       ├── Gender.java               # MALE, FEMALE, OTHER
│       └── RecordType.java           # LAB_REPORT, PRESCRIPTION, etc.
│
├── src/main/resources/
│   └── application.properties         # Configuration
│
├── src/test/java/                     # Unit Tests
│   └── com/healthcare/app/service/
│       ├── AppointmentServiceTest.java
│       ├── AuthServiceTest.java
│       └── PrescriptionServiceTest.java
│
├── frontend/                          # Frontend Files
│   ├── styles.css                    # Styling
│   ├── index.html                    # Landing page
│   ├── register.html                 # Registration
│   ├── login.html                    # Login
│   ├── patient-dashboard.html        # Patient portal
│   ├── doctor-dashboard.html         # Doctor portal
│   └── admin-dashboard.html          # Admin portal
│
├── database/                          # SQL Scripts
│   ├── schema.sql                    # Database schema
│   ├── seed.sql                      # Sample data
│   ├── drop_all.sql                  # Cleanup script
│   └── verify.sql                    # Verification queries
│
├── build.gradle                       # Dependencies
├── settings.gradle                    # Project settings
├── gradlew.bat                        # Gradle wrapper
├── BUILD.bat                          # Master build script
└── README.md                          # Documentation
```

---

## 🔐 DEFAULT CREDENTIALS

**Admin:**
- Email: admin@healthcare.com
- Password: admin123

**Doctor:**
- Email: doctor1@healthcare.com
- Password: doctor123

**Patient:**
- Email: patient1@healthcare.com
- Password: patient123

---

## 🛠 DETAILED SETUP

### Prerequisites
- Java 17 or higher
- MySQL 8.0 or higher
- Python 3.7+ (for generation scripts)
- Gradle (wrapper included)

### Configuration

Edit `src/main/resources/application.properties`:

```properties
# Update these:
spring.datasource.username=YOUR_MYSQL_USERNAME
spring.datasource.password=YOUR_MYSQL_PASSWORD
jwt.secret=YOUR_SECURE_SECRET_KEY_256_BITS_MINIMUM
```

### Build Commands

```batch
# Clean build
gradlew.bat clean build

# Run application
gradlew.bat bootRun

# Run tests
gradlew.bat test

# Skip tests
gradlew.bat build -x test
```

---

## 📡 API ENDPOINTS

### Public (No Authentication)
- `POST /api/auth/register` - Patient registration
- `POST /api/auth/login` - User login
- `GET /api/doctors` - List all doctors
- `GET /api/doctors/{id}` - Get doctor details

### Patient Endpoints (PATIENT role)
- `GET /api/patients/profile` - Get profile
- `PUT /api/patients/profile` - Update profile
- `POST /api/appointments` - Book appointment
- `GET /api/appointments/mine` - My appointments
- `PUT /api/appointments/{id}/cancel` - Cancel appointment
- `GET /api/prescriptions/mine` - My prescriptions
- `GET /api/medical-records/mine` - My medical records

### Doctor Endpoints (DOCTOR role)
- `GET /api/doctor/appointments` - My appointments
- `PUT /api/appointments/{id}/status` - Update status
- `POST /api/prescriptions` - Create prescription
- `GET /api/patients/{id}/history` - Patient history

### Admin Endpoints (ADMIN role)
- `POST /api/admin/doctors` - Create doctor
- `DELETE /api/admin/doctors/{id}` - Delete doctor
- `GET /api/admin/appointments` - All appointments
- `GET /api/admin/patients` - All patients
- `GET /api/admin/dashboard` - Statistics

---

## 🧪 TESTING

### Run All Tests
```batch
gradlew.bat test
```

### Test Coverage
- AppointmentService: 8 tests
- AuthService: 5 tests
- PrescriptionService: 4 tests

### Manual API Testing
1. Login via Swagger UI
2. Copy JWT token
3. Click "Authorize" button
4. Enter: `Bearer YOUR_JWT_TOKEN`
5. Test endpoints

---

## 🌐 FRONTEND USAGE

1. **Start Backend:** `gradlew.bat bootRun`
2. **Open:** `frontend/index.html` in browser
3. **Login** with credentials above
4. **Dashboard** auto-routes based on role

### Features:
- **Patient:** Book appointments, view prescriptions
- **Doctor:** Manage schedule, write prescriptions
- **Admin:** Add doctors, view statistics

---

## 📊 DATABASE SCHEMA

### Tables (7):
1. **users** - All system users
2. **doctor_profiles** - Doctor details
3. **patient_profiles** - Patient details
4. **appointments** - Appointment bookings
5. **prescriptions** - Prescriptions issued
6. **prescription_items** - Medicine details
7. **medical_records** - Medical documents

### Key Relationships:
- User → DoctorProfile (1:1)
- User → PatientProfile (1:1)
- Appointment → Prescription (1:1)
- Prescription → PrescriptionItems (1:Many)

---

## 🐛 TROUBLESHOOTING

### Port 8080 Already in Use
```properties
# Change in application.properties:
server.port=8081
```

### MySQL Connection Failed
1. Check MySQL is running
2. Verify credentials in application.properties
3. Ensure database exists: `CREATE DATABASE healthcare_db;`

### Gradle Build Failed
```batch
# Clean and rebuild:
gradlew.bat clean build --refresh-dependencies
```

### Frontend Not Connecting
1. Check backend is running: http://localhost:8080/api-docs
2. Verify CORS is enabled in SecurityConfig
3. Check JWT token in browser localStorage

---

## 📚 TECHNOLOGIES USED

**Backend:**
- Spring Boot 3.2
- Spring Security + JWT
- Spring Data JPA + Hibernate
- MySQL 8
- Gradle
- Lombok
- Swagger/OpenAPI 3

**Frontend:**
- HTML5
- CSS3
- Vanilla JavaScript (ES6+)
- Fetch API

**Testing:**
- JUnit 5
- Mockito
- AssertJ

---

## 📝 BUSINESS RULES

1. ✅ No duplicate appointments (same doctor, date, time)
2. ✅ Only SCHEDULED/CONFIRMED appointments can be cancelled
3. ✅ Prescriptions only for COMPLETED appointments
4. ✅ Doctors created by ADMIN only
5. ✅ Appointment date must be future
6. ✅ Booking respects doctor's available days
7. ✅ Duplicate email returns 409 Conflict

---

## 🔒 SECURITY FEATURES

- BCrypt password hashing (10 rounds)
- JWT token authentication (24hr expiration)
- Role-based access control (@PreAuthorize)
- Request filtering (JwtFilter)
- CORS configuration
- Stateless sessions
- Password never logged

---

## 📈 FUTURE ENHANCEMENTS

- Email notifications
- SMS reminders
- Payment integration
- Video consultations
- File upload for medical records
- Appointment reminders
- Rating system for doctors
- Search and filtering
- Export reports (PDF)

---

## 📄 LICENSE

MIT License - Free for portfolio/educational use

---

## 👨‍💻 SUPPORT

For issues or questions:
1. Check QUICKSTART.txt
2. Review error logs in console
3. Verify database schema
4. Check Swagger UI documentation

---

## ✅ GENERATION CHECKLIST

After running `BUILD.bat`, verify these were created:

### Java Files (44 files):
- [ ] 4 Enums
- [ ] 7 Entities
- [ ] 6 Repositories
- [ ] 3 Security classes
- [ ] 2 Config classes
- [ ] 5 Exceptions
- [ ] 8 Request DTOs
- [ ] 10 Response DTOs
- [ ] 6 Service interfaces
- [ ] 6 Service implementations
- [ ] 6 Controllers
- [ ] 3 Test files

### Database Files (4 files):
- [ ] schema.sql
- [ ] seed.sql
- [ ] drop_all.sql
- [ ] verify.sql

### Frontend Files (7 files):
- [ ] styles.css
- [ ] index.html
- [ ] register.html
- [ ] login.html
- [ ] patient-dashboard.html
- [ ] doctor-dashboard.html
- [ ] admin-dashboard.html

---

**🎉 You're all set! Happy coding!**
