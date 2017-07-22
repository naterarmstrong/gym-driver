/** Car class */
public abstract class Car {

    /** Car attributes */
    private Map map;
    protected int x; // x pixel on the Map
    protected int y; // y pixel on the Map
    protected double angle;
    protected double velocity;

    /** Car constructors */
    protected Car(Map m, int xPixel, int yPixel) {
        this(m, xPixel, yPixel, 0, 0);
    }

    protected Car(Map m, int xPixel, int yPixel, double a, double v) {
        map = m;
        x = xPixel;
        y = yPixel;
    }

    /** Modify attributes to reflect one step */
    protected abstract void step(double acceleration, double tireAngle);

}
