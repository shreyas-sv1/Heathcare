"""
Service Layer Generator for Healthcare Application
Generates all service interfaces and implementations
"""

import os
import sys

def create_directories():
    """Create the necessary directory structure"""
    base_path = "src/main/java/com/healthcare/app/service"
    impl_path = os.path.join(base_path, "impl")
    
    os.makedirs(base_path, exist_ok=True)
    os.makedirs(impl_path, exist_ok=True)
    
    print(f"✓ Created directory: {base_path}")
    print(f"✓ Created directory: {impl_path}")
    
    return base_path, impl_path

def generate_auth_service_interface(base_path):
    """Generate AuthService.java interface"""
    content = """package com.healthcare.app.service;

import com.healthcare.app.dto.AuthResponse;
import com.healthcare.app.dto.LoginRequest;
import com.healthcare.app.dto.RegisterRequest;

/**
 * Service interface for authentication operations
 */
public interface AuthService {
    
    /**
     * Register a new user
     * @param request registration details
     * @return authentication response with JWT token
     */
    AuthResponse register(RegisterRequest request);
    
    /**
     * Authenticate user and generate JWT token
     * @param request login credentials
     * @return authentication response with JWT token
     */
    AuthResponse login(LoginRequest request);
}
"""
    
    file_path = os.path.join(base_path, "AuthService.java")
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✓ Generated: {file_path}")

def generate_patient_service_interface(base_path):
    """Generate PatientService.java interface"""
    content = """package com.healthcare.app.service;

import com.healthcare.app.dto.DoctorResponse;
import com.healthcare.app.dto.MedicalRecordResponse;
import com.healthcare.app.dto.PatientProfileResponse;
import com.healthcare.app.dto.UpdatePatientProfileRequest;

import java.util.List;

/**
 * Service interface for patient operations
 */
public interface PatientService {
    
    /**
     * Get patient profile by email
     * @param email patient email
     * @return patient profile details
     */
    PatientProfileResponse getProfile(String email);
    
    /**
     * Update patient profile
     * @param email patient email
     * @param request update details
     * @return updated patient profile
     */
    PatientProfileResponse updateProfile(String email, UpdatePatientProfileRequest request);
    
    /**
     * Get all doctors
     * @return list of all doctors
     */
    List<DoctorResponse> getAllDoctors();
    
    /**
     * Get doctor by ID
     * @param id doctor ID
     * @return doctor details
     */
    DoctorResponse getDoctorById(Long id);
    
    /**
     * Get medical records for a patient
     * @param email patient email
     * @return list of medical records
     */
    List<MedicalRecordResponse> getMyMedicalRecords(String email);
}
"""
    
    file_path = os.path.join(base_path, "PatientService.java")
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✓ Generated: {file_path}")

def generate_doctor_service_interface(base_path):
    """Generate DoctorService.java interface"""
    content = """package com.healthcare.app.service;

import com.healthcare.app.dto.AppointmentResponse;

import java.util.List;

/**
 * Service interface for doctor operations
 */
public interface DoctorService {
    
    /**
     * Get all appointments for a doctor
     * @param email doctor email
     * @return list of appointments
     */
    List<AppointmentResponse> getMyAppointments(String email);
    
    /**
     * Get patient history
     * @param patientId patient ID
     * @return list of patient's appointments
     */
    List<AppointmentResponse> getPatientHistory(Long patientId);
}
"""
    
    file_path = os.path.join(base_path, "DoctorService.java")
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✓ Generated: {file_path}")

def generate_appointment_service_interface(base_path):
    """Generate AppointmentService.java interface"""
    content = """package com.healthcare.app.service;

import com.healthcare.app.dto.AppointmentResponse;
import com.healthcare.app.dto.BookAppointmentRequest;
import com.healthcare.app.dto.UpdateAppointmentStatusRequest;

import java.util.List;

/**
 * Service interface for appointment operations
 */
public interface AppointmentService {
    
    /**
     * Book a new appointment
     * @param patientEmail patient email
     * @param request appointment details
     * @return created appointment
     */
    AppointmentResponse bookAppointment(String patientEmail, BookAppointmentRequest request);
    
    /**
     * Get all appointments for a patient
     * @param patientEmail patient email
     * @return list of appointments
     */
    List<AppointmentResponse> getMyAppointments(String patientEmail);
    
    /**
     * Cancel an appointment
     * @param appointmentId appointment ID
     * @param patientEmail patient email
     * @return cancelled appointment
     */
    AppointmentResponse cancelAppointment(Long appointmentId, String patientEmail);
    
    /**
     * Update appointment status (doctor only)
     * @param appointmentId appointment ID
     * @param request status update details
     * @param doctorEmail doctor email
     * @return updated appointment
     */
    AppointmentResponse updateAppointmentStatus(Long appointmentId, UpdateAppointmentStatusRequest request, String doctorEmail);
    
    /**
     * Get all appointments (admin only)
     * @return list of all appointments
     */
    List<AppointmentResponse> getAllAppointments();
}
"""
    
    file_path = os.path.join(base_path, "AppointmentService.java")
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✓ Generated: {file_path}")

def generate_prescription_service_interface(base_path):
    """Generate PrescriptionService.java interface"""
    content = """package com.healthcare.app.service;

import com.healthcare.app.dto.CreatePrescriptionRequest;
import com.healthcare.app.dto.PrescriptionResponse;

import java.util.List;

/**
 * Service interface for prescription operations
 */
public interface PrescriptionService {
    
    /**
     * Create a new prescription
     * @param request prescription details
     * @param doctorEmail doctor email
     * @return created prescription
     */
    PrescriptionResponse createPrescription(CreatePrescriptionRequest request, String doctorEmail);
    
    /**
     * Get all prescriptions for a patient
     * @param patientEmail patient email
     * @return list of prescriptions
     */
    List<PrescriptionResponse> getMyPrescriptions(String patientEmail);
}
"""
    
    file_path = os.path.join(base_path, "PrescriptionService.java")
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✓ Generated: {file_path}")

def generate_admin_service_interface(base_path):
    """Generate AdminService.java interface"""
    content = """package com.healthcare.app.service;

import com.healthcare.app.dto.AppointmentResponse;
import com.healthcare.app.dto.CreateDoctorRequest;
import com.healthcare.app.dto.DashboardResponse;
import com.healthcare.app.dto.DoctorResponse;
import com.healthcare.app.dto.UserResponse;

import java.util.List;

/**
 * Service interface for admin operations
 */
public interface AdminService {
    
    /**
     * Create a new doctor
     * @param request doctor details
     * @return created doctor
     */
    DoctorResponse createDoctor(CreateDoctorRequest request);
    
    /**
     * Delete a doctor
     * @param doctorId doctor ID
     */
    void deleteDoctor(Long doctorId);
    
    /**
     * Get all appointments
     * @return list of all appointments
     */
    List<AppointmentResponse> getAllAppointments();
    
    /**
     * Get all patients
     * @return list of all patients
     */
    List<UserResponse> getAllPatients();
    
    /**
     * Get dashboard statistics
     * @return dashboard stats
     */
    DashboardResponse getDashboardStats();
}
"""
    
    file_path = os.path.join(base_path, "AdminService.java")
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✓ Generated: {file_path}")

def generate_auth_service_impl(impl_path):
    """Generate AuthServiceImpl.java implementation"""
    content = """package com.healthcare.app.service.impl;

import com.healthcare.app.dto.AuthResponse;
import com.healthcare.app.dto.LoginRequest;
import com.healthcare.app.dto.RegisterRequest;
import com.healthcare.app.entity.PatientProfile;
import com.healthcare.app.entity.User;
import com.healthcare.app.enums.Role;
import com.healthcare.app.exception.BadRequestException;
import com.healthcare.app.exception.ResourceNotFoundException;
import com.healthcare.app.repository.PatientProfileRepository;
import com.healthcare.app.repository.UserRepository;
import com.healthcare.app.security.JwtUtil;
import com.healthcare.app.service.AuthService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

/**
 * Implementation of AuthService
 */
@Service
@RequiredArgsConstructor
@Slf4j
public class AuthServiceImpl implements AuthService {
    
    private final UserRepository userRepository;
    private final PatientProfileRepository patientProfileRepository;
    private final PasswordEncoder passwordEncoder;
    private final JwtUtil jwtUtil;
    
    @Override
    @Transactional
    public AuthResponse register(RegisterRequest request) {
        log.info("Registering new user with email: {}", request.getEmail());
        
        // Check if user already exists
        if (userRepository.findByEmail(request.getEmail()).isPresent()) {
            log.error("User already exists with email: {}", request.getEmail());
            throw new BadRequestException("User already exists with email: " + request.getEmail());
        }
        
        // Create new user
        User user = new User();
        user.setEmail(request.getEmail());
        user.setPassword(passwordEncoder.encode(request.getPassword()));
        user.setRole(Role.PATIENT);
        user.setActive(true);
        
        User savedUser = userRepository.save(user);
        log.info("User created successfully with ID: {}", savedUser.getId());
        
        // Create patient profile
        PatientProfile profile = new PatientProfile();
        profile.setUser(savedUser);
        profile.setFirstName(request.getFirstName());
        profile.setLastName(request.getLastName());
        profile.setPhoneNumber(request.getPhoneNumber());
        profile.setDateOfBirth(request.getDateOfBirth());
        profile.setGender(request.getGender());
        profile.setAddress(request.getAddress());
        
        patientProfileRepository.save(profile);
        log.info("Patient profile created successfully for user ID: {}", savedUser.getId());
        
        // Generate JWT token
        String token = jwtUtil.generateToken(savedUser.getEmail(), savedUser.getRole().name());
        
        return AuthResponse.builder()
                .token(token)
                .email(savedUser.getEmail())
                .role(savedUser.getRole().name())
                .message("Registration successful")
                .build();
    }
    
    @Override
    public AuthResponse login(LoginRequest request) {
        log.info("Login attempt for user: {}", request.getEmail());
        
        // Find user by email
        User user = userRepository.findByEmail(request.getEmail())
                .orElseThrow(() -> {
                    log.error("User not found with email: {}", request.getEmail());
                    return new ResourceNotFoundException("Invalid email or password");
                });
        
        // Check if user is active
        if (!user.isActive()) {
            log.error("Inactive user attempted to login: {}", request.getEmail());
            throw new BadRequestException("User account is inactive");
        }
        
        // Verify password
        if (!passwordEncoder.matches(request.getPassword(), user.getPassword())) {
            log.error("Invalid password for user: {}", request.getEmail());
            throw new BadRequestException("Invalid email or password");
        }
        
        // Generate JWT token
        String token = jwtUtil.generateToken(user.getEmail(), user.getRole().name());
        
        log.info("Login successful for user: {}", request.getEmail());
        
        return AuthResponse.builder()
                .token(token)
                .email(user.getEmail())
                .role(user.getRole().name())
                .message("Login successful")
                .build();
    }
}
"""
    
    file_path = os.path.join(impl_path, "AuthServiceImpl.java")
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✓ Generated: {file_path}")

def generate_patient_service_impl(impl_path):
    """Generate PatientServiceImpl.java implementation"""
    content = """package com.healthcare.app.service.impl;

import com.healthcare.app.dto.DoctorResponse;
import com.healthcare.app.dto.MedicalRecordResponse;
import com.healthcare.app.dto.PatientProfileResponse;
import com.healthcare.app.dto.UpdatePatientProfileRequest;
import com.healthcare.app.entity.DoctorProfile;
import com.healthcare.app.entity.MedicalRecord;
import com.healthcare.app.entity.PatientProfile;
import com.healthcare.app.entity.User;
import com.healthcare.app.enums.Role;
import com.healthcare.app.exception.ResourceNotFoundException;
import com.healthcare.app.repository.DoctorProfileRepository;
import com.healthcare.app.repository.MedicalRecordRepository;
import com.healthcare.app.repository.PatientProfileRepository;
import com.healthcare.app.repository.UserRepository;
import com.healthcare.app.service.PatientService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.stream.Collectors;

/**
 * Implementation of PatientService
 */
@Service
@RequiredArgsConstructor
@Slf4j
public class PatientServiceImpl implements PatientService {
    
    private final UserRepository userRepository;
    private final PatientProfileRepository patientProfileRepository;
    private final DoctorProfileRepository doctorProfileRepository;
    private final MedicalRecordRepository medicalRecordRepository;
    
    @Override
    public PatientProfileResponse getProfile(String email) {
        log.info("Getting profile for patient: {}", email);
        
        User user = userRepository.findByEmail(email)
                .orElseThrow(() -> new ResourceNotFoundException("User not found"));
        
        PatientProfile profile = patientProfileRepository.findByUserId(user.getId())
                .orElseThrow(() -> new ResourceNotFoundException("Patient profile not found"));
        
        return mapToPatientProfileResponse(profile);
    }
    
    @Override
    @Transactional
    public PatientProfileResponse updateProfile(String email, UpdatePatientProfileRequest request) {
        log.info("Updating profile for patient: {}", email);
        
        User user = userRepository.findByEmail(email)
                .orElseThrow(() -> new ResourceNotFoundException("User not found"));
        
        PatientProfile profile = patientProfileRepository.findByUserId(user.getId())
                .orElseThrow(() -> new ResourceNotFoundException("Patient profile not found"));
        
        // Update profile fields
        if (request.getFirstName() != null) {
            profile.setFirstName(request.getFirstName());
        }
        if (request.getLastName() != null) {
            profile.setLastName(request.getLastName());
        }
        if (request.getPhoneNumber() != null) {
            profile.setPhoneNumber(request.getPhoneNumber());
        }
        if (request.getDateOfBirth() != null) {
            profile.setDateOfBirth(request.getDateOfBirth());
        }
        if (request.getGender() != null) {
            profile.setGender(request.getGender());
        }
        if (request.getAddress() != null) {
            profile.setAddress(request.getAddress());
        }
        if (request.getBloodGroup() != null) {
            profile.setBloodGroup(request.getBloodGroup());
        }
        if (request.getAllergies() != null) {
            profile.setAllergies(request.getAllergies());
        }
        if (request.getMedicalHistory() != null) {
            profile.setMedicalHistory(request.getMedicalHistory());
        }
        
        PatientProfile updatedProfile = patientProfileRepository.save(profile);
        log.info("Profile updated successfully for patient: {}", email);
        
        return mapToPatientProfileResponse(updatedProfile);
    }
    
    @Override
    public List<DoctorResponse> getAllDoctors() {
        log.info("Getting all doctors");
        
        List<User> doctors = userRepository.findByRole(Role.DOCTOR);
        
        return doctors.stream()
                .map(doctor -> {
                    DoctorProfile profile = doctorProfileRepository.findByUserId(doctor.getId())
                            .orElse(null);
                    return mapToDoctorResponse(doctor, profile);
                })
                .collect(Collectors.toList());
    }
    
    @Override
    public DoctorResponse getDoctorById(Long id) {
        log.info("Getting doctor by ID: {}", id);
        
        User doctor = userRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Doctor not found"));
        
        if (doctor.getRole() != Role.DOCTOR) {
            throw new ResourceNotFoundException("User is not a doctor");
        }
        
        DoctorProfile profile = doctorProfileRepository.findByUserId(doctor.getId())
                .orElse(null);
        
        return mapToDoctorResponse(doctor, profile);
    }
    
    @Override
    public List<MedicalRecordResponse> getMyMedicalRecords(String email) {
        log.info("Getting medical records for patient: {}", email);
        
        User user = userRepository.findByEmail(email)
                .orElseThrow(() -> new ResourceNotFoundException("User not found"));
        
        PatientProfile profile = patientProfileRepository.findByUserId(user.getId())
                .orElseThrow(() -> new ResourceNotFoundException("Patient profile not found"));
        
        List<MedicalRecord> records = medicalRecordRepository.findByPatientId(profile.getId());
        
        return records.stream()
                .map(this::mapToMedicalRecordResponse)
                .collect(Collectors.toList());
    }
    
    private PatientProfileResponse mapToPatientProfileResponse(PatientProfile profile) {
        return PatientProfileResponse.builder()
                .id(profile.getId())
                .userId(profile.getUser().getId())
                .email(profile.getUser().getEmail())
                .firstName(profile.getFirstName())
                .lastName(profile.getLastName())
                .phoneNumber(profile.getPhoneNumber())
                .dateOfBirth(profile.getDateOfBirth())
                .gender(profile.getGender())
                .address(profile.getAddress())
                .bloodGroup(profile.getBloodGroup())
                .allergies(profile.getAllergies())
                .medicalHistory(profile.getMedicalHistory())
                .build();
    }
    
    private DoctorResponse mapToDoctorResponse(User doctor, DoctorProfile profile) {
        DoctorResponse.DoctorResponseBuilder builder = DoctorResponse.builder()
                .id(doctor.getId())
                .email(doctor.getEmail());
        
        if (profile != null) {
            builder.firstName(profile.getFirstName())
                    .lastName(profile.getLastName())
                    .phoneNumber(profile.getPhoneNumber())
                    .specialization(profile.getSpecialization())
                    .qualification(profile.getQualification())
                    .experience(profile.getExperience())
                    .consultationFee(profile.getConsultationFee())
                    .available(profile.isAvailable());
        }
        
        return builder.build();
    }
    
    private MedicalRecordResponse mapToMedicalRecordResponse(MedicalRecord record) {
        return MedicalRecordResponse.builder()
                .id(record.getId())
                .patientId(record.getPatient().getId())
                .patientName(record.getPatient().getFirstName() + " " + record.getPatient().getLastName())
                .doctorId(record.getDoctor() != null ? record.getDoctor().getId() : null)
                .doctorName(record.getDoctor() != null ? 
                        record.getDoctor().getFirstName() + " " + record.getDoctor().getLastName() : null)
                .diagnosis(record.getDiagnosis())
                .treatment(record.getTreatment())
                .notes(record.getNotes())
                .recordDate(record.getRecordDate())
                .createdAt(record.getCreatedAt())
                .build();
    }
}
"""
    
    file_path = os.path.join(impl_path, "PatientServiceImpl.java")
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✓ Generated: {file_path}")

def generate_doctor_service_impl(impl_path):
    """Generate DoctorServiceImpl.java implementation"""
    content = """package com.healthcare.app.service.impl;

import com.healthcare.app.dto.AppointmentResponse;
import com.healthcare.app.entity.Appointment;
import com.healthcare.app.entity.DoctorProfile;
import com.healthcare.app.entity.User;
import com.healthcare.app.exception.ResourceNotFoundException;
import com.healthcare.app.repository.AppointmentRepository;
import com.healthcare.app.repository.DoctorProfileRepository;
import com.healthcare.app.repository.UserRepository;
import com.healthcare.app.service.DoctorService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

/**
 * Implementation of DoctorService
 */
@Service
@RequiredArgsConstructor
@Slf4j
public class DoctorServiceImpl implements DoctorService {
    
    private final UserRepository userRepository;
    private final DoctorProfileRepository doctorProfileRepository;
    private final AppointmentRepository appointmentRepository;
    
    @Override
    public List<AppointmentResponse> getMyAppointments(String email) {
        log.info("Getting appointments for doctor: {}", email);
        
        User doctor = userRepository.findByEmail(email)
                .orElseThrow(() -> new ResourceNotFoundException("Doctor not found"));
        
        DoctorProfile doctorProfile = doctorProfileRepository.findByUserId(doctor.getId())
                .orElseThrow(() -> new ResourceNotFoundException("Doctor profile not found"));
        
        List<Appointment> appointments = appointmentRepository.findByDoctorId(doctorProfile.getId());
        
        return appointments.stream()
                .map(this::mapToAppointmentResponse)
                .collect(Collectors.toList());
    }
    
    @Override
    public List<AppointmentResponse> getPatientHistory(Long patientId) {
        log.info("Getting patient history for patient ID: {}", patientId);
        
        List<Appointment> appointments = appointmentRepository.findByPatientId(patientId);
        
        return appointments.stream()
                .map(this::mapToAppointmentResponse)
                .collect(Collectors.toList());
    }
    
    private AppointmentResponse mapToAppointmentResponse(Appointment appointment) {
        return AppointmentResponse.builder()
                .id(appointment.getId())
                .patientId(appointment.getPatient().getId())
                .patientName(appointment.getPatient().getFirstName() + " " + 
                        appointment.getPatient().getLastName())
                .patientEmail(appointment.getPatient().getUser().getEmail())
                .doctorId(appointment.getDoctor().getId())
                .doctorName(appointment.getDoctor().getFirstName() + " " + 
                        appointment.getDoctor().getLastName())
                .doctorEmail(appointment.getDoctor().getUser().getEmail())
                .specialization(appointment.getDoctor().getSpecialization())
                .appointmentDate(appointment.getAppointmentDate())
                .appointmentTime(appointment.getAppointmentTime())
                .status(appointment.getStatus().name())
                .reason(appointment.getReason())
                .notes(appointment.getNotes())
                .createdAt(appointment.getCreatedAt())
                .updatedAt(appointment.getUpdatedAt())
                .build();
    }
}
"""
    
    file_path = os.path.join(impl_path, "DoctorServiceImpl.java")
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✓ Generated: {file_path}")

def generate_appointment_service_impl(impl_path):
    """Generate AppointmentServiceImpl.java implementation"""
    content = """package com.healthcare.app.service.impl;

import com.healthcare.app.dto.AppointmentResponse;
import com.healthcare.app.dto.BookAppointmentRequest;
import com.healthcare.app.dto.UpdateAppointmentStatusRequest;
import com.healthcare.app.entity.Appointment;
import com.healthcare.app.entity.DoctorProfile;
import com.healthcare.app.entity.PatientProfile;
import com.healthcare.app.entity.User;
import com.healthcare.app.enums.AppointmentStatus;
import com.healthcare.app.exception.BadRequestException;
import com.healthcare.app.exception.ResourceNotFoundException;
import com.healthcare.app.repository.AppointmentRepository;
import com.healthcare.app.repository.DoctorProfileRepository;
import com.healthcare.app.repository.PatientProfileRepository;
import com.healthcare.app.repository.UserRepository;
import com.healthcare.app.service.AppointmentService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDate;
import java.time.LocalTime;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Implementation of AppointmentService
 */
@Service
@RequiredArgsConstructor
@Slf4j
public class AppointmentServiceImpl implements AppointmentService {
    
    private final UserRepository userRepository;
    private final PatientProfileRepository patientProfileRepository;
    private final DoctorProfileRepository doctorProfileRepository;
    private final AppointmentRepository appointmentRepository;
    
    @Override
    @Transactional
    public AppointmentResponse bookAppointment(String patientEmail, BookAppointmentRequest request) {
        log.info("Booking appointment for patient: {}", patientEmail);
        
        // Get patient
        User patientUser = userRepository.findByEmail(patientEmail)
                .orElseThrow(() -> new ResourceNotFoundException("Patient not found"));
        
        PatientProfile patient = patientProfileRepository.findByUserId(patientUser.getId())
                .orElseThrow(() -> new ResourceNotFoundException("Patient profile not found"));
        
        // Get doctor
        DoctorProfile doctor = doctorProfileRepository.findById(request.getDoctorId())
                .orElseThrow(() -> new ResourceNotFoundException("Doctor not found"));
        
        // Validate appointment date (must be in future)
        if (request.getAppointmentDate().isBefore(LocalDate.now())) {
            throw new BadRequestException("Appointment date must be in the future");
        }
        
        // Check if doctor is available
        if (!doctor.isAvailable()) {
            throw new BadRequestException("Doctor is not available for appointments");
        }
        
        // Check for duplicate appointment slot
        boolean slotTaken = appointmentRepository.existsByDoctorIdAndAppointmentDateAndAppointmentTimeAndStatusIn(
                doctor.getId(),
                request.getAppointmentDate(),
                request.getAppointmentTime(),
                List.of(AppointmentStatus.SCHEDULED, AppointmentStatus.CONFIRMED)
        );
        
        if (slotTaken) {
            throw new BadRequestException("This time slot is already booked");
        }
        
        // Create appointment
        Appointment appointment = new Appointment();
        appointment.setPatient(patient);
        appointment.setDoctor(doctor);
        appointment.setAppointmentDate(request.getAppointmentDate());
        appointment.setAppointmentTime(request.getAppointmentTime());
        appointment.setReason(request.getReason());
        appointment.setStatus(AppointmentStatus.SCHEDULED);
        
        Appointment savedAppointment = appointmentRepository.save(appointment);
        log.info("Appointment booked successfully with ID: {}", savedAppointment.getId());
        
        return mapToAppointmentResponse(savedAppointment);
    }
    
    @Override
    public List<AppointmentResponse> getMyAppointments(String patientEmail) {
        log.info("Getting appointments for patient: {}", patientEmail);
        
        User patientUser = userRepository.findByEmail(patientEmail)
                .orElseThrow(() -> new ResourceNotFoundException("Patient not found"));
        
        PatientProfile patient = patientProfileRepository.findByUserId(patientUser.getId())
                .orElseThrow(() -> new ResourceNotFoundException("Patient profile not found"));
        
        List<Appointment> appointments = appointmentRepository.findByPatientId(patient.getId());
        
        return appointments.stream()
                .map(this::mapToAppointmentResponse)
                .collect(Collectors.toList());
    }
    
    @Override
    @Transactional
    public AppointmentResponse cancelAppointment(Long appointmentId, String patientEmail) {
        log.info("Cancelling appointment ID: {} for patient: {}", appointmentId, patientEmail);
        
        // Get patient
        User patientUser = userRepository.findByEmail(patientEmail)
                .orElseThrow(() -> new ResourceNotFoundException("Patient not found"));
        
        PatientProfile patient = patientProfileRepository.findByUserId(patientUser.getId())
                .orElseThrow(() -> new ResourceNotFoundException("Patient profile not found"));
        
        // Get appointment
        Appointment appointment = appointmentRepository.findById(appointmentId)
                .orElseThrow(() -> new ResourceNotFoundException("Appointment not found"));
        
        // Verify appointment belongs to patient
        if (!appointment.getPatient().getId().equals(patient.getId())) {
            throw new BadRequestException("You can only cancel your own appointments");
        }
        
        // Check if appointment can be cancelled
        if (appointment.getStatus() != AppointmentStatus.SCHEDULED && 
            appointment.getStatus() != AppointmentStatus.CONFIRMED) {
            throw new BadRequestException("Only SCHEDULED or CONFIRMED appointments can be cancelled");
        }
        
        // Cancel appointment
        appointment.setStatus(AppointmentStatus.CANCELLED);
        Appointment updatedAppointment = appointmentRepository.save(appointment);
        
        log.info("Appointment cancelled successfully: {}", appointmentId);
        
        return mapToAppointmentResponse(updatedAppointment);
    }
    
    @Override
    @Transactional
    public AppointmentResponse updateAppointmentStatus(Long appointmentId, 
                                                       UpdateAppointmentStatusRequest request, 
                                                       String doctorEmail) {
        log.info("Updating appointment status for ID: {} by doctor: {}", appointmentId, doctorEmail);
        
        // Get doctor
        User doctorUser = userRepository.findByEmail(doctorEmail)
                .orElseThrow(() -> new ResourceNotFoundException("Doctor not found"));
        
        DoctorProfile doctor = doctorProfileRepository.findByUserId(doctorUser.getId())
                .orElseThrow(() -> new ResourceNotFoundException("Doctor profile not found"));
        
        // Get appointment
        Appointment appointment = appointmentRepository.findById(appointmentId)
                .orElseThrow(() -> new ResourceNotFoundException("Appointment not found"));
        
        // Verify appointment belongs to doctor
        if (!appointment.getDoctor().getId().equals(doctor.getId())) {
            throw new BadRequestException("You can only update your own appointments");
        }
        
        // Update status
        try {
            AppointmentStatus newStatus = AppointmentStatus.valueOf(request.getStatus());
            appointment.setStatus(newStatus);
        } catch (IllegalArgumentException e) {
            throw new BadRequestException("Invalid appointment status: " + request.getStatus());
        }
        
        // Update notes if provided
        if (request.getNotes() != null) {
            appointment.setNotes(request.getNotes());
        }
        
        Appointment updatedAppointment = appointmentRepository.save(appointment);
        log.info("Appointment status updated successfully: {}", appointmentId);
        
        return mapToAppointmentResponse(updatedAppointment);
    }
    
    @Override
    public List<AppointmentResponse> getAllAppointments() {
        log.info("Getting all appointments");
        
        List<Appointment> appointments = appointmentRepository.findAll();
        
        return appointments.stream()
                .map(this::mapToAppointmentResponse)
                .collect(Collectors.toList());
    }
    
    private AppointmentResponse mapToAppointmentResponse(Appointment appointment) {
        return AppointmentResponse.builder()
                .id(appointment.getId())
                .patientId(appointment.getPatient().getId())
                .patientName(appointment.getPatient().getFirstName() + " " + 
                        appointment.getPatient().getLastName())
                .patientEmail(appointment.getPatient().getUser().getEmail())
                .doctorId(appointment.getDoctor().getId())
                .doctorName(appointment.getDoctor().getFirstName() + " " + 
                        appointment.getDoctor().getLastName())
                .doctorEmail(appointment.getDoctor().getUser().getEmail())
                .specialization(appointment.getDoctor().getSpecialization())
                .appointmentDate(appointment.getAppointmentDate())
                .appointmentTime(appointment.getAppointmentTime())
                .status(appointment.getStatus().name())
                .reason(appointment.getReason())
                .notes(appointment.getNotes())
                .createdAt(appointment.getCreatedAt())
                .updatedAt(appointment.getUpdatedAt())
                .build();
    }
}
"""
    
    file_path = os.path.join(impl_path, "AppointmentServiceImpl.java")
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✓ Generated: {file_path}")

def generate_prescription_service_impl(impl_path):
    """Generate PrescriptionServiceImpl.java implementation"""
    content = """package com.healthcare.app.service.impl;

import com.healthcare.app.dto.CreatePrescriptionRequest;
import com.healthcare.app.dto.PrescriptionItemResponse;
import com.healthcare.app.dto.PrescriptionResponse;
import com.healthcare.app.entity.Appointment;
import com.healthcare.app.entity.DoctorProfile;
import com.healthcare.app.entity.PatientProfile;
import com.healthcare.app.entity.Prescription;
import com.healthcare.app.entity.PrescriptionItem;
import com.healthcare.app.entity.User;
import com.healthcare.app.enums.AppointmentStatus;
import com.healthcare.app.exception.BadRequestException;
import com.healthcare.app.exception.ResourceNotFoundException;
import com.healthcare.app.repository.AppointmentRepository;
import com.healthcare.app.repository.DoctorProfileRepository;
import com.healthcare.app.repository.PatientProfileRepository;
import com.healthcare.app.repository.PrescriptionRepository;
import com.healthcare.app.repository.UserRepository;
import com.healthcare.app.service.PrescriptionService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDate;
import java.util.List;
import java.util.stream.Collectors;

/**
 * Implementation of PrescriptionService
 */
@Service
@RequiredArgsConstructor
@Slf4j
public class PrescriptionServiceImpl implements PrescriptionService {
    
    private final UserRepository userRepository;
    private final DoctorProfileRepository doctorProfileRepository;
    private final PatientProfileRepository patientProfileRepository;
    private final AppointmentRepository appointmentRepository;
    private final PrescriptionRepository prescriptionRepository;
    
    @Override
    @Transactional
    public PrescriptionResponse createPrescription(CreatePrescriptionRequest request, String doctorEmail) {
        log.info("Creating prescription for appointment ID: {} by doctor: {}", 
                request.getAppointmentId(), doctorEmail);
        
        // Get doctor
        User doctorUser = userRepository.findByEmail(doctorEmail)
                .orElseThrow(() -> new ResourceNotFoundException("Doctor not found"));
        
        DoctorProfile doctor = doctorProfileRepository.findByUserId(doctorUser.getId())
                .orElseThrow(() -> new ResourceNotFoundException("Doctor profile not found"));
        
        // Get appointment
        Appointment appointment = appointmentRepository.findById(request.getAppointmentId())
                .orElseThrow(() -> new ResourceNotFoundException("Appointment not found"));
        
        // Verify appointment belongs to doctor
        if (!appointment.getDoctor().getId().equals(doctor.getId())) {
            throw new BadRequestException("You can only create prescriptions for your own appointments");
        }
        
        // Validate appointment is completed
        if (appointment.getStatus() != AppointmentStatus.COMPLETED) {
            throw new BadRequestException("Prescription can only be created for completed appointments");
        }
        
        // Create prescription
        Prescription prescription = new Prescription();
        prescription.setAppointment(appointment);
        prescription.setPatient(appointment.getPatient());
        prescription.setDoctor(doctor);
        prescription.setDiagnosis(request.getDiagnosis());
        prescription.setNotes(request.getNotes());
        prescription.setPrescriptionDate(LocalDate.now());
        
        Prescription savedPrescription = prescriptionRepository.save(prescription);
        
        // Create prescription items
        if (request.getItems() != null && !request.getItems().isEmpty()) {
            List<PrescriptionItem> items = request.getItems().stream()
                    .map(itemDto -> {
                        PrescriptionItem item = new PrescriptionItem();
                        item.setPrescription(savedPrescription);
                        item.setMedicineName(itemDto.getMedicineName());
                        item.setDosage(itemDto.getDosage());
                        item.setFrequency(itemDto.getFrequency());
                        item.setDuration(itemDto.getDuration());
                        item.setInstructions(itemDto.getInstructions());
                        return item;
                    })
                    .collect(Collectors.toList());
            
            savedPrescription.setItems(items);
            savedPrescription = prescriptionRepository.save(savedPrescription);
        }
        
        log.info("Prescription created successfully with ID: {}", savedPrescription.getId());
        
        return mapToPrescriptionResponse(savedPrescription);
    }
    
    @Override
    public List<PrescriptionResponse> getMyPrescriptions(String patientEmail) {
        log.info("Getting prescriptions for patient: {}", patientEmail);
        
        User patientUser = userRepository.findByEmail(patientEmail)
                .orElseThrow(() -> new ResourceNotFoundException("Patient not found"));
        
        PatientProfile patient = patientProfileRepository.findByUserId(patientUser.getId())
                .orElseThrow(() -> new ResourceNotFoundException("Patient profile not found"));
        
        List<Prescription> prescriptions = prescriptionRepository.findByPatientId(patient.getId());
        
        return prescriptions.stream()
                .map(this::mapToPrescriptionResponse)
                .collect(Collectors.toList());
    }
    
    private PrescriptionResponse mapToPrescriptionResponse(Prescription prescription) {
        return PrescriptionResponse.builder()
                .id(prescription.getId())
                .appointmentId(prescription.getAppointment().getId())
                .patientId(prescription.getPatient().getId())
                .patientName(prescription.getPatient().getFirstName() + " " + 
                        prescription.getPatient().getLastName())
                .doctorId(prescription.getDoctor().getId())
                .doctorName(prescription.getDoctor().getFirstName() + " " + 
                        prescription.getDoctor().getLastName())
                .diagnosis(prescription.getDiagnosis())
                .notes(prescription.getNotes())
                .prescriptionDate(prescription.getPrescriptionDate())
                .items(prescription.getItems() != null ? 
                        prescription.getItems().stream()
                                .map(this::mapToPrescriptionItemResponse)
                                .collect(Collectors.toList()) : 
                        List.of())
                .createdAt(prescription.getCreatedAt())
                .build();
    }
    
    private PrescriptionItemResponse mapToPrescriptionItemResponse(PrescriptionItem item) {
        return PrescriptionItemResponse.builder()
                .id(item.getId())
                .medicineName(item.getMedicineName())
                .dosage(item.getDosage())
                .frequency(item.getFrequency())
                .duration(item.getDuration())
                .instructions(item.getInstructions())
                .build();
    }
}
"""
    
    file_path = os.path.join(impl_path, "PrescriptionServiceImpl.java")
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✓ Generated: {file_path}")

def generate_admin_service_impl(impl_path):
    """Generate AdminServiceImpl.java implementation"""
    content = """package com.healthcare.app.service.impl;

import com.healthcare.app.dto.AppointmentResponse;
import com.healthcare.app.dto.CreateDoctorRequest;
import com.healthcare.app.dto.DashboardResponse;
import com.healthcare.app.dto.DoctorResponse;
import com.healthcare.app.dto.UserResponse;
import com.healthcare.app.entity.Appointment;
import com.healthcare.app.entity.DoctorProfile;
import com.healthcare.app.entity.PatientProfile;
import com.healthcare.app.entity.User;
import com.healthcare.app.enums.AppointmentStatus;
import com.healthcare.app.enums.Role;
import com.healthcare.app.exception.BadRequestException;
import com.healthcare.app.exception.ResourceNotFoundException;
import com.healthcare.app.repository.AppointmentRepository;
import com.healthcare.app.repository.DoctorProfileRepository;
import com.healthcare.app.repository.PatientProfileRepository;
import com.healthcare.app.repository.UserRepository;
import com.healthcare.app.service.AdminService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.stream.Collectors;

/**
 * Implementation of AdminService
 */
@Service
@RequiredArgsConstructor
@Slf4j
public class AdminServiceImpl implements AdminService {
    
    private final UserRepository userRepository;
    private final DoctorProfileRepository doctorProfileRepository;
    private final PatientProfileRepository patientProfileRepository;
    private final AppointmentRepository appointmentRepository;
    private final PasswordEncoder passwordEncoder;
    
    @Override
    @Transactional
    public DoctorResponse createDoctor(CreateDoctorRequest request) {
        log.info("Creating new doctor with email: {}", request.getEmail());
        
        // Check if user already exists
        if (userRepository.findByEmail(request.getEmail()).isPresent()) {
            throw new BadRequestException("User already exists with email: " + request.getEmail());
        }
        
        // Create doctor user
        User user = new User();
        user.setEmail(request.getEmail());
        user.setPassword(passwordEncoder.encode(request.getPassword()));
        user.setRole(Role.DOCTOR);
        user.setActive(true);
        
        User savedUser = userRepository.save(user);
        log.info("Doctor user created with ID: {}", savedUser.getId());
        
        // Create doctor profile
        DoctorProfile profile = new DoctorProfile();
        profile.setUser(savedUser);
        profile.setFirstName(request.getFirstName());
        profile.setLastName(request.getLastName());
        profile.setPhoneNumber(request.getPhoneNumber());
        profile.setSpecialization(request.getSpecialization());
        profile.setQualification(request.getQualification());
        profile.setExperience(request.getExperience());
        profile.setConsultationFee(request.getConsultationFee());
        profile.setAvailable(true);
        
        DoctorProfile savedProfile = doctorProfileRepository.save(profile);
        log.info("Doctor profile created successfully for user ID: {}", savedUser.getId());
        
        return mapToDoctorResponse(savedUser, savedProfile);
    }
    
    @Override
    @Transactional
    public void deleteDoctor(Long doctorId) {
        log.info("Deleting doctor with ID: {}", doctorId);
        
        User doctor = userRepository.findById(doctorId)
                .orElseThrow(() -> new ResourceNotFoundException("Doctor not found"));
        
        if (doctor.getRole() != Role.DOCTOR) {
            throw new BadRequestException("User is not a doctor");
        }
        
        // Soft delete - deactivate user
        doctor.setActive(false);
        userRepository.save(doctor);
        
        // Optionally, mark doctor profile as unavailable
        doctorProfileRepository.findByUserId(doctorId).ifPresent(profile -> {
            profile.setAvailable(false);
            doctorProfileRepository.save(profile);
        });
        
        log.info("Doctor deleted successfully: {}", doctorId);
    }
    
    @Override
    public List<AppointmentResponse> getAllAppointments() {
        log.info("Getting all appointments");
        
        List<Appointment> appointments = appointmentRepository.findAll();
        
        return appointments.stream()
                .map(this::mapToAppointmentResponse)
                .collect(Collectors.toList());
    }
    
    @Override
    public List<UserResponse> getAllPatients() {
        log.info("Getting all patients");
        
        List<User> patients = userRepository.findByRole(Role.PATIENT);
        
        return patients.stream()
                .map(this::mapToUserResponse)
                .collect(Collectors.toList());
    }
    
    @Override
    public DashboardResponse getDashboardStats() {
        log.info("Getting dashboard statistics");
        
        // Count total users by role
        long totalPatients = userRepository.countByRole(Role.PATIENT);
        long totalDoctors = userRepository.countByRole(Role.DOCTOR);
        long totalAdmins = userRepository.countByRole(Role.ADMIN);
        
        // Count appointments by status
        long totalAppointments = appointmentRepository.count();
        long scheduledAppointments = appointmentRepository.countByStatus(AppointmentStatus.SCHEDULED);
        long confirmedAppointments = appointmentRepository.countByStatus(AppointmentStatus.CONFIRMED);
        long completedAppointments = appointmentRepository.countByStatus(AppointmentStatus.COMPLETED);
        long cancelledAppointments = appointmentRepository.countByStatus(AppointmentStatus.CANCELLED);
        
        return DashboardResponse.builder()
                .totalPatients(totalPatients)
                .totalDoctors(totalDoctors)
                .totalAdmins(totalAdmins)
                .totalAppointments(totalAppointments)
                .scheduledAppointments(scheduledAppointments)
                .confirmedAppointments(confirmedAppointments)
                .completedAppointments(completedAppointments)
                .cancelledAppointments(cancelledAppointments)
                .build();
    }
    
    private DoctorResponse mapToDoctorResponse(User doctor, DoctorProfile profile) {
        return DoctorResponse.builder()
                .id(doctor.getId())
                .email(doctor.getEmail())
                .firstName(profile.getFirstName())
                .lastName(profile.getLastName())
                .phoneNumber(profile.getPhoneNumber())
                .specialization(profile.getSpecialization())
                .qualification(profile.getQualification())
                .experience(profile.getExperience())
                .consultationFee(profile.getConsultationFee())
                .available(profile.isAvailable())
                .build();
    }
    
    private AppointmentResponse mapToAppointmentResponse(Appointment appointment) {
        return AppointmentResponse.builder()
                .id(appointment.getId())
                .patientId(appointment.getPatient().getId())
                .patientName(appointment.getPatient().getFirstName() + " " + 
                        appointment.getPatient().getLastName())
                .patientEmail(appointment.getPatient().getUser().getEmail())
                .doctorId(appointment.getDoctor().getId())
                .doctorName(appointment.getDoctor().getFirstName() + " " + 
                        appointment.getDoctor().getLastName())
                .doctorEmail(appointment.getDoctor().getUser().getEmail())
                .specialization(appointment.getDoctor().getSpecialization())
                .appointmentDate(appointment.getAppointmentDate())
                .appointmentTime(appointment.getAppointmentTime())
                .status(appointment.getStatus().name())
                .reason(appointment.getReason())
                .notes(appointment.getNotes())
                .createdAt(appointment.getCreatedAt())
                .updatedAt(appointment.getUpdatedAt())
                .build();
    }
    
    private UserResponse mapToUserResponse(User user) {
        UserResponse.UserResponseBuilder builder = UserResponse.builder()
                .id(user.getId())
                .email(user.getEmail())
                .role(user.getRole().name())
                .active(user.isActive())
                .createdAt(user.getCreatedAt());
        
        // Add patient profile details if available
        if (user.getRole() == Role.PATIENT) {
            patientProfileRepository.findByUserId(user.getId()).ifPresent(profile -> {
                builder.firstName(profile.getFirstName())
                        .lastName(profile.getLastName())
                        .phoneNumber(profile.getPhoneNumber());
            });
        }
        
        return builder.build();
    }
}
"""
    
    file_path = os.path.join(impl_path, "AdminServiceImpl.java")
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"✓ Generated: {file_path}")

def main():
    """Main function to generate all service files"""
    print("\n" + "="*60)
    print("Healthcare Application - Service Layer Generator")
    print("="*60 + "\n")
    
    try:
        # Create directory structure
        base_path, impl_path = create_directories()
        
        print("\n" + "-"*60)
        print("Generating Service Interfaces...")
        print("-"*60 + "\n")
        
        # Generate service interfaces
        generate_auth_service_interface(base_path)
        generate_patient_service_interface(base_path)
        generate_doctor_service_interface(base_path)
        generate_appointment_service_interface(base_path)
        generate_prescription_service_interface(base_path)
        generate_admin_service_interface(base_path)
        
        print("\n" + "-"*60)
        print("Generating Service Implementations...")
        print("-"*60 + "\n")
        
        # Generate service implementations
        generate_auth_service_impl(impl_path)
        generate_patient_service_impl(impl_path)
        generate_doctor_service_impl(impl_path)
        generate_appointment_service_impl(impl_path)
        generate_prescription_service_impl(impl_path)
        generate_admin_service_impl(impl_path)
        
        print("\n" + "="*60)
        print("✅ SUCCESS! All service files generated successfully!")
        print("="*60)
        print(f"\nGenerated Files:")
        print(f"  - 6 Service Interfaces in: {base_path}")
        print(f"  - 6 Service Implementations in: {impl_path}")
        print(f"\nTotal: 12 service layer files created")
        print("\nFeatures included:")
        print("  ✓ @Service annotations")
        print("  ✓ @Transactional where needed")
        print("  ✓ @Slf4j logging")
        print("  ✓ Proper exception handling")
        print("  ✓ Entity to DTO mapping")
        print("  ✓ Business logic validation")
        print("  ✓ Spring Boot best practices")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
