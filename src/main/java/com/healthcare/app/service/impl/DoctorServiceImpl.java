package com.healthcare.app.service.impl;

import com.healthcare.app.dto.response.AppointmentResponse;
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

@Service
@RequiredArgsConstructor
@Slf4j
public class DoctorServiceImpl implements DoctorService {

    private final UserRepository userRepository;
    private final DoctorProfileRepository doctorProfileRepository;
    private final AppointmentRepository appointmentRepository;

    @Override
    public List<AppointmentResponse> getMyAppointments(String email) {
        User doctor = userRepository.findByEmail(email)
                .orElseThrow(() -> new ResourceNotFoundException("Doctor not found"));

        doctorProfileRepository.findByUserId(doctor.getId())
                .orElseThrow(() -> new ResourceNotFoundException("Doctor profile not found"));

        return appointmentRepository.findByDoctorId(doctor.getId()).stream()
                .map(appointment -> mapToAppointmentResponse(appointment, doctorProfileRepository.findByUserId(doctor.getId()).orElse(null)))
                .collect(Collectors.toList());
    }

    @Override
    public List<AppointmentResponse> getPatientHistory(Long patientId) {
        return appointmentRepository.findByPatientId(patientId).stream()
                .map(appointment -> mapToAppointmentResponse(appointment, doctorProfileRepository.findByUserId(appointment.getDoctor().getId()).orElse(null)))
                .collect(Collectors.toList());
    }

    private AppointmentResponse mapToAppointmentResponse(Appointment appointment, DoctorProfile doctorProfile) {
        return AppointmentResponse.builder()
                .id(appointment.getId())
                .patientId(appointment.getPatient() != null ? appointment.getPatient().getId() : null)
                .patientEmail(appointment.getPatient() != null ? appointment.getPatient().getEmail() : null)
                .doctorId(appointment.getDoctor() != null ? appointment.getDoctor().getId() : null)
                .doctorEmail(appointment.getDoctor() != null ? appointment.getDoctor().getEmail() : null)
                .patientName(appointment.getPatient() != null ? appointment.getPatient().getName() : null)
                .doctorName(appointment.getDoctor() != null ? appointment.getDoctor().getName() : null)
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
