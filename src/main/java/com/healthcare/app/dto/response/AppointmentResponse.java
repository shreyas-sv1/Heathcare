package com.healthcare.app.dto.response;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDate;
import java.time.LocalTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class AppointmentResponse {
    private Long id;
    private Long patientId;
    private String patientEmail;
    private Long doctorId;
    private String doctorEmail;
    private LocalDate appointmentDate;
    private LocalTime appointmentTime;
    private String status;
    private String reason;
    private String notes;
    private String doctorName;
    private String doctorSpecialization;
    private String patientName;
    private String specialization;
    private java.time.LocalDateTime createdAt;
    private java.time.LocalDateTime updatedAt;
}
