package com.healthcare.app.service.impl;

import com.healthcare.app.dto.request.BookAppointmentRequest;
import com.healthcare.app.dto.request.UpdateAppointmentStatusRequest;
import com.healthcare.app.dto.response.AppointmentResponse;
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
import java.util.List;
import java.util.stream.Collectors;

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
                User patientUser = userRepository.findByEmail(patientEmail)
                                .orElseThrow(() -> new ResourceNotFoundException("Patient not found"));

                PatientProfile patient = patientProfileRepository.findByUserId(patientUser.getId())
                                .orElseThrow(() -> new ResourceNotFoundException("Patient profile not found"));

                User doctorUser = userRepository.findById(request.getDoctorId())
                                .orElseThrow(() -> new ResourceNotFoundException("Doctor not found"));
                if (doctorUser.getRole() != com.healthcare.app.enums.Role.DOCTOR) {
                        throw new BadRequestException("Selected user is not a doctor");
                }

                DoctorProfile doctorProfile = doctorProfileRepository.findByUserId(doctorUser.getId())
                                .orElseThrow(() -> new ResourceNotFoundException("Doctor profile not found"));

                if (request.getAppointmentDate().isBefore(LocalDate.now())) {
                        throw new BadRequestException("Appointment date must be in the future");
                }

                boolean slotTaken = appointmentRepository.existsByDoctorIdAndAppointmentDateAndAppointmentTimeAndStatusIn(
                                doctorUser.getId(),
                                request.getAppointmentDate(),
                                request.getAppointmentTime(),
                                List.of(AppointmentStatus.SCHEDULED, AppointmentStatus.CONFIRMED)
                );

                if (slotTaken) {
                        throw new BadRequestException("This time slot is already booked");
                }

                Appointment appointment = new Appointment();
                appointment.setPatient(patientUser);
                appointment.setDoctor(doctorUser);
                appointment.setAppointmentDate(request.getAppointmentDate());
                appointment.setAppointmentTime(request.getAppointmentTime());
                appointment.setReason(request.getReason());
                appointment.setStatus(AppointmentStatus.SCHEDULED);

                return mapToAppointmentResponse(appointmentRepository.save(appointment), patient, doctorProfile);
        }

        @Override
        public List<AppointmentResponse> getPatientAppointments(String patientEmail) {
                User patientUser = userRepository.findByEmail(patientEmail)
                                .orElseThrow(() -> new ResourceNotFoundException("Patient not found"));
                PatientProfile patient = patientProfileRepository.findByUserId(patientUser.getId())
                                .orElseThrow(() -> new ResourceNotFoundException("Patient profile not found"));

                return appointmentRepository.findByPatientId(patientUser.getId()).stream()
                                .map(appointment -> mapToAppointmentResponse(appointment, patient, findDoctorProfile(appointment.getDoctor().getId())))
                                .collect(Collectors.toList());
        }

        @Override
        @Transactional
        public AppointmentResponse cancelAppointment(Long appointmentId, String patientEmail) {
                User patientUser = userRepository.findByEmail(patientEmail)
                                .orElseThrow(() -> new ResourceNotFoundException("Patient not found"));

                Appointment appointment = appointmentRepository.findById(appointmentId)
                                .orElseThrow(() -> new ResourceNotFoundException("Appointment not found"));

                if (!appointment.getPatient().getId().equals(patientUser.getId())) {
                        throw new BadRequestException("You can only cancel your own appointments");
                }

                if (appointment.getStatus() != AppointmentStatus.SCHEDULED && appointment.getStatus() != AppointmentStatus.CONFIRMED) {
                        throw new BadRequestException("Only SCHEDULED or CONFIRMED appointments can be cancelled");
                }

                appointment.setStatus(AppointmentStatus.CANCELLED);
                Appointment saved = appointmentRepository.save(appointment);
                return mapToAppointmentResponse(saved, patientProfileRepository.findByUserId(patientUser.getId()).orElse(null), findDoctorProfile(saved.getDoctor().getId()));
        }

        @Override
        public AppointmentResponse getAppointmentById(Long appointmentId) {
                Appointment appointment = appointmentRepository.findById(appointmentId)
                                .orElseThrow(() -> new ResourceNotFoundException("Appointment not found"));
                return mapToAppointmentResponse(appointment, patientProfileRepository.findByUserId(appointment.getPatient().getId()).orElse(null), findDoctorProfile(appointment.getDoctor().getId()));
        }

        @Override
        @Transactional
        public AppointmentResponse updateAppointmentStatus(Long appointmentId, UpdateAppointmentStatusRequest request, String doctorEmail) {
                User doctorUser = userRepository.findByEmail(doctorEmail)
                                .orElseThrow(() -> new ResourceNotFoundException("Doctor not found"));

                Appointment appointment = appointmentRepository.findById(appointmentId)
                                .orElseThrow(() -> new ResourceNotFoundException("Appointment not found"));

                if (!appointment.getDoctor().getId().equals(doctorUser.getId())) {
                        throw new BadRequestException("You can only update your own appointments");
                }

                try {
                        appointment.setStatus(AppointmentStatus.valueOf(request.getStatus()));
                } catch (IllegalArgumentException ex) {
                        throw new BadRequestException("Invalid appointment status: " + request.getStatus());
                }

                if (request.getNotes() != null) {
                        appointment.setNotes(request.getNotes());
                }

                Appointment saved = appointmentRepository.save(appointment);
                return mapToAppointmentResponse(saved, patientProfileRepository.findByUserId(saved.getPatient().getId()).orElse(null), findDoctorProfile(saved.getDoctor().getId()));
        }

        @Override
        public List<AppointmentResponse> getAllAppointments() {
                return appointmentRepository.findAll().stream()
                                .map(appointment -> mapToAppointmentResponse(appointment, patientProfileRepository.findByUserId(appointment.getPatient().getId()).orElse(null), findDoctorProfile(appointment.getDoctor().getId())))
                                .collect(Collectors.toList());
        }

        private DoctorProfile findDoctorProfile(Long doctorUserId) {
                return doctorProfileRepository.findByUserId(doctorUserId).orElse(null);
        }

        private AppointmentResponse mapToAppointmentResponse(Appointment appointment, PatientProfile patientProfile, DoctorProfile doctorProfile) {
                String patientName = appointment.getPatient() != null ? appointment.getPatient().getName() : null;
                String doctorName = appointment.getDoctor() != null ? appointment.getDoctor().getName() : null;
                String doctorEmail = appointment.getDoctor() != null ? appointment.getDoctor().getEmail() : null;

                return AppointmentResponse.builder()
                                .id(appointment.getId())
                                .patientId(appointment.getPatient() != null ? appointment.getPatient().getId() : null)
                                .patientEmail(appointment.getPatient() != null ? appointment.getPatient().getEmail() : null)
                                .doctorId(appointment.getDoctor() != null ? appointment.getDoctor().getId() : null)
                                .doctorEmail(doctorEmail)
                                .patientName(patientName)
                                .doctorName(doctorName)
                                .doctorSpecialization(doctorProfile != null ? doctorProfile.getSpecialization() : null)
                                .specialization(doctorProfile != null ? doctorProfile.getSpecialization() : null)
                                .appointmentDate(appointment.getAppointmentDate())
                                .appointmentTime(appointment.getAppointmentTime())
                                .status(appointment.getStatus() != null ? appointment.getStatus().name() : null)
                                .reason(appointment.getReason())
                                .notes(appointment.getNotes())
                                .createdAt(appointment.getCreatedAt())
                                .build();
        }
}
