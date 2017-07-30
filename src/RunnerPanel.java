import java.awt.event.ActionEvent;

/** RunnerPanel class */
class RunnerPanel extends Panel {

    /** RunnerPanel attributes */
    private final int USER_CAR_Y   = TOP;
    private final int CPU_CARS_Y   = 200;
    private final int PLAY_PAUSE_Y = 350;
    private final int BUTTON_SIZE  = PANEL_WIDTH / 3;
    private double DEFAULT_ANGLE   = 0;

    /** RunnerPanel constructor */
    RunnerPanel(RunnerMenu m) {
        super(m);
        addUserCarOptions();
        addCPUCarOption();
        addPausePlayButtons();
        addBackOption();
    }

    /** Populate the RunnerPanel with UserCar options */
    private void addUserCarOptions() {
    	int UP_Y = USER_CAR_Y;
    	int LR_Y = UP_Y + BUTTON_SIZE;
    	int DN_Y = LR_Y + BUTTON_SIZE;
    	addButton("\u21E6", BUTTON_SIZE, UP_Y, BUTTON_SIZE, BUTTON_SIZE,
    		(ActionEvent a) -> {DEFAULT_ANGLE = 90;}
    	);
    	addButton("\u21E7", 0, LR_Y, BUTTON_SIZE, BUTTON_SIZE,
    		(ActionEvent a) -> {DEFAULT_ANGLE = 180;}
    	);
    	addButton("Agent", BUTTON_SIZE, LR_Y, BUTTON_SIZE, BUTTON_SIZE,
    		(ActionEvent a) -> {} // TODO
    	);
    	addButton("\u21E8", 2 * BUTTON_SIZE, LR_Y, BUTTON_SIZE, BUTTON_SIZE,
    		(ActionEvent a) -> {DEFAULT_ANGLE = 0;}
    	);
    	addButton("\u21E9", BUTTON_SIZE, DN_Y, BUTTON_SIZE, BUTTON_SIZE,
    		(ActionEvent a) -> {DEFAULT_ANGLE = 270;}
    	);
    }

    /** Populate the RunnerPanel with CPUCar options */
    private void addCPUCarOption() {
    	addButton("CPU", BUTTON_SIZE, CPU_CARS_Y, BUTTON_SIZE, BUTTON_SIZE,
    		(ActionEvent a) -> {} // TODO
    	);
    }

    /** Populate the RunnerPanel with pause & play buttons */
    private void addPausePlayButtons() {
    	int xR       = MIDDLE;
    	int xL       = MIDDLE - BUTTON_SIZE;
    	String pause = "<html>&#10073;&#10073;<html>";
    	String play  = "\u25B6";
    	addButton(pause, xL, PLAY_PAUSE_Y, BUTTON_SIZE, BUTTON_SIZE,
    		(ActionEvent a) -> {}
    	);
    	addButton(play, xR, PLAY_PAUSE_Y, BUTTON_SIZE, BUTTON_SIZE,
    		(ActionEvent a) -> {}
    	);
    }

    /** Update fields in the RunnerPanel after changing the Map */
    void updateFields() {
    }

}

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
