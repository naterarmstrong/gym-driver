from gym.envs.registration import register

register(
    id='driver-v0',
    entry_point='gym_foo.envs:DriverEnv',
)
