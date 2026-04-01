package com.healthcare.app.service;

import com.healthcare.app.dto.response.AppointmentResponse;

import java.util.List;

/**
 * Service interface for doctor operations
 */
public interface DoctorService {
    
    /**
     * Get all appointments for a doctor
     * @param email doctor email
     * @return list of appointments
     */
    List<AppointmentResponse> getMyAppointments(String email);
    
    /**
     * Get patient history
     * @param patientId patient ID
     * @return list of patient's appointments
     */
    List<AppointmentResponse> getPatientHistory(Long patientId);
}
