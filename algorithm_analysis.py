from header_import import *

if __name__ == "__main__":
    
    number_episode = 50
    grid_size = int(sys.argv[1])
    algorithm  = (sys.argv[2])
    plot = plot_graphs(grid_world_size=grid_size)

    if algorithm == "sarsa":
        regular = sarsa_algorithm(episode=10000, gamma=1, alpha=0.8, epsilon=0.1, max_time_step=10000, grid_world_size=grid_size)
        cumulative_reward, step_number = regular.sarsa(state="not_all")
        plot.plot_episode_time_step(cumulative_reward, algorithm="sarsa" ,type_graph = "cumulative_reward")
        plot.plot_episode_time_step(step_number, algorithm="sarsa", type_graph = "step_number")
    
        regular = sarsa_algorithm(episode=50, gamma=1, alpha=0.8, epsilon=0.1, max_time_step=50, grid_world_size=grid_size)
        q_value = regular.sarsa(state="all")
        plot.plot_grid_world_with_wind_and_obstacle(q_value, type_graph = "optimal path", type_graph_name="Sarsa reward | alpha 0.8")
        plot.save_q_value(q_value, type_graph_name="Sarsa_alpha_0.8")

    elif algorithm == "q_learning": 
        regular = q_learning_algorithm(episode=10000, gamma=1, alpha=0.8, epsilon=0.1, max_time_step=10000, grid_world_size=grid_size)
        cumulative_reward, step_number = regular.q_learning(state="not_all")
        plot.plot_episode_time_step(cumulative_reward, algorithm="q_learning" ,type_graph = "cumulative_reward")
        plot.plot_episode_time_step(step_number, algorithm="q_learning", type_graph = "step_number")
    
        regular = q_learning_algorithm(episode=50, gamma=1, alpha=0.8, epsilon=0.1, max_time_step=50, grid_world_size=grid_size)
        q_value = regular.q_learning(state="all")
        plot.plot_grid_world_with_wind_and_obstacle(q_value, type_graph = "optimal path", type_graph_name="Q_Learning reward | alpha 0.8")
        plot.save_q_value(q_value, type_graph_name="Q_Learning_alpha_0.8")

    elif algorithm == "double_q_learning":
        regular = q_learning_algorithm(episode=10000, gamma=1, alpha=0.8, epsilon=0.1, max_time_step=10000, grid_world_size=grid_size)
        cumulative_reward, step_number = regular.double_q_learning(state="not_all")
        plot.plot_episode_time_step(cumulative_reward, algorithm="double_q_learning" ,type_graph = "cumulative_reward")
        plot.plot_episode_time_step(step_number, algorithm="double_q_learning", type_graph = "step_number")
    
        regular = q_learning_algorithm(episode=50, gamma=1, alpha=0.8, epsilon=0.1, max_time_step=50, grid_world_size=grid_size)
        q_value = regular.double_q_learning(state="all")
        plot.plot_grid_world_with_wind_and_obstacle(q_value, type_graph = "optimal path", type_graph_name="Double_Q_Learning reward | alpha 0.8")
        plot.save_q_value(q_value, type_graph_name="Double_Q_Learning_alpha_0.8")
