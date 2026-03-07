# Misc

Follower requests for subsystems are made with the following template
`public TemplateSubsystem(String name, int motor1ID, int motor2ID, boolean reverseMotor2, SubsystemMode mode, double defaultValue)`
From 1-11-26-Position-and-Velocity.md

Motion Magic is a position controller. It reads a position value from the motor or source and using that to get a voltage and velocity number. It is not a regular PID controller; It is called a PID Motion Profile. Plans out exactly how it wants the position/velocity to go for the wheel. 
From 1-12-26-Position.md