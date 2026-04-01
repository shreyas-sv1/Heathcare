package com.healthcare.app.entity;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Table(name = "prescription_items")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class PrescriptionItem {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @ManyToOne
    @JoinColumn(name = "prescription_id", nullable = false)
    private Prescription prescription;
    
    @Column(name = "medicine_name", nullable = false)
    private String medicineName;
    
    @Column(nullable = false)
    private String dosage;
    
    @Column(nullable = false)
    private String frequency;
    
    @Column(name = "duration_days", nullable = false)
    private Integer durationDays;
    
    @Column(columnDefinition = "TEXT")
    private String instructions;
    
}
