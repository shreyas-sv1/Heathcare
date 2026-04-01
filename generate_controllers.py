import os

# Base directory for controllers
CONTROLLER_DIR = r"C:\Users\Arunkumar\Desktop\hc\src\main\java\com\healthcare\app\controller"

def create_directory():
    """Create the controller directory if it doesn't exist"""
    os.makedirs(CONTROLLER_DIR, exist_ok=True)
    print(f"Created directory: {CONTROLLER_DIR}")

def generate_auth_controller():
    """Generate AuthController.java"""
    content = '''package com.healthcare.app.controller;

import com.healthcare.app.dto.LoginRequest;
import com.healthcare.app.dto.RegisterRequest;
import com.healthcare.app.dto.AuthResponse;
import com.healthcare.app.service.AuthService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/auth")
@RequiredArgsConstructor
@Slf4j
@Tag(name = "Authentication", description = "Authentication management APIs - public endpoints for user registration and login")
public class AuthController {

    private final AuthService authService;

    @PostMapping("/register")
    @Operation(
        summary = "Register a new user",
        description = "Register a new user account with email, password, and role. Public endpoint."
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "201",
            description = "User registered successfully",
            content = @Content(schema = @Schema(implementation = AuthResponse.class))
        ),
        @ApiResponse(
            responseCode = "400",
            description = "Invalid input or email already exists",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "500",
            description = "Internal server error",
            content = @Content
        )
    })
    public ResponseEntity<AuthResponse> register(@Valid @RequestBody RegisterRequest request) {
        log.info("Registration request received for email: {}", request.getEmail());
        try {
            AuthResponse response = authService.register(request);
            log.info("User registered successfully: {}", request.getEmail());
            return ResponseEntity.status(HttpStatus.CREATED).body(response);
        } catch (Exception e) {
            log.error("Registration failed for email: {}", request.getEmail(), e);
            throw e;
        }
    }

    @PostMapping("/login")
    @Operation(
        summary = "User login",
        description = "Authenticate user with email and password. Returns JWT token on success. Public endpoint."
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "200",
            description = "Login successful",
            content = @Content(schema = @Schema(implementation = AuthResponse.class))
        ),
        @ApiResponse(
            responseCode = "401",
            description = "Invalid credentials",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "500",
            description = "Internal server error",
            content = @Content
        )
    })
    public ResponseEntity<AuthResponse> login(@Valid @RequestBody LoginRequest request) {
        log.info("Login request received for email: {}", request.getEmail());
        try {
            AuthResponse response = authService.login(request);
            log.info("User logged in successfully: {}", request.getEmail());
            return ResponseEntity.ok(response);
        } catch (Exception e) {
            log.error("Login failed for email: {}", request.getEmail(), e);
            throw e;
        }
    }
}
'''
    return content

def generate_patient_controller():
    """Generate PatientController.java"""
    content = '''package com.healthcare.app.controller;

import com.healthcare.app.dto.PatientProfileDTO;
import com.healthcare.app.dto.UpdatePatientProfileRequest;
import com.healthcare.app.service.PatientService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/patients")
@RequiredArgsConstructor
@Slf4j
@PreAuthorize("hasRole('PATIENT')")
@Tag(name = "Patient", description = "Patient profile management APIs - requires PATIENT role")
@SecurityRequirement(name = "Bearer Authentication")
public class PatientController {

    private final PatientService patientService;

    @GetMapping("/profile")
    @Operation(
        summary = "Get patient profile",
        description = "Retrieve the profile information of the currently authenticated patient"
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "200",
            description = "Profile retrieved successfully",
            content = @Content(schema = @Schema(implementation = PatientProfileDTO.class))
        ),
        @ApiResponse(
            responseCode = "401",
            description = "Unauthorized - invalid or missing token",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "403",
            description = "Forbidden - user does not have PATIENT role",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "404",
            description = "Patient profile not found",
            content = @Content
        )
    })
    public ResponseEntity<PatientProfileDTO> getProfile(
            @AuthenticationPrincipal UserDetails userDetails) {
        log.info("Fetching profile for patient: {}", userDetails.getUsername());
        try {
            PatientProfileDTO profile = patientService.getPatientProfile(userDetails.getUsername());
            return ResponseEntity.ok(profile);
        } catch (Exception e) {
            log.error("Error fetching profile for patient: {}", userDetails.getUsername(), e);
            throw e;
        }
    }

    @PutMapping("/profile")
    @Operation(
        summary = "Update patient profile",
        description = "Update the profile information of the currently authenticated patient"
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "200",
            description = "Profile updated successfully",
            content = @Content(schema = @Schema(implementation = PatientProfileDTO.class))
        ),
        @ApiResponse(
            responseCode = "400",
            description = "Invalid input data",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "401",
            description = "Unauthorized - invalid or missing token",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "403",
            description = "Forbidden - user does not have PATIENT role",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "404",
            description = "Patient profile not found",
            content = @Content
        )
    })
    public ResponseEntity<PatientProfileDTO> updateProfile(
            @AuthenticationPrincipal UserDetails userDetails,
            @Valid @RequestBody UpdatePatientProfileRequest request) {
        log.info("Updating profile for patient: {}", userDetails.getUsername());
        try {
            PatientProfileDTO updatedProfile = patientService.updatePatientProfile(
                userDetails.getUsername(), request);
            log.info("Profile updated successfully for patient: {}", userDetails.getUsername());
            return ResponseEntity.ok(updatedProfile);
        } catch (Exception e) {
            log.error("Error updating profile for patient: {}", userDetails.getUsername(), e);
            throw e;
        }
    }
}
'''
    return content

def generate_doctor_controller():
    """Generate DoctorController.java"""
    content = '''package com.healthcare.app.controller;

import com.healthcare.app.dto.AppointmentDTO;
import com.healthcare.app.dto.PatientHistoryDTO;
import com.healthcare.app.dto.PrescriptionDTO;
import com.healthcare.app.dto.CreatePrescriptionRequest;
import com.healthcare.app.service.DoctorService;
import com.healthcare.app.service.PrescriptionService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/doctor")
@RequiredArgsConstructor
@Slf4j
@PreAuthorize("hasRole('DOCTOR')")
@Tag(name = "Doctor", description = "Doctor management APIs - requires DOCTOR role")
@SecurityRequirement(name = "Bearer Authentication")
public class DoctorController {

    private final DoctorService doctorService;
    private final PrescriptionService prescriptionService;

    @GetMapping("/appointments")
    @Operation(
        summary = "Get doctor's appointments",
        description = "Retrieve all appointments for the currently authenticated doctor"
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "200",
            description = "Appointments retrieved successfully",
            content = @Content(schema = @Schema(implementation = AppointmentDTO.class))
        ),
        @ApiResponse(
            responseCode = "401",
            description = "Unauthorized - invalid or missing token",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "403",
            description = "Forbidden - user does not have DOCTOR role",
            content = @Content
        )
    })
    public ResponseEntity<List<AppointmentDTO>> getDoctorAppointments(
            @AuthenticationPrincipal UserDetails userDetails) {
        log.info("Fetching appointments for doctor: {}", userDetails.getUsername());
        try {
            List<AppointmentDTO> appointments = doctorService.getDoctorAppointments(
                userDetails.getUsername());
            return ResponseEntity.ok(appointments);
        } catch (Exception e) {
            log.error("Error fetching appointments for doctor: {}", userDetails.getUsername(), e);
            throw e;
        }
    }

    @GetMapping("/patients/{id}/history")
    @Operation(
        summary = "Get patient medical history",
        description = "Retrieve the complete medical history for a specific patient"
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "200",
            description = "Patient history retrieved successfully",
            content = @Content(schema = @Schema(implementation = PatientHistoryDTO.class))
        ),
        @ApiResponse(
            responseCode = "401",
            description = "Unauthorized - invalid or missing token",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "403",
            description = "Forbidden - user does not have DOCTOR role",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "404",
            description = "Patient not found",
            content = @Content
        )
    })
    public ResponseEntity<PatientHistoryDTO> getPatientHistory(
            @Parameter(description = "Patient ID") @PathVariable Long id,
            @AuthenticationPrincipal UserDetails userDetails) {
        log.info("Doctor {} fetching history for patient ID: {}", userDetails.getUsername(), id);
        try {
            PatientHistoryDTO history = doctorService.getPatientHistory(id);
            return ResponseEntity.ok(history);
        } catch (Exception e) {
            log.error("Error fetching patient history for ID: {}", id, e);
            throw e;
        }
    }

    @PostMapping("/prescriptions")
    @Operation(
        summary = "Create prescription",
        description = "Create a new prescription for a patient"
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "201",
            description = "Prescription created successfully",
            content = @Content(schema = @Schema(implementation = PrescriptionDTO.class))
        ),
        @ApiResponse(
            responseCode = "400",
            description = "Invalid input data",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "401",
            description = "Unauthorized - invalid or missing token",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "403",
            description = "Forbidden - user does not have DOCTOR role",
            content = @Content
        )
    })
    public ResponseEntity<PrescriptionDTO> createPrescription(
            @AuthenticationPrincipal UserDetails userDetails,
            @Valid @RequestBody CreatePrescriptionRequest request) {
        log.info("Doctor {} creating prescription for patient ID: {}", 
            userDetails.getUsername(), request.getPatientId());
        try {
            PrescriptionDTO prescription = prescriptionService.createPrescription(
                userDetails.getUsername(), request);
            log.info("Prescription created successfully by doctor: {}", userDetails.getUsername());
            return ResponseEntity.status(HttpStatus.CREATED).body(prescription);
        } catch (Exception e) {
            log.error("Error creating prescription by doctor: {}", userDetails.getUsername(), e);
            throw e;
        }
    }
}

// Compatibility endpoint for prescriptions
@RestController
@RequestMapping("/api/prescriptions")
@RequiredArgsConstructor
@Slf4j
@PreAuthorize("hasRole('DOCTOR')")
@Tag(name = "Prescriptions", description = "Prescription management APIs - compatibility endpoint")
@SecurityRequirement(name = "Bearer Authentication")
class PrescriptionController {

    private final PrescriptionService prescriptionService;

    @PostMapping
    @Operation(
        summary = "Create prescription (compatibility endpoint)",
        description = "Create a new prescription for a patient - alternative endpoint for compatibility"
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "201",
            description = "Prescription created successfully",
            content = @Content(schema = @Schema(implementation = PrescriptionDTO.class))
        ),
        @ApiResponse(
            responseCode = "400",
            description = "Invalid input data",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "401",
            description = "Unauthorized - invalid or missing token",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "403",
            description = "Forbidden - user does not have DOCTOR role",
            content = @Content
        )
    })
    public ResponseEntity<PrescriptionDTO> createPrescription(
            @AuthenticationPrincipal UserDetails userDetails,
            @Valid @RequestBody CreatePrescriptionRequest request) {
        log.info("Creating prescription via compatibility endpoint for patient ID: {}", 
            request.getPatientId());
        try {
            PrescriptionDTO prescription = prescriptionService.createPrescription(
                userDetails.getUsername(), request);
            return ResponseEntity.status(HttpStatus.CREATED).body(prescription);
        } catch (Exception e) {
            log.error("Error creating prescription via compatibility endpoint", e);
            throw e;
        }
    }
}
'''
    return content

def generate_appointment_controller():
    """Generate AppointmentController.java"""
    content = '''package com.healthcare.app.controller;

import com.healthcare.app.dto.AppointmentDTO;
import com.healthcare.app.dto.BookAppointmentRequest;
import com.healthcare.app.dto.UpdateAppointmentStatusRequest;
import com.healthcare.app.service.AppointmentService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/appointments")
@RequiredArgsConstructor
@Slf4j
@Tag(name = "Appointments", description = "Appointment management APIs")
@SecurityRequirement(name = "Bearer Authentication")
public class AppointmentController {

    private final AppointmentService appointmentService;

    @PostMapping
    @PreAuthorize("hasRole('PATIENT')")
    @Operation(
        summary = "Book appointment",
        description = "Book a new appointment with a doctor - requires PATIENT role"
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "201",
            description = "Appointment booked successfully",
            content = @Content(schema = @Schema(implementation = AppointmentDTO.class))
        ),
        @ApiResponse(
            responseCode = "400",
            description = "Invalid input data or time slot not available",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "401",
            description = "Unauthorized - invalid or missing token",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "403",
            description = "Forbidden - user does not have PATIENT role",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "404",
            description = "Doctor not found",
            content = @Content
        )
    })
    public ResponseEntity<AppointmentDTO> bookAppointment(
            @AuthenticationPrincipal UserDetails userDetails,
            @Valid @RequestBody BookAppointmentRequest request) {
        log.info("Patient {} booking appointment with doctor ID: {}", 
            userDetails.getUsername(), request.getDoctorId());
        try {
            AppointmentDTO appointment = appointmentService.bookAppointment(
                userDetails.getUsername(), request);
            log.info("Appointment booked successfully for patient: {}", userDetails.getUsername());
            return ResponseEntity.status(HttpStatus.CREATED).body(appointment);
        } catch (Exception e) {
            log.error("Error booking appointment for patient: {}", userDetails.getUsername(), e);
            throw e;
        }
    }

    @GetMapping("/mine")
    @PreAuthorize("hasRole('PATIENT')")
    @Operation(
        summary = "Get my appointments",
        description = "Retrieve all appointments for the currently authenticated patient"
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "200",
            description = "Appointments retrieved successfully",
            content = @Content(schema = @Schema(implementation = AppointmentDTO.class))
        ),
        @ApiResponse(
            responseCode = "401",
            description = "Unauthorized - invalid or missing token",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "403",
            description = "Forbidden - user does not have PATIENT role",
            content = @Content
        )
    })
    public ResponseEntity<List<AppointmentDTO>> getMyAppointments(
            @AuthenticationPrincipal UserDetails userDetails) {
        log.info("Fetching appointments for patient: {}", userDetails.getUsername());
        try {
            List<AppointmentDTO> appointments = appointmentService.getPatientAppointments(
                userDetails.getUsername());
            return ResponseEntity.ok(appointments);
        } catch (Exception e) {
            log.error("Error fetching appointments for patient: {}", userDetails.getUsername(), e);
            throw e;
        }
    }

    @PutMapping("/{id}/cancel")
    @PreAuthorize("hasRole('PATIENT')")
    @Operation(
        summary = "Cancel appointment",
        description = "Cancel an existing appointment - requires PATIENT role"
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "200",
            description = "Appointment cancelled successfully",
            content = @Content(schema = @Schema(implementation = AppointmentDTO.class))
        ),
        @ApiResponse(
            responseCode = "401",
            description = "Unauthorized - invalid or missing token",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "403",
            description = "Forbidden - user does not have PATIENT role or not the appointment owner",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "404",
            description = "Appointment not found",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "409",
            description = "Appointment cannot be cancelled (already completed or cancelled)",
            content = @Content
        )
    })
    public ResponseEntity<AppointmentDTO> cancelAppointment(
            @Parameter(description = "Appointment ID") @PathVariable Long id,
            @AuthenticationPrincipal UserDetails userDetails) {
        log.info("Patient {} cancelling appointment ID: {}", userDetails.getUsername(), id);
        try {
            AppointmentDTO appointment = appointmentService.cancelAppointment(
                id, userDetails.getUsername());
            log.info("Appointment {} cancelled successfully", id);
            return ResponseEntity.ok(appointment);
        } catch (Exception e) {
            log.error("Error cancelling appointment {}", id, e);
            throw e;
        }
    }

    @PutMapping("/{id}/status")
    @PreAuthorize("hasRole('DOCTOR')")
    @Operation(
        summary = "Update appointment status",
        description = "Update the status of an appointment - requires DOCTOR role"
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "200",
            description = "Appointment status updated successfully",
            content = @Content(schema = @Schema(implementation = AppointmentDTO.class))
        ),
        @ApiResponse(
            responseCode = "400",
            description = "Invalid status value",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "401",
            description = "Unauthorized - invalid or missing token",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "403",
            description = "Forbidden - user does not have DOCTOR role or not the assigned doctor",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "404",
            description = "Appointment not found",
            content = @Content
        )
    })
    public ResponseEntity<AppointmentDTO> updateAppointmentStatus(
            @Parameter(description = "Appointment ID") @PathVariable Long id,
            @AuthenticationPrincipal UserDetails userDetails,
            @Valid @RequestBody UpdateAppointmentStatusRequest request) {
        log.info("Doctor {} updating status for appointment ID: {} to {}", 
            userDetails.getUsername(), id, request.getStatus());
        try {
            AppointmentDTO appointment = appointmentService.updateAppointmentStatus(
                id, userDetails.getUsername(), request);
            log.info("Appointment {} status updated successfully to {}", id, request.getStatus());
            return ResponseEntity.ok(appointment);
        } catch (Exception e) {
            log.error("Error updating appointment {} status", id, e);
            throw e;
        }
    }
}
'''
    return content

def generate_admin_controller():
    """Generate AdminController.java"""
    content = '''package com.healthcare.app.controller;

import com.healthcare.app.dto.AppointmentDTO;
import com.healthcare.app.dto.CreateDoctorRequest;
import com.healthcare.app.dto.DashboardStatsDTO;
import com.healthcare.app.dto.DoctorDTO;
import com.healthcare.app.dto.PatientDTO;
import com.healthcare.app.service.AdminService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/admin")
@RequiredArgsConstructor
@Slf4j
@PreAuthorize("hasRole('ADMIN')")
@Tag(name = "Admin", description = "Admin management APIs - requires ADMIN role")
@SecurityRequirement(name = "Bearer Authentication")
public class AdminController {

    private final AdminService adminService;

    @PostMapping("/doctors")
    @Operation(
        summary = "Create doctor",
        description = "Create a new doctor account with profile information"
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "201",
            description = "Doctor created successfully",
            content = @Content(schema = @Schema(implementation = DoctorDTO.class))
        ),
        @ApiResponse(
            responseCode = "400",
            description = "Invalid input data or email already exists",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "401",
            description = "Unauthorized - invalid or missing token",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "403",
            description = "Forbidden - user does not have ADMIN role",
            content = @Content
        )
    })
    public ResponseEntity<DoctorDTO> createDoctor(@Valid @RequestBody CreateDoctorRequest request) {
        log.info("Admin creating doctor with email: {}", request.getEmail());
        try {
            DoctorDTO doctor = adminService.createDoctor(request);
            log.info("Doctor created successfully with email: {}", request.getEmail());
            return ResponseEntity.status(HttpStatus.CREATED).body(doctor);
        } catch (Exception e) {
            log.error("Error creating doctor with email: {}", request.getEmail(), e);
            throw e;
        }
    }

    @DeleteMapping("/doctors/{id}")
    @Operation(
        summary = "Delete doctor",
        description = "Delete a doctor account and associated profile"
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "204",
            description = "Doctor deleted successfully",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "401",
            description = "Unauthorized - invalid or missing token",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "403",
            description = "Forbidden - user does not have ADMIN role",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "404",
            description = "Doctor not found",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "409",
            description = "Cannot delete doctor with active appointments",
            content = @Content
        )
    })
    public ResponseEntity<Void> deleteDoctor(
            @Parameter(description = "Doctor ID") @PathVariable Long id) {
        log.info("Admin deleting doctor with ID: {}", id);
        try {
            adminService.deleteDoctor(id);
            log.info("Doctor deleted successfully with ID: {}", id);
            return ResponseEntity.noContent().build();
        } catch (Exception e) {
            log.error("Error deleting doctor with ID: {}", id, e);
            throw e;
        }
    }

    @GetMapping("/appointments")
    @Operation(
        summary = "Get all appointments",
        description = "Retrieve all appointments in the system"
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "200",
            description = "Appointments retrieved successfully",
            content = @Content(schema = @Schema(implementation = AppointmentDTO.class))
        ),
        @ApiResponse(
            responseCode = "401",
            description = "Unauthorized - invalid or missing token",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "403",
            description = "Forbidden - user does not have ADMIN role",
            content = @Content
        )
    })
    public ResponseEntity<List<AppointmentDTO>> getAllAppointments() {
        log.info("Admin fetching all appointments");
        try {
            List<AppointmentDTO> appointments = adminService.getAllAppointments();
            return ResponseEntity.ok(appointments);
        } catch (Exception e) {
            log.error("Error fetching all appointments", e);
            throw e;
        }
    }

    @GetMapping("/patients")
    @Operation(
        summary = "Get all patients",
        description = "Retrieve all patient profiles in the system"
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "200",
            description = "Patients retrieved successfully",
            content = @Content(schema = @Schema(implementation = PatientDTO.class))
        ),
        @ApiResponse(
            responseCode = "401",
            description = "Unauthorized - invalid or missing token",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "403",
            description = "Forbidden - user does not have ADMIN role",
            content = @Content
        )
    })
    public ResponseEntity<List<PatientDTO>> getAllPatients() {
        log.info("Admin fetching all patients");
        try {
            List<PatientDTO> patients = adminService.getAllPatients();
            return ResponseEntity.ok(patients);
        } catch (Exception e) {
            log.error("Error fetching all patients", e);
            throw e;
        }
    }

    @GetMapping("/dashboard")
    @Operation(
        summary = "Get dashboard statistics",
        description = "Retrieve dashboard statistics including counts and analytics"
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "200",
            description = "Dashboard statistics retrieved successfully",
            content = @Content(schema = @Schema(implementation = DashboardStatsDTO.class))
        ),
        @ApiResponse(
            responseCode = "401",
            description = "Unauthorized - invalid or missing token",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "403",
            description = "Forbidden - user does not have ADMIN role",
            content = @Content
        )
    })
    public ResponseEntity<DashboardStatsDTO> getDashboardStats() {
        log.info("Admin fetching dashboard statistics");
        try {
            DashboardStatsDTO stats = adminService.getDashboardStats();
            return ResponseEntity.ok(stats);
        } catch (Exception e) {
            log.error("Error fetching dashboard statistics", e);
            throw e;
        }
    }
}
'''
    return content

def generate_public_controller():
    """Generate PublicController.java"""
    content = '''package com.healthcare.app.controller;

import com.healthcare.app.dto.DoctorDTO;
import com.healthcare.app.service.DoctorService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.Parameter;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api")
@RequiredArgsConstructor
@Slf4j
@Tag(name = "Public", description = "Public APIs - no authentication required")
public class PublicController {

    private final DoctorService doctorService;

    @GetMapping("/doctors")
    @Operation(
        summary = "List all doctors",
        description = "Get a list of all doctors with their specializations and basic information. Public endpoint."
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "200",
            description = "Doctors list retrieved successfully",
            content = @Content(schema = @Schema(implementation = DoctorDTO.class))
        ),
        @ApiResponse(
            responseCode = "500",
            description = "Internal server error",
            content = @Content
        )
    })
    public ResponseEntity<List<DoctorDTO>> getAllDoctors() {
        log.info("Public endpoint: Fetching all doctors");
        try {
            List<DoctorDTO> doctors = doctorService.getAllDoctors();
            log.info("Retrieved {} doctors", doctors.size());
            return ResponseEntity.ok(doctors);
        } catch (Exception e) {
            log.error("Error fetching all doctors", e);
            throw e;
        }
    }

    @GetMapping("/doctors/{id}")
    @Operation(
        summary = "Get doctor details",
        description = "Get detailed information about a specific doctor by ID. Public endpoint."
    )
    @ApiResponses(value = {
        @ApiResponse(
            responseCode = "200",
            description = "Doctor details retrieved successfully",
            content = @Content(schema = @Schema(implementation = DoctorDTO.class))
        ),
        @ApiResponse(
            responseCode = "404",
            description = "Doctor not found",
            content = @Content
        ),
        @ApiResponse(
            responseCode = "500",
            description = "Internal server error",
            content = @Content
        )
    })
    public ResponseEntity<DoctorDTO> getDoctorById(
            @Parameter(description = "Doctor ID") @PathVariable Long id) {
        log.info("Public endpoint: Fetching doctor with ID: {}", id);
        try {
            DoctorDTO doctor = doctorService.getDoctorById(id);
            return ResponseEntity.ok(doctor);
        } catch (Exception e) {
            log.error("Error fetching doctor with ID: {}", id, e);
            throw e;
        }
    }
}
'''
    return content

def write_controller_file(filename, content):
    """Write controller content to file"""
    filepath = os.path.join(CONTROLLER_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated: {filepath}")

def main():
    print("=" * 80)
    print("Healthcare Application - Controller Generator")
    print("=" * 80)
    
    # Create directory
    create_directory()
    print()
    
    # Generate all controllers
    controllers = [
        ("AuthController.java", generate_auth_controller()),
        ("PatientController.java", generate_patient_controller()),
        ("DoctorController.java", generate_doctor_controller()),
        ("AppointmentController.java", generate_appointment_controller()),
        ("AdminController.java", generate_admin_controller()),
        ("PublicController.java", generate_public_controller())
    ]
    
    print("Generating controller files...")
    print("-" * 80)
    
    for filename, content in controllers:
        write_controller_file(filename, content)
    
    print("-" * 80)
    print(f"\n✅ Successfully generated {len(controllers)} controller files!")
    print("\nGenerated Controllers:")
    print("  1. AuthController.java - Authentication endpoints (register, login)")
    print("  2. PatientController.java - Patient profile management")
    print("  3. DoctorController.java - Doctor appointments and prescriptions")
    print("  4. AppointmentController.java - Appointment management")
    print("  5. AdminController.java - Admin operations")
    print("  6. PublicController.java - Public doctor listing")
    print("\nAll controllers include:")
    print("  ✓ Spring Boot REST annotations")
    print("  ✓ Lombok annotations (@RequiredArgsConstructor, @Slf4j)")
    print("  ✓ Role-based security (@PreAuthorize)")
    print("  ✓ Request validation (@Valid)")
    print("  ✓ Swagger/OpenAPI documentation")
    print("  ✓ Comprehensive logging")
    print("  ✓ Proper error handling")
    print("=" * 80)

if __name__ == "__main__":
    main()
'''