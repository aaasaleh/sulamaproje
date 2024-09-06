# Irrigation Scheduling Environment for Reinforcement Learning

This repository provides a custom **Reinforcement Learning (RL) environment** for simulating **irrigation scheduling** using the OpenAI Gym-style interface. The environment allows an RL agent to learn efficient irrigation strategies to maintain optimal soil moisture for crop growth. The environment models weather conditions, soil moisture dynamics, and crop growth stages over a simulated period of time.

## Features
- **Custom RL environment** compatible with the `gymnasium` interface.
- Simulates crop growth, soil moisture levels, and daily weather conditions.
- Supports actions for controlling irrigation levels to optimize crop growth.
- Reward system encourages the agent to maintain soil moisture within optimal ranges.
- Easily extendable for RL training algorithms like DQN, PPO, or A2C using frameworks such as `stable-baselines3`.

## Installation

To use this environment, first clone the repository and install the necessary dependencies.

```bash
git clone https://github.com/your-username/irrigation-rl.git
cd irrigation-rl
pip install -r requirements.txt
```

Ensure you have `gymnasium` installed:
```bash
pip install gymnasium
```


## Usage

### Running the Environment with a Random Agent

To test the environment with a random agent, you can run the following example code:

```python
import random
from irrigation_env import IrrigationEnv  # Import your environment

# Initialize the environment
env = IrrigationEnv()

# Reset the environment to the initial state
state = env.reset()

done = False
while not done:
    # Select a random action
    action = env.action_space.sample()  # Replace with your RL agent action later
    
    # Take the action and receive feedback from the environment
    state, reward, done, _ = env.step(action)
    
    # Render the environment (optional)
    env.render()

# Close the environment when done
env.close()
```
