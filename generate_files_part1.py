"""
Healthcare Application - Complete Source Generator
Run this after setup.ps1 to create all Java source files
"""

import os

def write_file(path, content):
    """Write content to file, creating directories as needed"""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f"✓ {path}")

# =======================
# ENUMS
# =======================

ROLE_ENUM = """package com.healthcare.app.enums;

public enum Role {
    PATIENT,
    DOCTOR,
    ADMIN
}
"""

APPOINTMENT_STATUS_ENUM = """package com.healthcare.app.enums;

public enum AppointmentStatus {
    SCHEDULED,
    CONFIRMED,
    COMPLETED,
    CANCELLED,
    NO_SHOW
}
"""

GENDER_ENUM = """package com.healthcare.app.enums;

public enum Gender {
    MALE,
    FEMALE,
    OTHER
}
"""

RECORD_TYPE_ENUM = """package com.healthcare.app.enums;

public enum RecordType {
    LAB_REPORT,
    PRESCRIPTION,
    DIAGNOSIS,
    IMAGING,
    OTHER
}
"""

# =======================
# ENTITIES
# =======================

USER_ENTITY = """package com.healthcare.app.entity;

import com.healthcare.app.enums.Role;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.CreationTimestamp;

import java.time.LocalDateTime;

@Entity
@Table(name = "users")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class User {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @Column(nullable = false)
    private String name;
    
    @Column(nullable = false, unique = true)
    private String email;
    
    @Column(nullable = false)
    private String password;
    
    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private Role role;
    
    @Column(nullable = false)
    private String phone;
    
    @CreationTimestamp
    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;
    
}
"""

DOCTOR_PROFILE_ENTITY = """package com.healthcare.app.entity;

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
"""

PATIENT_PROFILE_ENTITY = """package com.healthcare.app.entity;

import com.healthcare.app.enums.Gender;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDate;

@Entity
@Table(name = "patient_profiles")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class PatientProfile {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @OneToOne
    @JoinColumn(name = "user_id", nullable = false, unique = true)
    private User user;
    
    @Column(name = "date_of_birth")
    private LocalDate dateOfBirth;
    
    @Enumerated(EnumType.STRING)
    private Gender gender;
    
    @Column(name = "blood_group")
    private String bloodGroup;
    
    @Column(columnDefinition = "TEXT")
    private String address;
    
}
"""

APPOINTMENT_ENTITY = """package com.healthcare.app.entity;

import com.healthcare.app.enums.AppointmentStatus;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.CreationTimestamp;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;

@Entity
@Table(name = "appointments")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Appointment {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @ManyToOne
    @JoinColumn(name = "patient_id", nullable = false)
    private User patient;
    
    @ManyToOne
    @JoinColumn(name = "doctor_id", nullable = false)
    private User doctor;
    
    @Column(name = "appointment_date", nullable = false)
    private LocalDate appointmentDate;
    
    @Column(name = "appointment_time", nullable = false)
    private LocalTime appointmentTime;
    
    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private AppointmentStatus status;
    
    @Column(columnDefinition = "TEXT")
    private String reason;
    
    @Column(columnDefinition = "TEXT")
    private String notes;
    
    @CreationTimestamp
    @Column(name = "created_at", nullable = false, updatable = false)
    private LocalDateTime createdAt;
    
}
"""

PRESCRIPTION_ENTITY = """package com.healthcare.app.entity;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name = "prescriptions")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class Prescription {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @OneToOne
    @JoinColumn(name = "appointment_id", nullable = false, unique = true)
    private Appointment appointment;
    
    @ManyToOne
    @JoinColumn(name = "doctor_id", nullable = false)
    private User doctor;
    
    @ManyToOne
    @JoinColumn(name = "patient_id", nullable = false)
    private User patient;
    
    @Column(name = "issued_date", nullable = false)
    private LocalDate issuedDate;
    
    @Column(nullable = false)
    private String diagnosis;
    
    @Column(columnDefinition = "TEXT")
    private String notes;
    
    @OneToMany(mappedBy = "prescription", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<PrescriptionItem> items = new ArrayList<>();
    
}
"""

PRESCRIPTION_ITEM_ENTITY = """package com.healthcare.app.entity;

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
"""

MEDICAL_RECORD_ENTITY = """package com.healthcare.app.entity;

import com.healthcare.app.enums.RecordType;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDate;

@Entity
@Table(name = "medical_records")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class MedicalRecord {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    
    @ManyToOne
    @JoinColumn(name = "patient_id", nullable = false)
    private User patient;
    
    @Column(name = "record_date", nullable = false)
    private LocalDate recordDate;
    
    @Enumerated(EnumType.STRING)
    @Column(name = "record_type", nullable = false)
    private RecordType recordType;
    
    @Column(nullable = false)
    private String title;
    
    @Column(columnDefinition = "TEXT")
    private String description;
    
    @ManyToOne
    @JoinColumn(name = "uploaded_by", nullable = false)
    private User uploadedBy;
    
}
"""

# Write all files
print("Generating Healthcare Application Source Files...\n")

write_file("src/main/java/com/healthcare/app/enums/Role.java", ROLE_ENUM)
write_file("src/main/java/com/healthcare/app/enums/AppointmentStatus.java", APPOINTMENT_STATUS_ENUM)
write_file("src/main/java/com/healthcare/app/enums/Gender.java", GENDER_ENUM)
write_file("src/main/java/com/healthcare/app/enums/RecordType.java", RECORD_TYPE_ENUM)

write_file("src/main/java/com/healthcare/app/entity/User.java", USER_ENTITY)
write_file("src/main/java/com/healthcare/app/entity/DoctorProfile.java", DOCTOR_PROFILE_ENTITY)
write_file("src/main/java/com/healthcare/app/entity/PatientProfile.java", PATIENT_PROFILE_ENTITY)
write_file("src/main/java/com/healthcare/app/entity/Appointment.java", APPOINTMENT_ENTITY)
write_file("src/main/java/com/healthcare/app/entity/Prescription.java", PRESCRIPTION_ENTITY)
write_file("src/main/java/com/healthcare/app/entity/PrescriptionItem.java", PRESCRIPTION_ITEM_ENTITY)
write_file("src/main/java/com/healthcare/app/entity/MedicalRecord.java", MEDICAL_RECORD_ENTITY)

print("\n✓ Phase 1 Complete: Enums and Entities created!")
print("\nNext: Run generate_files_part2.py for Repositories and DTOs")
