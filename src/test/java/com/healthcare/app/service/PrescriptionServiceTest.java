package com.healthcare.app.service;

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
