# Modern Snake Game 🐍

A classic Snake game implemented in Python with pygame, featuring modern design and smooth gameplay.

## Features

- **Modern Dark Theme**: Dark background with bright, contrasting colors for excellent visibility
- **Real-time Score Tracking**: Score updates instantly as you eat food
- **Smooth Controls**: Responsive arrow key controls
- **Collision Detection**: Game ends when snake hits walls or its own body
- **Restart Functionality**: Quick restart with spacebar after game over
- **Visual Enhancements**: Rounded corners, subtle grid, and distinct head/body colors

## Requirements

- Python 3.7 or higher
- pygame 2.5.0 or higher

## Installation

1. Clone the repository:
```bash
git clone https://github.com/napegadie/snakenew-game.git
cd snakenew-game
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Play

1. Run the game:
```bash
python snake_game.py
```

2. **Controls**:
   - **Arrow Keys**: Control snake direction (Up, Down, Left, Right)
   - **SPACE**: Restart game after game over
   - **ESC**: Quit game

3. **Objective**:
   - Eat the pink/red food to grow longer and increase your score
   - Each food gives you 10 points
   - Avoid hitting the walls or your own body
   - Try to get the highest score possible!

## Game Elements

- **Snake Head**: Bright blue color - this is where collisions are detected
- **Snake Body**: Bright cyan-green color - avoid running into it!
- **Food**: Bright pink-red color - eat this to grow and score points
- **Score**: Displayed in white at the top-left corner

## Design

The game features a modern aesthetic with:
- Dark blue-black background (20, 20, 30)
- Bright cyan-green snake body (0, 255, 150)
- Bright blue snake head (0, 200, 255)
- Bright pink-red food (255, 50, 100)
- Clean, rounded shapes for a polished look
- Subtle grid lines for visual guidance

## Technical Details

- **Grid Size**: 800x600 pixels divided into 20px grid cells
- **Frame Rate**: 10 FPS for classic snake game feel
- **Architecture**: Object-oriented design with Snake, Food, and SnakeGame classes

## License

This project is open source and available for educational purposes.