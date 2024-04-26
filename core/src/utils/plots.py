import matplotlib.pyplot as plt
from tabulate import tabulate


def plot_loss_and_metrics(history, metrics_history, SLICE_START=10):
    plt.plot(history["train_loss"][SLICE_START:], label="train loss")
    plt.plot(history["test_loss"][SLICE_START:], label="test loss")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.show()

    plt.plot(metrics_history["train_mae"][SLICE_START:], label="train mae")
    plt.plot(metrics_history["test_mae"][SLICE_START:], label="test mae")
    plt.xlabel("Epoch")
    plt.ylabel("MAE")
    plt.legend()
    plt.show()

    plt.plot(metrics_history["train_rmse"][SLICE_START:], label="train rmse")
    plt.plot(metrics_history["test_rmse"][SLICE_START:], label="test rmse")
    plt.xlabel("Epoch")
    plt.ylabel("RMSE")
    plt.legend()
    plt.show()

    plt.plot(metrics_history["train_r2"][SLICE_START:], label="train r2")
    plt.plot(metrics_history["test_r2"][SLICE_START:], label="test r2")
    plt.xlabel("Epoch")
    plt.ylabel("R2")
    plt.legend()
    plt.show()

    plt.plot(metrics_history["train_mse"][SLICE_START:], label="train mse")
    plt.plot(metrics_history["test_mse"][SLICE_START:], label="test mse")
    plt.xlabel("Epoch")
    plt.ylabel("MSE")
    plt.legend()
    plt.show()


def print_metrics_table(metrics_history):
    headers = ["Epoch", "MAE", "RMSE", "R2", "MSE"]

    # Prepare train data
    train_data = [
        [
            len(metrics_history["train_mae"]) - 1,
            f"{metrics_history['train_mae'][-1]:.5f}",
            f"{metrics_history['train_rmse'][-1]:.5f}",
            f"{metrics_history['train_r2'][-1]:.5f}",
            f"{metrics_history['train_mse'][-1]:.5f}",
        ]
    ]

    # Prepare test data
    test_data = [
        [
            len(metrics_history["test_mae"]) - 1,
            f"{metrics_history['test_mae'][-1]:.5f}",
            f"{metrics_history['test_rmse'][-1]:.5f}",
            f"{metrics_history['test_r2'][-1]:.5f}",
            f"{metrics_history['test_mse'][-1]:.5f}",
        ]
    ]

    # Print train metrics table
    print("Train Metrics")
    print(tabulate(train_data, headers=headers, tablefmt="grid"))

    # Print test metrics table
    print("\nTest Metrics")
    print(tabulate(test_data, headers=headers, tablefmt="grid"))
