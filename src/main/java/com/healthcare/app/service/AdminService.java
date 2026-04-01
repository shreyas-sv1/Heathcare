package com.healthcare.app.service;

import com.healthcare.app.dto.request.CreateDoctorRequest;
import com.healthcare.app.dto.response.AppointmentResponse;
import com.healthcare.app.dto.response.DashboardResponse;
import com.healthcare.app.dto.response.DoctorResponse;
import com.healthcare.app.dto.response.PatientProfileResponse;

import java.util.List;

/**
 * Service interface for admin operations
 */
public interface AdminService {
    
    /**
     * Create a new doctor
     * @param request doctor details
     * @return created doctor
     */
    DoctorResponse createDoctor(CreateDoctorRequest request);
    
    /**
     * Delete a doctor
     * @param doctorId doctor ID
     */
    void deleteDoctor(Long doctorId);
    
    /**
     * Get all appointments
     * @return list of all appointments
     */
    List<AppointmentResponse> getAllAppointments();
    
    /**
     * Get all patients
     * @return list of all patients
     */
    List<PatientProfileResponse> getAllPatients();
    
    /**
     * Get dashboard statistics
     * @return dashboard stats
     */
    DashboardResponse getDashboardStats();
}
