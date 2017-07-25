/** Car class */
abstract class Car {

    /** Car attributes */
    static Map map; // the Map
    int x;          // x pixel on the Map
    int y;          // y pixel on the Map
    double angle;   // angle
    double vel;     // velocity
    double acc;     // acceleration
    double maxVel;  // maximal velocity
    double mass;    // mass

    /** Car constructors */
    Car(Map m, int xPixel, int yPixel, double mss) {
        map   = m;
        x     = xPixel;
        y     = yPixel;
        angle = 0;
        vel   = 0;
        acc   = 0;
        mass  = mss;
    }

    /** Modify attributes to reflect one step */
    abstract void step(double acceleration, double steering);

}
