import pandas

# data =pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
#
# # print(temp_list)
# # print(data["temp"].mean())
# # print(data["temp"].max())
# #
# # #get data in columns
# # # print(data["condition"])
# # print(data.condition)
# #print
# # #Get Data in Row
# #
# # print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# mondayfahr = (monday.temp * 9/5)+32
# print(mondayfahr)
#
#
# data_dict = {
#     ""
# }

#ID / Fur color / Count

data = pandas.read_csv("squirreldata.csv")
df = pandas.DataFrame(data)
# furcolor = df["Primary Fur Color"]
# gray = (furcolor == "Gray")
# cinnamon = (furcolor == "Cinnamon")
# black = (furcolor == "Black")
#
# x = data[data["Primary Fur Color"] == "Black"].count()
gray = (df["Primary Fur Color"].str.contains("Gray").sum())
cinnamon = (df["Primary Fur Color"].str.contains("Cinnamon").sum())
black = (df["Primary Fur Color"].str.contains("Black").sum())

columns = ["Primary Fur Color", "Amount"]
newdata = [("Gray",gray),("Cinnamon",cinnamon),("Black",black)]
nowydb = pandas.DataFrame(newdata, columns=columns)

nowydb.to_csv("Squirrel_Fur")


print(nowydb)


