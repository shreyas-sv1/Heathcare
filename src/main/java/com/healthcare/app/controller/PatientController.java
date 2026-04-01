package com.healthcare.app.controller;

import com.healthcare.app.dto.request.UpdatePatientProfileRequest;
import com.healthcare.app.dto.response.MedicalRecordResponse;
import com.healthcare.app.dto.response.PatientProfileResponse;
import com.healthcare.app.service.PatientService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/patients")
@RequiredArgsConstructor
@PreAuthorize("hasRole('PATIENT')")
@Tag(name = "Patient", description = "Patient profile management APIs")
@SecurityRequirement(name = "bearerAuth")
public class PatientController {

    private final PatientService patientService;

    @GetMapping({"/profile", "/me"})
    @Operation(summary = "Get patient profile", description = "Retrieve patient profile information")
    public ResponseEntity<PatientProfileResponse> getProfile(@AuthenticationPrincipal UserDetails userDetails) {
        PatientProfileResponse response = patientService.getProfile(userDetails.getUsername());
        return ResponseEntity.ok(response);
    }

    @PutMapping({"/profile", "/me"})
    @Operation(summary = "Update patient profile", description = "Update patient profile information")
    public ResponseEntity<PatientProfileResponse> updateProfile(
            @AuthenticationPrincipal UserDetails userDetails,
            @Valid @RequestBody UpdatePatientProfileRequest request) {
        PatientProfileResponse response = patientService.updateProfile(userDetails.getUsername(), request);
        return ResponseEntity.ok(response);
    }

    @GetMapping("/medical-records")
    @Operation(summary = "Get medical records", description = "Retrieve all medical records for the patient")
    public ResponseEntity<java.util.List<MedicalRecordResponse>> getMedicalRecords(@AuthenticationPrincipal UserDetails userDetails) {
        java.util.List<MedicalRecordResponse> records = patientService.getMedicalRecords(userDetails.getUsername());
        return ResponseEntity.ok(records);
    }
}
