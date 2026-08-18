## Procedure for Testing Motors on the testbench
1. Hardware (Testbench)
    a. Roborio/systemcore
    b. PDP/PDH
    c. Motor
    d. Power Source/Battery
    e, Circuit Breaker
    f. CAN wiring
    g. Any encoder/sensor being tested
    h. Laptop/driver station
2. Software configuration
    a. WPILib 
    b. Phoenix 6 
    c. Motor CAN ID
    d. Motor inversion
    e. Neutral mode
    f. Current limits
    g. Voltage limits
    h. Phoenix Tuner X
3. Testing Procedure
    a. Label the Motor with a Motor number/name
    b. Secure the motor to the testbench.
    c. Verify all wiring and CAN connections.
    d. Establish a connection between Roborio/systemcore and Driver Station
    e. Load Phoenix Tuner X
    f. Enable the robot.
    g. Using Phoenix Tuner, feed the motor direct voltage
    h. Start with 1 volt and go up to 5 - 6 volts depending on the behavior of the motor
    i. Verify the motor rotates in the expected direction.
    j. Plot Stator Current, Supply Current, and Velocity
        i. Kraken X60
            a. Test Voltage: ~ 5 V
            b. Velocity: ~ 50 RPM
            c. Stator Current: ~1.1 A
        ii. Falcon
            a. Test Voltage: ~ 5 V
            b. Velocity: ~ 44 RPM
            c. Stator Current: ~ 0.9 A
        iii. Kraken X44
            a. Test Voltage: ~ 5 V
            b. Velocity: ~ 75 RPM
            c. Stator Current: ~ 2.2 A
    k. Repeat the test in the reverse direction.
    l. Observe any rumbling or loud, unusual noises
    m. Disable the motor
NOTE: Additional testing at different voltages and under load should be performed before concluding motor performance. This is only the free spin test.
4. Recording
    a. Motor Information
        i. Motor type/model
    b. Test Conditions
        i. Applied voltage
        ii. Whether the motor was free-spinning or under load
    c. Motor Measurements
        i. Velocity (RPM)
        ii. Stator Current (A)
        iii. Supply Current (A)
        iv. Applied Voltage (V)
    d. Motor Behavior
        i. Unusual noises 
        ii. Rumbling, screeching, clicking
        iii. Vibrations or wobbling
        iv. Skipping or inconsistent rotation
        v. Changes in velocity or current
        vi. Any visible mechanical issues
    e. Controller/Communication
        i. Phoenix Tuner X faults
        ii. CAN errors
        iii. Motor controller warnings
        iv. Any unexpected behavior
    f. Final Assessment
        i. Good / Bad
        ii. Any important reasoning

