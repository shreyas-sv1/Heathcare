package com.healthcare.app.repository;

import com.healthcare.app.entity.Appointment;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.time.LocalDate;
import java.time.LocalTime;
import java.util.List;

@Repository
public interface AppointmentRepository extends JpaRepository<Appointment, Long> {
    List<Appointment> findByPatientId(Long patientId);
    List<Appointment> findByDoctorId(Long doctorId);
    boolean existsByDoctorIdAndAppointmentDateAndAppointmentTime(Long doctorId, LocalDate date, LocalTime time);
    boolean existsByDoctorIdAndAppointmentDateAndAppointmentTimeAndStatusIn(Long doctorId, LocalDate date, LocalTime time, List<com.healthcare.app.enums.AppointmentStatus> status);
}
