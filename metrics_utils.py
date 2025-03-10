import pandas as pd
from sklearn.metrics import f1_score,precision_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def calculate_metrics(df):
    # Ensure correct data types
    df["classification"] = df["classification"].astype(str)
    df["groundtruth"] = df["groundtruth"].astype(str)

    # Calculate F1 score and precision
    f1 = f1_score(df["groundtruth"], df["classification"], average="weighted")
    precision = precision_score(df["groundtruth"], df["classification"], average="weighted")

    print(f"F1 Score: {f1:.4f}")
    print(f"Precision: {precision:.4f}")
        # Compute confusion matrix
    cm = confusion_matrix(df["groundtruth"], df["classification"], labels=df["groundtruth"].unique())

    # Plot confusion matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=df["groundtruth"].unique(), yticklabels=df["groundtruth"].unique())
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")

    # Save the confusion matrix as an image
    plt.savefig("images/confusion_matrix.png")
    #plt.show()