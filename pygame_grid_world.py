# from evaluator import *
from header_import import *


class Agent_Enviroment(Grid_World_Enviroment_with_Wind_Obstacle, grid_world_enviroment_display):
    def __init__(self, grid_world_size, graph_data_name, grid_play_task):
        super().__init__(grid_world_size)
        
        self.WIDTH = 500
        self.HEIGHT = 500
        
        # define colors
        self.start_color = pg.Color(100, 0, 0)
        self.goal_color = pg.Color(0, 100, 0)
        self.bad_color = pg.Color(100, 0, 0)
        self.bg_color = pg.Color(0, 0, 0)
        self.enemy_agent_color = pg.Color(255, 100, 100)
        self.death_color = pg.Color(255, 0, 0)
        self.line_color = pg.Color(128, 128, 128)
        self.agent_color = pg.Color(120,120,0)
        self.wind_color_strong = pg.Color(30,144,255)
        self.wind_color_weak =  pg.Color(173,216,230)
        self.obstacle_color = pg.Color(255,255,255)
        self.teleport_1_color = pg.Color(10,10,120)
        self.teleport_2_color = pg.Color(100,120,40)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 128)
        
        pg.init() 
        self.screen = pg.display.set_mode((self.WIDTH+2, self.HEIGHT+2))
        pg.display.set_caption("Ronaldson Bellande")
        self.bg = pg.Surface(self.screen.get_size())
        self.bg = self.bg.convert()
        self.bg.fill(self.bg_color)
        self.screen.blit(self.bg, (0,0))
        self.Font = pg.font.SysFont('timesnewroman',  20)
        self.clock = pg.time.Clock()
        
        self.grid_world_size = grid_world_size
        self.grid_play_task = grid_play_task
        self.q_value_path = "q_values/"
        self.size_of_world_path = str(grid_world_size) + "/"
        self.graph_data_name = graph_data_name
        
        if self.grid_world_size == 20:
            self.grid_world = 25
            self.moving_object = 4
            self.start_goal = 7
        elif self.grid_world_size == 50:
            self.grid_world = 10
            self.moving_object = 1
            self.start_goal = 3


    def show(self):
        for x in range(0, self.WIDTH, self.grid_world):
            for y in range(0, self.HEIGHT, self.grid_world):
                self.my_rect = pg.Rect(x,y, self.grid_world, self.grid_world)
                pg.draw.rect(self.screen, self.line_color, self.my_rect, 1)
                self.show_enviroment(x, y)


    def show_enviroment(self, x, y):
        self.wind_enviroment_draw(x,y)
        self.teleport_draw(x,y)
        self.obstacle_draw(x,y)
        self.starting_goal_position_draw(x,y)
        self.death_traps_draw(x,y)

        
    def action_path(self, q_value, starting_position):
        x, y = starting_position
        path = [starting_position]
 
        for _ in range(100):
            best_action = np.argmax([q_value[(x,y), a] for a in self.action_space])
            x, y, reward = self.transition(x, y, best_action)
            path.append((x,y))

            if x == self.goal[0] and y == self.goal[1]:
                break
                
        return path
        
    
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
        path = self.action_path(q_value_dict, starting_position)
        
        return path

    def move(self, x, y):
        pg.draw.rect(self.screen, self.agent_color,  (x*self.grid_world +self.moving_object, y*self.grid_world +self.moving_object,self.grid_world -(self.moving_object + self.moving_object), self.grid_world - (self.moving_object + self.moving_object)))
        self.show()


    def enemy_move(self, x, y):
        pg.draw.rect(self.screen, self.enemy_agent_color, (x*self.grid_world +self.moving_object, y*self.grid_world +self.moving_object,self.grid_world -(self.moving_object + self.moving_object), self.grid_world - (self.moving_object + self.moving_object)))
        self.show()


    def main(self, starting_position):

        # Agent Starts
        x, y = starting_position
        self.show()
        self.move(x,y)
        pg.display.flip()
        run = True
        reward = -1
        path = self.play_optimal_path(starting_position)
        count = 0

        while run:
            self.clock.tick(60)
            if self.grid_play_task == "True" and count < len(path):
                    self.enemy_enviroment()
                    x, y = path[count]
                    self.move(x,y)
            else:
                for event in pg.event.get():
                    self.enemy_enviroment()
                    if event.type == pg.QUIT:
                        run = False
                    # Action 0
                    elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                        action = 0
                        x,y, reward = self.transition(x, y, action)
                    # Action 1
                    elif event.type == pg.KEYUP and event.key == pg.K_UP:
                        action = 1
                        x,y, reward = self.transition(x, y, action)
                    # Action 2
                    elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                        action = 2
                        x,y, reward = self.transition(x, y, action)
                    # Action 3
                    elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                        action = 3
                        x, y, reward = self.transition(x, y, action)
            
            count += 1
            text = self.Font.render("Reward: "+str(reward), True, self.green)
            self.screen.blit(self.bg, (0,0))
            self.move(x,y)
            self.enemy_move(self.enemy_x, self.enemy_y)
            self.show()
            pg.display.flip()
            self.screen.blit(text, (230,480))
            pg.display.update()
            time.sleep(1)
        pg.quit()


if __name__ == "__main__":
    grid_size = int(sys.argv[1])
    initial_position = sys.argv[2]
    play_task = sys.argv[3]
    data_name = "Q_Learning_alpha_0.8"

    Agent_Enviroment_obj = Agent_Enviroment(grid_world_size = grid_size, graph_data_name = data_name, grid_play_task = play_task)
    Agent_Enviroment_obj.main(starting_position=(0,10))
