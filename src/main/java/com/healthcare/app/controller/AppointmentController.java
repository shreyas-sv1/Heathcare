package com.healthcare.app.controller;

import com.healthcare.app.dto.request.BookAppointmentRequest;
import com.healthcare.app.dto.response.AppointmentResponse;
import com.healthcare.app.service.AppointmentService;
import com.healthcare.app.service.DoctorService;
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
@RequestMapping("/api/appointments")
@RequiredArgsConstructor
@Tag(name = "Appointment", description = "Appointment management APIs")
@SecurityRequirement(name = "bearerAuth")
public class AppointmentController {

    private final AppointmentService appointmentService;
    private final DoctorService doctorService;

    @PostMapping
    @PreAuthorize("hasRole('PATIENT')")
    @Operation(summary = "Book appointment", description = "Book a new appointment with a doctor")
    public ResponseEntity<AppointmentResponse> bookAppointment(
            @Valid @RequestBody BookAppointmentRequest request,
            @AuthenticationPrincipal UserDetails userDetails) {
        AppointmentResponse response = appointmentService.bookAppointment(request, userDetails.getUsername());
        return ResponseEntity.status(HttpStatus.CREATED).body(response);
    }

    @GetMapping("/my")
    @PreAuthorize("hasRole('PATIENT')")
    @Operation(summary = "Get my appointments", description = "Retrieve all appointments for the authenticated patient")
    public ResponseEntity<List<AppointmentResponse>> getMyAppointments(@AuthenticationPrincipal UserDetails userDetails) {
        List<AppointmentResponse> appointments = appointmentService.getPatientAppointments(userDetails.getUsername());
        return ResponseEntity.ok(appointments);
    }

    @GetMapping("/doctor/me")
    @PreAuthorize("hasRole('DOCTOR')")
    @Operation(summary = "Get doctor appointments", description = "Retrieve all appointments for the authenticated doctor")
    public ResponseEntity<List<AppointmentResponse>> getDoctorAppointments(@AuthenticationPrincipal UserDetails userDetails) {
        List<AppointmentResponse> appointments = doctorService.getMyAppointments(userDetails.getUsername());
        return ResponseEntity.ok(appointments);
    }

    @PutMapping("/{id}/status")
    @PreAuthorize("hasRole('DOCTOR')")
    @Operation(summary = "Update appointment status", description = "Update the status of an appointment")
    public ResponseEntity<AppointmentResponse> updateAppointmentStatus(
            @PathVariable Long id,
            @Valid @RequestBody com.healthcare.app.dto.request.UpdateAppointmentStatusRequest request,
            @AuthenticationPrincipal UserDetails userDetails) {
        AppointmentResponse response = appointmentService.updateAppointmentStatus(id, request, userDetails.getUsername());
        return ResponseEntity.ok(response);
    }

    @GetMapping("/{id}")
    @Operation(summary = "Get appointment by ID", description = "Retrieve appointment details by ID")
    public ResponseEntity<AppointmentResponse> getAppointmentById(@PathVariable Long id) {
        AppointmentResponse appointment = appointmentService.getAppointmentById(id);
        return ResponseEntity.ok(appointment);
    }

    @DeleteMapping("/{id}")
    @PreAuthorize("hasRole('PATIENT')")
    @Operation(summary = "Cancel appointment", description = "Cancel an appointment")
    public ResponseEntity<Void> cancelAppointment(
            @PathVariable Long id,
            @AuthenticationPrincipal UserDetails userDetails) {
        appointmentService.cancelAppointment(id, userDetails.getUsername());
        return ResponseEntity.noContent().build();
    }
}
