# Variance & Standard Deviation
import statistics

team_A = [48, 49, 50, 51, 52]
team_B = [20, 35, 50, 65, 80]

mean_A = statistics.mean(team_A)
std_A = statistics.stdev(team_A)

mean_B = statistics.mean(team_B)
std_B = statistics.stdev(team_B)

print("Team A Mean:", mean_A)
print("Team A SD:", round(std_A, 2))

print("Team B Mean:", mean_B)
print("Team B SD:", round(std_B, 2))

if std_A < std_B:
    print("Team A is more consistent.")
else:
    print("Team B is more consistent.")