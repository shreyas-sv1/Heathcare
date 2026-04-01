# 🚀 QUICK START GUIDE

## ⚡ Get Your Healthcare System Running in 5 Minutes!

### Prerequisites Check
- [ ] Java 17+ installed
- [ ] Gradle OR Maven installed  
- [ ] MySQL 8.0+ installed

Don't have these? See **Installation** section below.

---

## 🏃 FASTEST PATH TO RUNNING

### Option 1: Using Gradle (Recommended)

```powershell
# 1. Navigate to project
cd C:\Users\Arunkumar\Desktop\hc

# 2. Build the project
gradle build

# 3. Run the application
gradle bootRun

# 4. Open Swagger UI
# http://localhost:8080/swagger-ui.html
```

### Option 2: Using Gradle Wrapper

```powershell
# If gradle wrapper is configured:
./gradlew build
./gradlew bootRun
```

### Option 3: Run JAR directly

```powershell
# After building
java -jar build/libs/healthcare-app-1.0.0.jar
```

---

## 📦 INSTALLATION (If Tools Missing)

### Install Gradle (Windows)

**Option A: Chocolatey (Easiest)**
```powershell
# Install Chocolatey first if needed:
# https://chocolatey.org/install

choco install gradle
```

**Option B: Manual**
1. Download from https://gradle.org/releases/
2. Extract to C:\Gradle
3. Add to PATH: C:\Gradle\gradle-8.5\bin
4. Verify: `gradle --version`

### Install MySQL (Windows)

**Option A: Chocolatey**
```powershell
choco install mysql
```

**Option B: Installer**
1. Download MySQL Installer: https://dev.mysql.com/downloads/installer/
2. Run installer
3. Choose "Developer Default"
4. Set root password
5. Complete installation

### Install Java 17 (if needed)

```powershell
# Using Chocolatey
choco install openjdk17

# Verify
java -version
```

---

## 🗄️ DATABASE SETUP (First Time Only)

### Step 1: Start MySQL
```powershell
# Check if MySQL is running
mysql --version

# If not running, start service
net start MySQL80
```

### Step 2: Create Database
```powershell
# Open MySQL command line
mysql -u root -p

# In MySQL prompt:
CREATE DATABASE healthcare_db;
USE healthcare_db;
source C:/Users/Arunkumar/Desktop/hc/database/schema.sql
source C:/Users/Arunkumar/Desktop/hc/database/seed.sql
exit;
```

### Step 3: Update Database Password

Edit `src/main/resources/application.properties`:
```properties
spring.datasource.password=YOUR_MYSQL_PASSWORD
```

---

## ✅ VERIFICATION

### Test API with Swagger

1. **Start Application**
   ```powershell
   gradle bootRun
   ```

2. **Open Swagger UI**
   - URL: http://localhost:8080/swagger-ui.html

3. **Test Login Endpoint**
   - Find `POST /api/auth/login`
   - Click "Try it out"
   - Use credentials:
     ```json
     {
       "email": "admin@healthcare.com",
       "password": "admin123"
     }
     ```
   - Click "Execute"
   - Copy the JWT token from response

4. **Authorize Swagger**
   - Click "Authorize" button (🔒)
   - Enter: `Bearer YOUR_JWT_TOKEN`
   - Click "Authorize"

5. **Test Protected Endpoints**
   - Now all endpoints are accessible!

---

## 🌐 ACCESS FRONTEND

### Open in Browser

1. **Landing Page**
   ```
   C:\Users\Arunkumar\Desktop\hc\frontend\index.html
   ```

2. **Login Page**
   ```
   C:\Users\Arunkumar\Desktop\hc\frontend\login.html
   ```

3. **Test with default users:**
   - **Admin**: admin@healthcare.com / admin123
   - **Doctor**: doctor1@healthcare.com / doctor123
   - **Patient**: patient1@healthcare.com / patient123

---

## 🐛 TROUBLESHOOTING

### Problem: "gradle not recognized"
**Solution:** Install Gradle or add to PATH
```powershell
choco install gradle
```

### Problem: "Could not connect to database"
**Solution:** 
1. Check MySQL is running: `net start MySQL80`
2. Verify credentials in application.properties
3. Ensure database exists: `SHOW DATABASES;` in MySQL

### Problem: "Port 8080 already in use"
**Solution:** Change port in application.properties
```properties
server.port=8081
```

### Problem: "gradle build fails"
**Solution:** Clean and rebuild
```powershell
gradle clean
gradle build --refresh-dependencies
```

### Problem: "JWT secret too short"
**Solution:** Using default secret from application.properties (256-bit)
Already configured correctly!

---

## 📊 WHAT YOU GET

### API Endpoints (28+ endpoints)
- ✅ Authentication (register, login)
- ✅ Patient management (profile, appointments, prescriptions)
- ✅ Doctor management (appointments, prescriptions)
- ✅ Admin management (users, dashboard, statistics)

### Frontend Pages (7 pages)
- ✅ Landing page
- ✅ Registration
- ✅ Login
- ✅ Patient dashboard
- ✅ Doctor dashboard
- ✅ Admin dashboard
- ✅ Responsive CSS

### Database (7 tables)
- ✅ users, doctor_profiles, patient_profiles
- ✅ appointments, prescriptions, prescription_items
- ✅ medical_records

---

## 🔥 POWER USER TIPS

### Hot Reload Development
```powershell
# Terminal 1: Run with auto-restart
gradle bootRun --continuous

# Terminal 2: Make code changes
# Application restarts automatically!
```

### Run Tests
```powershell
# Run all tests
gradle test

# View test report
start build/reports/tests/test/index.html
```

### Check Dependencies
```powershell
gradle dependencies
```

### Generate Gradle Wrapper (if missing)
```powershell
gradle wrapper
```

---

## 📚 NEXT STEPS

### 1. Explore Swagger UI
- Test all endpoints
- Understand API structure
- Try different user roles

### 2. Customize Application
- Update JWT secret for production
- Modify database credentials
- Add more features

### 3. Deploy to Cloud
- Railway: https://railway.app
- Heroku: https://heroku.com
- AWS: https://aws.amazon.com

---

## 🎯 SUMMARY

**You have a complete healthcare management system with:**
- ✅ 80 generated files
- ✅ Spring Boot 3.2 backend
- ✅ JWT authentication
- ✅ MySQL database
- ✅ Swagger documentation
- ✅ Frontend UI
- ✅ Role-based access
- ✅ Unit tests

**Ready to run with just 3 commands:**
```powershell
gradle build
gradle bootRun
# Open http://localhost:8080/swagger-ui.html
```

**Need help?** Check PROJECT_COMPLETE.md for full documentation!

---

*Healthcare Appointment & Health Records System v1.0.0*
*Spring Boot 3.2 | MySQL 8.0 | JWT Authentication*
