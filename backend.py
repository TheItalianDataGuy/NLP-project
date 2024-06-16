import glob
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Get list of files
diaries = glob.glob("diary/*.txt")

# Extract dates from names' files
date = [dates.removeprefix(f"diary\\").removesuffix(".txt") for dates in diaries]


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
score = [analyzer.polarity_scores(text) for text in d]

# Extract the positivity and negativity scores from the dictionary in the list score
positivity = [dict["pos"] for dict in score]
negativity = [dict["neg"] for dict in score]

print(date)
print(positivity)
print(negativity)
