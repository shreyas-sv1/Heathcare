package com.healthcare.app.service;

import com.healthcare.app.dto.request.UpdatePatientProfileRequest;
import com.healthcare.app.dto.response.DoctorResponse;
import com.healthcare.app.dto.response.MedicalRecordResponse;
import com.healthcare.app.dto.response.PatientProfileResponse;

import java.util.List;

/**
 * Service interface for patient operations
 */
public interface PatientService {
    
    /**
     * Get patient profile by email
     * @param email patient email
     * @return patient profile details
     */
    PatientProfileResponse getProfile(String email);
    
    /**
     * Update patient profile
     * @param email patient email
     * @param request update details
     * @return updated patient profile
     */
    PatientProfileResponse updateProfile(String email, UpdatePatientProfileRequest request);
    
    /**
     * Get all doctors
     * @return list of all doctors
     */
    List<DoctorResponse> getAllDoctors();
    
    /**
     * Get doctor by ID
     * @param id doctor ID
     * @return doctor details
     */
    DoctorResponse getDoctorById(Long id);
    
    /**
     * Get medical records for a patient
     * @param email patient email
     * @return list of medical records
     */
    List<MedicalRecordResponse> getMedicalRecords(String email);
}
