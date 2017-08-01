/** DynamicCar subclass */
class DynamicCar extends Car {

    /** DynamicCar constructor */
    private DynamicCar(Map m, int x, int y, double mss) {
        super(m, x, y, mss);
    }

    /** Modify attributes to reflect one step */
    void step(double acceleration, double steering) {
        // Note: The current system's `action` list is steering, THEN acceleration
    }

}
