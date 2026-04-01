package com.healthcare.app.service.impl;

import com.healthcare.app.dto.request.CreatePrescriptionRequest;
import com.healthcare.app.dto.response.PrescriptionItemResponse;
import com.healthcare.app.dto.response.PrescriptionResponse;
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
        User doctorUser = userRepository.findByEmail(doctorEmail)
                .orElseThrow(() -> new ResourceNotFoundException("Doctor not found"));

        DoctorProfile doctorProfile = doctorProfileRepository.findByUserId(doctorUser.getId())
                .orElseThrow(() -> new ResourceNotFoundException("Doctor profile not found"));

        Appointment appointment = appointmentRepository.findById(request.getAppointmentId())
                .orElseThrow(() -> new ResourceNotFoundException("Appointment not found"));

        if (!appointment.getDoctor().getId().equals(doctorUser.getId())) {
            throw new BadRequestException("You can only create prescriptions for your own appointments");
        }

        if (appointment.getStatus() != AppointmentStatus.COMPLETED) {
            throw new BadRequestException("Prescription can only be created for completed appointments");
        }

        Prescription prescription = new Prescription();
        prescription.setAppointment(appointment);
        prescription.setPatient(appointment.getPatient());
        prescription.setDoctor(doctorUser);
        prescription.setDiagnosis(request.getDiagnosis());
        prescription.setNotes(request.getNotes());
        prescription.setIssuedDate(LocalDate.now());

        Prescription saved = prescriptionRepository.save(prescription);

        if (request.getItems() != null && !request.getItems().isEmpty()) {
            List<PrescriptionItem> items = request.getItems().stream().map(itemRequest -> {
                PrescriptionItem item = new PrescriptionItem();
                item.setPrescription(saved);
                item.setMedicineName(itemRequest.getMedicineName());
                item.setDosage(itemRequest.getDosage());
                item.setFrequency(itemRequest.getFrequency());
                item.setDurationDays(itemRequest.getDurationDays());
                item.setInstructions(itemRequest.getInstructions());
                return item;
            }).collect(Collectors.toList());
            saved.setItems(items);
            saved = prescriptionRepository.save(saved);
        }

        return mapToPrescriptionResponse(saved, doctorProfile);
    }

    @Override
    public List<PrescriptionResponse> getMyPrescriptions(String patientEmail) {
        User patientUser = userRepository.findByEmail(patientEmail)
                .orElseThrow(() -> new ResourceNotFoundException("Patient not found"));

        PatientProfile profile = patientProfileRepository.findByUserId(patientUser.getId())
                .orElseThrow(() -> new ResourceNotFoundException("Patient profile not found"));

        return prescriptionRepository.findByPatientId(patientUser.getId()).stream()
                .map(prescription -> mapToPrescriptionResponse(prescription, doctorProfileRepository.findByUserId(prescription.getDoctor().getId()).orElse(null)))
                .collect(Collectors.toList());
    }

    private PrescriptionResponse mapToPrescriptionResponse(Prescription prescription, DoctorProfile doctorProfile) {
        List<PrescriptionItemResponse> items = prescription.getItems() == null ? List.of() : prescription.getItems().stream()
                .map(this::mapToPrescriptionItemResponse)
                .collect(Collectors.toList());

        return PrescriptionResponse.builder()
                .id(prescription.getId())
                .appointmentId(prescription.getAppointment().getId())
                .patientName(prescription.getPatient() != null ? prescription.getPatient().getName() : null)
                .doctorName(prescription.getDoctor() != null ? prescription.getDoctor().getName() : null)
                .issuedDate(prescription.getIssuedDate())
                .prescriptionDate(prescription.getIssuedDate())
                .diagnosis(prescription.getDiagnosis())
                .notes(prescription.getNotes())
                .items(items)
                .medicines(items)
                .build();
    }

    private PrescriptionItemResponse mapToPrescriptionItemResponse(PrescriptionItem item) {
        return PrescriptionItemResponse.builder()
                .id(item.getId())
                .medicineName(item.getMedicineName())
                .dosage(item.getDosage())
                .frequency(item.getFrequency())
                .durationDays(item.getDurationDays())
                .duration(item.getDurationDays())
                .instructions(item.getInstructions())
                .build();
    }
}
