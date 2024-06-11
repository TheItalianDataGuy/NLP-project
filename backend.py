import glob
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Get list of files
diaries = glob.glob("diary/*.txt")

# Create an empty list where to put the content of the files
d = []

# For loop to append teh content of the files in the list.
for diary in diaries:
    if diary.endswith(".txt"):
        with open(diary, "r") as files:
            content = files.read().strip()
            d.append(content)

# Create an instance of SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Analyse the content of each files
for text in d:
    score = analyzer.polarity_scores(text)
    print(score)


