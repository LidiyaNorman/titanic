import os
import pathlib

import pandas as pd

from research.plot_funcs import (plot_stats_of_2_features,
                                 plot_categorical_feature_statistics)


def main():
    try:
        abs_path = pathlib.Path(__file__).parent.parent
    except NameError:
        abs_path = ""
    data = pd.read_csv(os.path.join(abs_path, "data", "train.csv"))

    plot_categorical_feature_statistics(data, col="Survived", title="Survived")
    plot_stats_of_2_features(data, col1="Sex", col2="Survived", title="Sex:Survived vs Dead")
    n_pass = data["PassengerId"].nunique()
    # print(f"PassengerId uniques: {n_pass}")
    return data


if __name__ == "__main__":
    data = main()
