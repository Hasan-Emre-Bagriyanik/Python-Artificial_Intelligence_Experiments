# -*- coding: utf-8 -*-
"""
Created on Thu May 11 15:14:56 2023

@author: Hasan Emre
"""

import gym

env = gym.make("Taxi-v3").env
env.reset()
env.render()

