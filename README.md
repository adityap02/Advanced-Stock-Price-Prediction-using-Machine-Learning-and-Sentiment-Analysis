# Advanced Stock Price Prediction using Machine Learning and Sentiment Analysis

## Introduction
This project integrates Machine Learning (ML) and Sentiment Analysis to predict stock prices. It leverages Python for analyzing stock data and sentiment from various sources to forecast market trends.

## Features
- **ML-Based Prediction**: Utilizes machine learning models for accurate stock price forecasting.
- **Sentiment Analysis**: Incorporates sentiment analysis to understand market opinions, using `textblob_analysis.py` and `sentiment.py`.
- **Comprehensive Data Analysis**: Employs `main.py` for orchestrating data collection, analysis, and prediction processes.

## Technologies
- Python
- Libraries: pandas, NumPy, scikit-learn, TextBlob

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/adityap02/Stock-Price-Prediction-Using-ML-and-Sentimental-Analysis.git
   ```
2. Install required Python packages:
   ```
   pip install pandas numpy scikit-learn textblob
   ```

## Usage
- Run `main.py` to start the analysis.
- The scripts will process stock data and apply sentiment analysis for predictions.

## Code Structure
- `sentiment.py`: Handles sentiment analysis of market news.
- `textblob_analysis.py`: Utilizes TextBlob for processing and analyzing textual data.
- `main.py`: Main script coordinating data processing and predictions.

## How It Works
- **Data Collection**: Gathers stock data and relevant news articles.
- **Sentiment Analysis**: Analyzes news sentiment to understand market mood.
- **Stock Price Prediction**: ML models predict future stock prices based on historical data and sentiment scores.

## Contributing
Contributions to improve this project are highly appreciated. Please refer to [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## License
This project is licensed under the MIT License - see [LICENSE.md](LICENSE.md) for details.

## Acknowledgments
- Financial data sources
- Open-source Python libraries
- Community contributors
