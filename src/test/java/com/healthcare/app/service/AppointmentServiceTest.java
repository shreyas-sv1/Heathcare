package com.healthcare.app.service;

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
