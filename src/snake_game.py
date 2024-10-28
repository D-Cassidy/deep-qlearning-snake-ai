# Import statements
import random

# Local imports
import constants

class Game:
    def __init__(self, grid_size, window_size):
        self.grid_size = grid_size
        self.window_size = window_size
        self.snake = Snake(grid_size)
        self.food = Food(grid_size, window_size)
        self.score = 0
        self.game_over = False 

    def update(self):
        """
        Moves snake, check for food collision, then checks for snake collision
        """
        self.snake.move()
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.food.respawn_food()
            self.score += 1
        self.check_game_over()

    def check_game_over(self):
        """
        Checks if the head has collided with snake body, or if head is out of bounds
        """
        right_bound = self.window_size[0] / self.grid_size
        lower_bound = self.window_size[1] / self.grid_size
        head = self.snake.body[0]
        if (head in self.snake.body[1:]
            or head[0] < 0 or head[0] > right_bound
            or head[1] < 0 or head[1] > lower_bound):
            self.game_over = True

    def reset(self):
        self.__init__(self.grid_size, self.window_size)

class Snake:
    def __init__(self, grid_size):
        self.body = [(5, 5), (5, 4), (5, 3)]
        self.direction = constants.RIGHT
        self.grid_size = grid_size

    def move(self):
        """
        Moves the snake in the direction of its motion
        """
        # Create new snake part using head as reference
        head = (self.body[0][0] + self.direction[0],
                self.body[0][1] + self.direction[1])
        
        # Add new snake part to body, while removing the last one in the chain
        self.body = [head] + self.body[:-1]

    def grow(self):
        """
        Adds a duplicate of the last body part to the snake body list.
        This works because it effectively stops the final body part from being deleted upon the
        next movement.
        """
        self.body.append(self.body[-1])

    def change_direction(self, direction):
        """
        Changes snake direction, while preventing snake from turning backwards and losing
        """
        if direction != (-self.direction[0], -self.direction[1]):
            self.direction = direction

class Food:
    def __init__(self, grid_size, window_size):
        self.grid_size = grid_size
        self.window_size = window_size
        self.spawn_food()

    def spawn_food(self):
        """
        Sets food position as random square on the screen
        """
        right_bound = self.window_size[0] / self.grid_size
        lower_bound = self.window_size[1] / self.grid_size
        self.position = (random.randint(0,  int(right_bound)-1), random.randint(0, int(lower_bound)))

    def respawn_food(self):
        self.spawn_food()