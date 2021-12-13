from header_import import *


class grid_evaluate(Grid_World_Enviroment_with_Wind_Obstacle):
    def __init__(self, grid_world_size, graph_data_name, grid_play_task = "False"):
        super().__init__(grid_world_size)

        self.grid_world_size = grid_world_size
        self.grid_play_task = grid_play_task

        self.path = "graphs_charts/"
        self.chart_path = self.path + "charts/"
        self.q_value_path = "q_values/"
        self.size_of_world_path = str(grid_world_size) + "/"
        self.graph_data_name = graph_data_name

        
    def action_path(self, q_value, starting_position):
        x, y = starting_position
        path = [starting_position]
        reward_list = 0
 
        for _ in range(100):
            best_action = np.argmax([q_value[(x,y), a] for a in self.action_space])
            x, y, reward = self.transition(x, y, best_action)
            path.append((x,y))
            reward_list += reward

            if x == self.goal[0] and y == self.goal[1]:
                break
                
        return path, reward_list
        
    
    def play_optimal_path(self, starting_position):
        original_array = open(self.q_value_path + self.size_of_world_path + str(self.graph_data_name) + ".txt", "r+")
        q_value = original_array.readlines()
        state = []
        value = []
        count = 0
        for line in q_value:
            count += 1
            if count % 2:
                state.append(eval(line.rstrip()))
            else:
                value.append(float(line.strip()))

        q_value_dict = dict(zip(state, value))
        path, reward_list = self.action_path(q_value_dict, starting_position)
        
        return path, reward_list

    def plot_episode_time_step(self, data,  type_graph = "cumulative_reward"):

        fig = plt.figure()
        axis = fig.add_subplot(111)
        if self.grid_world_size == 20:
            color_graph = "blue"
        else:
            color_graph = "red"

        if type_graph == "cumulative_reward":
            axis.plot(data, color=color_graph)
            plt.axhline(y=max(data), color='red', linestyle='-')
            axis.set_title(str(self.grid_world_size)+"Number of Test vs Total Reward Value")
            axis.set_xlabel("Number of Tests")
            axis.set_ylabel("Total Reward Values")
        plt.savefig((str(self.chart_path) + str(self.grid_world_size) + "cumulative_reward" + "_" + ".png"), dpi =500)


    def calculate_std_error(self, data):
        
        std = np.std(data)
        min_data = min(data)
        max_data = max(data)
        new_list = set(data)
        new_list.remove(max(new_list))
        second_max_data = max(new_list)
        min_error = second_max_data - max_data
        max_error = min_data - max_data

        actual, pred = np.array(data), np.array(max_data)
        mse = np.square(np.subtract(actual,pred)).mean() 

        print("Standard Deviation:", std)
        print("Minimum error:", min_error)
        print("Maximum error:", max_error)
        print("MSE of the data:", mse)


if __name__ == "__main__":
    
    grid_size = int(sys.argv[1])
    data_name = "Q_Learning_alpha_0.8"
    cumulative_reward = []

    Grid_world_Eval = grid_evaluate(grid_world_size = grid_size, graph_data_name = data_name)
    for i in range(100):
        x = random.randint(0, grid_size - 1)
        y = random.randint(0, grid_size - 1)
        _, reward_list = Grid_world_Eval.play_optimal_path(starting_position=(x,y))
        cumulative_reward.append(reward_list)
    
    Grid_world_Eval.plot_episode_time_step(cumulative_reward, type_graph = "cumulative_reward")
    Grid_world_Eval.calculate_std_error(cumulative_reward)






        
        
