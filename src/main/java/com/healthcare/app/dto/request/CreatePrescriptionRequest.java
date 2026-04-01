package com.healthcare.app.dto.request;

import jakarta.validation.constraints.NotNull;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class CreatePrescriptionRequest {
    
    @NotNull(message = "Appointment ID is required")
    private Long appointmentId;
    
    private String diagnosis;
    private String notes;
    
    @NotNull(message = "Prescription items are required")
    private List<PrescriptionItemRequest> items;
}
