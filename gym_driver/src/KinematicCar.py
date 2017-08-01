from numpy import arange, sin, cos, tan, arctan, deg2rad, rad2deg
from scipy.integrate import odeint

from Car import Car, MAX_VEL, LEN_REAR, LEN_FRONT

# KinematicCar class
class KinematicCar(Car):

    # Modify attributes to reflect one game step
    def step(self, action_acc, action_angle):
        # Pre-process actions
        action_angle = deg2rad(action_angle)
        angle = deg2rad(self.angle)
        action_acc = max(min(action_acc, MAX_VEL - self.vel), -self.vel)
        # Solve differential equations
        t = arange(0.0, 1.0, 0.1)
        ode_state = (self.x, self.y, self.vel, angle)
        deltas = odeint(self.integrate, ode_state, t, action_acc, action_angle)
        x, y, vel, angle = deltas[-1]
        self.x, self.y, self.vel, self.angle = x, y, vel, rad2deg(angle) % 360

    # Calculate numerical values for variables in the differential equation
    @staticmethod
    def integrate(state, t, action_acc, action_angle):
        x, y, vel, angle = state
        beta = arctan((LEN_REAR / (LEN_REAR + LEN_FRONT)) * tan(action_angle))
        dx = vel * cos(angle + beta)
        dy = vel * sin(angle + beta)
        delta_vel = action_acc
        delta_angle = (vel / LEN_REAR) * sin(beta)
        return dx, dy, delta_vel, delta_angle
