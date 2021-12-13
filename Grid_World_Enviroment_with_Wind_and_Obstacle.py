from header_import import *


class Grid_World_Enviroment_with_Wind_Obstacle(grid_world_enviroment_display):
    def __init__(self, grid_world_size):
        super().__init__()
        
        self.grid_world_size = grid_world_size
        self.action_space = [0, 1, 2, 3]
         
        if self.grid_world_size == 20:
            self.start = (0, 0)
            self.goal = (19, 19)
            
            # Teleport function
            self.teleport_1 = [(0, 19), (17, 1)]
            self.teleport_2 = [(19, 4), (0, 2)]
            
        elif self.grid_world_size == 50:
            self.start = (0, 0)
            self.goal = (49, 49)
            
            # Teleport function
            self.teleport_1 = [(0, 41), (38, 19)]
            self.teleport_2 = [(47, 8), (0, 5)]

        self.death = False
        self.enemy_trajectory = [(37, 36), (37, 35), (37, 34), (37, 33), (36, 33), (35, 33), (34, 33), (34, 34), (34, 35), (34, 36), (35, 36), (36, 36), (37, 36)]
        self.i = 0

        
    def action_type_space(self):
        return self.action_space
        
    def reset(self, start):
        self.x_position, self.y_position = start
        return start
    
    def step(self, action):
        self.x_position, self.y_position, reward = self.transition(self.x_position, self.y_position, action)

        if self.x_position == self.goal[0] and self.y_position == self.goal[1]:
            return True, reward, (self.x_position, self.y_position)

        if self.death == True:
            return True, reward, (self.x_position, self.y_position)

        if self.x_position == self.enemy_x and self.y_position == self.enemy_y:
            return True, reward, (self.x_position, self.y_position)

        return False, reward, (self.x_position, self.y_position)
        

    def transition(self, x, y, action):
        
        reward = -1 
        
        # Teleport Enviroment
        x, y, reward = self.teleport_enviroment(x,y, reward)
        
        # Wind Enviroment
        x, y, reward = self.wind_enviroment(x,y, reward)
        
        self.enemy_enviroment()

        x_next = x
        y_next = y

        # Action taken
        if action == 0:
            x -= 1
        elif action == 1:
            y -= 1
        elif action == 2:
            x += 1
        elif action == 3:
            y += 1

        # Obstacle Enviroment
        x_next, y_next, detect = self.obstacle_enviroment(x, y)
        
        # Dead Enviroment
        x, y, death, reward = self.death_traps(x, y, reward)
        self.death = death


        if detect == True:
            x = x_next
            y = y_next
        else:
            if action == 0:
                x += 1
            elif action == 1:
                y += 1
            elif action == 2:
                x -= 1
            elif action == 3:
                y -= 1

         
        x = np.clip(x, 0, self.grid_world_size)
        y = np.clip(y, 0, self.grid_world_size)

        if x == self.goal[0] and y == self.goal[1]:
            reward = 5
            return x, y, reward 
        
        if self.death == True:
            reward = -5
            return self.start[0],self.start[1], reward

        if x == self.enemy_x and y  == self.enemy_y:
            reward = -5
            return self.start[0], self.start[1], reward

        return x, y, reward
