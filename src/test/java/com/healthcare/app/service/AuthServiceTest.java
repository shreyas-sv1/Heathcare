package com.healthcare.app.service;

import com.healthcare.app.dto.LoginRequestDTO;
import com.healthcare.app.dto.LoginResponseDTO;
import com.healthcare.app.dto.RegisterRequestDTO;
import com.healthcare.app.dto.UserResponseDTO;
import com.healthcare.app.entity.User;
import com.healthcare.app.enums.UserRole;
import com.healthcare.app.exception.DuplicateResourceException;
import com.healthcare.app.exception.ResourceNotFoundException;
import com.healthcare.app.exception.UnauthorizedException;
import com.healthcare.app.repository.UserRepository;
import com.healthcare.app.security.JwtTokenProvider;
import com.healthcare.app.service.impl.AuthServiceImpl;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.security.crypto.password.PasswordEncoder;

import java.util.Optional;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.api.Assertions.assertThatThrownBy;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.ArgumentMatchers.anyString;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
@DisplayName("Authentication Service Tests")
class AuthServiceTest {

    @Mock
    private UserRepository userRepository;

    @Mock
    private PasswordEncoder passwordEncoder;

    @Mock
    private JwtTokenProvider jwtTokenProvider;

    @InjectMocks
    private AuthServiceImpl authService;

    private User user;
    private RegisterRequestDTO registerRequest;
    private LoginRequestDTO loginRequest;

    @BeforeEach
    void setUp() {
        // Setup user
        user = new User();
        user.setId(1L);
        user.setEmail("test@healthcare.com");
        user.setPassword("encodedPassword123");
        user.setFirstName("John");
        user.setLastName("Doe");
        user.setRole(UserRole.PATIENT);
        user.setPhoneNumber("1234567890");

        // Setup register request
        registerRequest = new RegisterRequestDTO();
        registerRequest.setEmail("test@healthcare.com");
        registerRequest.setPassword("password123");
        registerRequest.setFirstName("John");
        registerRequest.setLastName("Doe");
        registerRequest.setRole(UserRole.PATIENT);
        registerRequest.setPhoneNumber("1234567890");

        // Setup login request
        loginRequest = new LoginRequestDTO();
        loginRequest.setEmail("test@healthcare.com");
        loginRequest.setPassword("password123");
    }

    @Test
    @DisplayName("Should successfully register new user")
    void testRegister_Success() {
        // Arrange
        when(userRepository.existsByEmail("test@healthcare.com")).thenReturn(false);
        when(passwordEncoder.encode("password123")).thenReturn("encodedPassword123");
        when(userRepository.save(any(User.class))).thenReturn(user);

        // Act
        UserResponseDTO result = authService.register(registerRequest);

        // Assert
        assertThat(result).isNotNull();
        assertThat(result.getId()).isEqualTo(1L);
        assertThat(result.getEmail()).isEqualTo("test@healthcare.com");
        assertThat(result.getFirstName()).isEqualTo("John");
        assertThat(result.getLastName()).isEqualTo("Doe");
        assertThat(result.getRole()).isEqualTo(UserRole.PATIENT);
        assertThat(result.getPhoneNumber()).isEqualTo("1234567890");

        verify(userRepository, times(1)).existsByEmail("test@healthcare.com");
        verify(passwordEncoder, times(1)).encode("password123");
        verify(userRepository, times(1)).save(any(User.class));
    }

    @Test
    @DisplayName("Should throw DuplicateResourceException when email already exists")
    void testRegister_DuplicateEmail_ThrowsDuplicateResourceException() {
        // Arrange
        when(userRepository.existsByEmail("test@healthcare.com")).thenReturn(true);

        // Act & Assert
        assertThatThrownBy(() -> authService.register(registerRequest))
                .isInstanceOf(DuplicateResourceException.class)
                .hasMessageContaining("Email already registered");

        verify(userRepository, times(1)).existsByEmail("test@healthcare.com");
        verify(passwordEncoder, never()).encode(anyString());
        verify(userRepository, never()).save(any(User.class));
    }

    @Test
    @DisplayName("Should successfully login with valid credentials")
    void testLogin_Success() {
        // Arrange
        String token = "jwt.token.here";
        when(userRepository.findByEmail("test@healthcare.com")).thenReturn(Optional.of(user));
        when(passwordEncoder.matches("password123", "encodedPassword123")).thenReturn(true);
        when(jwtTokenProvider.generateToken(user)).thenReturn(token);

        // Act
        LoginResponseDTO result = authService.login(loginRequest);

        // Assert
        assertThat(result).isNotNull();
        assertThat(result.getToken()).isEqualTo(token);
        assertThat(result.getEmail()).isEqualTo("test@healthcare.com");
        assertThat(result.getRole()).isEqualTo(UserRole.PATIENT);
        assertThat(result.getFirstName()).isEqualTo("John");
        assertThat(result.getLastName()).isEqualTo("Doe");

        verify(userRepository, times(1)).findByEmail("test@healthcare.com");
        verify(passwordEncoder, times(1)).matches("password123", "encodedPassword123");
        verify(jwtTokenProvider, times(1)).generateToken(user);
    }

    @Test
    @DisplayName("Should throw UnauthorizedException when password is incorrect")
    void testLogin_WrongPassword_ThrowsUnauthorizedException() {
        // Arrange
        when(userRepository.findByEmail("test@healthcare.com")).thenReturn(Optional.of(user));
        when(passwordEncoder.matches("password123", "encodedPassword123")).thenReturn(false);

        // Act & Assert
        assertThatThrownBy(() -> authService.login(loginRequest))
                .isInstanceOf(UnauthorizedException.class)
                .hasMessageContaining("Invalid credentials");

        verify(userRepository, times(1)).findByEmail("test@healthcare.com");
        verify(passwordEncoder, times(1)).matches("password123", "encodedPassword123");
        verify(jwtTokenProvider, never()).generateToken(any(User.class));
    }

    @Test
    @DisplayName("Should throw ResourceNotFoundException when user not found")
    void testLogin_UserNotFound_ThrowsResourceNotFoundException() {
        // Arrange
        when(userRepository.findByEmail("test@healthcare.com")).thenReturn(Optional.empty());

        // Act & Assert
        assertThatThrownBy(() -> authService.login(loginRequest))
                .isInstanceOf(ResourceNotFoundException.class)
                .hasMessageContaining("User not found");

        verify(userRepository, times(1)).findByEmail("test@healthcare.com");
        verify(passwordEncoder, never()).matches(anyString(), anyString());
        verify(jwtTokenProvider, never()).generateToken(any(User.class));
    }
}
