import numpy as np
import gymnasium as gym
from gymnasium import spaces

class IrrigationEnv(gym.Env):
    """
    Custom Environment for Irrigation Scheduling using RL.
    """
    def __init__(self):
        super(IrrigationEnv, self).__init__()
        
        # Define action space (discrete irrigation levels)
        # 0 = no irrigation, 1 = small irrigation, 2 = medium, 3 = large
        self.action_space = spaces.Discrete(4)
        
        # Define observation space (soil moisture, crop growth stage, weather conditions)
        # - soil moisture: float between 0 and 1 (0 = dry, 1 = saturated)
        # - crop growth stage: 0 (early), 1 (mid), 2 (late)
        # - weather: 0 (dry), 1 (rainy)
        self.observation_space = spaces.Box(low=np.array([0.0, 0, 0]), 
                                            high=np.array([1.0, 2, 1]), 
                                            dtype=np.float32)
        
        # Environment parameters
        self.max_days = 30  # Number of simulation days
        self.day = 0
        
        # Initial conditions
        self.soil_moisture = 0.5  # Initialize with moderate moisture
        self.growth_stage = 0  # Start at early growth stage
        self.weather = 0  # Assume dry weather initially (can be randomized)
        
    def step(self, action):
        """
        Perform one step in the environment based on the action taken.
        """
        # Irrigation effect on soil moisture
        irrigation_amounts = [0, 0.1, 0.2, 0.3]  # water added by irrigation levels
        irrigation = irrigation_amounts[action]
        
        # Simulate weather (randomly rainy or dry, rainy adds moisture)
        weather_rain = np.random.choice([0, 1], p=[0.7, 0.3])  # 30% chance of rain
        weather_effect = 0.2 if weather_rain else -0.1  # Rain adds water, dry reduces
        
        # Update soil moisture
        self.soil_moisture = max(0, min(1, self.soil_moisture + irrigation + weather_effect))
        
        # Reward: penalize under-irrigation (soil < 0.3) and over-irrigation (soil > 0.7)
        if 0.3 <= self.soil_moisture <= 0.7:
            reward = 1.0  # Good moisture level
        else:
            reward = -1.0  # Bad moisture level (too dry or too wet)
        
        # Update growth stage based on day (simple progression)
        if self.day > 10:
            self.growth_stage = 1  # Mid stage after 10 days
        if self.day > 20:
            self.growth_stage = 2  # Late stage after 20 days
        
        # Increase day count
        self.day += 1
        
        # Check if simulation is done (end of season)
        done = self.day >= self.max_days
        
        # Observation (state): soil moisture, crop growth stage, and weather
        observation = np.array([self.soil_moisture, self.growth_stage, weather_rain], dtype=np.float32)
        
        return observation, reward, done, {}
    
    def reset(self):
        """
        Reset the environment to an initial state.
        """
        self.day = 0
        self.soil_moisture = 0.5  # Reset soil moisture to moderate
        self.growth_stage = 0  # Reset crop growth stage
        self.weather = 0  # Assume dry weather initially
        
        # Return the initial observation
        return np.array([self.soil_moisture, self.growth_stage, self.weather], dtype=np.float32)
    
    def render(self, mode='human'):
        """
        Render the environment (prints the current state for debugging).
        """
        print(f"Day: {self.day}, Soil Moisture: {self.soil_moisture:.2f}, "
              f"Growth Stage: {self.growth_stage}, Weather: {'Rainy' if self.weather else 'Dry'}")
    
    def close(self):
        """
        Close the environment (optional cleanup).
        """
        pass
