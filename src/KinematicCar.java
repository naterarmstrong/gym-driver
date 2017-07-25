/** KinematicCar subclass */
class KinematicCar extends Car {

    /** KinematicCar constructor */
    private KinematicCar(Map m, int x, int y, double mss) {
        super(m, x, y, mss);
    }

    /** Modify attributes to reflect one step */
    void step(double accAction, double steerAction) {
//        # Unpack actions, convert angles to radians
//                delta_f, a = action
//        delta_f, rad_angle = np.radians(delta_f), np.radians(self.angle)
//
//        # Clamp acceleration if above maximum velocity
//        if a > self.max_vel - self.vel:
//        a = self.max_vel - self.vel
//        elif self.vel + a < 0:
//        a = - self.vel
//
//        # Differential equations
//        ode_state = [self.x, self.y, self.vel, rad_angle]
//        aux_state = (a, delta_f)
//        t = np.arange(0.0, 1.0, 0.1)
//        delta_ode_state = odeint(self.integrator, ode_state, t, args=aux_state)
//        x, y, vel, angle = delta_ode_state[-1]
//
//        # Update car
//        self.x, self.y, self.vel, self.angle = x, y, vel, np.rad2deg(angle)
//        self.angle %= 360.0
//        self.corners = self.calculate_corners()
    }

}
