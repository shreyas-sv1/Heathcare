package com.healthcare.app.service;

import com.healthcare.app.dto.request.LoginRequest;
import com.healthcare.app.dto.request.RegisterRequest;
import com.healthcare.app.dto.response.AuthResponse;

/**
 * Service interface for authentication operations
 */
public interface AuthService {
    
    /**
     * Register a new user
     * @param request registration details
     * @return authentication response with JWT token
     */
    AuthResponse register(RegisterRequest request);
    
    /**
     * Authenticate user and generate JWT token
     * @param request login credentials
     * @return authentication response with JWT token
     */
    AuthResponse login(LoginRequest request);
}
