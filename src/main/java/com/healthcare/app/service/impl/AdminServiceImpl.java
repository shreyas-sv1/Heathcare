package com.healthcare.app.service.impl;

import com.healthcare.app.dto.request.CreateDoctorRequest;
import com.healthcare.app.dto.response.AppointmentResponse;
import com.healthcare.app.dto.response.DashboardResponse;
import com.healthcare.app.dto.response.DoctorResponse;
import com.healthcare.app.dto.response.PatientProfileResponse;
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
        if (userRepository.findByEmail(request.getEmail()).isPresent()) {
            throw new BadRequestException("User already exists with email: " + request.getEmail());
        }

        User user = new User();
        user.setName(request.getName());
        user.setEmail(request.getEmail());
        user.setPassword(passwordEncoder.encode(request.getPassword()));
        user.setPhone(request.getPhone());
        user.setRole(Role.DOCTOR);
        user.setActive(true);

        User savedUser = userRepository.save(user);

        DoctorProfile profile = new DoctorProfile();
        profile.setUser(savedUser);
        profile.setSpecialization(request.getSpecialization());
        profile.setExperienceYears(request.getExperienceYears());
        profile.setQualification(request.getQualification());
        profile.setAvailableDays(request.getAvailableDays() != null ? request.getAvailableDays() : "MON-FRI");
        profile.setSlotDurationMinutes(request.getSlotDurationMinutes() != null ? request.getSlotDurationMinutes() : 30);

        DoctorProfile savedProfile = doctorProfileRepository.save(profile);
        return mapToDoctorResponse(savedUser, savedProfile);
    }

    @Override
    @Transactional
    public void deleteDoctor(Long doctorId) {
        User doctor = userRepository.findById(doctorId)
                .orElseThrow(() -> new ResourceNotFoundException("Doctor not found"));

        if (doctor.getRole() != Role.DOCTOR) {
            throw new BadRequestException("User is not a doctor");
        }

        doctor.setActive(false);
        userRepository.save(doctor);
    }

    @Override
    public List<AppointmentResponse> getAllAppointments() {
        return appointmentRepository.findAll().stream()
                .map(appointment -> mapToAppointmentResponse(appointment))
                .collect(Collectors.toList());
    }

    @Override
    public List<PatientProfileResponse> getAllPatients() {
        return userRepository.findByRole(Role.PATIENT).stream()
                .map(user -> patientProfileRepository.findByUserId(user.getId())
                        .map(profile -> mapToPatientResponse(user, profile))
                        .orElseGet(() -> mapToPatientResponse(user, null)))
                .collect(Collectors.toList());
    }

    @Override
    public DashboardResponse getDashboardStats() {
        long totalPatients = userRepository.findByRole(Role.PATIENT).size();
        long totalDoctors = userRepository.findByRole(Role.DOCTOR).size();
        long totalAppointments = appointmentRepository.findAll().size();
        long completedAppointments = appointmentRepository.findAll().stream()
                .filter(appointment -> appointment.getStatus() == AppointmentStatus.COMPLETED)
                .count();
        long pendingAppointments = appointmentRepository.findAll().stream()
                .filter(appointment -> appointment.getStatus() == AppointmentStatus.SCHEDULED || appointment.getStatus() == AppointmentStatus.CONFIRMED)
                .count();

        return DashboardResponse.builder()
                .totalPatients(totalPatients)
                .totalDoctors(totalDoctors)
                .totalAppointments(totalAppointments)
                .completedAppointments(completedAppointments)
                .pendingAppointments(pendingAppointments)
                .build();
    }

    private DoctorResponse mapToDoctorResponse(User doctor, DoctorProfile profile) {
        return DoctorResponse.builder()
                .id(doctor.getId())
                .name(doctor.getName())
                .email(doctor.getEmail())
                .phone(doctor.getPhone())
                .specialization(profile != null ? profile.getSpecialization() : null)
                .experienceYears(profile != null ? profile.getExperienceYears() : null)
                .qualification(profile != null ? profile.getQualification() : null)
                .availableDays(profile != null ? profile.getAvailableDays() : null)
                .slotDurationMinutes(profile != null ? profile.getSlotDurationMinutes() : null)
                .firstName(doctor.getName())
                .phoneNumber(doctor.getPhone())
                .experience(profile != null ? profile.getExperienceYears() : null)
                .available(Boolean.TRUE)
                .build();
    }

    private AppointmentResponse mapToAppointmentResponse(Appointment appointment) {
        return AppointmentResponse.builder()
                .id(appointment.getId())
                .patientId(appointment.getPatient() != null ? appointment.getPatient().getId() : null)
                .patientEmail(appointment.getPatient() != null ? appointment.getPatient().getEmail() : null)
                .doctorId(appointment.getDoctor() != null ? appointment.getDoctor().getId() : null)
                .doctorEmail(appointment.getDoctor() != null ? appointment.getDoctor().getEmail() : null)
                .appointmentDate(appointment.getAppointmentDate())
                .appointmentTime(appointment.getAppointmentTime())
                .status(appointment.getStatus() != null ? appointment.getStatus().name() : null)
                .reason(appointment.getReason())
                .notes(appointment.getNotes())
                .patientName(appointment.getPatient() != null ? appointment.getPatient().getName() : null)
                .doctorName(appointment.getDoctor() != null ? appointment.getDoctor().getName() : null)
                .doctorSpecialization(findDoctorProfile(appointment.getDoctor() != null ? appointment.getDoctor().getId() : null))
                .specialization(findDoctorProfile(appointment.getDoctor() != null ? appointment.getDoctor().getId() : null))
                .createdAt(appointment.getCreatedAt())
                .build();
    }

    private String findDoctorProfile(Long doctorUserId) {
        if (doctorUserId == null) {
            return null;
        }
        return doctorProfileRepository.findByUserId(doctorUserId).map(DoctorProfile::getSpecialization).orElse(null);
    }

    private PatientProfileResponse mapToPatientResponse(User user, PatientProfile profile) {
        return PatientProfileResponse.builder()
                .id(profile != null ? profile.getId() : null)
                .userId(user.getId())
                .name(user.getName())
                .email(user.getEmail())
                .phone(user.getPhone())
                .dateOfBirth(profile != null ? profile.getDateOfBirth() : null)
                .gender(profile != null && profile.getGender() != null ? profile.getGender().name() : null)
                .bloodGroup(profile != null ? profile.getBloodGroup() : null)
                .address(profile != null ? profile.getAddress() : null)
                .firstName(user.getName())
                .phoneNumber(user.getPhone())
                .build();
    }
}
