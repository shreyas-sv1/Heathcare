package com.healthcare.app.controller;

import com.healthcare.app.dto.request.CreatePrescriptionRequest;
import com.healthcare.app.dto.request.UpdateAppointmentStatusRequest;
import com.healthcare.app.dto.response.AppointmentResponse;
import com.healthcare.app.dto.response.PrescriptionResponse;
import com.healthcare.app.service.AppointmentService;
import com.healthcare.app.service.DoctorService;
import com.healthcare.app.service.PrescriptionService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.security.SecurityRequirement;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/doctor")
@RequiredArgsConstructor
@Tag(name = "Doctor", description = "Doctor management APIs")
@SecurityRequirement(name = "bearerAuth")
@PreAuthorize("hasRole('DOCTOR')")
public class DoctorController {

    private final DoctorService doctorService;
    private final AppointmentService appointmentService;
    private final PrescriptionService prescriptionService;

    @GetMapping("/appointments")
    @Operation(summary = "Get doctor appointments", description = "Retrieve all appointments for the doctor")
    public ResponseEntity<List<AppointmentResponse>> getAppointments(@AuthenticationPrincipal UserDetails userDetails) {
        return ResponseEntity.ok(doctorService.getMyAppointments(userDetails.getUsername()));
    }

    @PutMapping("/appointments/{id}/status")
    @Operation(summary = "Update appointment status", description = "Update the status of an appointment")
    public ResponseEntity<AppointmentResponse> updateAppointmentStatus(
            @PathVariable Long id,
            @Valid @RequestBody UpdateAppointmentStatusRequest request,
            @AuthenticationPrincipal UserDetails userDetails) {
        return ResponseEntity.ok(appointmentService.updateAppointmentStatus(id, request, userDetails.getUsername()));
    }

    @PostMapping("/prescriptions")
    @Operation(summary = "Create prescription", description = "Create a new prescription for a patient")
    public ResponseEntity<PrescriptionResponse> createPrescription(
            @Valid @RequestBody CreatePrescriptionRequest request,
            @AuthenticationPrincipal UserDetails userDetails) {
        return ResponseEntity.status(HttpStatus.CREATED).body(prescriptionService.createPrescription(request, userDetails.getUsername()));
    }
}
