from header_import import *

class plot_graphs(Grid_World_Enviroment_with_Wind_Obstacle):
    def __init__(self, grid_world_size):
        super().__init__(grid_world_size)
        
        self.path = "graphs_charts/"
        self.grid_world_size = grid_world_size
        
        self.chart_path = self.path + "charts/"
        self.enviroment = self.path + "enviroment/"
        self.q_value_path = "q_values/"
        self.size_of_world_path = str(grid_world_size) + "/"


    def action_path(self, q_value, starting_position = (0,0)):
        x, y = self.start
        path = [self.start]
        
        for _ in range(100):
            best_action = np.argmax([q_value[(x,y), a] for a in self.action_space])
            x, y, reward = self.transition(x, y, best_action)
            path.append((x,y))
            if x == self.goal[0] and y == self.goal[1]:
                break
        return path


    def plot_grid_world_with_wind_and_obstacle(self, q_value, type_graph = "reward", type_graph_name = "default"): 
        
        action_path = self.action_path(q_value)
        fig = plt.figure()
        axis = fig.add_subplot(111)
        
        if self.grid_world_size == 20:
            
            axis.set_xlim(-0.5, 19.5)
            axis.set_ylim(-0.5, 19.5)

            axis.set_yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
            axis.invert_yaxis()
            axis.set_yticklabels([1, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0], fontsize = 5)
            
            axis.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
            axis.set_xticklabels([0, 0, 0, 1, 0, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 1, 1, 0], fontsize = 5)
            
            axis.text(self.start[0], self.start[1], 'S', fontsize=5, horizontalalignment='center', verticalalignment='center')
            axis.text(self.goal[0], self.goal[1], 'G', fontsize=5, horizontalalignment='center', verticalalignment='center')
            
        elif self.grid_world_size == 50:
            axis.set_xlim(-0.5, 49.5)
            axis.set_ylim(-0.5, 49.5)

            axis.set_yticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49])
            axis.invert_yaxis()
            axis.set_yticklabels([1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0], fontsize=5)
            
            axis.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49])
            axis.set_xticklabels([0, 0, 0, 1, 0, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1], fontsize = 5)
            
            axis.text(self.start[0], self.start[1], 'S', fontsize=5, horizontalalignment='center', verticalalignment='center')
            axis.text(self.goal[0], self.goal[1], 'G', fontsize=5, horizontalalignment='center', verticalalignment='center')
    
        for x in range(self.grid_world_size):
            for y in range(self.grid_world_size):
                axis.add_patch(patches.Rectangle([x-0.5, y-0.5], 1, 1, fill=False))
            
                params = {'head_width':0.2, 'head_length':0.2, 'color':'gray', 'alpha':.2}
                action = np.argmax([q_value[(x,y), a] for a in self.action_space])
                if action == 0:
                    axis.arrow(x, y, -0.1, 0, **params)
                elif action == 1:
                    axis.arrow(x, y, 0, -0.1, **params)
                elif action == 2:
                    axis.arrow(x, y,  0.1, 0, **params)
                elif action == 3:
                    axis.arrow(x, y, 0,  0.1, **params)
                        
        for i in range(len(action_path)-1):
            x, y = action_path[i]
            next_x, next_y = action_path[i+1]
            axis.plot([x, next_x], [y, next_y], color='blue', alpha=1.0)

        plt.savefig((str(self.enviroment) + type_graph_name + "_" + str(self.grid_world_size) + "_" + type_graph + "_paths.png"), dpi =500)
   

    def save_q_value(self, q_value, type_graph_name):
        a_file = open(self.q_value_path + self.size_of_world_path + str(type_graph_name) + ".txt", "w")
        q_value_array = list(q_value.items())
        q_value_array = np.array(q_value_array, dtype=object)

        for row in q_value_array:
            np.savetxt(a_file, row, fmt='%s')
        a_file.close() 


    def plot_episode_time_step(self, data, algorithm, type_graph = "reward"):

        fig = plt.figure()
        axis = fig.add_subplot(111)
        if self.grid_world_size == 20:
            color_graph = "blue"
        else:
            color_graph = "red"

        if type_graph == "cumulative_reward":
            axis.plot(data, color=color_graph)
            axis.set_title(str(self.grid_world_size)+"Reward vs Time Step")
            axis.set_xlabel("Time Steps")
            axis.set_ylabel("Reward per Step")

        elif type_graph == "step_number":
            axis.plot(data, color=color_graph)
            axis.set_title(str(self.grid_world_size) +"Number of steps per episode vs. number of episodes")
            axis.set_xlabel("Number of Steps")
            axis.set_ylabel("Episodes")
        plt.savefig((str(self.chart_path) + str(self.grid_world_size) + "_" + type_graph + "_" + algorithm + ".png"), dpi =500)



        



