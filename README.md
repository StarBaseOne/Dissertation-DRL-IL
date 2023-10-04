

# Deep Reinforcement Learning and Imitation Learning for Autonomous Driving in a Minimalist Environment


## About

* Dissertation for Master of Science in Artificial Intelligence from University of Limerick submitted June 2021
* Publication can be accessed here - []

Autonomous driving technology has seen significant advancements in recent years, but fully autonomous self-driving cars are yet to be deployed at scale. This study delves into the world of deep reinforcement learning and imitation learning to evaluate their effectiveness in minimalist autonomous driving environments.

This study focuses on assessing various deep reinforcement learning and imitation learning techniques in a set of minimalist autonomous driving environments. These simulations mirror specific driving scenarios akin to the capabilities of systems like Tesla Autopilot. Scenarios include vehicle parking, highway navigation, intersection handling, hairpin turns, overtaking, merging, and summoning the vehicle while avoiding traffic.

## Aims and Objectives

The primary aim of this thesis is to evaluate the performance of deep reinforcement learning, offline reinforcement learning, and imitation learning in challenging driving tasks. We hypothesize that data-driven reinforcement learning, particularly offline and imitation learning, outperforms online reinforcement learning in common challenging driving scenarios.

Our objectives include:

- Measuring rewards and success rates for training completion.
- Evaluating collision avoidance metrics.
- Analyzing the agents' ability to generalize to unseen conditions.

## Algorithms
![image](https://github.com/hougiebear/Dissertation-DRL-IL/assets/22470422/9c3aeaa2-2fed-47f9-b1e5-88af78d48748)

**Online Reinforcement Learning Algorithms**

| Long form Name | Short form Name | Iteration Method |
|----------|----------|----------|
| Deep Q Network | DQN | Value | 
| Quantile Regression Deep Q Network | QRDQN | Value |
| Advantage Actor Critic | A2C | On-Policy | Online |
| Trust Region Policy Optimization | TRPO | On-Policy |
| Proximal Policy Optimization | PPO |  On-Policy |
| Deep Deterministic Policy Gradient | DDPG |  Off-Policy & Value | 
| Twin Delayed Deep Deterministic Policy Gradient | TD3 |  Off-Policy & Value | 
| Soft Actor Critic | SAC |  Off-Policy & Value |
| Truncated Quantile Critics | TQC |  Off-Policy & Value |
| Hindsight Experience Replay | HER | Off-Policy & Value | 


**Offline Reinforcement Learning Algorithms**

| Long form Name | Short form Name | Iteration Method | 
|----------|----------|----------|
| Conservative Q-Learning | CQL | Value | 

**Imitation Learning Algorithms**

| Long form Name | Short form Name | Iteration Method | 
|----------|----------|----------|
| Generative Adversarial Imitation Learning | GAIL | Off-Policy | 


## Libraries

* Stable Baselines - Link 
* Stable Baselines 3 - Link
* Deep Data Driven Reinforment Learning - D3rlpy - Link
*  Highway-env - Link

## Hardware & Pre-Requisities 
* Inst
* install Stable Baselines
* Install Stable Baselines 3





