package com.healthcare.app.service;

import com.healthcare.app.dto.request.CreatePrescriptionRequest;
import com.healthcare.app.dto.response.PrescriptionResponse;

import java.util.List;

/**
 * Service interface for prescription operations
 */
public interface PrescriptionService {
    
    /**
     * Create a new prescription
     * @param request prescription details
     * @param doctorEmail doctor email
     * @return created prescription
     */
    PrescriptionResponse createPrescription(CreatePrescriptionRequest request, String doctorEmail);
    
    /**
     * Get all prescriptions for a patient
     * @param patientEmail patient email
     * @return list of prescriptions
     */
    List<PrescriptionResponse> getMyPrescriptions(String patientEmail);
}
