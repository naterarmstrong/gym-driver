/** RunnerPanel class */
class RunnerPanel extends Panel {

    /** RunnerPanel constructor */
    RunnerPanel(RunnerMenu m) {
        super(m);
        addBackOption();
    }

    /** Update fields in the RunnerPanel after changing the Map */
    void updateFields() {
    }

}

// TODO: frame.setTile("") accordingly. "Main Menu", "Map Maker", "Map Runner" etc
// TODO: fix laggy scrolling
// TODO: clean up the main method

// TODO: MapRunner
// You put the car down, specifying a cardinal direction on the menu. It appears, but the angle is plus or minus some error, generally going in that direction.
// You put the CPU cars down too, with no randomness added to their angle.
// Also make an AI for the CPU cars, so that they go straight if straight road, or turn if curved road.
// You click to put down a car, click again to delete it.
// Click "Play" to start.
// He gives us acceleration and steer angle. We have to give back (from the step function) this tuple:
// An observation, which is a pixel array of what's on screen
// A float returned from calling some function `getReward`, specified in the UserCar class
// A boolean specifying whether it's time to finish.
