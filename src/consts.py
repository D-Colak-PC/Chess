import yaml
from pathlib import Path
import logging
logger = logging.getLogger('main')

# Load configuration from YAML
config_path = Path(__file__).resolve().parents[1] / "config.yaml"
try:
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
except FileNotFoundError:
    print(f"Configuration file not found at {config_path}")
    raise SystemExit(0)

# Extract window configuration
WINDOW_WIDTH = config['window']['width']
WINDOW_HEIGHT = config['window']['height']
WINDOW_TITLE = config['window']['title']

# FPS
FPS = config['fps']

# Extract board configuration
BOARD_WIDTH = config['board']['width']
BOARD_HEIGHT = config['board']['height']
SQUARE_SIZE = BOARD_WIDTH // 8

# Extract square colors
DARK_SQUARE_COLOR = config['colors']['dark_square_color']
LIGHT_SQUARE_COLOR = config['colors']['light_square_color']
SELECTED_SQUARE_COLOR = config['colors']['selected_square_color']
VALID_SQUARE_COLOR = config['colors']['valid_square_color']

VALID_SQUARE_DOT_RADIUS = config['valid_square_dot_radius']

# Extract piece configuration
PIECES_TO_NAMES = config['pieces_to_names']
NAMES_TO_PIECES = {v: k for k, v in PIECES_TO_NAMES.items()}

# FEN string for the starting position
STARTING_POSITION = config['fen']['start']
EXAMPLE_POSITION = config['fen']['example']