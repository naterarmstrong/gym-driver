from numpy import arange, sin, cos, deg2rad, rad2deg

from Car import Car

# DynamicCar class
class DynamicCar(Car):

    # DynamicCar constructor
    def __init__(self, map, x, y, angle, mass):
        Car.__init__(map, x, y, angle, mass)
        self.delta_angle = 0

    # Modify attributes to reflect one game step
    def step(self, action_acc, action_angle):
        # Pre-process actions
        action_angle = deg2rad(action_angle)
        angle = deg2rad(self.angle)
        delta_angle = deg2rad(self.delta_angle)


        # # Friction coefficient
        # if info_dict is None:
        #     mu = 0.9
        # else:
        #     collisions = info_dict['terrain_collisions']
        #     if len(collisions) == 0:
        #         mu = 0.9
        #     else:
        #         mu = min([terrain.friction for terrain in collisions])
        # 
        # # Differential equations
        # ode_state = [self.x, self.y, self.dx_body, self.dy_body, rad_angle, rad_dangle]
        # aux_state = (mu, action_angle, action_acc)
        # t = np.arange(0.0, 1.0, 0.1)
        # delta_ode_state = odeint(self.integrator, ode_state, t, args=aux_state)
        # x, y, dx_body, dy_body, rad_angle, rad_dangle = delta_ode_state[-1]
        # 
        # # Update car 
        # self.x, self.y, self.dx_body, self.dy_body, self.angle, self.dangle = \
        #     x, y, dx_body, dy_body, np.rad2deg(rad_angle), np.rad2deg(rad_dangle)
        # 
        # self.dy_body = dampen_val(self.dy_body, lim=0.1, coef=0.75)
        # self.body_vel = np.sqrt(self.dx_body ** 2 + self.dy_body ** 2)
        # self.angle %= 360.0
        # self.dangle = dampen_val(self.dangle, lim=0.1, coef=0.95)
