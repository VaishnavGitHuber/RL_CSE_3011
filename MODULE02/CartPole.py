import gymnasium as gym 

# Create a cart-pole environment 
env = gym.make("CartPole-v0", render_mode="human")

# State space of the CartPole 
print("State space: \n" , env.observation_space)  # Continuous, 4D vector

# Action space 
print(f"Action Space: {env.action_space}")  # Discrete(2): 0 (left), 1 (right)

# Create environment 
no_episodes = 100
no_timesteps = 20 
Return = 0

for episode in range(no_episodes):
    # Reset environment 
    state = env.reset()
    
    for time_step in range(no_timesteps):
        # Random action 
        random_action = env.action_space.sample()
        
        # Take action 
        next_state, reward, terminated, truncated, info = env.step(random_action)
        is_done = terminated or truncated
        
        # Accumulate reward 
        Return += reward
        
        # End episode if done
        if is_done:
            break
    if (episode % 10) == 0:
        print(f"EPISODE: {episode} RETURN: {Return}")
