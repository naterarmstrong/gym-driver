/** PointCar subclass */
class PointCar extends Car {

    /** PointCar constructor */
    private PointCar(Map m, int x, int y, double mss) {
        super(m, x, y, mss);
    }

    /** Modify attributes to reflect one step */
    void step(double accAction, double steerAction) {
        angle       = (angle + steerAction) % 360;
        acc         = Math.max(Math.min(accAction, maxVel - vel), -vel);
        double dist = vel + 0.5 * acc;
        double dx   = dist * Math.cos(Math.toRadians(angle));
        double dy   = dist * Math.sin(Math.toRadians(angle));
        x          += dx;
        y          += dy;
        vel         = Math.max(Math.min(vel, maxVel), 0);
    }

}
