import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
FPS = 10
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Snake Game Class
class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.reset_game()

    def reset_game(self):
        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.snake_direction = RIGHT
        self.score = 0
        self.food_position = self.spawn_food()
        self.game_over = False

    def spawn_food(self):
        while True:
            position = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if position not in self.snake:
                return position

    def change_direction(self, new_direction):
        if (self.snake_direction[0] + new_direction[0] != 0 or
            self.snake_direction[1] + new_direction[1] != 0):
            self.snake_direction = new_direction

    def update(self):
        if not self.game_over:
            head_x, head_y = self.snake[0]
            new_head = (head_x + self.snake_direction[0], head_y + self.snake_direction[1])

            # Check for wall collisions
            if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or
                    new_head[1] < 0 or new_head[1] >= GRID_HEIGHT or
                    new_head in self.snake):
                self.game_over = True
                return

            self.snake.insert(0, new_head)
            if new_head == self.food_position:
                self.score += 10
                self.food_position = self.spawn_food()
            else:
                self.snake.pop()

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        for segment in self.snake:
            pygame.draw.rect(self.screen, SNAKE_COLOR, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(self.screen, FOOD_COLOR, (self.food_position[0] * CELL_SIZE, self.food_position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        # Draw the score
        font = pygame.font.SysFont(None, 35)
        score_surface = font.render(f'Score: {self.score}', True, (255, 255, 255))
        self.screen.blit(score_surface, (10, 10))

        pygame.display.flip()

    def run(self):
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.change_direction(UP)
                    elif event.key == pygame.K_DOWN:
                        self.change_direction(DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.change_direction(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.change_direction(RIGHT)

            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()