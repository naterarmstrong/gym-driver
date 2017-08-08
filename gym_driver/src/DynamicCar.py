#from numpy import arange, sqrt, sin, cos, tan, arctan, deg2rad, rad2deg
import numpy as np
from scipy.integrate import odeint

from Car import Car, MAX_VEL, LEN_REAR, LEN_FRONT, MASS, YAW_INTERTIA




def dampen_val(val, lim, coef):
    damped = val * coef
    if np.abs(damped) < lim:
        return 0.0
    else:
        return damped

# DynamicCar class
class DynamicCar(Car):

    # DynamicCar constructor
    def __init__(self, map, x, y, angle, canvas=None, color='orange'):
        Car.__init__(self, map, x, y, angle, canvas, color)
        # Dynamic car specific
        self.max_vel = 20.0
        self.mass = 1000.0
        self.l_f = self.l_r = 50.0 / 2.0
        self.dangle = self.a_f = self.dx_body = self.dy_body = 0.0
        #self.count = 0
        self.friction = 0.9

    def save(self):
        # Returns a list of x, y, angle, dangle, a_f, dx_body, dy_body
        # TODO: make first element of the list 'dynamic' and have the load function read it to construct
        return [self.x, self.y, self.dx_body, self.dy_body, self.angle, self.dangle]

    def load_to_state(self, state):
        self.x, self.y, self.dx_body, self.dy_body, self.angle, self.dangle = state

    def step(self, action):
        """
        Updates the car for one timestep.

        Args:
            action: 1x2 array, steering / acceleration action.
            info_dict: dict, contains information about the environment.
        """
        #self.count += 1
        a_f, delta_f = action

        # Convert to radians 
        delta_f, rad_angle, rad_dangle = np.radians(delta_f), np.radians(self.angle), np.radians(self.dangle)

        # Friction coefficient
        mu = self.map.get_point_friction(self.x, self.y)

        # Differential equations
        ode_state = [self.x, self.y, self.dx_body, self.dy_body, rad_angle, rad_dangle]
        aux_state = (mu, delta_f, a_f)
        t = np.arange(0.0, 1.0, 0.1)
        delta_ode_state = odeint(self.integrator, ode_state, t, args=aux_state)
        x, y, dx_body, dy_body, rad_angle, rad_dangle = delta_ode_state[-1]

        # Update car 
        self.x, self.y, self.dx_body, self.dy_body, self.angle, self.dangle = \
            x, y, dx_body, dy_body, np.rad2deg(rad_angle), np.rad2deg(rad_dangle)

        self.dy_body = dampen_val(self.dy_body, lim=0.1, coef=0.75)
        self.body_vel = np.sqrt(self.dx_body ** 2 + self.dy_body ** 2)
        self.angle %= 360.0

        self.dangle = dampen_val(self.dangle, lim=0.1, coef=0.95)

        #self.corners = self.calculate_corners()

    def integrator(self, state, t, mu, delta_f, a_f):
        """
        Calculates numerical values of differential 
        equation variables for dynamics. 
        SciPy ODE integrator calls this function.

        Args:
            state: 1x6 array, contains x, y, dx_body, dy_body, rad_angle, rad_dangle
                of car.
            t: float, timestep.
            mu: float, friction coefficient.
            delta_f: float, steering angle.
            a_f: float, acceleration.

        Returns:
            output: list, contains dx, dy, ddx_body, ddy_body, dangle, ddangle.
        """
        x, y, dx_body, dy_body, rad_angle, rad_dangle = state
        # Yaw Inertia
        I_z = 2510.15 * 25.0  * 2

        # Limit backwards acceleration
        dx_body = max(dx_body, 0.0)

        # Slip angle calculation
        beta = np.arctan((self.l_r / (self.l_f + self.l_r)) * np.tan(delta_f))
        vel = np.sqrt(dx_body ** 2 + dy_body ** 2)
        slip_angle = (vel / self.l_r) * np.sin(beta)

        # Slip angles
        alpha_f = -slip_angle
        alpha_r = 0.0

        # Tire cornering stiffness
        c_f_est = self.mass * (self.l_r / (self.l_f + self.l_r))
        c_f = c_r = mu * c_f_est

        # Cornering force
        F_cf = -c_f * alpha_f
        F_cr = -c_r * alpha_r

        # Differential equations
        ddx_body = rad_dangle * dy_body + a_f
        ddy_body = -rad_dangle * dx_body + (2 / self.mass) * (F_cf * np.cos(delta_f) + F_cr)
        
        # Clamp acceleration if above maximum velocity
        body_vel = np.sqrt((ddx_body + dx_body) ** 2 + (ddy_body + dy_body) ** 2)
        if body_vel > self.max_vel:
            a = ddx_body ** 2 + ddy_body ** 2
            b = 2 * (ddx_body * dx_body + ddy_body * dy_body)
            c = dx_body ** 2 + dy_body ** 2 - self.max_vel ** 2
            sqrt_term = b**2 - 4*a*c

            # Truncate if ratio is too small to avoid floating point error
            epsilon = 0.0001
            if sqrt_term < epsilon:
                ratio = 0.0
            else:
                ratios = (-b + np.sqrt(b**2 - 4*a*c)) / (2*a) , (-b - np.sqrt(b**2 - 4*a*c)) / (2*a) 
                ratio = max(ratios)
            ddx_body, ddy_body = ddx_body * ratio, ddy_body * ratio

        dangle = rad_dangle
        ddangle = (2 / I_z) * (self.l_f * F_cf - self.l_r * F_cr)

        dx = dx_body * np.cos(rad_angle) - dy_body * np.sin(rad_angle)
        dy = dx_body * np.sin(rad_angle) + dy_body * np.sin(rad_angle)
        
        # Clamp velocity
        vel = np.sqrt(dx ** 2 + dy ** 2)
        if vel > self.max_vel:
            ratio = self.max_vel / vel
            dx, dy = dx * ratio, dy * ratio

        output = [dx, dy, ddx_body, ddy_body, dangle, ddangle]
        return output

    # Sequoia's code below. Broken somehow, not sure how
    # Modify attributes to reflect one game step
    #def step(self, action):
    #    action_acc, action_angle = action
    #    # Pre-process actions
    #    action_angle = deg2rad(action_angle)
    #    angle = deg2rad(self.angle)
    #    d_angle = deg2rad(self.d_angle)
    #    friction = self.map.get_point_friction(self.x, self.y)
    #    # Solve differential equations
    #    t = arange(0.0, 1.0, 0.1)
    #    ode_state = (self.x, self.y, self.d_x, self.d_y, angle, d_angle)
    #    aux_state = (friction, action_acc, action_angle)
    #    deltas = odeint(self.integrate, ode_state, t, args=aux_state)
    #    x, y, d_x, d_y, angle, d_angle = deltas[-1]
    #    self.x, self.y, self.d_x, self.d_y = x, y, d_x, d_y
    #    self.vel = sqrt(self.d_x ** 2 + self.d_y ** 2)
    #    self.angle = rad2deg(angle) % 360
    #    self.d_angle = (d_angle) % 360

    # Calculate numerical values for variables in the differential equation
    #@staticmethod
    #def integrate(state, t, friction, action_acc, action_angle):
    #    # Extract the state
    #    x, y, d_x, d_y, angle, d_angle = state
    #    vel = sqrt(d_x ** 2 + d_y ** 2)
    #    # Calculate slip angle
    #    beta = arctan((LEN_REAR / (LEN_REAR + LEN_FRONT)) * tan(action_angle))
    #    slip_angle = (vel / LEN_REAR) * sin(beta)
    #    slip_front = -slip_angle
    #    slip_rear = 0
    #    # Calculate tire cornering stiffness
    #    cornering_force = MASS * (LEN_REAR / (LEN_REAR + LEN_FRONT))
    #    cr_f = -friction * cornering_force * slip_front
    #    cr_r = -friction * cornering_force * slip_rear
    #    # Calculate deltas
    #    d_x = d_x * cos(angle) - d_y * sin(angle)
    #    d_y = d_x * sin(angle) + d_y * sin(angle)
    #    dd_x = d_angle * d_y + action_acc
    #    dd_y = -d_angle * d_x + (2 / MASS) * (cr_f * cos(action_angle) + cr_r)
    #    dd_angle = (2 / YAW_INTERTIA) * (LEN_FRONT * cr_f - LEN_REAR * cr_r)
    #    # Clamp acceleration
    #    acc = sqrt((dd_x + d_x) ** 2 + (dd_y + d_y) ** 2)
    #    if acc > MAX_VEL:
    #        a = dd_x ** 2 + dd_y ** 2
    #        b = 2 * (dd_x * d_x + dd_y + d_y)
    #        c = d_x ** 2 + d_y ** 2 - MAX_VEL ** 2
    #        max_fraction = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    #        dd_x *= max_fraction
    #        dd_y *= max_fraction
    #    # Clamp velocity
    #    if vel > MAX_VEL:
    #        max_fraction = MAX_VEL / vel
    #        d_x *= max_fraction
    #        d_y *= max_fraction
    #    return d_x, d_y, dd_x, dd_y, d_angle, dd_angle



