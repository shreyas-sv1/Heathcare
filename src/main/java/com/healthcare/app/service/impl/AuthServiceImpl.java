package com.healthcare.app.service.impl;

import com.healthcare.app.dto.request.LoginRequest;
import com.healthcare.app.dto.request.RegisterRequest;
import com.healthcare.app.dto.response.AuthResponse;
import com.healthcare.app.entity.PatientProfile;
import com.healthcare.app.entity.User;
import com.healthcare.app.enums.Gender;
import com.healthcare.app.enums.Role;
import com.healthcare.app.exception.BadRequestException;
import com.healthcare.app.exception.ResourceNotFoundException;
import com.healthcare.app.repository.PatientProfileRepository;
import com.healthcare.app.repository.UserRepository;
import com.healthcare.app.security.JwtUtil;
import com.healthcare.app.service.AuthService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@RequiredArgsConstructor
@Slf4j
public class AuthServiceImpl implements AuthService {

    private final UserRepository userRepository;
    private final PatientProfileRepository patientProfileRepository;
    private final PasswordEncoder passwordEncoder;
    private final JwtUtil jwtUtil;

    @Override
    @Transactional
    public AuthResponse register(RegisterRequest request) {
        log.info("Registering new user with email: {}", request.getEmail());

        if (userRepository.findByEmail(request.getEmail()).isPresent()) {
            throw new BadRequestException("User already exists with email: " + request.getEmail());
        }

        User user = new User();
        user.setName(request.getName());
        user.setEmail(request.getEmail());
        user.setPassword(passwordEncoder.encode(request.getPassword()));
        user.setPhone(request.getPhone());
        user.setRole(Role.PATIENT);
        user.setActive(true);

        User savedUser = userRepository.save(user);

        PatientProfile profile = new PatientProfile();
        profile.setUser(savedUser);
        profile.setDateOfBirth(request.getDateOfBirth());
        profile.setGender(Gender.valueOf(request.getGender()));
        profile.setBloodGroup(request.getBloodGroup());
        profile.setAddress(request.getAddress());
        patientProfileRepository.save(profile);

        String token = jwtUtil.generateToken(savedUser.getEmail(), savedUser.getRole());

        return AuthResponse.builder()
                .token(token)
                .userType(savedUser.getRole().name())
                .role(savedUser.getRole().name())
                .name(savedUser.getName())
                .email(savedUser.getEmail())
                .message("Registration successful")
                .build();
    }

    @Override
    public AuthResponse login(LoginRequest request) {
        User user = userRepository.findByEmail(request.getEmail())
                .orElseThrow(() -> new ResourceNotFoundException("Invalid email or password"));

        if (!user.isActive()) {
            throw new BadRequestException("User account is inactive");
        }

        if (!passwordEncoder.matches(request.getPassword(), user.getPassword())) {
            throw new BadRequestException("Invalid email or password");
        }

        String token = jwtUtil.generateToken(user.getEmail(), user.getRole());

        return AuthResponse.builder()
                .token(token)
                .userType(user.getRole().name())
                .role(user.getRole().name())
                .name(user.getName())
                .email(user.getEmail())
                .message("Login successful")
                .build();
    }
}
