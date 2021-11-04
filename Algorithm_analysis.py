from header_import import *

if __name__ == "__main__":
    
    number_episode = 10000
    grid_size = int(sys.argv[1])

    # Algorithums
    regular = sarsa_algorithm(episode=number_episode, gamma=1, alpha=0.5, epsilon=0.1, max_time_step=number_episode, grid_world_size=grid_size)



    regular_time_step, q_value = regular.sarsa()
    plot = plot_graphs(grid_world_size=grid_size)
    plot.plot_episode_time_step(regular_time_step, type_graph = "time_step", type_graph_name="Sarsa | 4 action")
    plot.plot_grid_world_with_wind_and_obstacle(q_value, type_graph = "time_step", type_graph_name="Sarsa | 4 action")
    plot.save_q_value(q_value, type_graph_name="Sarsa | 4 action")



    regular = q_learning_algorithm(episode=number_episode, gamma=1, alpha=1, epsilon=0.1, max_time_step=number_episode, grid_world_size=grid_size)



    reward_average, max_action, q_value = regular.q_learning()
    plot.plot_episode_time_step(reward_average, type_graph = "reward", type_graph_name="Q_Learning reward | alpha 1")
    plot.plot_episode_time_step(max_action, type_graph = "action", type_graph_name="Q Learning action | alpha 1")
    plot.plot_grid_world_with_wind_and_obstacle(q_value, type_graph = "optimal path", type_graph_name="Q_Learning reward | alpha 1")
    plot.save_q_value(q_value, type_graph_name="Q_Learning reward | alpha 1")


    reward_average, max_action, q_value = regular.double_q_learning()
    plot.plot_episode_time_step(reward_average, type_graph = "reward", type_graph_name="Double Q_Learning reward | alpha 1")
    plot.plot_episode_time_step(max_action, type_graph = "action", type_graph_name="Double Q Learning action | alpha 1")
    plot.plot_grid_world_with_wind_and_obstacle(q_value, type_graph = "optimal path", type_graph_name="Double Q_Learning reward | alpha 1")
    plot.save_q_value(q_value, type_graph_name="Double Q_Learning reward | alpha 1")


    regular = q_learning_algorithm(episode=number_episode, gamma=1, alpha=0.8, epsilon=0.1, max_time_step=10000, grid_world_size=grid_size)



    reward_average, max_action, q_value = regular.q_learning()
    plot.plot_episode_time_step(reward_average, type_graph = "reward", type_graph_name="Q_Learning reward | alpha 0.8")
    plot.plot_episode_time_step(max_action, type_graph = "action", type_graph_name="Q Learning action | alpha 0.8")
    plot.plot_grid_world_with_wind_and_obstacle(q_value, type_graph = "optimal path", type_graph_name="Q_Learning reward | alpha 0.8")
    plot.save_q_value(q_value, type_graph_name="Q_Learning reward | alpha 0.8")


    reward_average, max_action, q_value = regular.double_q_learning()
    plot.plot_episode_time_step(reward_average, type_graph = "reward", type_graph_name="Double Q_Learning reward | alpha 0.8")
    plot.plot_episode_time_step(max_action, type_graph = "action", type_graph_name="Double Q Learning action | alpha 0.8")
    plot.plot_grid_world_with_wind_and_obstacle(q_value, type_graph = "optimal path", type_graph_name="Double Q_Learning reward | alpha 0.8")
    plot.save_q_value(q_value,  type_graph_name="Double Q_Learning reward | alpha 0.8")

