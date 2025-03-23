# classify sentiment score as positive, neutral, negative
# If score if positive 1, negative -1, neutral 0
# Function to classify sentiment
def classify_sentiment(score):
    if score > 0:
        return 1  # Positive
    elif score < 0:
        return -1  # Negative
    else:
        return 0  # Neutral

# classify Market Cap into categories
# Function to classify Market Cap into categories
def classify_market_cap(market_cap):
    if market_cap > 200e9:
        return 'Mega'
    elif 10e9 <= market_cap <= 200e9:
        return 'Large'
    elif 2e9 <= market_cap < 10e9:
        return 'Medium'
    elif 300e6 <= market_cap < 2e9:
        return 'Small'
    elif 50e6 <= market_cap < 300e6:
        return 'Micro'
    else:
        return 'Nano'

def extract_headlines_per_ticker(df1, ticker):
  '''
  Function to extract all headlines from news articles based on ticker
  '''
  df = df1.copy()
  all_headlines = df[df['stock'] == ticker]['headline'].tolist()
  return all_headlines

def classify_recommendation(score):
    if score >= 0.5:
        return "Buy"
    elif score <= -0.5:
        return "Sell"
    else:
        return "Hold"