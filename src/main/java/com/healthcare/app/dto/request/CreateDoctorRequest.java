package com.healthcare.app.dto.request;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class CreateDoctorRequest {
    
    @NotBlank(message = "Name is required")
    private String name;
    
    @NotBlank(message = "Email is required")
    @Email(message = "Email should be valid")
    private String email;
    
    @NotBlank(message = "Password is required")
    private String password;
    
    @NotBlank(message = "Phone is required")
    private String phone;
    
    @NotBlank(message = "Specialization is required")
    private String specialization;
    
    @NotNull(message = "Experience years is required")
    private Integer experienceYears;
    
    @NotBlank(message = "Qualification is required")
    private String qualification;
    
    private String availableDays;
    
    private Integer slotDurationMinutes;
}
