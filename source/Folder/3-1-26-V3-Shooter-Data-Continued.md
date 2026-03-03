# V3 Counter Rollers, and Left and Right Shooter Data Analysis
    Daniel Gonzalez

## Goals
- Analyze the data to find the the kF Values of left shooter and counter rollers
- Find the kS values to offset the kF value
- Find the inverse of the equations
- Make a rough blueprint for an SOP

## Notes
- There is variation in the all of the kF Values off by thousandths to millionths for each subsystem
- In the equation x = Volts and y = Velocity

## Results
- Analyzed the kf Values for the shooters and counter rollers
- Found an average kF Value for shooters and counter rollers
- Found the inverse of the equations
- Made a rough blueprint for an SOP
- Found the kS Values for Shooter left and Right
- Calculated kA Values for Shooter left and right
- Found Feedforward Equation for left and right shooters

### Average kF Values
- Right Shooter   = 0.123
- Left Shooter    = 0.126
- Counter rollers = 0.129

### Offset kF Values
- Shooter right = 0.3315359183
- Shooter left  = 0.376049244

### kF Equations
- Shooter right   = y=8.21159x-0.483724
- Shooter left    = y=8.16927x-1.20443
- Counter rollers = y=8.22103x-2.69531

### Inverse of the equations
- Shooter right   = (x+0.483724)/8.21159 = y
- Shooter left    = (x+1.20443)/8.16927 = y
- Counter rollers = (x+2.69531)/8.22103 = y

### kS Values
- Shooter right = 0.208437
- Shooter left  = 0.250255

### kA Values
- Shooter right = 0.021071
- Shooter left  = 0.006534

### kV Values
- Shooter right = 0.119947
- Shooter left  = 0.122817

### Feedforward Equation
- Shooter right = Vapp = 0.208437 + (0.119947 • vtarget) + (0.021071 • atarget)
- Shooter left  = Vapp = 0.250255 + (0.122817 • vtarget) + (0.006534 • atarget)
- Vapp  = The final voltage applied to the motor controller.
- vtarget = Your target speed in Rotations Per Second (RPS).
- atarget = Your target acceleration in Rotations Per Second squared (RPS2)

## Continuation
- Find kS value for Counter rollers
- Offset kF value with kS value for Counter rollers
- find feedforward equation for Counter Rollers
- Work on writing an SOP