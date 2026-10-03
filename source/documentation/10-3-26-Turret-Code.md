# 10-3-2026 Turret Code
    Zachary Martinez, Anthony Wheeler, Mason Tsai

## Goals
- Write as much turret code as possible before the turret bot is created

## Results
- Over the course of multiple days
- Refactored SuperSystem to use an enum-based approach to creating commands for individual subsystems
- Moved SuperSystem helper functions into `SuperSystemBase.java`
- Refactored `lookAtHub` into a new, combined function, `getExpectedTurretPosition()`.
- Created initial versions of shoot with distance and prep turret commands
- Created a skeleton for `shootCommand`
- Added controller bindings
- Refactored `LInTable`
- Added javadocs and other documentation

## Continuation
- Continue writing code
- Finish `shootCommand`
- Test on robot when assembled