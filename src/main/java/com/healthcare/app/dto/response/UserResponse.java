package com.healthcare.app.dto.response;

import com.healthcare.app.enums.Role;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class UserResponse {
    private Long id;
    private String name;
    private String email;
    private Role role;
    private String phone;
    private String firstName;
    private String lastName;
    private String phoneNumber;
    private Boolean active;
    private java.time.LocalDateTime createdAt;
    private java.time.LocalDate dateOfBirth;
    private String gender;
    private String bloodGroup;
}
