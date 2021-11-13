from header_import import *


class Grid_World_Enviroment_with_Wind_Obstacle(object):
    def __init__(self, simulation, grid_world_size = 20):
        
        self.grid_world_size = grid_world_size
        self.action_space = [0, 1, 2, 3]
        self.simulation = simulation
         
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
            self.teleport_2 = [(47, 8), (0, 4)]

        self.death = False
        self.enemy_trajectory = [(37, 36), (37, 35), (37, 34), (37, 33), (36, 33), (35, 33), (34, 33), (34, 34), (34, 35), (34, 36), (35, 36), (36, 36), (37, 36)]
        self.i = 0

        
    def action_type_space(self):
        return self.action_space
        
    def reset(self):
        self.x_position, self.y_position = self.start
        return self.start
    
    def step(self, action):
        self.x_position, self.y_position, reward = self.transition(self.x_position, self.y_position, action)
        
        if self.x_position == self.goal[0] and self.y_position == self.goal[1]:
            return True, reward, (self.x_position, self.y_position)

        if self.death == True:
            return True, reward, (self.x_position, self.y_position)

        if self.x_position == self.enemy_x and self.y_position == self.enemy_y:
            return True, reward, (self.x_position, self.y_position)

        return False, reward, (self.x_position, self.y_position)
        
        
    def wind_enviroment(self, x, y):

        if self.grid_world_size == 20:
            
            x_next = x
            y_next = y

            # Weak wind on the x axis
            if x in [3, 8, 17, 18]:
                y += 1
            
            # Obstacle Enviroment
            x_next, y_next, detect = self.obstacle_enviroment(x, y)

            if detect == True:
                x = x_next
                y = y_next
            else:
                y -= 1


            
            # Stronger Wind on the x axis
            if x in [6, 13]:
                # First
                y += 1

                # Obstacle Enviroment
                x_next, y_next, detect = self.obstacle_enviroment(x, y)

                if detect == True:
                    x = x_next
                    y = y_next
                else:
                    y -= 1

                
                # Second
                y += 1

                # Obstacle Enviroment
                x_next, y_next, detect = self.obstacle_enviroment(x, y)

                if detect == True:
                    x = x_next
                    y = y_next
                else:
                    y -= 1



            
            # Weak wind on the y axis
            if y in [0, 5]:
                x += 1

                # Obstacle Enviroment
                x_next, y_next, detect = self.obstacle_enviroment(x, y)

                if detect == True:
                    x = x_next
                    y = y_next
                else:
                    x -= 1

        
            # Strong wind on the y axis
            if y in [1, 16]:
                x += 1

                # Obstacle Enviroment
                x_next, y_next, detect = self.obstacle_enviroment(x, y)

                if detect == True:
                    x = x_next
                    y = y_next
                else:
                    x -= 1

                
                # Second
                x += 1

                # Obstacle Enviroment
                x_next, y_next, detect = self.obstacle_enviroment(x, y)

                if detect == True:
                    x = x_next
                    y = y_next
                else:
                    x -= 1


        elif self.grid_world_size == 50:
            

            x_next = x
            y_next = y


            # Weak wind on the x axis
            if x in [3, 8, 18, 20, 28, 34, 49]:
                y += 1

                # Obstacle Enviroment
                x_next, y_next, detect = self.obstacle_enviroment(x, y)

                if detect == True:
                    x = x_next
                    y = y_next
                else:
                    y -= 1

            
            # Stronger Wind on the x axis
            elif x in [6, 13, 37, 46]:
                y += 1

                # Obstacle Enviroment
                x_next, y_next, detect = self.obstacle_enviroment(x, y)

                if detect == True:
                    x = x_next
                    y = y_next
                else:
                    y -= 1

                
                # Second
                y += 1

                # Obstacle Enviroment
                x_next, y_next, detect = self.obstacle_enviroment(x, y)

                if detect == True:
                    x = x_next
                    y = y_next
                else:
                    y -= 1
            
            # Weak wind on the y axis
            elif y in [0, 5, 19, 27, 48]:
                x += 1

                # Obstacle Enviroment
                x_next, y_next, detect = self.obstacle_enviroment(x, y)

                if detect == True:
                    x = x_next
                    y = y_next
                else:
                    x -= 1

        
            # Strong wind on the y axis
            elif y in [16, 22, 38, 46]:
                x += 1

                # Obstacle Enviroment
                x_next, y_next, detect = self.obstacle_enviroment(x, y)

                if detect == True:
                    x = x_next
                    y = y_next
                else:
                    x -= 1

                
                # Second
                x += 1

                # Obstacle Enviroment
                x_next, y_next, detect = self.obstacle_enviroment(x, y)

                if detect == True:
                    x = x_next
                    y = y_next
                else:
                    x -= 1
                
        return x, y
        
        
    def obstacle_enviroment(self, x, y):
        
        # Small = 3
        # Big = 6
        if self.grid_world_size == 20:
            
            # Obstacle at y = 4, small
            if x in range(0,2) and y == 4:
                return x, y, False
        
            # Obstacle at y = 7, small
            elif x in range(16,18) and y == 7:
                return x, y, False
            
            # Obstacle at y = 12, big
            elif x in range(15,19) and y == 12:
                return x, y, False
            
            # Obstacle at y = 17, big
            elif x in range(2,6) and y == 17:
                return x, y, False
        
            # Obstacle at x = 5, small
            elif x == 5 and y in range(2,4):
                return x, y, False
        
            # Obstacle at x = 13, small
            elif x == 13 and y in range(12,15):
                return x, y, False
            
            # Obstacle at x = 16, big
            elif x == 16 and y in range(4,8):
                return x, y, False
            
            # Obstacle at x = 17, big
            elif x == 17 and y in range(10,14):
                return x, y, False

            # Bounder of the world
            elif x in range(-1,self.grid_world_size) and y == -1:
                return x, y, False

            elif x in range(-1,self.grid_world_size) and y == self.grid_world_size:
                return x, y, False

            elif x == -1 and y in range(-1,self.grid_world_size):
                return x, y, False

            elif x == self.grid_world_size and y in range(-1,self.grid_world_size):
                return x, y, False
            
            else:
                return x, y, True
            
            
            
        if self.grid_world_size == 50:
            
            if x in range(0,2) and y == 4:
                return x, y, False
        
            # Obstacle at y = 7, small
            elif x in range(16,18) and y == 7:
                return x, y, False
 
            # Obstacle at y = 12, big
            elif x in range(15,19) and y == 12:
                return x, y, False
 
            # Obstacle at y = 17, big
            elif x in range(2,6) and y == 17:
                return x, y, False

            # Obstacle at y = 4, small
            elif x in range(7,9) and y == 44:
                return x, y, False
        
            elif x in range(6,8) and y == 37:
                return x, y, False
 
            # Obstacle at y = 12, big
            elif x in range(5,9) and y == 22:
                return x, y, False
 
            # Obstacle at y = 17, big
            elif x in range(12,16) and y == 17:
                return x, y, False
            
             # Obstacle at y = 4, small
            elif x in range(20,22) and y == 14:
                return x, y, False
        
            # Obstacle at y = 7, small
            elif x in range(26,28) and y == 27:
                return x, y, False
 
            # Obstacle at y = 12, big
            elif x in range(25,29) and y == 32:
                return x, y, False
 
            # Obstacle at y = 17, big
            elif x in range(22,26) and y == 47:
                return x, y, False

            # Obstacle at y = 4, small
            elif x in range(37,39) and y == 44:
                return x, y, False
        
            elif x in range(36,38) and y == 37:
                return x, y, False
 
            # Obstacle at y = 12, big
            elif x in range(35,39) and y == 22:
                return x, y, False
 
            # Obstacle at y = 17, big
            elif x in range(32,36) and y == 17:
                return x, y, False



            # Obstacle at x = 5, small
            elif x == 5 and y in range(2,4):
                return x, y, False
        
            # Obstacle at x = 13, small
            elif x == 13 and y in range(12,15):
                return x, y, False
            
            # Obstacle at x = 16, big
            elif x == 16 and y in range(4,8):
                return x, y, False
            
            # Obstacle at x = 17, big
            elif x == 17 and y in range(10,14):
                return x, y, False
            
            # Obstacle at x = 5, small
            elif x == 45 and y in range(12,14):
                return x, y, False
        
            # Obstacle at x = 13, small
            elif x == 33 and y in range(2,5):
                return x, y, False
            
            # Obstacle at x = 16, big
            elif x == 26 and y in range(14,18):
                return x, y, False
            
            # Obstacle at x = 17, big
            elif x == 17 and y  in range(0,4):
                return x, y, False

            # Obstacle at x = 5, small
            elif x == 15 and y in range(22,24):
                return x, y, False
        
            # Obstacle at x = 13, small
            elif x == 23 and y in range(22,25):
                return x, y, False
            
            # Obstacle at x = 16, big
            elif x == 36 and y in range(24,28):
                return x, y, False
            
            # Obstacle at x = 17, big
            elif x == 47 and y in range(20,24):
                return x, y, False
            
            # Obstacle at x = 5, small
            elif x == 45 and y in range(32,34):
                return x, y, False
        
            # Obstacle at x = 13, small
            elif x == 33 and y in range(32,35):
                return x, y, False
            
            # Obstacle at x = 16, big
            elif x == 26 and y in range(34,38):
                return x, y, False
            
            # Obstacle at x = 17, big
            elif x == 17 and y  in range(30,34):
                return x, y, False

            # Bounder of the world
            elif x in range(-1,self.grid_world_size) and y == -1:
                return x, y, False

            elif x in range(-1,self.grid_world_size) and y == self.grid_world_size:
                return x, y, False

            elif x == -1 and y in range(-1,self.grid_world_size):
                return x, y, False

            elif x == self.grid_world_size and y in range(-1,self.grid_world_size):
                return x, y, False
            else:
                return x, y, True
        
    
    def teleport_enviroment(self, x, y):
        if self.grid_world_size == 20:
            # Teleport 1
            if x == self.teleport_1[0][0] and y == self.teleport_1[0][1]:
                x = self.teleport_1[1][0]
                y = self.teleport_1[1][1]
                
            # Teleport 2
            if x == self.teleport_2[0][0] and y == self.teleport_2[0][1]:
                x = self.teleport_2[1][0]
                y = self.teleport_2[1][1]
        
        elif self.grid_world_size == 50:
            # Teleport 1
            if x == self.teleport_1[0][0] and y == self.teleport_1[0][1]:
                x = self.teleport_1[1][0]
                y = self.teleport_1[1][1]
                
            # Teleport 2
            if x == self.teleport_2[0][0] and y == self.teleport_2[0][1]:
                x = self.teleport_2[1][0]
                y = self.teleport_2[1][1]
                
        return x, y
       


    def death_traps(self, x, y):
        
        if self.grid_world_size == 50:
            
            if x in range(13,17) and y == 5:
                return x, y, True
        
            elif x in range(30,34) and y == 28:
                return x, y, True
            
            elif x in range(42,46) and y == 33:
                return x, y, True
            
            elif x in range(2,6) and y == 49:
                return x, y, True
            
            elif x in range(22,26) and y == 19:
                return x, y, True
        
            elif x == 4 and y in range(24,28):
                return x, y, True
        
            elif x == 17 and y in range(32,36):
                return x, y, True
            
            elif x == 26 and y in range(4,8):
                return x, y, True
            
            elif x == 37 and y in range(14,18):
                return x, y, True

            elif x == 47 and y in range(44,48):
                return x, y, True
            
            else:
                return x, y, False


        else:
            return x, y, False
 

    # Enemy Trajectory
    def enemy_enviroment(self):
        
        self.enemy_x = self.enemy_trajectory[self.i][0]
        self.enemy_y =  self.enemy_trajectory[self.i][1]
        self.i += 1
    
        if self.i == len(self.enemy_trajectory):
            self.i = 0
        
        return self.enemy_x, self.enemy_y


    def transition(self, x, y, action):
        
        reward = -1 
        
        # Teleport Enviroment
        x, y = self.teleport_enviroment(x,y)
        
        # Wind Enviroment
        x, y = self.wind_enviroment(x,y)
        
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
        x, y, death = self.death_traps(x, y)
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
            reward = 1

        if self.simulation == True: 
            if self.death == True:
                reward = -2
                return self.start[0],self.start[1], reward

            if x == self.enemy_x and y  == self.enemy_y:
                reward = -2
                return self.start[0],self.start[1], reward

        return x, y, reward
