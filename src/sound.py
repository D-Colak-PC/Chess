import pygame as pg
from pathlib import Path

import logging
logger = logging.getLogger(__name__)


def play_effect(effect_name: str) -> None:
    effect = pg.mixer.Sound(str(Path(__file__).resolve().parents[1] / "assets" / "audio" / f"{effect_name}.mp3"))
    effect.play(0)
    logger.debug(f"Played effect: {effect_name}") #? Logging

