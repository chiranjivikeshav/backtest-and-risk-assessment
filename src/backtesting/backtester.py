# Implementing a rolling backtesting approach with a sliding window training strategy

import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import joblib

# Load the trained model & scaler
model = load_model("../../models/lstm_model.h5")
scaler = joblib.load("../../models/scaler.pkl")

# Load test data
X_test = np.load("../../data/X_test.npy")
Y_test = np.load("../../data/Y_test.npy")

# Parameters for rolling window
test_window_size = 100   
step_size = 100          

# Backtesting loop
results = []
for t in range(0, len(X_test) - test_window_size, step_size):
    # Select rolling test window
    X_window = X_test[t:t+test_window_size]
    Y_actual = Y_test[t:t+test_window_size]

    # Predict future values
    Y_pred = model.predict(X_window)

    # Inverse transform predictions & actual values
    Y_pred = scaler.inverse_transform(Y_pred)
    Y_actual = scaler.inverse_transform(Y_actual)

    # Compute Returns
    df = pd.DataFrame({"Actual": Y_actual.flatten(), "Predicted": Y_pred.flatten()})
    df["Return_Actual"] = df["Actual"].pct_change()
    df["Return_Predicted"] = df["Predicted"].pct_change()

    # Compute Strategy Performance
    df["Strategy_Return"] = df["Return_Predicted"] * df["Return_Actual"].shift(-1)

    # Compute Metrics
    total_return = df["Strategy_Return"].sum()
    mse = np.mean((df["Predicted"] - df["Actual"])**2)

    results.append({"Start": t, "End": t+test_window_size, "Total_Return": total_return, "MSE": mse})

    print(f"Backtest {t}-{t+test_window_size}: Return={total_return:.4f}, MSE={mse:.4f}")

# Convert results to DataFrame
results_df = pd.DataFrame(results)
results_df.to_csv("backtest_results.csv", index=False)

print("Backtesting Complete! Results saved to backtest_results.csv")
