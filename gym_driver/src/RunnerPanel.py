from Panel import Panel

# RunnerPanel class
class RunnerPanel(Panel):

    None

# import javax.swing.Timer;
#
# import java.awt.event.ActionEvent;
#
# /** RunnerPanel class */
# class RunnerPanel extends Panel {
#
#     /** RunnerPanel attributes */
#     private static final int PLAY_Y        = TOP;
#     private static final int PAUSE_Y       = 300;
#     private static final int BUTTON_SIZE   = PANEL_WIDTH / 3;
#     private static final int STEP_DURATION = 500; // Milliseconds
#     private double START_ANGLE             = 0;
#     private Timer timer;
#
#     /** RunnerPanel constructor */
#     RunnerPanel(RunnerMenu m) {
#         super(m);
#         addPausePlayButtons();
#         addBackOption();
#         setTimer();
#     }
#
#     /** Populate the RunnerPanel with pause & play buttons */
#     private void addPausePlayButtons() {
#         String pause = "<html>&#10073;&#10073;<html>";
#         String play  = "\u25B6";
#         addButton(pause, BUTTON_SIZE, PAUSE_Y, BUTTON_SIZE, BUTTON_SIZE,
#             (ActionEvent a) -> {timer.stop();}
#         );
#         addButton(play, BUTTON_SIZE, PLAY_Y, BUTTON_SIZE, BUTTON_SIZE,
#             (ActionEvent a) -> {timer.start();}
#         );
#     }
#
#     /** Initialize the Timer */
#     private void setTimer() {
#         timer = new Timer(STEP_DURATION, (ActionEvent a) -> {
#             // TODO: call each Car's `step` method
#             repaint();
#         });
#     }
#
#     /** Update fields in the RunnerPanel after changing the Map */
#     void updateFields() {
#     }
#
# }
#
# // TODO: address the panel bug that occurs when you have no maps and click "new map"
#
# // TODO: test the NUM_CPUs field in the MakerPanel
#
# // TODO: what happens if you enter a word into height/width textbox?
#
# // TDOO: what happens if you enter a word into num CPUs textbox?
#
# // TODO: MapRunner
# // You put the car down, specifying a cardinal direction on the menu. It appears, but the angle is plus or minus some error, generally going in that direction.
# // You put the CPU cars down too, with no randomness added to their angle.
# // Also make an AI for the CPU cars, so that they go straight if straight road, or turn if curved road.
# // You click to put down a car, click again to delete it.
# // Click "Play" to start.
# // He gives us acceleration and steer angle. We have to give back (from the step function) this tuple:
# // An observation, which is a pixel array of what's on screen
# // A float returned from calling some function `getReward`, specified in the UserCar class
# // A boolean specifying whether it's time to finish.
