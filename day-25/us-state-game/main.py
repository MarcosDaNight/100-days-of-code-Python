import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

data_list = data["temp"].to_list()
print(data_list)

average = (sum(data_list)) // len(data_list)
pandas_average = data["temp"].mean()
max_temperature = data["temp"].max()

print(f"The temperature average is {average}\nThe highest temperature is {max_temperature}")

# Get Data in Columns
print(data["condition"])
print(data.condition)

# Get data in Row
print(data[data.day == "Monday"])

# Create a DataFrame from scratch

data_dict = {
    "students": ["Amy", "Max", "Liza"],
    "scores": [56, 89, 92]
}
dataFrame = pandas.DataFrame(data_dict)
dataFrame.to_csv("new_data.csv")