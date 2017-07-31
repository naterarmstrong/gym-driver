/** KinematicCar subclass */
class KinematicCar extends Car {

    /** KinematicCar constructor */
    private KinematicCar(Map m, int x, int y, double mss) {
        super(m, x, y, mss);
    }

    /** Modify attributes to reflect one step */
    void step(double accAction, double steerAction) {
    	double radSteer = Math.toRadians(steerAction);
    	double radAngle = Math.toRadians(angle);
    	accAction = Math.max(Math.min(accAction, maxVel - vel), -vel);



//        # Differential equations
//        ode_state = [self.x, self.y, self.vel, rad_angle]
//        aux_state = (accAction, steerAction)
//        t = np.arange(0.0, 1.0, 0.1)
//        delta_ode_state = odeint(self.integrator, ode_state, t, args=aux_state)
//        x, y, vel, angle = delta_ode_state[-1]
//
//        self.angle = x, y, vel, np.rad2deg(angle) % 360
    }

}
