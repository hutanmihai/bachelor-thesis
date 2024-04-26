import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def compute_metrics(predictions, ground_truths):
    mae = mean_absolute_error(ground_truths, predictions)
    mse = mean_squared_error(ground_truths, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(ground_truths, predictions)

    return {"MAE": mae, "MSE": mse, "RMSE": rmse, "R2": r2}
