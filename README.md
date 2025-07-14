# AI Data Analyst

This web application allows you to upload a CSV file and interact with an AI agent powered by Google's Gemini Pro model to analyze and visualize your data.

## Features

-   **Natural Language Interaction**: Ask questions about your data in Natural Language.
-   **Data Visualization**: Generate plots and charts on the fly.
-   **Powered by Gemini Pro**: Leverages Google's state-of-the-art language model for insightful analysis.
-   **Secure**: Your API key is stored securely in a `.env` file.
-   **Modular Architecture**: The code is organized into logical modules for better maintainability.

## How it Works

The application functions as follows:
1.  **Data Upload:** Users upload a CSV file through the Streamlit web interface.
2.  **Agent Initialization:** The `app.py` script initializes the LangChain agent, utilizing `agent_handler.py` to configure the agent with Google's Gemini Pro model.
3.  **Natural Language Querying:** Users can ask questions about their data in plain English.
4.  **Data Analysis & Visualization:** The AI agent processes these queries, performs analysis, and generates visualizations (charts, plots) using components defined in `ui_components.py`.
5.  **Output Display:** The results of the analysis and visualizations are presented back to the user within the Streamlit application.

## Project Structure

```
├── .gitignore
├── .env
├── app.py              # Main entry point of the Streamlit application.
├── agent_handler.py    # Module for creating and managing the LangChain agent.
├── requirements.txt    # Lists all project dependencies.
├── README.md           # Project documentation.
├── sample_dataset.csv  # Sample dataset for demonstration.
├── ui_components.py    # Module for creating reusable Streamlit UI components.
├── utils.py            # Module for utility functions.
└── assets/             # Directory for static assets like CSS and images.
    └── style.css       # Custom CSS for styling the application.
```

## 🚀 Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/kamaliramin/conversational-csv-analyst.git
    ```

1.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Create a `.env` file:**
    Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey) and add it to a new file named `.env`:
    ```
    GOOGLE_API_KEY="your-key-here"
    ```

4.  **Run the app:**
    ```bash
    streamlit run app.py
