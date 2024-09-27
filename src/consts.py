import yaml
from pathlib import Path
from typing import Dict

import logging
logger = logging.getLogger(__name__)


# Load configuration from YAML
config_path = Path(__file__).resolve().parents[1] / ".config" / "config.yaml"
try:
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
except FileNotFoundError:
    logger.exception(f"Configuration file not found at {config_path}")
    raise SystemExit(0)

# Extract window configuration
WINDOW_WIDTH: str = config['window']['width']
WINDOW_HEIGHT: str = config['window']['height']
WINDOW_TITLE: str = config['window']['title']

# FPS
FPS: str = config['fps']

# Extract board configuration
BOARD_WIDTH: str = config['board']['width']
BOARD_HEIGHT: str = config['board']['height']
SQUARE_SIZE: str = BOARD_WIDTH // 8

# Extract square colors
DARK_SQUARE_COLOR: str = config['colors']['dark_square_color']
LIGHT_SQUARE_COLOR: str = config['colors']['light_square_color']
SELECTED_SQUARE_COLOR: str = config['colors']['selected_square_color']
VALID_SQUARE_COLOR: str = config['colors']['valid_square_color']

VALID_SQUARE_DOT_RADIUS: str = config['valid_square_dot_radius']

# Extract piece configuration
PIECES_TO_NAMES: Dict[str, str] = config['pieces_to_names']
NAMES_TO_PIECES: Dict[str, str] = {v: k for k, v in PIECES_TO_NAMES.items()}

# FEN string for the starting position
STARTING_POSITION: str = config['fen']['start']
EXAMPLE_POSITION: str = config['fen']['example']