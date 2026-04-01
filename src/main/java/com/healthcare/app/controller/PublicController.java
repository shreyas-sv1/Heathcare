package com.healthcare.app.controller;

import com.healthcare.app.dto.response.DoctorResponse;
import com.healthcare.app.service.PatientService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/api")
@RequiredArgsConstructor
@Tag(name = "Public", description = "Public APIs - no authentication required")
public class PublicController {

    private final PatientService patientService;

    @GetMapping("/doctors")
    @Operation(summary = "List all doctors", description = "Public doctor listing")
    public ResponseEntity<List<DoctorResponse>> getAllDoctors() {
        return ResponseEntity.ok(patientService.getAllDoctors());
    }

    @GetMapping("/doctors/{id}")
    @Operation(summary = "Get doctor details", description = "Public doctor details")
    public ResponseEntity<DoctorResponse> getDoctorById(@PathVariable Long id) {
        return ResponseEntity.ok(patientService.getDoctorById(id));
    }
}