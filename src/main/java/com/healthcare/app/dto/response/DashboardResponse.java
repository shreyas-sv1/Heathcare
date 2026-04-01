package com.healthcare.app.dto.response;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class DashboardResponse {
    private Long totalPatients;
    private Long totalDoctors;
    private Long totalAppointments;
    private Long completedAppointments;
    private Long pendingAppointments;
    private Long totalAdmins;
    private Long scheduledAppointments;
    private Long confirmedAppointments;
    private Long cancelledAppointments;
}
