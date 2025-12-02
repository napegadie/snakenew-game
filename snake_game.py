"""
Modern Snake Game
A classic Snake game with modern design, featuring:
- Dark background with bright contrasting colors
- Real-time score tracking
- Collision detection (walls and self-collision)
- Restart functionality
- Arrow key controls
"""

import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Game Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE
FPS = 10

# Modern Color Palette (Dark theme with bright contrasts)
COLOR_BACKGROUND = (20, 20, 30)  # Dark blue-black
COLOR_SNAKE = (0, 255, 150)  # Bright cyan-green
COLOR_SNAKE_HEAD = (0, 200, 255)  # Bright blue
COLOR_FOOD = (255, 50, 100)  # Bright pink-red
COLOR_SCORE = (255, 255, 255)  # White
COLOR_GAME_OVER = (255, 200, 50)  # Yellow-orange
COLOR_GRID = (40, 40, 50)  # Subtle grid lines

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    """Snake class to manage snake position, movement, and growth"""
    
    def __init__(self):
        """Initialize snake in the center of the screen"""
        self.length = 3
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        self.positions = [(start_x, start_y), (start_x - 1, start_y), (start_x - 2, start_y)]
        self.direction = RIGHT
        self.grow_pending = False
    
    def get_head_position(self):
        """Return the position of snake's head"""
        return self.positions[0]
    
    def update(self):
        """Move the snake in current direction"""
        current_head = self.get_head_position()
        new_head = (
            current_head[0] + self.direction[0],
            current_head[1] + self.direction[1]
        )
        
        # Add new head position
        self.positions.insert(0, new_head)
        
        # Remove tail if not growing
        if not self.grow_pending:
            self.positions.pop()
        else:
            self.grow_pending = False
            self.length += 1
    
    def grow(self):
        """Mark snake to grow on next update"""
        self.grow_pending = True
    
    def change_direction(self, new_direction):
        """Change direction if not opposite to current direction"""
        # Prevent 180-degree turns
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction
    
    def check_self_collision(self):
        """Check if snake head collides with its body"""
        head = self.get_head_position()
        return head in self.positions[1:]
    
    def check_wall_collision(self):
        """Check if snake hits the wall"""
        head = self.get_head_position()
        return (
            head[0] < 0 or head[0] >= GRID_WIDTH or
            head[1] < 0 or head[1] >= GRID_HEIGHT
        )
    
    def reset(self):
        """Reset snake to initial state"""
        self.__init__()


class Food:
    """Food class to manage food position"""
    
    def __init__(self):
        """Initialize food at a random position"""
        self.position = (0, 0)
        self.randomize_position()
    
    def randomize_position(self, snake_positions=None):
        """Place food at a random position avoiding snake body"""
        while True:
            self.position = (
                random.randint(0, GRID_WIDTH - 1),
                random.randint(0, GRID_HEIGHT - 1)
            )
            # Ensure food doesn't spawn on snake
            if snake_positions is None or self.position not in snake_positions:
                break


class SnakeGame:
    """Main game class to manage game state and rendering"""
    
    def __init__(self):
        """Initialize game window and game objects"""
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Modern Snake Game")
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.Font(None, 72)
        self.font_medium = pygame.font.Font(None, 48)
        self.font_small = pygame.font.Font(None, 36)
        
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False
    
    def handle_events(self):
        """Handle keyboard input and window events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                if self.game_over:
                    # Restart game on SPACE or RETURN key when game is over
                    if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                        self.restart_game()
                else:
                    # Handle direction changes
                    if event.key == pygame.K_UP:
                        self.snake.change_direction(UP)
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction(DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction(RIGHT)
                    elif event.key == pygame.K_ESCAPE:
                        return False
        
        return True
    
    def update(self):
        """Update game state"""
        if not self.game_over:
            self.snake.update()
            
            # Check food collision
            if self.snake.get_head_position() == self.food.position:
                self.snake.grow()
                self.score += 10
                self.food.randomize_position(self.snake.positions)
            
            # Check collisions
            if self.snake.check_wall_collision() or self.snake.check_self_collision():
                self.game_over = True
    
    def draw_grid(self):
        """Draw subtle grid lines for visual enhancement"""
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, COLOR_GRID, (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, COLOR_GRID, (0, y), (WINDOW_WIDTH, y))
    
    def draw(self):
        """Render all game elements"""
        # Clear screen with dark background
        self.screen.fill(COLOR_BACKGROUND)
        
        # Draw grid
        self.draw_grid()
        
        # Draw snake
        for i, pos in enumerate(self.snake.positions):
            rect = pygame.Rect(
                pos[0] * GRID_SIZE,
                pos[1] * GRID_SIZE,
                GRID_SIZE - 2,
                GRID_SIZE - 2
            )
            if i == 0:  # Head
                pygame.draw.rect(self.screen, COLOR_SNAKE_HEAD, rect, border_radius=5)
            else:  # Body
                pygame.draw.rect(self.screen, COLOR_SNAKE, rect, border_radius=3)
        
        # Draw food
        food_rect = pygame.Rect(
            self.food.position[0] * GRID_SIZE,
            self.food.position[1] * GRID_SIZE,
            GRID_SIZE - 2,
            GRID_SIZE - 2
        )
        pygame.draw.rect(self.screen, COLOR_FOOD, food_rect, border_radius=5)
        
        # Draw score
        score_text = self.font_small.render(f"Score: {self.score}", True, COLOR_SCORE)
        self.screen.blit(score_text, (10, 10))
        
        # Draw game over screen
        if self.game_over:
            # Semi-transparent overlay
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            overlay.set_alpha(180)
            overlay.fill(COLOR_BACKGROUND)
            self.screen.blit(overlay, (0, 0))
            
            # Game Over text
            game_over_text = self.font_large.render("GAME OVER", True, COLOR_GAME_OVER)
            game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 60))
            self.screen.blit(game_over_text, game_over_rect)
            
            # Final score
            final_score_text = self.font_medium.render(f"Final Score: {self.score}", True, COLOR_SCORE)
            final_score_rect = final_score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 10))
            self.screen.blit(final_score_text, final_score_rect)
            
            # Restart instruction
            restart_text = self.font_small.render("Press SPACE to Restart", True, COLOR_SCORE)
            restart_rect = restart_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 70))
            self.screen.blit(restart_text, restart_rect)
        
        pygame.display.flip()
    
    def restart_game(self):
        """Reset game to initial state"""
        self.snake.reset()
        self.food.randomize_position(self.snake.positions)
        self.score = 0
        self.game_over = False
    
    def run(self):
        """Main game loop"""
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()


def main():
    """Entry point for the game"""
    game = SnakeGame()
    game.run()


if __name__ == "__main__":
    main()
