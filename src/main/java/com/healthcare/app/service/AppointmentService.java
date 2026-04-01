package com.healthcare.app.service;

import com.healthcare.app.dto.request.BookAppointmentRequest;
import com.healthcare.app.dto.request.UpdateAppointmentStatusRequest;
import com.healthcare.app.dto.response.AppointmentResponse;

import java.util.List;

/**
 * Service interface for appointment operations
 */
public interface AppointmentService {
    
    /**
     * Book a new appointment
     * @param patientEmail patient email
     * @param request appointment details
     * @return created appointment
     */
    AppointmentResponse bookAppointment(String patientEmail, BookAppointmentRequest request);
    
    /**
     * Get all appointments for a patient
     * @param patientEmail patient email
     * @return list of appointments
     */
    List<AppointmentResponse> getPatientAppointments(String patientEmail);
    
    /**
     * Cancel an appointment
     * @param appointmentId appointment ID
     * @param patientEmail patient email
     * @return cancelled appointment
     */
    AppointmentResponse cancelAppointment(Long appointmentId, String patientEmail);

    /**
     * Get an appointment by ID
     * @param appointmentId appointment ID
     * @return appointment details
     */
    AppointmentResponse getAppointmentById(Long appointmentId);
    
    /**
     * Update appointment status (doctor only)
     * @param appointmentId appointment ID
     * @param request status update details
     * @param doctorEmail doctor email
     * @return updated appointment
     */
    AppointmentResponse updateAppointmentStatus(Long appointmentId, UpdateAppointmentStatusRequest request, String doctorEmail);
    
    /**
     * Get all appointments (admin only)
     * @return list of all appointments
     */
    List<AppointmentResponse> getAllAppointments();
}
