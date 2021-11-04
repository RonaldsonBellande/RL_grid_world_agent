from header_import import *


class Agent_Enviroment(Grid_World_Enviroment_with_Wind_Obstacle):
    def __init__(self, grid_world_size = 20):
        super().__init__(grid_world_size)
        
        self.WIDTH = 500
        self.HEIGHT = 500
        
        # define colors
        self.start_color = pg.Color(100, 0, 0)
        self.goal_color = pg.Color(0, 100, 0)
        self.bad_color = pg.Color(100, 0, 0)
        self.bg_color = pg.Color(0, 0, 0)
        self.line_color = pg.Color(128, 128, 128)
        self.agent_color = pg.Color(120,120,0)
        self.wind_color_strong = pg.Color(30,144,255)
        self.wind_color_weak =  pg.Color(173,216,230)
        self.obstacle_color = pg.Color(255,255,255)
        self.teleport_1_color = pg.Color(10,10,120)
        self.teleport_2_color = pg.Color(100,120,40)

        pg.init() 
        self.screen = pg.display.set_mode((self.WIDTH+2, self.HEIGHT+2))
        pg.display.set_caption("Ronaldson Bellande")
        self.bg = pg.Surface(self.screen.get_size())
        self.bg = self.bg.convert()
        self.bg.fill(self.bg_color)
        self.screen.blit(self.bg, (0,0))
        self.clock = pg.time.Clock()


        
        self.grid_world_size = grid_world_size

        if self.grid_world_size == 20:
            self.grid_world = 25
        elif self.grid_world_size == 50:
            self.grid_world = 10



    def show(self):
        for x in range(0, self.WIDTH, self.grid_world):
            for y in range(0, self.HEIGHT, self.grid_world):
                self.my_rect = pg.Rect(x,y, self.grid_world, self.grid_world)
                pg.draw.rect(self.screen, self.line_color, self.my_rect, 1)

                # Enviroment init
                self.show_enviroment(x, y)


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
                pg.draw.rect(self.screen, self.teleport_1_color, (x+9,y+9,self.grid_world - 18, self.grid_world - 18))
            
            # Teleport 1 End
            if x == self.teleport_1[1][0]*self.grid_world and y == self.teleport_1[1][1]*self.grid_world:
                pg.draw.rect(self.screen, self.teleport_1_color, (x+9,y+9,self.grid_world - 18, self.grid_world - 18))


            # Teleport 2 Start
            if x == self.teleport_2[0][0]*self.grid_world and y == self.teleport_2[0][1]*self.grid_world:
                pg.draw.rect(self.screen, self.teleport_2_color, (x+9,y+9,self.grid_world - 18, self.grid_world - 18))


            # Teleport 2 End
            if x == self.teleport_2[1][0]*self.grid_world and y == self.teleport_2[1][1]*self.grid_world:
                pg.draw.rect(self.screen, self.teleport_2_color, (x+9,y+9,self.grid_world - 18, self.grid_world - 18))

      
        
        elif self.grid_world_size == 50:
            # Teleport 1 Start
            if x == self.teleport_1[0][0]*self.grid_world and y == self.teleport_1[0][1]*self.grid_world:
                pg.draw.rect(self.screen, self.teleport_1_color, (x+9,y+9,self.grid_world - 18, self.grid_world - 18))
            
            # Teleport 1 End
            if x == self.teleport_1[1][0]*self.grid_world and y == self.teleport_1[1][1]*self.grid_world:
                pg.draw.rect(self.screen, self.teleport_1_color, (x+9,y+9,self.grid_world - 18, self.grid_world - 18))


            # Teleport 2 Start
            if x == self.teleport_2[0][0]*self.grid_world and y == self.teleport_2[0][1]*self.grid_world:
                pg.draw.rect(self.screen, self.teleport_2_color, (x+9,y+9,self.grid_world - 18, self.grid_world - 18))


            # Teleport 2 End
            if x == self.teleport_2[1][0]*self.grid_world and y == self.teleport_2[1][1]*self.grid_world:
                pg.draw.rect(self.screen, self.teleport_2_color, (x+9,y+9,self.grid_world - 18, self.grid_world - 18))


    def starting_goal_position_draw(self, x, y):
        
        if self.grid_world_size == 20:
            
            # Starting Position
            if x == self.start[0]*self.grid_world and y == self.start[1]*self.grid_world:
                pg.draw.rect(self.screen, self.start_color, (x+9,y+9,self.grid_world - 18, self.grid_world - 18))
            
            # Goal Position
            if x == self.goal[0]*self.grid_world and y == self.goal[1]*self.grid_world:
                pg.draw.rect(self.screen, self.goal_color, (x+9,y+9,self.grid_world - 18, self.grid_world - 18))

        elif self.grid_world_size == 50:
            
            # Starting Position
            if x == self.start[0]*self.grid_world and y == self.start[1]*self.grid_world:
                pg.draw.rect(self.screen, self.start_color, (x+9,y+9,self.grid_world - 18, self.grid_world - 18))
            
            # Goal Position
            if x == self.goal[0]*self.grid_world and y == self.goal[1]*self.grid_world:
                pg.draw.rect(self.screen, self.goal_color, (x+9,y+9,self.grid_world - 18, self.grid_world - 18))


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

    
    def show_enviroment(self, x, y):
        
        self.wind_enviroment_draw(x,y)
        self.teleport_draw(x,y)
        self.obstacle_draw(x,y)
        self.starting_goal_position_draw(x,y)

    
    def play_optimal_path(self):
        original_array = np.loadtxt("q_values/"+ str(type_graph_name) + ".txt").reshape(4, 2)


    def move(self, x, y):
        pg.draw.rect(self.screen, self.agent_color,  (x*self.grid_world +4, y*self.grid_world +4,self.grid_world - 8, self.grid_world - 8))
        self.show()


    def main(self):

        # Agent Starts
        x, y = self.start
        self.show()
        self.move(x,y)
        pg.display.flip()
        run = True
        while run:
            self.clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False
            
                # Action 0
                elif event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                    action = 0
                    x,y = self.transition(x, y, action)
                # Action 1
                elif event.type == pg.KEYDOWN and event.key == pg.K_UP:
                    action = 1
                    x,y = self.transition(x, y, action)
                # Action 2
                elif event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                    action = 2
                    x,y = self.transition(x, y, action)
                # Action 3
                elif event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                    action = 3
                    x,y = self.transition(x, y, action)

            self.screen.blit(self.bg, (0,0))
            self.move(x,y)

            self.show()
            pg.display.flip()
            pg.display.update()
        pg.quit()


if __name__ == "__main__":
    grid_size = int(sys.argv[1])

    Agent_Enviroment_obj = Agent_Enviroment(grid_world_size = grid_size)
    Agent_Enviroment_obj.main()
