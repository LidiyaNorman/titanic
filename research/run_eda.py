import os
import pathlib

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_categorical_feature_statistics(data, col, title):
    """
    Plot the statistics of a categorical feature, absolute and normalized values.

    Parameters
    ----------
    data: pandas DataFrame
        Data table
    col: str
        Categorical column name from data
    title: str
        Title for the graphs
    Returns
    -------
    """
    f, ax = plt.subplots(1, 2, figsize=(18, 8))
    data[col].value_counts().plot.pie(
        explode=[0, 0.1], autopct="%1.1f%%", ax=ax[0], shadow=True)
    ax[0].set_title(title)
    ax[0].set_ylabel("")
    sns.countplot(x=col, data=data, ax=ax[1])
    ax[1].set_title(title)
    plt.show()


def plot_stats_of_2_features(data, col1, col2, title):
    """
    Multivariate statistics for 2 features

    Parameters
    ----------
    data: pandas DataFrame
        Data table
    col1: str
        The first categorical column name from data
    col2: str
        The second categorical column name from data
    title: str
        Title for the graphs

    Returns
    -------

    """
    f, ax = plt.subplots(1, 2, figsize=(18, 8))
    data[[col1, col2]].groupby([col1]).mean().plot.bar(ax=ax[0])
    ax[0].set_title(f"{col2} vs {col1}")
    sns.countplot(x=col1, hue=col2, data=data, ax=ax[1])
    ax[1].set_title(title)
    plt.show()


def main():
    plt.rcParams['font.size'] = 20
    abs_path = pathlib.Path(__file__).parent.parent
    data = pd.read_csv(os.path.join(abs_path, "data", "train.csv"))

    plot_categorical_feature_statistics(data, "Survived", "Survived")
    plot_stats_of_2_features(data, "Sex", "Survived", "Sex:Survived vs Dead")
    return data


if __name__ == "__main__":
    data = main()
