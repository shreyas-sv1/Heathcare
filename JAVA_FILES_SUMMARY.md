# Healthcare Application - Java Source Files Summary

## Total Files to be Generated: 34

### Repository Layer (6 files)
Located in: `src/main/java/com/healthcare/app/repository/`

1. **UserRepository.java**
   - Extends: JpaRepository<User, Long>
   - Method: Optional<User> findByEmail(String email)

2. **DoctorProfileRepository.java**
   - Extends: JpaRepository<DoctorProfile, Long>
   - Method: Optional<DoctorProfile> findByUserId(Long userId)

3. **PatientProfileRepository.java**
   - Extends: JpaRepository<PatientProfile, Long>
   - Method: Optional<PatientProfile> findByUserId(Long userId)

4. **AppointmentRepository.java**
   - Extends: JpaRepository<Appointment, Long>
   - Methods:
     * List<Appointment> findByPatientId(Long patientId)
     * List<Appointment> findByDoctorId(Long doctorId)
     * boolean existsByDoctorIdAndAppointmentDateAndAppointmentTime(...)

5. **PrescriptionRepository.java**
   - Extends: JpaRepository<Prescription, Long>
   - Methods:
     * List<Prescription> findByPatientId(Long patientId)
     * Optional<Prescription> findByAppointmentId(Long appointmentId)

6. **MedicalRecordRepository.java**
   - Extends: JpaRepository<MedicalRecord, Long>
   - Method: List<MedicalRecord> findByPatientId(Long patientId)

### Security Layer (3 files)
Located in: `src/main/java/com/healthcare/app/security/`

1. **JwtUtil.java**
   - JWT token generation and validation
   - Uses auth0 JWT library
   - Methods:
     * generateToken(String email, Role role)
     * validateToken(String token)
     * extractEmail(String token)
     * extractRole(String token)

2. **JwtFilter.java**
   - Extends: OncePerRequestFilter
   - Extracts JWT from Authorization header
   - Validates token and sets SecurityContext

3. **UserDetailsServiceImpl.java**
   - Implements: UserDetailsService
   - Loads user details with authorities from Role

### Configuration Layer (2 files)
Located in: `src/main/java/com/healthcare/app/config/`

1. **SecurityConfig.java**
   - @Configuration @EnableWebSecurity @EnableMethodSecurity
   - Beans:
     * PasswordEncoder (BCryptPasswordEncoder)
     * SecurityFilterChain
   - Permits /api/auth/** public
   - Adds JwtFilter before UsernamePasswordAuthenticationFilter
   - Disables CSRF, enables CORS
   - Stateless session management

2. **SwaggerConfig.java**
   - OpenAPI configuration
   - JWT Bearer authentication support
   - API documentation setup

### Exception Handling (5 files)
Located in: `src/main/java/com/healthcare/app/exception/`

1. **ResourceNotFoundException.java**
   - HTTP 404 - Not Found

2. **BadRequestException.java**
   - HTTP 400 - Bad Request

3. **UnauthorizedException.java**
   - HTTP 401 - Unauthorized

4. **DuplicateResourceException.java**
   - HTTP 409 - Conflict

5. **GlobalExceptionHandler.java**
   - @RestControllerAdvice
   - Handles all 4 custom exceptions
   - Returns ErrorResponse with status, error, message, timestamp

### Request DTOs (8 files)
Located in: `src/main/java/com/healthcare/app/dto/request/`

1. **RegisterRequest.java**
   - Fields: name, email, password, phone, dateOfBirth, gender, bloodGroup, address
   - Validations: @NotBlank, @Email, @NotNull

2. **LoginRequest.java**
   - Fields: email, password
   - Validations: @NotBlank, @Email

3. **UpdatePatientProfileRequest.java**
   - Fields: name, phone, dateOfBirth, gender, bloodGroup, address

4. **CreateDoctorRequest.java**
   - Fields: name, email, password, phone, specialization, experienceYears, 
            qualification, availableDays, slotDurationMinutes
   - Validations: @NotBlank, @Email, @NotNull

5. **BookAppointmentRequest.java**
   - Fields: doctorId, appointmentDate, appointmentTime, reason
   - Validations: @NotNull

6. **UpdateAppointmentStatusRequest.java**
   - Fields: status, notes
   - Validations: @NotBlank for status

7. **CreatePrescriptionRequest.java**
   - Fields: appointmentId, diagnosis, notes, items (List<PrescriptionItemRequest>)
   - Validations: @NotNull

8. **PrescriptionItemRequest.java**
   - Fields: medicineName, dosage, frequency, durationDays, instructions
   - Validations: @NotBlank, @NotNull

### Response DTOs (10 files)
Located in: `src/main/java/com/healthcare/app/dto/response/`

1. **AuthResponse.java**
   - Fields: token, userType, name, email
   - Uses: @Builder

2. **UserResponse.java**
   - Fields: id, name, email, role, phone
   - Uses: @Builder

3. **DoctorResponse.java**
   - Fields: id, name, email, phone, specialization, experienceYears, 
            qualification, availableDays, slotDurationMinutes
   - Uses: @Builder

4. **PatientProfileResponse.java**
   - Fields: id, name, email, phone, dateOfBirth, gender, bloodGroup, address
   - Uses: @Builder

5. **AppointmentResponse.java**
   - Fields: id, appointmentDate, appointmentTime, status, reason, notes,
            doctorName, doctorSpecialization, patientName
   - Uses: @Builder

6. **PrescriptionResponse.java**
   - Fields: id, appointmentId, doctorName, patientName, issuedDate, 
            diagnosis, notes, items (List<PrescriptionItemResponse>)
   - Uses: @Builder

7. **PrescriptionItemResponse.java**
   - Fields: id, medicineName, dosage, frequency, durationDays, instructions
   - Uses: @Builder

8. **MedicalRecordResponse.java**
   - Fields: id, recordDate, recordType, title, description, uploadedByName
   - Uses: @Builder

9. **DashboardResponse.java**
   - Fields: totalPatients, totalDoctors, totalAppointments, 
            completedAppointments, pendingAppointments
   - Uses: @Builder

10. **ErrorResponse.java**
    - Fields: status, error, message, timestamp
    - Uses: @Builder

## Common Annotations Used
- **Lombok**: @Data, @NoArgsConstructor, @AllArgsConstructor, @Builder
- **Spring**: @Repository, @Service, @Component, @Configuration, @Bean
- **Security**: @EnableWebSecurity, @EnableMethodSecurity
- **Validation**: @NotBlank, @NotNull, @Email
- **Exception Handling**: @RestControllerAdvice, @ExceptionHandler

## Dependencies Required
These files use the following dependencies (already in build.gradle):
- spring-boot-starter-web
- spring-boot-starter-data-jpa
- spring-boot-starter-security
- spring-boot-starter-validation
- java-jwt (auth0)
- springdoc-openapi-starter-webmvc-ui
- lombok
- mysql-connector-j

## Integration Points
These files integrate with:
- Entity classes (User, DoctorProfile, PatientProfile, Appointment, Prescription, MedicalRecord)
- Service layer (to be implemented)
- Controller layer (to be implemented)
- Role enum (PATIENT, DOCTOR, ADMIN)

## Generation Command
Run one of these:
```
generate_java_files.bat          (Batch file - easiest)
python generate_all_java_files.py  (Python)
node generate_all_java_files.js    (Node.js)
```

## Status
✓ All 34 files are ready to be generated
✓ Directory structure will be auto-created
✓ Files use proper Spring Boot 3.2 and Java 17 syntax
✓ JWT authentication configured
✓ Validation annotations in place
✓ Exception handling configured
✓ Swagger documentation support included
