# Cannonball
 
Design a class Cannonball to model a cannonball that is fired into the air. A ball has
An x- and a y-position.
An x- and a y-velocity.
Supply the following methods:
A constructor with an x-position (the y-position is initially 0)
A method move(sec) that moves the ball to the next position (First compute the distance traveled in sec seconds, using the current velocities, then update the x- and y-positions; then update the y-velocity by taking into account the gravitational acceleration of -9.81 m/sec2; the x-velocity is unchanged.)
Methods getX and getY that get the current location of the cannonball
A method shoot whose arguments are the angle alpha and the y-velocity as v*sin(alpha); then keep calling move with a time interval of 0.1 seconds until the y-position is approximately 0; call getX and getY after every move and display the position; draw a figure to show the cannonball positions and trajectory.)