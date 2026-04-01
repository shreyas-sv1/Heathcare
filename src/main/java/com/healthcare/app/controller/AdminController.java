package com.healthcare.app.controller;

import com.healthcare.app.dto.request.CreateDoctorRequest;
import com.healthcare.app.dto.response.DashboardResponse;
import com.healthcare.app.dto.response.DoctorResponse;
import com.healthcare.app.dto.response.PatientProfileResponse;
import com.healthcare.app.dto.response.AppointmentResponse;
import com.healthcare.app.service.AdminService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/admin")
@RequiredArgsConstructor
@PreAuthorize("hasRole('ADMIN')")
@Tag(name = "Admin", description = "Admin management APIs")
@SecurityRequirement(name = "bearerAuth")
public class AdminController {

    private final AdminService adminService;

    @GetMapping("/dashboard")
    @Operation(summary = "Get dashboard statistics", description = "Retrieve dashboard statistics for admin")
    public ResponseEntity<DashboardResponse> getDashboardStats() {
        DashboardResponse response = adminService.getDashboardStats();
        return ResponseEntity.ok(response);
    }

    @GetMapping("/patients")
    @Operation(summary = "Get all patients", description = "Retrieve list of all patients")
    public ResponseEntity<List<PatientProfileResponse>> getAllPatients() {
        List<PatientProfileResponse> patients = adminService.getAllPatients();
        return ResponseEntity.ok(patients);
    }

    @GetMapping("/appointments")
    @Operation(summary = "Get all appointments", description = "Retrieve list of all appointments")
    public ResponseEntity<List<AppointmentResponse>> getAllAppointments() {
        List<AppointmentResponse> appointments = adminService.getAllAppointments();
        return ResponseEntity.ok(appointments);
    }

    @PostMapping("/doctors")
    @Operation(summary = "Create doctor", description = "Create a new doctor account")
    public ResponseEntity<DoctorResponse> createDoctor(@Valid @RequestBody CreateDoctorRequest request) {
        DoctorResponse response = adminService.createDoctor(request);
        return ResponseEntity.status(HttpStatus.CREATED).body(response);
    }

    @DeleteMapping("/doctors/{id}")
    @Operation(summary = "Delete doctor", description = "Delete a doctor account")
    public ResponseEntity<Void> deleteDoctor(@PathVariable Long id) {
        adminService.deleteDoctor(id);
        return ResponseEntity.noContent().build();
    }
}
