# FORDS (First ORder Driving Simulator)

Link to the original driving simulator https://github.com/WesleyHsieh/gym-driving

Link to Google drive of 2 pages of notes I took on things that are wanted for simulator: (Take with a grain of salt)
https://drive.google.com/drive/folders/0B_uaUEKgQylrX2Y4LVhSTFBMcWs?usp=sharing


### For now, the readme is for you guys (Sequoia / Robert) so you know the goals for the simulator, etc. 

## Features We Want
### State Space 
  The state space should be available in both positions and image format, at arbitrary resolution. Realistically, this can be handled by downsampling, so we really only need to be able to capture different sizes of state space. The position format should presumably be an array of the terrain (including terrain type) in the viewport, the other cars' position/angle, and the main car's position/angle. It should also include the distance around the track remaining. This discussed more in detail later / don't worry about it yet.

### OpenAI Gym Integration
   I'll handle this part. The file structure is already in place, and the only real thing needed is a wrapper DriverEnv class to handle interactions between your java code and the python OpenAI Gym.
   
### Interface and Configuration from Config Files
  I'll also handle this part. The interface should be entirely for setting up config files and such. It will probably be written in Python in TKinter, but I might be able to find a better package for doing this. We'll see. The config file to read from will almost certainly be a .JSON file containing all relevant parameters.
  
### Variable Terrain
  The terrain was previously all defined as rectangles but will now likely be defined in terms of an array. The terrain should be easily query-able for the terrain at a specific point, or within a certain range (iteration is probably fine because the cars will be small).
  
### Three (Maybe 2) Different Dynamics Models
  This will probably end up being pretty easy to implement. The three models should be as follows:
   
>  Point Car: Simple, simple calculation of x_new = x_old + vel\* cos(angle) or something

> Kinematic Car: http://www.me.berkeley.edu/~frborrel/pdfpub/IV_KinematicMPC_jason.pdf to find model

> Dynamic Car: Same link as kinematic to find model. Also used the below    
>    Cornering stiffness calculation:
>       http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.46.28&rep=rep1&type=pdf
>    Yaw inertia estimate:
>        https://www.degruyter.com/downloadpdf/j/mecdc.2013.11.issue-1/mecdc-2013-0003/mecdc-2013-0003.pdf
>
>    Friction coefficients:
>        http://www.gipsa-lab.grenoble-inp.fr/~moustapha.doumiati/MED2010.pdf

### Reward / Cost Function
  I imagine the cost function being based on two factors. 
  1. The remaining distance parallel to track to a "finish point".
  2. The distance to the nearest other car.
  This should be easily calculable at every step.

### CPU Cars
  The CPU cars should ideally be able to follow the track. I imagine that we could handle this by creating separate physics and track/terrain files. The track/terrain file could have some statistics about it precomputed, before running any experiments on the track. This could include the creation of the 'path to follow' along the track. The CPU cars could then attempt to follow this. *It is likely that these cars will have to use different physics than the main car for performance reasons.* That said, these cars should most likely be initialized as Point Cars. 

# Most Important Pieces
## Speed
  We need the simulator to be fast, as that is functionally our only edge over other, existing driving simulators.

## Customizability
  We want the simulator to be easily customizable. Ideally, we can actually create a generator function for random tracks within certain parameters. 
