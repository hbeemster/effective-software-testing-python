"""Estimate Dataclass to represent an estimate."""
from dataclasses import dataclass


@dataclass
class Estimate:
    developer: str
    estimate: int
