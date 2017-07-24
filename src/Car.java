/** Car class */
abstract class Car {

    /** Car attributes */
    private Map map;
    private int x; // x pixel on the Map
    private int y; // y pixel on the Map
    private double angle;
    private double velocity;

    /** Car constructors */
    Car(Map m, int xPixel, int yPixel) {
        this(m, xPixel, yPixel, 0, 0);
    }

    private Car(Map m, int xPixel, int yPixel, double a, double v) {
        map = m;
        x = xPixel;
        y = yPixel;
    }

    /** Modify attributes to reflect one step */
    abstract void step(double acceleration, double steering);

}
