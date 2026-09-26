# 9-26-2026 Turret Shoot on the Move
    Zachary Martinez, Anthony Wheeler

## Goals
- Create a shoot on the move system for the turret bot
- Test the shoot on the move algorithm

## Results
- Wrote `aimAtHub()` in `SuperSystem`, which uses the robot's translational and angular velocity to create a "lookahead pose", where the robot would be if its velocity stayed constant in a given "factor". This is provided by `NerdDrivetrain`.
- Also wrote `aimAtHubMason()` which only uses the translational velocity for the lookahead pose, then adds the velocity tangential to the turret as the robot rotates. This may be more accurate?
- Set up drivetrain simulation for the turret, allowing us to look at how the turret aims. `Field2d` logging seems broken right now, so Elastic cannot place the robot's position in the field. For now, use AdvantageScope to visualize the position of seperately logged `Pose2d` objects.

## Continuation
- Test SOTM with the real turret bot.