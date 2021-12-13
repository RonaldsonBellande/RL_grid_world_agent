from header_import import *


class grid_world_enviroment_display(object):
    def __init__(self):
        pass


    def wind_enviroment_draw(self, x, y):
        
        if self.grid_world_size == 20:
           
            # Weak wind on the x axis
            if x in [3*self.grid_world, 8*self.grid_world, 17*self.grid_world, 18*self.grid_world]:
                pg.draw.rect(self.screen, self.wind_color_weak, self.my_rect, 1)

            # Stronger Wind on the x axis
            if x in [6*self.grid_world, 13*self.grid_world]:
                pg.draw.rect(self.screen, self.wind_color_strong, self.my_rect, 1)
 
            # Weak wind on the y axis
            if y in [0*self.grid_world, 5*self.grid_world]:
                pg.draw.rect(self.screen, self.wind_color_weak, self.my_rect, 1)
 
            # Strong wind on the y axis
            if y in [1*self.grid_world, 16*self.grid_world]:
                pg.draw.rect(self.screen, self.wind_color_strong, self.my_rect, 1)
 
        elif self.grid_world_size == 50:
            
            # Weak wind on the x axis
            if x in [3*self.grid_world, 8*self.grid_world, 18*self.grid_world, 20*self.grid_world, 28*self.grid_world, 34*self.grid_world, 49*self.grid_world]:
                pg.draw.rect(self.screen, self.wind_color_weak, self.my_rect, 1)
            
            # Stronger Wind on the x axis
            if x in [6*self.grid_world, 13*self.grid_world, 37*self.grid_world, 46*self.grid_world]:
                pg.draw.rect(self.screen, self.wind_color_strong, self.my_rect, 1)
            
            # Weak wind on the y axis
            if y in [0*self.grid_world, 5*self.grid_world, 19*self.grid_world, 27*self.grid_world, 48*self.grid_world]:
                pg.draw.rect(self.screen, self.wind_color_weak, self.my_rect, 1)
        
            # Strong wind on the y axis
            if y in [16*self.grid_world, 22*self.grid_world, 38*self.grid_world, 46*self.grid_world]:
                pg.draw.rect(self.screen, self.wind_color_strong, self.my_rect, 1)
                

    def teleport_draw(self, x, y):

        if self.grid_world_size == 20:
            # Teleport 1 Start
            if x == self.teleport_1[0][0]*self.grid_world and y == self.teleport_1[0][1]*self.grid_world:
                pg.draw.rect(self.screen, self.teleport_1_color,  (x+self.start_goal,y+self.start_goal,self.grid_world - (self.start_goal + self.start_goal), self.grid_world - (self.start_goal + self.start_goal)))
            
            # Teleport 1 End
            if x == self.teleport_1[1][0]*self.grid_world and y == self.teleport_1[1][1]*self.grid_world:
                pg.draw.rect(self.screen, self.teleport_1_color,  (x+self.start_goal,y+self.start_goal,self.grid_world - (self.start_goal + self.start_goal), self.grid_world - (self.start_goal + self.start_goal)))

            # Teleport 2 Start
            if x == self.teleport_2[0][0]*self.grid_world and y == self.teleport_2[0][1]*self.grid_world:
                pg.draw.rect(self.screen, self.teleport_2_color,  (x+self.start_goal,y+self.start_goal,self.grid_world - (self.start_goal + self.start_goal), self.grid_world - (self.start_goal + self.start_goal)))

            # Teleport 2 End
            if x == self.teleport_2[1][0]*self.grid_world and y == self.teleport_2[1][1]*self.grid_world:
                pg.draw.rect(self.screen, self.teleport_2_color,  (x+self.start_goal,y+self.start_goal,self.grid_world - (self.start_goal + self.start_goal), self.grid_world - (self.start_goal + self.start_goal)))

      
        
        elif self.grid_world_size == 50:
            # Teleport 1 Start
            if x == self.teleport_1[0][0]*self.grid_world and y == self.teleport_1[0][1]*self.grid_world:
                pg.draw.rect(self.screen, self.teleport_1_color,  (x+self.start_goal,y+self.start_goal,self.grid_world - (self.start_goal + self.start_goal), self.grid_world - (self.start_goal + self.start_goal)))
            
            # Teleport 1 End
            if x == self.teleport_1[1][0]*self.grid_world and y == self.teleport_1[1][1]*self.grid_world:
                pg.draw.rect(self.screen, self.teleport_1_color,  (x+self.start_goal,y+self.start_goal,self.grid_world - (self.start_goal + self.start_goal), self.grid_world - (self.start_goal + self.start_goal)))


            # Teleport 2 Start
            if x == self.teleport_2[0][0]*self.grid_world and y == self.teleport_2[0][1]*self.grid_world:
                pg.draw.rect(self.screen, self.teleport_2_color,  (x+self.start_goal,y+self.start_goal,self.grid_world - (self.start_goal + self.start_goal), self.grid_world - (self.start_goal + self.start_goal)))


            # Teleport 2 End
            if x == self.teleport_2[1][0]*self.grid_world and y == self.teleport_2[1][1]*self.grid_world:
                pg.draw.rect(self.screen, self.teleport_2_color,  (x+self.start_goal,y+self.start_goal,self.grid_world - (self.start_goal + self.start_goal), self.grid_world - (self.start_goal + self.start_goal)))


    def starting_goal_position_draw(self, x, y):
        
        if self.grid_world_size == 20:
            
            # Starting Position
            if x == self.start[0]*self.grid_world and y == self.start[1]*self.grid_world:
                pg.draw.rect(self.screen, self.start_color, (x+self.start_goal,y+self.start_goal,self.grid_world - (self.start_goal + self.start_goal), self.grid_world - (self.start_goal + self.start_goal)))
            
            # Goal Position
            if x == self.goal[0]*self.grid_world and y == self.goal[1]*self.grid_world:
                pg.draw.rect(self.screen, self.goal_color, (x+self.start_goal,y+self.start_goal,self.grid_world - (self.start_goal + self.start_goal), self.grid_world - (self.start_goal + self.start_goal)))

        elif self.grid_world_size == 50:
            
            # Starting Position
            if x == self.start[0]*self.grid_world and y == self.start[1]*self.grid_world:
                pg.draw.rect(self.screen, self.start_color, (x+self.start_goal,y+self.start_goal,self.grid_world - (self.start_goal + self.start_goal), self.grid_world - (self.start_goal + self.start_goal)))
            
            # Goal Position
            if x == self.goal[0]*self.grid_world and y == self.goal[1]*self.grid_world:
                pg.draw.rect(self.screen, self.goal_color, (x+self.start_goal,y+self.start_goal,self.grid_world - (self.start_goal + self.start_goal), self.grid_world - (self.start_goal + self.start_goal)))


    def obstacle_draw(self,x,y):
        
        if self.grid_world_size == 20:
            
            # Obstacle at y = 4, small
            if x in range(0*self.grid_world,2*self.grid_world) and y == 4*self.grid_world:
                pg.draw.rect(self.screen,self.obstacle_color, (x,y ,self.grid_world, self.grid_world))

            # Obstacle at y = 7, small
            elif x in range(16*self.grid_world,18*self.grid_world) and y == 7*self.grid_world:
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
 
            # Obstacle at y = 12, big
            elif x in range(15*self.grid_world,19*self.grid_world) and y == 12*self.grid_world:
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
 
            # Obstacle at y = 17, big
            elif x in range(2*self.grid_world,6*self.grid_world) and y == 17*self.grid_world:
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
        
            # Obstacle at x = 5, small
            elif x == 5*self.grid_world and y in range(2*self.grid_world,4*self.grid_world):
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
        
            # Obstacle at x = 13, small
            elif x == 13*self.grid_world and y in range(12*self.grid_world,15*self.grid_world):
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
            
            # Obstacle at x = 16, big
            elif x  == 16*self.grid_world and y in range(4*self.grid_world,8*self.grid_world):
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
            
            # Obstacle at x = 17, big
            elif x == 17*self.grid_world and y  in range(10*self.grid_world,14*self.grid_world):
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
            
           

        if self.grid_world_size == 50:
            
            # Obstacle at y = 4, small
            if x in range(0*self.grid_world,2*self.grid_world) and y == 4*self.grid_world:
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
        
            # Obstacle at y = 7, small
            elif x in range(16*self.grid_world,18*self.grid_world) and y == 7*self.grid_world:
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
 
            # Obstacle at y = 12, big
            elif x in range(15*self.grid_world,19*self.grid_world) and y == 12*self.grid_world:
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
 
            # Obstacle at y = 17, big
            elif x in range(2*self.grid_world,6*self.grid_world) and y == 17*self.grid_world:
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))

            # Obstacle at y = 4, small
            elif x in range(7*self.grid_world,9*self.grid_world) and y == 44*self.grid_world:
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
        
            elif x in range(6*self.grid_world,8*self.grid_world) and y == 37*self.grid_world:
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
 
            # Obstacle at y = 12, big
            elif x in range(5*self.grid_world,9*self.grid_world) and y == 22*self.grid_world:
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
 
            # Obstacle at y = 17, big
            elif x in range(12*self.grid_world,16*self.grid_world) and y == 17*self.grid_world:
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
            
             # Obstacle at y = 4, small
            elif x in range(20*self.grid_world,22*self.grid_world) and y == 14*self.grid_world:
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
        
            # Obstacle at y = 7, small
            elif x in range(26*self.grid_world,28*self.grid_world) and y == 27*self.grid_world:
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
 
            # Obstacle at y = 12, big
            elif x in range(25*self.grid_world,29*self.grid_world) and y == 32*self.grid_world:
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
 
            # Obstacle at y = 17, big
            elif x in range(22*self.grid_world,26*self.grid_world) and y == 47*self.grid_world:
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))

            # Obstacle at y = 4, small
            elif x in range(37*self.grid_world,39*self.grid_world) and y == 44*self.grid_world:
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
        
            elif x in range(36*self.grid_world,38*self.grid_world) and y == 37*self.grid_world:
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
 
            # Obstacle at y = 12, big
            elif x in range(35*self.grid_world,39*self.grid_world) and y == 22*self.grid_world:
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
 
            # Obstacle at y = 17, big
            elif x in range(32*self.grid_world,36*self.grid_world) and y == 17*self.grid_world:
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))




            # Obstacle at x = 5, small
            elif x == 5*self.grid_world and y in range(2*self.grid_world,4*self.grid_world):
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
        
            # Obstacle at x = 13, small
            elif x == 13*self.grid_world and y in range(12*self.grid_world,15*self.grid_world):
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
            
            # Obstacle at x = 16, big
            elif x == 16*self.grid_world and y in range(4*self.grid_world,8*self.grid_world):
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
            
            # Obstacle at x = 17, big
            elif x == 17*self.grid_world and y in range(10*self.grid_world,14*self.grid_world):
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
            
            # Obstacle at x = 5, small
            elif x == 45*self.grid_world and y in range(12*self.grid_world,14*self.grid_world):
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
        
            # Obstacle at x = 13, small
            elif x == 33*self.grid_world and y in range(2*self.grid_world,5*self.grid_world):
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
            
            # Obstacle at x = 16, big
            elif x == 26*self.grid_world and y in range(14*self.grid_world,18*self.grid_world):
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
            
            # Obstacle at x = 17, big
            elif x == 17*self.grid_world and y  in range(0*self.grid_world,4*self.grid_world):
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))

            # Obstacle at x = 5, small
            elif x == 15*self.grid_world and y in range(22*self.grid_world,24*self.grid_world):
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
        
            # Obstacle at x = 13, small
            elif x == 23*self.grid_world and y in range(22*self.grid_world,25*self.grid_world):
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
            
            # Obstacle at x = 16, big
            elif x == 36*self.grid_world and y in range(24*self.grid_world,28*self.grid_world):
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
            
            # Obstacle at x = 17, big
            elif x == 47*self.grid_world and y in range(20*self.grid_world,24*self.grid_world):
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
            
            # Obstacle at x = 5, small
            elif x == 45*self.grid_world and y in range(32*self.grid_world,34*self.grid_world):
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
        
            # Obstacle at x = 13, small
            elif x == 33*self.grid_world and y in range(32*self.grid_world,35*self.grid_world):
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
            
            # Obstacle at x = 16, big
            elif x == 26*self.grid_world and y in range(34*self.grid_world,38*self.grid_world):
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))
            
            # Obstacle at x = 17, big
            elif x == 17*self.grid_world and y  in range(30*self.grid_world,34*self.grid_world):
                pg.draw.rect(self.screen, self.obstacle_color, (x,y ,self.grid_world, self.grid_world))


    def death_traps_draw(self, x, y):

        if self.grid_world_size == 50:
            
            if x in range(13*self.grid_world,17*self.grid_world) and y == 5*self.grid_world:
                pg.draw.rect(self.screen, self.death_color, (x,y ,self.grid_world, self.grid_world))
        
            elif x in range(30*self.grid_world,34*self.grid_world) and y == 28*self.grid_world:
                pg.draw.rect(self.screen, self.death_color, (x,y ,self.grid_world, self.grid_world))
            
            elif x in range(42*self.grid_world,46*self.grid_world) and y == 33*self.grid_world:
                pg.draw.rect(self.screen, self.death_color, (x,y ,self.grid_world, self.grid_world))
            
            elif x in range(2*self.grid_world,6*self.grid_world) and y == 49*self.grid_world:
                pg.draw.rect(self.screen, self.death_color, (x,y ,self.grid_world, self.grid_world))
            
            elif x in range(22*self.grid_world,26*self.grid_world) and y == 19*self.grid_world:
                pg.draw.rect(self.screen, self.death_color, (x,y ,self.grid_world, self.grid_world))
        
            elif x == 4*self.grid_world and y in range(24*self.grid_world,28*self.grid_world):
                pg.draw.rect(self.screen, self.death_color, (x,y ,self.grid_world, self.grid_world))
        
            elif x == 17*self.grid_world and y in range(32*self.grid_world,36*self.grid_world):
                pg.draw.rect(self.screen, self.death_color, (x,y ,self.grid_world, self.grid_world))
            
            elif x == 26*self.grid_world and y in range(4*self.grid_world,8*self.grid_world):
                pg.draw.rect(self.screen, self.death_color, (x,y ,self.grid_world, self.grid_world))
            
            elif x == 37*self.grid_world and y in range(14*self.grid_world,18*self.grid_world):
                pg.draw.rect(self.screen, self.death_color, (x,y ,self.grid_world, self.grid_world))

            elif x == 47*self.grid_world and y in range(44*self.grid_world,48*self.grid_world):
                pg.draw.rect(self.screen, self.death_color, (x,y ,self.grid_world, self.grid_world))
               

    def wind_enviroment(self, x, y, reward):
        
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
                
        return x, y, reward
        
        
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
        
    
    def teleport_enviroment(self, x, y, reward):
        
        if self.grid_world_size == 20:
            # Teleport 1
            if x == self.teleport_1[0][0] and y == self.teleport_1[0][1]:
                x = self.teleport_1[1][0]
                y = self.teleport_1[1][1]
                reward = 2
                
            # Teleport 2
            if x == self.teleport_2[0][0] and y == self.teleport_2[0][1]:
                x = self.teleport_2[1][0]
                y = self.teleport_2[1][1]
                reward = 2
        
        elif self.grid_world_size == 50:
            # Teleport 1
            if x == self.teleport_1[0][0] and y == self.teleport_1[0][1]:
                x = self.teleport_1[1][0]
                y = self.teleport_1[1][1]
                reward = 2
                
            # Teleport 2
            if x == self.teleport_2[0][0] and y == self.teleport_2[0][1]:
                x = self.teleport_2[1][0]
                y = self.teleport_2[1][1]
                reward = 2
                
        return x, y, reward
       


    def death_traps(self, x, y, reward):
        
        if self.grid_world_size == 50:
            if x in range(13,17) and y == 5:
                reward = -5
                return x, y, True, reward
            elif x in range(30,34) and y == 28:
                reward = -5
                return x, y, True, reward
            elif x in range(42,46) and y == 33:
                reward = -5
                return x, y, True, reward
            elif x in range(2,6) and y == 49:
                reward = -5
                return x, y, True, reward
            elif x in range(22,26) and y == 19:
                reward = -5
                return x, y, True, reward
            elif x == 4 and y in range(24,28):
                reward = -5
                return x, y, True, reward
            elif x == 17 and y in range(32,36):
                reward = -5
                return x, y, True, reward
            elif x == 26 and y in range(4,8):
                reward = -5
                return x, y, True, reward
            elif x == 37 and y in range(14,18):
                reward = -5
                return x, y, True, reward
            elif x == 47 and y in range(44,48):
                reward = -5
                return x, y, True, reward
            else:
                return x, y, False, reward
        else:
            return x, y, False, reward
 

    # Enemy Trajectory
    def enemy_enviroment(self):
        
        self.enemy_x = self.enemy_trajectory[self.i][0]
        self.enemy_y =  self.enemy_trajectory[self.i][1]
        self.i += 1
    
        if self.i == len(self.enemy_trajectory):
            self.i = 0
        
        return self.enemy_x, self.enemy_y,


