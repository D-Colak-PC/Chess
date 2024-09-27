import yaml
import logging
import logging.config
from pathlib import Path 
from datetime import datetime   

def setup_logging():
    config_path = Path(__file__).resolve().parents[1] / ".config" / "logging_config.yaml"
    try:
        with open(config_path, 'r') as file:
            logging_config = yaml.safe_load(file)
    except FileNotFoundError:
        print(f"Configuration file not found at {config_path}")
        raise SystemExit(0)
    
    log_folder_path = Path(__file__).resolve().parents[1] / "logs"
    log_folder_path.mkdir(exist_ok=True)
    
    log_filename = log_folder_path / f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
    logging_config["handlers"]["file"]["filename"] = log_filename

    logging.config.dictConfig(logging_config)