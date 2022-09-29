# Exctract CSV file from web
# https://football-data.co.uk/englandm.php
import pandas as pd


# get data
test = pd.read_csv("https://football-data.co.uk/mmz4281/2223/E0.csv")

print(test)

# rename columns
test.rename(columns={'FTHG':'home_goals',
                     'FTAG':'away_goals'}, inplace=True)

print(test)
