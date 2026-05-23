import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ollama

# Function to Generate AI Insights
def generate_ai_insights(df_summary):

    prompt = f"""
Analyze the dataset summary and provide useful insights:

{df_summary}
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


# Function to Generate Visualizations
def generate_visualizations(df):

    plot_paths = []

    # Histograms
    for col in df.select_dtypes(include=['number']).columns:

        plt.figure(figsize=(6, 4))

        sns.histplot(df[col], bins=30, kde=True, color="blue")

        plt.title(f"Distribution of {col}")

        path = f"{col}_distribution.png"

        plt.savefig(path)

        plot_paths.append(path)

        plt.close()

    # Correlation Heatmap
    numeric_df = df.select_dtypes(include=['number'])

    if not numeric_df.empty:

        plt.figure(figsize=(8, 5))

        sns.heatmap(
            numeric_df.corr(),
            annot=True,
            cmap='coolwarm',
            fmt=".2f",
            linewidths=0.5
        )

        plt.title("Correlation Heatmap")

        path = "correlation_heatmap.png"

        plt.savefig(path)

        plot_paths.append(path)

        plt.close()

    return plot_paths


# Main EDA Function
def eda_analysis(file_path):

    # Load CSV
    df = pd.read_csv(file_path)

    # Fill missing numeric values
    for col in df.select_dtypes(include=['number']).columns:
        df[col] = df[col].fillna(df[col].mean())

    # Fill missing categorical values
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    # Summary
    summary = df.describe(include='all').to_string()

    # Missing values report
    missing_values = df.isnull().sum().to_string()

    # AI insights
    insights = generate_ai_insights(summary)

    # Generate plots
    plot_paths = generate_visualizations(df)

    report = f"""
Data Loaded Successfully!

========================
SUMMARY
========================

{summary}

========================
MISSING VALUES
========================

{missing_values}

========================
AI INSIGHTS
========================

{insights}
"""

    return report, plot_paths


# Gradio Interface
demo = gr.Interface(
    fn=eda_analysis,
    inputs=gr.File(type="filepath"),
    outputs=[
        gr.Textbox(label="EDA Report"),
        gr.Gallery(label="Data Visualizations")
    ],
    title="📊 AI-Powered Exploratory Data Analysis",
    description="Upload a CSV file and get automated EDA insights with visualizations."
)

# Launch App
demo.launch(share=True)