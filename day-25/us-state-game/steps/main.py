import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# data_list = data["temp"].to_list()
# print(data_list)
#
# average = (sum(data_list)) // len(data_list)
# pandas_average = data["temp"].mean()
# max_temperature = data["temp"].max()
#
# print(f"The temperature average is {average}\nThe highest temperature is {max_temperature}")
#
# # Get Data in Columns
# print(data["condition"])
# print(data.condition)
#
# # Get data in Row
# print(data[data.day == "Monday"])
#
# # Create a DataFrame from scratch
#
# data_dict = {
#     "students": ["Amy", "Max", "Liza"],
#     "scores": [56, 89, 92]
# }
# dataFrame = pandas.DataFrame(data_dict)
# dataFrame.to_csv("new_data.csv")

data_frame = pandas.read_csv("2018-squirrel_count.csv")
gray = 0
cinnamon = 0
black = 0

for color in data_frame["Primary Fur Color"]:
    if color == "Gray":
        gray += 1
    elif color == "Cinnamon":
        cinnamon += 1
    elif color == "Black":
        black += 1

squirrel_dict = {
    "Four Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}
squirrel_data_frame = pandas.DataFrame(squirrel_dict)
squirrel_data_frame.to_csv("squirrel_count.csv")