import os

def create_directories():
    """Create the test directory structure"""
    base_path = r"C:\Users\Arunkumar\Desktop\hc\src\test\java\com\healthcare\app\service"
    os.makedirs(base_path, exist_ok=True)
    return base_path

def generate_appointment_service_test():
    """Generate AppointmentServiceTest.java"""
    return '''package com.healthcare.app.service;

import com.healthcare.app.dto.AppointmentRequestDTO;
import com.healthcare.app.dto.AppointmentResponseDTO;
import com.healthcare.app.entity.Appointment;
import com.healthcare.app.entity.Doctor;
import com.healthcare.app.entity.Patient;
import com.healthcare.app.entity.User;
import com.healthcare.app.enums.AppointmentStatus;
import com.healthcare.app.enums.UserRole;
import com.healthcare.app.exception.BadRequestException;
import com.healthcare.app.exception.ResourceNotFoundException;
import com.healthcare.app.repository.AppointmentRepository;
import com.healthcare.app.repository.DoctorRepository;
import com.healthcare.app.repository.PatientRepository;
import com.healthcare.app.service.impl.AppointmentServiceImpl;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.time.LocalDateTime;
import java.util.Arrays;
import java.util.List;
import java.util.Optional;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.eq;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
@DisplayName("Appointment Service Tests")
class AppointmentServiceTest {

    @Mock
    private AppointmentRepository appointmentRepository;

    @Mock
    private DoctorRepository doctorRepository;

    @Mock
    private PatientRepository patientRepository;

    @InjectMocks
    private AppointmentServiceImpl appointmentService;

    private User doctorUser;
    private User patientUser;
    private Doctor doctor;
    private Patient patient;
    private Appointment appointment;
    private AppointmentRequestDTO appointmentRequest;
    private LocalDateTime futureDateTime;

    @BeforeEach
    void setUp() {
        futureDateTime = LocalDateTime.now().plusDays(1);

        // Setup doctor user and entity
        doctorUser = new User();
        doctorUser.setId(1L);
        doctorUser.setEmail("doctor@healthcare.com");
        doctorUser.setRole(UserRole.DOCTOR);

        doctor = new Doctor();
        doctor.setId(1L);
        doctor.setUser(doctorUser);
        doctor.setSpecialization("Cardiology");
        doctor.setLicenseNumber("DOC12345");

        // Setup patient user and entity
        patientUser = new User();
        patientUser.setId(2L);
        patientUser.setEmail("patient@healthcare.com");
        patientUser.setRole(UserRole.PATIENT);

        patient = new Patient();
        patient.setId(1L);
        patient.setUser(patientUser);
        patient.setDateOfBirth(LocalDateTime.now().minusYears(30));
        patient.setMedicalHistory("None");

        // Setup appointment
        appointment = new Appointment();
        appointment.setId(1L);
        appointment.setDoctor(doctor);
        appointment.setPatient(patient);
        appointment.setAppointmentDateTime(futureDateTime);
        appointment.setStatus(AppointmentStatus.SCHEDULED);
        appointment.setReason("Regular checkup");

        // Setup request DTO
        appointmentRequest = new AppointmentRequestDTO();
        appointmentRequest.setDoctorId(1L);
        appointmentRequest.setPatientId(1L);
        appointmentRequest.setAppointmentDateTime(futureDateTime);
        appointmentRequest.setReason("Regular checkup");
    }

    @Test
    @DisplayName("Should successfully book appointment with valid data")
    void testBookAppointment_Success() {
        // Arrange
        when(doctorRepository.findById(1L)).thenReturn(Optional.of(doctor));
        when(patientRepository.findById(1L)).thenReturn(Optional.of(patient));
        when(appointmentRepository.existsByDoctorIdAndAppointmentDateTimeAndStatus(
                eq(1L), eq(futureDateTime), eq(AppointmentStatus.SCHEDULED)))
                .thenReturn(false);
        when(appointmentRepository.save(any(Appointment.class))).thenReturn(appointment);

        // Act
        AppointmentResponseDTO result = appointmentService.bookAppointment(appointmentRequest);

        // Assert
        assertThat(result).isNotNull();
        assertThat(result.getId()).isEqualTo(1L);
        assertThat(result.getStatus()).isEqualTo(AppointmentStatus.SCHEDULED);
        assertThat(result.getReason()).isEqualTo("Regular checkup");
        
        verify(doctorRepository, times(1)).findById(1L);
        verify(patientRepository, times(1)).findById(1L);
        verify(appointmentRepository, times(1)).save(any(Appointment.class));
    }

    @Test
    @DisplayName("Should throw BadRequestException when booking duplicate time slot")
    void testBookAppointment_DuplicateSlot_ThrowsBadRequestException() {
        // Arrange
        when(doctorRepository.findById(1L)).thenReturn(Optional.of(doctor));
        when(patientRepository.findById(1L)).thenReturn(Optional.of(patient));
        when(appointmentRepository.existsByDoctorIdAndAppointmentDateTimeAndStatus(
                eq(1L), eq(futureDateTime), eq(AppointmentStatus.SCHEDULED)))
                .thenReturn(true);

        // Act & Assert
        assertThatThrownBy(() -> appointmentService.bookAppointment(appointmentRequest))
                .isInstanceOf(BadRequestException.class)
                .hasMessageContaining("Doctor already has an appointment at this time");

        verify(appointmentRepository, never()).save(any(Appointment.class));
    }

    @Test
    @DisplayName("Should throw BadRequestException when booking appointment in the past")
    void testBookAppointment_PastDate_ThrowsBadRequestException() {
        // Arrange
        LocalDateTime pastDateTime = LocalDateTime.now().minusDays(1);
        appointmentRequest.setAppointmentDateTime(pastDateTime);

        when(doctorRepository.findById(1L)).thenReturn(Optional.of(doctor));
        when(patientRepository.findById(1L)).thenReturn(Optional.of(patient));

        // Act & Assert
        assertThatThrownBy(() -> appointmentService.bookAppointment(appointmentRequest))
                .isInstanceOf(BadRequestException.class)
                .hasMessageContaining("Appointment date must be in the future");

        verify(appointmentRepository, never()).save(any(Appointment.class));
    }

    @Test
    @DisplayName("Should throw ResourceNotFoundException when doctor not found")
    void testBookAppointment_DoctorNotFound_ThrowsResourceNotFoundException() {
        // Arrange
        when(doctorRepository.findById(1L)).thenReturn(Optional.empty());

        // Act & Assert
        assertThatThrownBy(() -> appointmentService.bookAppointment(appointmentRequest))
                .isInstanceOf(ResourceNotFoundException.class)
                .hasMessageContaining("Doctor not found");

        verify(appointmentRepository, never()).save(any(Appointment.class));
    }

    @Test
    @DisplayName("Should successfully cancel scheduled appointment")
    void testCancelAppointment_Success() {
        // Arrange
        when(appointmentRepository.findById(1L)).thenReturn(Optional.of(appointment));
        appointment.setStatus(AppointmentStatus.SCHEDULED);
        when(appointmentRepository.save(any(Appointment.class))).thenReturn(appointment);

        // Act
        appointmentService.cancelAppointment(1L);

        // Assert
        verify(appointmentRepository, times(1)).findById(1L);
        verify(appointmentRepository, times(1)).save(any(Appointment.class));
        assertThat(appointment.getStatus()).isEqualTo(AppointmentStatus.CANCELLED);
    }

    @Test
    @DisplayName("Should throw BadRequestException when trying to cancel completed appointment")
    void testCancelAppointment_WrongStatus_ThrowsBadRequestException() {
        // Arrange
        appointment.setStatus(AppointmentStatus.COMPLETED);
        when(appointmentRepository.findById(1L)).thenReturn(Optional.of(appointment));

        // Act & Assert
        assertThatThrownBy(() -> appointmentService.cancelAppointment(1L))
                .isInstanceOf(BadRequestException.class)
                .hasMessageContaining("Cannot cancel appointment with status");

        verify(appointmentRepository, never()).save(any(Appointment.class));
    }

    @Test
    @DisplayName("Should throw ResourceNotFoundException when canceling non-existent appointment")
    void testCancelAppointment_NotFound_ThrowsResourceNotFoundException() {
        // Arrange
        when(appointmentRepository.findById(1L)).thenReturn(Optional.empty());

        // Act & Assert
        assertThatThrownBy(() -> appointmentService.cancelAppointment(1L))
                .isInstanceOf(ResourceNotFoundException.class)
                .hasMessageContaining("Appointment not found");

        verify(appointmentRepository, never()).save(any(Appointment.class));
    }

    @Test
    @DisplayName("Should successfully retrieve patient's appointments")
    void testGetMyAppointments_Success() {
        // Arrange
        Appointment appointment2 = new Appointment();
        appointment2.setId(2L);
        appointment2.setDoctor(doctor);
        appointment2.setPatient(patient);
        appointment2.setAppointmentDateTime(futureDateTime.plusDays(1));
        appointment2.setStatus(AppointmentStatus.SCHEDULED);
        appointment2.setReason("Follow-up");

        List<Appointment> appointments = Arrays.asList(appointment, appointment2);
        when(appointmentRepository.findByPatientId(1L)).thenReturn(appointments);

        // Act
        List<AppointmentResponseDTO> result = appointmentService.getMyAppointments(1L);

        // Assert
        assertThat(result).isNotNull();
        assertThat(result).hasSize(2);
        assertThat(result.get(0).getId()).isEqualTo(1L);
        assertThat(result.get(1).getId()).isEqualTo(2L);
        
        verify(appointmentRepository, times(1)).findByPatientId(1L);
    }
}
'''

def generate_auth_service_test():
    """Generate AuthServiceTest.java"""
    return '''package com.healthcare.app.service;

import com.healthcare.app.dto.LoginRequestDTO;
import com.healthcare.app.dto.LoginResponseDTO;
import com.healthcare.app.dto.RegisterRequestDTO;
import com.healthcare.app.dto.UserResponseDTO;
import com.healthcare.app.entity.User;
import com.healthcare.app.enums.UserRole;
import com.healthcare.app.exception.DuplicateResourceException;
import com.healthcare.app.exception.ResourceNotFoundException;
import com.healthcare.app.exception.UnauthorizedException;
import com.healthcare.app.repository.UserRepository;
import com.healthcare.app.security.JwtTokenProvider;
import com.healthcare.app.service.impl.AuthServiceImpl;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.security.crypto.password.PasswordEncoder;

import java.util.Optional;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.anyString;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
@DisplayName("Authentication Service Tests")
class AuthServiceTest {

    @Mock
    private UserRepository userRepository;

    @Mock
    private PasswordEncoder passwordEncoder;

    @Mock
    private JwtTokenProvider jwtTokenProvider;

    @InjectMocks
    private AuthServiceImpl authService;

    private User user;
    private RegisterRequestDTO registerRequest;
    private LoginRequestDTO loginRequest;

    @BeforeEach
    void setUp() {
        // Setup user
        user = new User();
        user.setId(1L);
        user.setEmail("test@healthcare.com");
        user.setPassword("encodedPassword123");
        user.setFirstName("John");
        user.setLastName("Doe");
        user.setRole(UserRole.PATIENT);
        user.setPhoneNumber("1234567890");

        // Setup register request
        registerRequest = new RegisterRequestDTO();
        registerRequest.setEmail("test@healthcare.com");
        registerRequest.setPassword("password123");
        registerRequest.setFirstName("John");
        registerRequest.setLastName("Doe");
        registerRequest.setRole(UserRole.PATIENT);
        registerRequest.setPhoneNumber("1234567890");

        // Setup login request
        loginRequest = new LoginRequestDTO();
        loginRequest.setEmail("test@healthcare.com");
        loginRequest.setPassword("password123");
    }

    @Test
    @DisplayName("Should successfully register new user")
    void testRegister_Success() {
        // Arrange
        when(userRepository.existsByEmail("test@healthcare.com")).thenReturn(false);
        when(passwordEncoder.encode("password123")).thenReturn("encodedPassword123");
        when(userRepository.save(any(User.class))).thenReturn(user);

        // Act
        UserResponseDTO result = authService.register(registerRequest);

        // Assert
        assertThat(result).isNotNull();
        assertThat(result.getId()).isEqualTo(1L);
        assertThat(result.getEmail()).isEqualTo("test@healthcare.com");
        assertThat(result.getFirstName()).isEqualTo("John");
        assertThat(result.getLastName()).isEqualTo("Doe");
        assertThat(result.getRole()).isEqualTo(UserRole.PATIENT);
        assertThat(result.getPhoneNumber()).isEqualTo("1234567890");

        verify(userRepository, times(1)).existsByEmail("test@healthcare.com");
        verify(passwordEncoder, times(1)).encode("password123");
        verify(userRepository, times(1)).save(any(User.class));
    }

    @Test
    @DisplayName("Should throw DuplicateResourceException when email already exists")
    void testRegister_DuplicateEmail_ThrowsDuplicateResourceException() {
        // Arrange
        when(userRepository.existsByEmail("test@healthcare.com")).thenReturn(true);

        // Act & Assert
        assertThatThrownBy(() -> authService.register(registerRequest))
                .isInstanceOf(DuplicateResourceException.class)
                .hasMessageContaining("Email already registered");

        verify(userRepository, times(1)).existsByEmail("test@healthcare.com");
        verify(passwordEncoder, never()).encode(anyString());
        verify(userRepository, never()).save(any(User.class));
    }

    @Test
    @DisplayName("Should successfully login with valid credentials")
    void testLogin_Success() {
        // Arrange
        String token = "jwt.token.here";
        when(userRepository.findByEmail("test@healthcare.com")).thenReturn(Optional.of(user));
        when(passwordEncoder.matches("password123", "encodedPassword123")).thenReturn(true);
        when(jwtTokenProvider.generateToken(user)).thenReturn(token);

        // Act
        LoginResponseDTO result = authService.login(loginRequest);

        // Assert
        assertThat(result).isNotNull();
        assertThat(result.getToken()).isEqualTo(token);
        assertThat(result.getEmail()).isEqualTo("test@healthcare.com");
        assertThat(result.getRole()).isEqualTo(UserRole.PATIENT);
        assertThat(result.getFirstName()).isEqualTo("John");
        assertThat(result.getLastName()).isEqualTo("Doe");

        verify(userRepository, times(1)).findByEmail("test@healthcare.com");
        verify(passwordEncoder, times(1)).matches("password123", "encodedPassword123");
        verify(jwtTokenProvider, times(1)).generateToken(user);
    }

    @Test
    @DisplayName("Should throw UnauthorizedException when password is incorrect")
    void testLogin_WrongPassword_ThrowsUnauthorizedException() {
        // Arrange
        when(userRepository.findByEmail("test@healthcare.com")).thenReturn(Optional.of(user));
        when(passwordEncoder.matches("password123", "encodedPassword123")).thenReturn(false);

        // Act & Assert
        assertThatThrownBy(() -> authService.login(loginRequest))
                .isInstanceOf(UnauthorizedException.class)
                .hasMessageContaining("Invalid credentials");

        verify(userRepository, times(1)).findByEmail("test@healthcare.com");
        verify(passwordEncoder, times(1)).matches("password123", "encodedPassword123");
        verify(jwtTokenProvider, never()).generateToken(any(User.class));
    }

    @Test
    @DisplayName("Should throw ResourceNotFoundException when user not found")
    void testLogin_UserNotFound_ThrowsResourceNotFoundException() {
        // Arrange
        when(userRepository.findByEmail("test@healthcare.com")).thenReturn(Optional.empty());

        // Act & Assert
        assertThatThrownBy(() -> authService.login(loginRequest))
                .isInstanceOf(ResourceNotFoundException.class)
                .hasMessageContaining("User not found");

        verify(userRepository, times(1)).findByEmail("test@healthcare.com");
        verify(passwordEncoder, never()).matches(anyString(), anyString());
        verify(jwtTokenProvider, never()).generateToken(any(User.class));
    }
}
'''

def generate_prescription_service_test():
    """Generate PrescriptionServiceTest.java"""
    return '''package com.healthcare.app.service;

import com.healthcare.app.dto.PrescriptionRequestDTO;
import com.healthcare.app.dto.PrescriptionResponseDTO;
import com.healthcare.app.entity.Appointment;
import com.healthcare.app.entity.Doctor;
import com.healthcare.app.entity.Patient;
import com.healthcare.app.entity.Prescription;
import com.healthcare.app.entity.User;
import com.healthcare.app.enums.AppointmentStatus;
import com.healthcare.app.enums.UserRole;
import com.healthcare.app.exception.BadRequestException;
import com.healthcare.app.exception.ResourceNotFoundException;
import com.healthcare.app.repository.AppointmentRepository;
import com.healthcare.app.repository.PrescriptionRepository;
import com.healthcare.app.service.impl.PrescriptionServiceImpl;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.time.LocalDateTime;
import java.util.Arrays;
import java.util.List;
import java.util.Optional;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
@DisplayName("Prescription Service Tests")
class PrescriptionServiceTest {

    @Mock
    private PrescriptionRepository prescriptionRepository;

    @Mock
    private AppointmentRepository appointmentRepository;

    @InjectMocks
    private PrescriptionServiceImpl prescriptionService;

    private User doctorUser;
    private User patientUser;
    private Doctor doctor;
    private Patient patient;
    private Appointment appointment;
    private Prescription prescription;
    private PrescriptionRequestDTO prescriptionRequest;

    @BeforeEach
    void setUp() {
        // Setup doctor user and entity
        doctorUser = new User();
        doctorUser.setId(1L);
        doctorUser.setEmail("doctor@healthcare.com");
        doctorUser.setFirstName("Dr. Smith");
        doctorUser.setLastName("Johnson");
        doctorUser.setRole(UserRole.DOCTOR);

        doctor = new Doctor();
        doctor.setId(1L);
        doctor.setUser(doctorUser);
        doctor.setSpecialization("Cardiology");
        doctor.setLicenseNumber("DOC12345");

        // Setup patient user and entity
        patientUser = new User();
        patientUser.setId(2L);
        patientUser.setEmail("patient@healthcare.com");
        patientUser.setFirstName("Jane");
        patientUser.setLastName("Doe");
        patientUser.setRole(UserRole.PATIENT);

        patient = new Patient();
        patient.setId(1L);
        patient.setUser(patientUser);
        patient.setDateOfBirth(LocalDateTime.now().minusYears(30));
        patient.setMedicalHistory("Hypertension");

        // Setup appointment
        appointment = new Appointment();
        appointment.setId(1L);
        appointment.setDoctor(doctor);
        appointment.setPatient(patient);
        appointment.setAppointmentDateTime(LocalDateTime.now().minusHours(1));
        appointment.setStatus(AppointmentStatus.COMPLETED);
        appointment.setReason("Regular checkup");

        // Setup prescription
        prescription = new Prescription();
        prescription.setId(1L);
        prescription.setAppointment(appointment);
        prescription.setMedication("Lisinopril 10mg");
        prescription.setDosage("Once daily");
        prescription.setDuration("30 days");
        prescription.setInstructions("Take with food");
        prescription.setIssuedDate(LocalDateTime.now());

        // Setup request DTO
        prescriptionRequest = new PrescriptionRequestDTO();
        prescriptionRequest.setAppointmentId(1L);
        prescriptionRequest.setMedication("Lisinopril 10mg");
        prescriptionRequest.setDosage("Once daily");
        prescriptionRequest.setDuration("30 days");
        prescriptionRequest.setInstructions("Take with food");
    }

    @Test
    @DisplayName("Should successfully create prescription for completed appointment")
    void testCreatePrescription_Success() {
        // Arrange
        when(appointmentRepository.findById(1L)).thenReturn(Optional.of(appointment));
        when(prescriptionRepository.save(any(Prescription.class))).thenReturn(prescription);

        // Act
        PrescriptionResponseDTO result = prescriptionService.createPrescription(prescriptionRequest);

        // Assert
        assertThat(result).isNotNull();
        assertThat(result.getId()).isEqualTo(1L);
        assertThat(result.getMedication()).isEqualTo("Lisinopril 10mg");
        assertThat(result.getDosage()).isEqualTo("Once daily");
        assertThat(result.getDuration()).isEqualTo("30 days");
        assertThat(result.getInstructions()).isEqualTo("Take with food");
        assertThat(result.getAppointmentId()).isEqualTo(1L);

        verify(appointmentRepository, times(1)).findById(1L);
        verify(prescriptionRepository, times(1)).save(any(Prescription.class));
    }

    @Test
    @DisplayName("Should throw BadRequestException when appointment is not completed")
    void testCreatePrescription_AppointmentNotCompleted_ThrowsBadRequestException() {
        // Arrange
        appointment.setStatus(AppointmentStatus.SCHEDULED);
        when(appointmentRepository.findById(1L)).thenReturn(Optional.of(appointment));

        // Act & Assert
        assertThatThrownBy(() -> prescriptionService.createPrescription(prescriptionRequest))
                .isInstanceOf(BadRequestException.class)
                .hasMessageContaining("Prescription can only be created for completed appointments");

        verify(appointmentRepository, times(1)).findById(1L);
        verify(prescriptionRepository, never()).save(any(Prescription.class));
    }

    @Test
    @DisplayName("Should throw ResourceNotFoundException when appointment not found")
    void testCreatePrescription_AppointmentNotFound_ThrowsResourceNotFoundException() {
        // Arrange
        when(appointmentRepository.findById(1L)).thenReturn(Optional.empty());

        // Act & Assert
        assertThatThrownBy(() -> prescriptionService.createPrescription(prescriptionRequest))
                .isInstanceOf(ResourceNotFoundException.class)
                .hasMessageContaining("Appointment not found");

        verify(appointmentRepository, times(1)).findById(1L);
        verify(prescriptionRepository, never()).save(any(Prescription.class));
    }

    @Test
    @DisplayName("Should successfully retrieve patient's prescriptions")
    void testGetMyPrescriptions_Success() {
        // Arrange
        Prescription prescription2 = new Prescription();
        prescription2.setId(2L);
        prescription2.setAppointment(appointment);
        prescription2.setMedication("Aspirin 81mg");
        prescription2.setDosage("Once daily");
        prescription2.setDuration("Ongoing");
        prescription2.setInstructions("Take in the morning");
        prescription2.setIssuedDate(LocalDateTime.now());

        List<Prescription> prescriptions = Arrays.asList(prescription, prescription2);
        when(prescriptionRepository.findByAppointmentPatientId(1L)).thenReturn(prescriptions);

        // Act
        List<PrescriptionResponseDTO> result = prescriptionService.getMyPrescriptions(1L);

        // Assert
        assertThat(result).isNotNull();
        assertThat(result).hasSize(2);
        assertThat(result.get(0).getId()).isEqualTo(1L);
        assertThat(result.get(0).getMedication()).isEqualTo("Lisinopril 10mg");
        assertThat(result.get(1).getId()).isEqualTo(2L);
        assertThat(result.get(1).getMedication()).isEqualTo("Aspirin 81mg");

        verify(prescriptionRepository, times(1)).findByAppointmentPatientId(1L);
    }
}
'''

def main():
    """Main function to generate all test files"""
    print("Starting test file generation...")
    
    # Create directories
    base_path = create_directories()
    print(f"Created directory structure at: {base_path}")
    
    # Generate test files
    test_files = {
        "AppointmentServiceTest.java": generate_appointment_service_test(),
        "AuthServiceTest.java": generate_auth_service_test(),
        "PrescriptionServiceTest.java": generate_prescription_service_test()
    }
    
    # Write files
    for filename, content in test_files.items():
        file_path = os.path.join(base_path, filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Generated: {filename}")
    
    print("\n" + "="*60)
    print("SUCCESS! All test files have been generated.")
    print("="*60)
    print(f"\nLocation: {base_path}")
    print("\nGenerated files:")
    for filename in test_files.keys():
        print(f"  - {filename}")
    print("\nTest files include:")
    print("  • JUnit 5 annotations (@Test, @BeforeEach, @DisplayName)")
    print("  • Mockito framework (@Mock, @InjectMocks)")
    print("  • AssertJ assertions")
    print("  • Comprehensive test coverage (success & failure scenarios)")
    print("  • Proper arrange-act-assert pattern")
    print("\nRun the tests with: ./gradlew test")

if __name__ == "__main__":
    main()
