from header_import import *

class sarsa_algorithm(Grid_World_Enviroment_with_Wind_Obstacle):
    def __init__(self, episode, gamma, alpha, epsilon, max_time_step, grid_world_size):
        super().__init__(grid_world_size)
        
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.number_episode = episode
        self.max_time_step = max_time_step
        self.q_value = defaultdict(float)
        self.time_step = []
        
        
    def argmax_rand(self, max_act):
        return np.random.choice(np.flatnonzero(max_act == np.max(max_act)))
    
    def policy(self, state):
        if np.random.rand() > self.epsilon:
            return self.argmax_rand([self.q_value[state, a] for a in self.action_space])
        else:
            return np.random.choice(self.action_space)
    
    def sarsa(self):

        for i in range(self.number_episode):
            state = self.reset()
            action = self.policy(state)
            done, reward, next_state = self.step(action)

            while True:
                done, reward, next_state = self.step(action)
                next_action = self.policy(next_state)
                self.q_value[state, action] = self.q_value[state, action] + self.alpha * (reward + self.gamma * self.q_value[next_state, next_action] - self.q_value[state, action])
                state, action = next_state, next_action
                self.time_step.append(i)
                if len(self.time_step) >= self.max_time_step:
                    return self.time_step, self.q_value
    
                if done:
                    break
                   
        return self.time_step, self.q_value
                    

class learner(Grid_World_Enviroment_with_Wind_Obstacle):
    def __init__(self, episode, gamma, alpha, epsilon, max_time_step, grid_world_size):
        super().__init__(grid_world_size)
        
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.number_episode = episode
        self.max_time_step = max_time_step
        self.q_value = defaultdict(float)
        self.time_step = []
        
    def argmax_rand(self, max_act):
        pass
    
    def policy(self, state):
        pass
    
    def learn(self):
        
        for i in range(self.number_episode):
            state = self.reset()
            
            while True:
                action = np.random.choice(self.action_space)
                done, reward, next_state = self.step(action)
                state = next_state
                
                if done:
                    break
                
                
                
class q_learning_algorithm(Grid_World_Enviroment_with_Wind_Obstacle):
    def __init__(self, episode, gamma, alpha, epsilon, max_time_step, grid_world_size):
        super().__init__(grid_world_size)
        
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.epsilon = epsilon
        self.number_episode = episode
        self.rewards = []
        self.reward_average = []
        self.max_time_step = max_time_step
        self.q_value = defaultdict(float)
        self.q_value_2 = defaultdict(float)
        self.q_value_sum = defaultdict(float)
        self.cumulative_reward = []
        self.step_number = []
        
    def argmax_rand(self, max_act):
        return np.random.choice(np.flatnonzero(max_act == np.max(max_act)))
    
    
    def policy(self, state):
        if np.random.rand() > self.epsilon:
            return self.argmax_rand([self.q_value[state, a] for a in self.action_space])
        else:
            return np.random.choice(self.action_space)
    
    def q_learning(self, state):
        
        if state != "all":
            for _ in range(self.number_episode):
                state = self.reset(start=(0,0))
                count = 0
                reward_list = 0
                while True:
                    action = self.policy(state)
                    done, reward, next_state = self.step(action)
                    max_qvalue = np.max([self.q_value[next_state, a] for a in self.action_space])
                    self.q_value[state, action] = self.q_value[state, action] + self.alpha * (reward + self.gamma * max_qvalue - self.q_value[state, action])
                    reward_list += reward
                    state = next_state
                    count += 1
                    if done:
                        break
                self.step_number.append(count)
                self.cumulative_reward.append(reward_list)
            return self.cumulative_reward, self.step_number

        else:
            for i in range(self.grid_world_size):
                for ii in range(self.grid_world_size):
                    reward_list = 0
                    for _ in range(self.number_episode):
                        state = self.reset((i,ii))
                        while True:
                            action = self.policy(state)
                            done, reward, next_state = self.step(action)
                            max_qvalue = np.max([self.q_value[next_state, a] for a in self.action_space])
                            self.q_value[state, action] = self.q_value[state, action] + self.alpha * (reward + self.gamma * max_qvalue - self.q_value[state, action])
                            reward_list += reward
                            state = next_state
                            if i == 17 and ii == 12:
                                break

                            if done:
                                break
            return self.q_value


    
    def double_q_learning(self):
        reward_list = 0
        max_qvalue_2 = 0
        max_qvalue = 0
        for i in range(self.number_episode):
            state = self.reset()
            count = 0

            while True:
                action = self.policy(state)
                done, reward, next_state = self.step(action)
                
                if random.random()<0.5:
                    max_qvalue = np.max([self.q_value[next_state, a] for a in self.action_space])
                    self.q_value[state, action] = self.q_value[state, action] + self.alpha * (reward + self.gamma * max_qvalue_2 - self.q_value[state, action])
                else:
                    max_qvalue_2 = np.max([self.q_value_2[next_state, a] for a in self.action_space])
                    self.q_value_2[state, action] = self.q_value_2[state, action] + self.alpha * (reward + self.gamma * max_qvalue - self.q_value_2[state, action])
                
                self.q_value_sum[state, action] = self.q_value[state, action] + self.q_value_2[state, action]
                reward_list += reward
                state = next_state
                count += 1
                if done:
                    break
                    
            reward_list /= count
            self.rewards.append(reward_list)
            self.reward_average.append(sum(self.rewards) / len(self.rewards))
        
        self.reward_average = self.reward_average[:-self.number_episode]
        # self.max_action = self.max_action[:-self.number_episode]

        return self.reward_average,  self.max_action, self.q_value

    

        
