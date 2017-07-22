# Config Parameters
## Action Space
### Control Space
* control_space_type: 'discrete' or 'continuous' for a discrete or continuous control space. default discrete
* noise_type: 'gaussian' or 'random' based on which type of noise is added to actions. default 0.1
* noise_mag: magnitude of the noise, default 0.1
* steer_max, steer_min, steer_num: 2 floats, int. range of steering inputs, and number of discrete divisions. defaults -15.0, 15.0, 5
* acc_max, acc_min, acc_num: 2 floats, int. range of acceleration, and number of discretizations. default 3.0, 3.0, 3
### State Space
* num_cpu_cars: int, number of CPU cars, default 5
* state_space_type: 'positions' or 'image' for an image or (array?) state space. default 'image'
* downsampled_size: ONLY IF IMAGE: size of provided image, int tuple
### Dynamics
* main_car_dynamics: 'kinematic' or 'dynamic'. refers to each dynamics model. default kinematic
