import pandas as pd
import matplotlib.pyplot as plt


csvFile = 'all_seasons.csv'
nba = pd.read_csv(csvFile)
print(nba)

age_mean = nba["age"].mean()

print("The average age of a player in all seasons since 1996 is", age_mean)

points_mean = nba["pts"].mean()

print("The average total points of a player in all seasons since 1996 is", points_mean)

x = nba['age']
y = nba['pts']

plt.scatter(x, y)

plt.xlabel('Age')
plt.ylabel('Points')

plt.title('Age vs Points Scatter Plot')

plt.show()

#nba.info()

