"""Estimate Dataclass to represent an estimate."""
from dataclasses import dataclass


@dataclass
class Estimate:
    developer: str
    estimate: int

    def __eq__(self, other):
        return self.estimate == other.estimate

    def __lt__(self, other):
        return self.estimate < other.estimate
