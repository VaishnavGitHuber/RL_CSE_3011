### CHAPTER 2 : A GUIDE TO GYM TOOL KIT

#### Introduction to Gym Tool Kit 
- Gym is a tool kit devoloped by **OpenAi** for training RL Agents.

#### Installation of Gym Toolkit 
This text book follows a slight older version
```
!pip install gym == 0.15.4
```

#### Creating an environement 
- make('<environment-id') function 
- Gym Library offers a plenty of environment to train the agents
```
env = gym.make('<environment-id')
eg: gym.make("FrozenLake-v0")
```

#### Run / Render an environement 
- render() function can be used to run the environement.
```
# env : environement
env.render() 
```

#### State Space 
- observation_space
```
env.observation_space
```

#### Action Space 
- action_space
```
env.action_space
```

#### Creating an episode 
