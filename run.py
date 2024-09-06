import random

# Create the irrigation environment
env = IrrigationEnv()

# Reset environment to initial state
state = env.reset()

# Run the simulation for the maximum number of days
done = False
while not done:
    # Randomly select an action
    action = env.action_space.sample()  # Take a random action (can be replaced by RL agent)
    
    # Step the environment with the selected action
    state, reward, done, _ = env.step(action)
    
    # Render the current state
    env.render()

# Close the environment when done
env.close()
