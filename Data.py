import pandas as pd

# data reading
df1 = pd.read_csv("Crop_Data2.csv")
df2 = pd.read_csv("Farm_Data.csv")

# Crop data
N = df1["N"].tolist()
P = df1["P"].tolist()
K = df1["K"].tolist()
max_temp = df1["max_temp"].tolist()
min_temp = df1["min_temp"].tolist()
max_hum = df1["max_humidity"].tolist()
min_hum = df1["min_humidity"].tolist()
max_ph = df1["max_ph"].tolist()
min_ph = df1["min_ph"].tolist()
max_water = df1["max_water"].tolist()
min_water = df1["min_water"].tolist()
soil_type = df1["soil_type"].tolist()
Crop = df1["crop"].tolist()

# Farm data
Farm_ID = df2["Farm_ID"].tolist()
min_farm_PH = df2["Min_PH"].tolist()
max_farm_PH = df2["Max_PH"].tolist()
Farm_Soil_type = df2["Soil_Type"].tolist()

# data manipulation
soil_crop = {i: j.split(",") for i, j in zip(Crop, soil_type)}
print(soil_crop)

# list of list of all crop soil type

plant_soil_type = []
for key, value in soil_crop.items():
    plant_soil_type.append(value)
print(plant_soil_type)

raw = []
for a, b, c in zip(min_farm_PH, max_farm_PH, Farm_Soil_type):
    raw.append([a, b, c])
farm_data = {p: q for p, q in zip(Farm_ID, raw)}
print(farm_data)

def cost(rec_cost, area):
    total_rec_cost = []
    for i in rec_cost:
        total_rec_cost.append(int(i) * area)
    return total_rec_cost