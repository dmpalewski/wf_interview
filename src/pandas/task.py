from pathlib import Path
from typing import Any
import pandas as pd


DEFAULT_DATA_SOURCE = Path(__file__).parents[2] / "data" / "students_100.csv"


def analyze_previous_class_influence(data: pd.DataFrame, target_class: str) -> Any:
    # WRITE YOUR CODE HERE
    raise NotImplementedError


if __name__ == "__main__":
    target_class = "math"
    # WRITE YOUR CODE HERE
    data = ... # create a DataFrame form the .csv file
    res = analyze_previous_class_influence(data=data, target_class=target_class)
    print(res)
