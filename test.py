import gradio as gd
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ollama

print("All Installed Successfully")

# Load Titanice dataset
# url = r"D:\DS_PRACTICE\22-05-2026\titanic_ dataset_final.csv"
df = pd.read_csv(r"D:\DS_PRACTICE\22-05-2026\titanic_ dataset_final.csv")
df
df.describe
print("missing values",df.isnull().sum())