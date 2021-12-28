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
        self.cumulative_reward = []
        self.step_number = []
        
    def argmax_rand(self, max_act):
        return np.random.choice(np.flatnonzero(max_act == np.max(max_act)))
    
    def policy(self, state):
        if np.random.rand() > self.epsilon:
            return self.argmax_rand([self.q_value[state, a] for a in self.action_space])
        else:
            return np.random.choice(self.action_space)
    
    def sarsa(self, state):

        if state != "all":
            for _ in range(self.number_episode):
                state = self.reset(start=(0,0))
                count = 0
                reward_list = 0
                action = self.policy(state)
                while True:
                    done, reward, next_state = self.step(action)
                    next_action = self.policy(next_state)
                    self.q_value[state, action] = self.q_value[state, action] + self.alpha * (reward + self.gamma * self.q_value[next_state, next_action] - self.q_value[state, action])
                    state, action = next_state, next_action
                    reward_list += reward
                    count += 1
                    if done:
                        break
                self.step_number.append(count)
                self.cumulative_reward.append(reward_list)
            return self.cumulative_reward, self.step_number

        else:
            for _ in range(self.number_episode):
                for i in range(self.grid_world_size):
                    for ii in range(self.grid_world_size):
                        state = self.reset(start=(i,ii))
                        count = 0
                        reward_list = 0
                        action = self.policy(state)
                        while True:
                            done, reward, next_state = self.step(action)
                            next_action = self.policy(next_state)
                            self.q_value[state, action] = self.q_value[state, action] + self.alpha * (reward + self.gamma * self.q_value[next_state, next_action] - self.q_value[state, action])
                            state, action = next_state, next_action
                            reward_list += reward
                            count += 1
                            if i == 17 and ii == 12:
                                break

                            if done:
                                break
            return self.q_value



class learner(Grid_World_Enviroment_with_Wind_Obstacle):
    def __init__(self, episode, gamma, alpha, epsilon, max_time_step, grid_world_size):
        super().__init__(grid_world_size)
        
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.number_episode = episode
        self.max_time_step = max_time_step
        self.q_value = defaultdict(float)
        self.cumulative_reward = []
        self.step_number = []
        
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
                    next_best_action = self.argmax_rand([self.q_value[next_state, a] for a in self.action_space])
                    self.q_value[state, action] = self.q_value[state, action] + self.alpha * (reward + self.gamma * self.q_value[next_state, next_best_action] - self.q_value[state, action])
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
                    for _ in range(self.number_episode):
                        state = self.reset(start=(i,ii))
                        while True:
                            action = self.policy(state)
                            done, reward, next_state = self.step(action)
                            next_best_action = self.argmax_rand([self.q_value[next_state, a] for a in self.action_space])
                            self.q_value[state, action] = self.q_value[state, action] + self.alpha * (reward + self.gamma * self.q_value[next_state, next_best_action] - self.q_value[state, action])
                            state = next_state
                            if i == 17 and ii == 12:
                                break

                            if done:
                                break
            return self.q_value


    
    def double_q_learning(self, state):
        
        next_best_action1 = 0
        next_best_action2 = 0
        if state != "all":
            for _ in range(self.number_episode):
                state = self.reset(start=(0,0))
                count = 0
                reward_list = 0
                action = self.policy(state)
                while True:
                    done, reward, next_state = self.step(action)
                    if random.random()<0.5:
                        next_best_action1 = self.argmax_rand([self.q_value[next_state, a] for a in self.action_space])
                        self.q_value[state, action] = self.q_value[state, action] + self.alpha * (reward + self.gamma * self.q_value_2[next_state, next_best_action1] - self.q_value[state, action])
                    else:
                        next_best_action2 = self.argmax_rand([self.q_value_2[next_state, a] for a in self.action_space])
                        self.q_value_2[state, action] = self.q_value_2[state, action] + self.alpha * (reward + self.gamma * self.q_value_2[next_state, next_best_action2]  - self.q_value_2[state, action])
                
                    self.q_value_sum[state, action] = self.q_value[state, action] + self.q_value_2[state, action]
                    action =  self.argmax_rand([self.q_value_sum[next_state, a] for a in self.action_space])

                    reward_list += reward
                    state = next_state
                    count += 1
                    if done:
                        break
                self.step_number.append(count)
                self.cumulative_reward.append(reward_list)
                self.q_value_sum[state, action] = self.q_value[state, action] + self.q_value_2[state, action]
            return self.cumulative_reward, self.step_number

        else:
            for _ in range(self.number_episode):
                for i in range(self.grid_world_size):
                    for ii in range(self.grid_world_size):
                        state = self.reset(start=(i,ii))
                        action = self.policy(state)
                        while True:
                            done, reward, next_state = self.step(action)
                            if random.random()<0.5:
                                next_best_action1 = self.argmax_rand([self.q_value[next_state, a] for a in self.action_space])
                                self.q_value[state, action] = self.q_value[state, action] + self.alpha * (reward + self.gamma * self.q_value_2[next_state, next_best_action1] - self.q_value[state, action])
                            else:
                                next_best_action2 = self.argmax_rand([self.q_value_2[next_state, a] for a in self.action_space])
                                self.q_value_2[state, action] = self.q_value_2[state, action] + self.alpha * (reward + self.gamma * self.q_value_2[next_state, next_best_action2]  - self.q_value_2[state, action])
                
                            self.q_value_sum[state, action] = self.q_value[state, action] + self.q_value_2[state, action]
                            action =  self.argmax_rand([self.q_value_sum[next_state, a] for a in self.action_space])
                            state = next_state
                            if i == 17 and ii == 12:
                                break

                            if done:
                                break

                        self.q_value_sum[state, action] = self.q_value[state, action] + self.q_value_2[state, action]
                return self.q_value_sum
                    
                

    

        
