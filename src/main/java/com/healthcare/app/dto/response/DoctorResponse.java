package com.healthcare.app.dto.response;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class DoctorResponse {
    private Long id;
    private String name;
    private String email;
    private String phone;
    private String specialization;
    private Integer experienceYears;
    private String qualification;
    private String availableDays;
    private Integer slotDurationMinutes;
    private String firstName;
    private String lastName;
    private String phoneNumber;
    private Integer experience;
    private String consultationFee;
    private Boolean available;
}
