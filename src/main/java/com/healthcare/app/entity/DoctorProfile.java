package com.healthcare.app.entity;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Table(name = "doctor_profiles")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class DoctorProfile {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @OneToOne
    @JoinColumn(name = "user_id", nullable = false, unique = true)
    private User user;
    
    @Column(nullable = false)
    private String specialization;
    
    @Column(name = "experience_years", nullable = false)
    private Integer experienceYears;
    
    @Column(nullable = false)
    private String qualification;
    
    @Column(name = "available_days", nullable = false)
    private String availableDays;
    
    @Column(name = "slot_duration_minutes", nullable = false)
    private Integer slotDurationMinutes;
    
}
