package com.healthcare.app.service.impl;

import com.healthcare.app.dto.request.UpdatePatientProfileRequest;
import com.healthcare.app.dto.response.DoctorResponse;
import com.healthcare.app.dto.response.MedicalRecordResponse;
import com.healthcare.app.dto.response.PatientProfileResponse;
import com.healthcare.app.entity.DoctorProfile;
import com.healthcare.app.entity.MedicalRecord;
import com.healthcare.app.entity.PatientProfile;
import com.healthcare.app.entity.User;
import com.healthcare.app.enums.Gender;
import com.healthcare.app.enums.RecordType;
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
        User user = userRepository.findByEmail(email)
                .orElseThrow(() -> new ResourceNotFoundException("User not found"));
        PatientProfile profile = patientProfileRepository.findByUserId(user.getId())
                .orElseThrow(() -> new ResourceNotFoundException("Patient profile not found"));
        return mapToPatientProfileResponse(user, profile);
    }

    @Override
    @Transactional
    public PatientProfileResponse updateProfile(String email, UpdatePatientProfileRequest request) {
        User user = userRepository.findByEmail(email)
                .orElseThrow(() -> new ResourceNotFoundException("User not found"));

        if (request.getName() != null) {
            user.setName(request.getName());
        }
        if (request.getPhone() != null) {
            user.setPhone(request.getPhone());
        }
        userRepository.save(user);

        PatientProfile profile = patientProfileRepository.findByUserId(user.getId())
                .orElseThrow(() -> new ResourceNotFoundException("Patient profile not found"));

        if (request.getDateOfBirth() != null) {
            profile.setDateOfBirth(request.getDateOfBirth());
        }
        if (request.getGender() != null) {
            profile.setGender(Gender.valueOf(request.getGender()));
        }
        if (request.getBloodGroup() != null) {
            profile.setBloodGroup(request.getBloodGroup());
        }
        if (request.getAddress() != null) {
            profile.setAddress(request.getAddress());
        }

        PatientProfile updatedProfile = patientProfileRepository.save(profile);
        return mapToPatientProfileResponse(user, updatedProfile);
    }

    @Override
    public List<DoctorResponse> getAllDoctors() {
        return userRepository.findByRole(Role.DOCTOR).stream()
                .map(doctor -> mapToDoctorResponse(doctor, doctorProfileRepository.findByUserId(doctor.getId()).orElse(null)))
                .collect(Collectors.toList());
    }

    @Override
    public DoctorResponse getDoctorById(Long id) {
        User doctor = userRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Doctor not found"));
        if (doctor.getRole() != Role.DOCTOR) {
            throw new ResourceNotFoundException("User is not a doctor");
        }
        return mapToDoctorResponse(doctor, doctorProfileRepository.findByUserId(doctor.getId()).orElse(null));
    }

    @Override
    public List<MedicalRecordResponse> getMedicalRecords(String email) {
        User user = userRepository.findByEmail(email)
                .orElseThrow(() -> new ResourceNotFoundException("User not found"));

        PatientProfile profile = patientProfileRepository.findByUserId(user.getId())
                .orElseThrow(() -> new ResourceNotFoundException("Patient profile not found"));

        List<MedicalRecord> records = medicalRecordRepository.findByPatientId(user.getId());
        return records.stream().map(this::mapToMedicalRecordResponse).collect(Collectors.toList());
    }

    private PatientProfileResponse mapToPatientProfileResponse(User user, PatientProfile profile) {
        return PatientProfileResponse.builder()
                .id(profile.getId())
                .userId(user.getId())
                .name(user.getName())
                .email(user.getEmail())
                .phone(user.getPhone())
                .dateOfBirth(profile.getDateOfBirth())
                .gender(profile.getGender() != null ? profile.getGender().name() : null)
                .bloodGroup(profile.getBloodGroup())
                .address(profile.getAddress())
                .firstName(user.getName())
                .phoneNumber(user.getPhone())
                .build();
    }

    private DoctorResponse mapToDoctorResponse(User doctor, DoctorProfile profile) {
        DoctorResponse.DoctorResponseBuilder builder = DoctorResponse.builder()
                .id(doctor.getId())
                .name(doctor.getName())
                .email(doctor.getEmail())
                .phone(doctor.getPhone())
                .firstName(doctor.getName())
                .phoneNumber(doctor.getPhone())
                .available(Boolean.TRUE);

        if (profile != null) {
            builder.specialization(profile.getSpecialization())
                    .experienceYears(profile.getExperienceYears())
                    .qualification(profile.getQualification())
                    .availableDays(profile.getAvailableDays())
                    .slotDurationMinutes(profile.getSlotDurationMinutes())
                    .experience(profile.getExperienceYears());
        }

        return builder.build();
    }

    private MedicalRecordResponse mapToMedicalRecordResponse(MedicalRecord record) {
        return MedicalRecordResponse.builder()
                .id(record.getId())
                .recordDate(record.getRecordDate())
                .recordType(record.getRecordType() != null ? record.getRecordType().name() : RecordType.OTHER.name())
                .title(record.getTitle())
                .description(record.getDescription())
                .uploadedByName(record.getUploadedBy() != null ? record.getUploadedBy().getName() : null)
                .build();
    }
}
