import pygame as pg
from pathlib import Path


def play_effect(effect_name: str) -> None:
    effect = pg.mixer.Sound(str(Path(__file__).resolve().parents[1] / "assets" / "audio" / f"{effect_name}.mp3"))
    effect.play(0)

