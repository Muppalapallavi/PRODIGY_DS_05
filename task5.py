import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Weather": ["Clear", "Rainy", "Foggy", "Rainy", "Clear", "Foggy"],
    "Time": ["Morning", "Night", "Evening", "Morning", "Night", "Evening"],
    "Accidents": [15, 30, 20, 25, 10, 18]
}
df = pd.DataFrame(data)
weather_accidents = df.groupby("Weather")["Accidents"].sum()
plt.bar(weather_accidents.index, weather_accidents.values)
plt.title("Accidents by Weather Condition")
plt.xlabel("Weather")
plt.ylabel("Number of Accidents")
plt.show()
print(weather_accidents)