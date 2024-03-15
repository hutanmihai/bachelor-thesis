import matplotlib.pyplot as plt
import missingno as msno
import numpy as np
import pandas as pd
import seaborn as sns

from core.src.constants import CSV_PATH, GRAPHS_PATH


def plot_price_distribution(df: pd.DataFrame) -> None:
    plt.figure(figsize=(12, 8))
    plt.hist(df["price"], bins=100, alpha=0.7, color="blue")
    plt.title("Price distribution")
    plt.xlabel("Price")
    plt.ylabel("Frequency")
    plt.savefig(GRAPHS_PATH / "price_distribution.png")
    plt.show()


def plot_year_distribution(df: pd.DataFrame) -> None:
    plt.figure(figsize=(12, 8))
    plt.hist(df["anul producției"], bins=100, alpha=0.7, color="blue")
    plt.title("Year distribution")
    plt.xlabel("Year")
    plt.ylabel("Frequency")
    plt.savefig(GRAPHS_PATH / "year_distribution.png")
    plt.show()


def plot_manufacturer_distribution(df: pd.DataFrame) -> None:
    plt.figure(figsize=(12, 8))
    plt.hist(df["marca"], bins=100, alpha=0.7, color="blue")
    plt.title("Manufacturer distribution")
    plt.xlabel("Manufacturer")
    plt.ylabel("Frequency")
    plt.savefig(GRAPHS_PATH / "manufacturer_distribution.png")
    plt.xticks(rotation=90)
    plt.show()


def plot_vehicle_type_distribution(df: pd.DataFrame) -> None:
    plt.figure(figsize=(12, 8))
    plt.hist(df["tip caroserie"], bins=100, alpha=0.7, color="blue")
    plt.title("Vehicle type distribution")
    plt.xlabel("Vehicle type")
    plt.ylabel("Frequency")
    plt.savefig(GRAPHS_PATH / "vehicle_type_distribution.png")
    plt.xticks(rotation=90)
    plt.show()


def plot_fuel_type_distribution(df: pd.DataFrame) -> None:
    plt.figure(figsize=(12, 8))
    plt.hist(df["combustibil"], bins=100, alpha=0.7, color="blue")
    plt.title("Fuel type distribution")
    plt.xlabel("Fuel type")
    plt.ylabel("Frequency")
    plt.savefig(GRAPHS_PATH / "fuel_type_distribution.png")
    plt.xticks(rotation=90)
    plt.show()


def plot_model_distribution(df: pd.DataFrame) -> None:
    plt.figure(figsize=(12, 8))
    plt.hist(df["model"], bins=100, alpha=0.7, color="blue")
    plt.title("Model distribution")
    plt.xlabel("Model")
    plt.ylabel("Frequency")
    plt.savefig(GRAPHS_PATH / "model_distribution.png")
    plt.xticks(rotation=90)
    plt.show()


def plot_transmission_distribution(df: pd.DataFrame) -> None:
    df["transmisie"] = df["transmisie"].astype(str)

    plt.figure(figsize=(12, 8))
    plt.hist(df["transmisie"], bins=100, alpha=0.7, color="blue")
    plt.title("Transmission distribution")
    plt.xlabel("Transmission")
    plt.ylabel("Frequency")
    plt.savefig(GRAPHS_PATH / "transmission_distribution.png")
    plt.show()


def plot_km_distribution(df: pd.DataFrame) -> None:
    df["km"] = df["km"].fillna("0").str.replace(" km", "").str.replace(" ", "").astype(float).astype(int)
    df["km_bins"] = pd.cut(df["km"], bins=np.arange(0, 500000, 10000))
    km_values = df["km_bins"].apply(lambda x: x.left)

    plt.figure(figsize=(12, 8))
    plt.hist(km_values, bins=100, alpha=0.7, color="blue")
    plt.title("Km distribution")
    plt.xlabel("Km")
    plt.ylabel("Frequency")
    plt.savefig(GRAPHS_PATH / "km_distribution.png")
    plt.show()


def plot_gearbox_distribution(df: pd.DataFrame) -> None:
    df["cutie de viteze"] = df["cutie de viteze"].astype(str)

    plt.figure(figsize=(12, 8))
    plt.hist(df["cutie de viteze"], bins=2, alpha=0.7, color="blue")
    plt.title("Gearbox distribution")
    plt.xlabel("Gearbox")
    plt.ylabel("Frequency")

    # Set tick labels to be unique values from the column
    plt.xticks(ticks=np.arange(len(df["cutie de viteze"].unique())), labels=df["cutie de viteze"].unique(), rotation=90)

    plt.savefig(GRAPHS_PATH / "gearbox_distribution.png")
    plt.show()


def plot_pollution_distribution(df: pd.DataFrame) -> None:
    df["norma de poluare"] = df["norma de poluare"].astype(str)

    plt.figure(figsize=(12, 8))
    sns.countplot(data=df, x="norma de poluare", palette="viridis")
    plt.title("Pollution distribution")
    plt.xticks(rotation=30)
    plt.savefig(GRAPHS_PATH / "pollution_distribution.png")
    plt.show()


if __name__ == "__main__":
    df = pd.read_csv(CSV_PATH)

    sns.set(rc={"figure.figsize": (20, 20)})

    # plot_price_distribution(df)
    # plot_year_distribution(df)
    # plot_manufacturer_distribution(df)
    # plot_vehicle_type_distribution(df)
    # plot_fuel_type_distribution(df)
    # plot_model_distribution(df)
    # plot_transmission_distribution(df)
    # plot_km_distribution(df)
    # plot_gearbox_distribution(df)
    # plot_pollution_distribution(df)

    msno.matrix(df, color=(0.2, 0.2, 0.2), figsize=(20, 20))
