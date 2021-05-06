import gym
import highway_env
import numpy as np
from stable_baselines import GAIL, DQN
from stable_baselines.deepq.policies import MlpPolicy
from stable_baselines.gail import ExpertDataset, generate_expert_traj

def train():

    # Load Model

    env = gym.make('roundabout-v0')

    model = DQN(MlpPolicy, env, verbose=1)
    generate_expert_traj(model, 'expert_roundabout', n_timesteps=1000, n_episodes=10)

    #Data Augmentation
    expert_data = dict(np.load('expert_roundabout.npz'))
    print("my keys are:" + str(expert_data.keys()))
    obs = expert_data['obs']
    obs.shape
    expert_data['obs'] = obs.ravel()  # convert to 1D array
    print("my keys are:" + str(expert_data.keys()))
    np.savez('expert_roundabout.npz', expert_data)

    dataset = ExpertDataset(expert_path='expert_roundabout.npz', traj_limitation=10, verbose=1)
    model = GAIL('MlpPolicy', env, dataset, verbose=1)
    model.learn(total_timesteps=1000)
    model.save("gail_roundabout")

    env.close()
    del env


if __name__ == '__main__':
    train()

