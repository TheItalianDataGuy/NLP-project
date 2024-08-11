# Sentiment Analysis of a Diary

This project performs sentiment analysis on a series of diary entries, visualizing the levels of positivity and negativity over time. It uses Streamlit for the frontend interface and NLTK's Sentiment Intensity Analyzer for sentiment analysis.

## Features

- **Date Extraction**: Automatically extracts dates from diary entry filenames.
- **Sentiment Analysis**: Analyzes the sentiment of each diary entry using NLTK's VADER (Valence Aware Dictionary and sEntiment Reasoner).
- **Data Visualization**: Plots the positivity and negativity scores over time using Plotly.

## Project Structure

```plaintext
.
├── diary/                  # Folder containing diary entries as text files
│   ├── 2023-01-01.txt      # Example diary file
│   ├── 2023-01-02.txt      # Example diary file
│   └── ...
├── backend.py              # Script for processing and analyzing diary entries
├── frontend.py             # Streamlit app to visualize the sentiment analysis
└── README.md               # Project documentation
```

## Requirements
- Python 3.8+
- Streamlit
- Plotly
- NLTK

## Installation
1. Clone the repository:

  ```bash
  
  git clone https://github.com/yourusername/diary-sentiment-analysis.git
  cd diary-sentiment-analysis
  ```

2. Install the required packages:

  ```bash
  pip install -r requirements.txt
  ```

3. Download the necessary NLTK data:

  ```bash
  import nltk
  nltk.download('vader_lexicon')
  ```

## Usage
1. Add Diary Entries: Add your diary text files in the diary/ folder. The filename should be in the format YYYY-MM-DD.txt.
2. Run the Backend: The backend processes the diary entries and extracts sentiment data.

  ```bash
  backend.py
  ```
3. Run the Frontend: Launch the Streamlit app to visualize the sentiment analysis.

  ```bash
  streamlit run frontend.py
  ```
4. View the Results: Open the Streamlit app in your browser to see the positivity and negativity trends over time.

## Example
If you have diary entries named 2023-01-01.txt, 2023-01-02.txt, etc., the app will extract the dates, analyze the sentiment, and display line charts showing how positivity and negativity change over the specified period.

## License
This project is licensed under the MIT License.

## Acknowledgments
- Streamlit
- Plotly
- NLTK
