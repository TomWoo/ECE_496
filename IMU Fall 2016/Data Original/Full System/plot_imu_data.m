clear; close all;

%% Import and process data
% Parameters
imu_file_loc = '.\All Tests\Pressure chamber\Test Data 11_8 am\10dof_15.csv';  % Location of IMU data retrieved from ESP8266
ground_truth = true;  % Set to True if you have hand recorded pressure chamber readings you would like to compare to. Else set false.
chamber_file_loc = '.\Highlighted tests\pressure_chamber_11_8_2016_chamber_log.csv';  % Location of hand recorded pressure chamber readings (if used)

% Import IMU log
disp(sprintf('\nProcessing: \n\t%s', imu_file_loc))
[t_ms,ax,ay,az,rvx,rvy,rvz,pres,temp] = import_imu_log(imu_file_loc);

% Optional: Import pressure ground truth
if ground_truth
    [truth_sec, truth_kgpcm2] = import_chamber_log(chamber_file_loc);
    truth_hpa = truth_kgpcm2 * 980.7;
end

% Process
t_s = t_ms / 1000;
t_step = diff(t_s);

% Give feedback
runtime = (t_s(end) - t_s(1)) / 60;
disp(sprintf('\nRuntime was %.2f minutes', runtime))

%% Plot everything
% Timesteps
figure()
plot(t_s(1:size(t_s)-1),t_step)
title('Update Interals')
xlabel('Time (s)')
ylabel('Time Delay (s)')
grid on

% Acceleration and rotation
figure()
subplot(2,1,1)
plot(t_s, ax,'r',t_s,ay,'g',t_s,az,'b')
title('Linear Acceleration')
xlabel('Time (s)')
ylabel('Acceleration (m/s^2)')
legend('x','y','z')
grid on

subplot(2,1,2)
plot(t_s, rvx,'r',t_s,rvy,'g',t_s,rvz,'b')
title('Rotational Velocity')
xlabel('Time (s)')
ylabel('Rotational Velocity (degrees/s)')
legend('x','y','z')
grid on

% Pressure and temperature
figure()
subfigs = 2 + ground_truth;
subplot(subfigs,1,1)
plot(t_s, pres,'k')
title('Pressure in Epoxy (from IMU)')
xlabel('Time (s)')
ylabel('Pressure (hPa)')
grid on

if ground_truth
    subplot(subfigs, 1, 2)
    plot(truth_sec, truth_hpa,'k--')
    title('Pressure in Chamber (from gauge)')
    xlabel('Time (s)')
    ylabel('Pressure (hPa)')
    grid on
end

subplot(subfigs, 1, 2 + ground_truth)
plot(t_s, temp)
title('Temperature')
xlabel('Time (s)')
ylabel('Temperature (^{\circ}C)')
grid on