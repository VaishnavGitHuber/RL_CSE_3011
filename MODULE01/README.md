### CHAPTER 1 : FUNDAMENTALS OF REINFORCEMENT LEARNING
#### Introduction to RL
-  Reinforcement Learning is one of the area of Machine Learning.Unlike other ML paradiagram(Supervised & Unsupervised ML).
-  RL works by interacting with the evirionment.
  
#### Key Components of RL 
1. Agent : software programme, that makes intelligent decisions
2. Evironement : Environment is world of Agent.
3. Action : agent interact with the environemt by performing an action.
4. State : state is space in environement where the agent can be.
5. Reward : if the action is good(recives positive reward) & if action is bad (neg reward).

#### How RL Algorithm works 
step 1 : agent interact with the environment by performing an action.
step 2 : By performing an action, agent move from one state to another state.
step 3 : agenet receive reward based on the action, if action is good receives positive reward and else negative.

#### RL in Grid World Environement
![Gridworld](Images/gridworld.png)
- In the above mentioned gridworld environment the goal is to reach the state I from A with out reaching the shaded regions.
- Action A to B : bad action since B is a shaded grid
- Action A to D : good action since D is a non shaded grid

#### Markov Decision Process(MDP) 
- Markov Decision Process is a **mathematical framework** for solving the RL learning problems.
- It can be used to solve the optimization problems.
- Before understanding MDP, we should understand Markov chain & Markov Property
- Markov Property : according to markov property, future depends only on the present state not on the past.
(eg: if the climate is cloudy now, next would be rainy, depends only on the present state)
- Markov Chain / Markov Process : consists of a set of states that follows Markov Property.
- Transition Probability: change in state from one to another is called transition, the probability asosiated with the transition is known as transition probablity
- Ways to represent transition probability,
  1. Transition Table(Current state, Next state, probablity)
  2. State Diagram
  3. Transition Matrix
