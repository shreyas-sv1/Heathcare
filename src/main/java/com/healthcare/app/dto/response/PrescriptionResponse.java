package com.healthcare.app.dto.response;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDate;
import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class PrescriptionResponse {
    private Long id;
    private Long appointmentId;
    private String doctorName;
    private String patientName;
    private LocalDate issuedDate;
    private String diagnosis;
    private String notes;
    private List<PrescriptionItemResponse> items;
    private LocalDate prescriptionDate;
    private List<PrescriptionItemResponse> medicines;
    private java.time.LocalDateTime createdAt;
}
