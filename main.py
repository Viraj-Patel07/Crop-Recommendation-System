import Data
import Costs

# Frm data
farm = Data.farm_data.copy()
mph = Data.min_farm_PH.copy()
maph = Data.max_farm_PH.copy()

# Crop data
crops = Data.Crop.copy()
plant_req_soil = Data.plant_soil_type.copy()
mcph = Data.min_ph.copy()
macph = Data.max_ph.copy()

# cost data
inputs = Costs.Input_cost.copy()
In_t = Costs.Tillage_Interculture_cost.copy()
Irr = Costs.Irrigation_Cost.copy()
Harv = Costs.Harvesting_cost.copy()
Oth = Costs.Other_costs.copy()

id = int(input("Enter farm id from 1 to 50 : "))

req = []
for key, value in farm.items():
    if id == key:
        for i in value:
            r eq.append(i)
    print(req)

s = req[2]

print("The farm with id You entered has following data:\n"
      "Minimum pH : {}\n"
      "Maximum pH : {}\n"
      "Soil type : {}\n".format(req[0],req[1],req[2]))

# extracting matching crop with user input soil type
recd_crops = []
ind = []
for index, member in enumerate(plant_req_soil):
    if req[2] in member:
        recd_crops.append(crops[index])
        ind.append(index)

# Removing duplicates
rec_crops = list(set(recd_crops))
ind_f = list(set(ind))

# Create a list of lists
list_of_lists = [inputs, In_t, Irr, Harv, Oth]

# Zip the lists together
zipped_list = zip(*list_of_lists)

# create list of lists from zipped list of tuples
crop_cost = []
for i in zipped_list:
    crop_cost.append(list(i))

# create crop wise total cost list from list of lists
total_cost_list = []
for j in crop_cost:
    total_cost_list.append(sum(j))

# creating dictionary of crops with crop name as key and its total cost as value
total_crop_wise_cost = {s: v for s, v in zip(crops, total_cost_list)}

# Separating total cost of recommended crop from list
rec_cost = []
for r in ind_f:
    rec_cost.append(total_cost_list[r])

rec_Crop_cost = {c: d for c, d in zip(rec_crops, rec_cost)}

area = float(input("Enter your farm area in acre : "))

print("We recommend you crops listed below for your farm :\n",
      rec_crops)

print("Per acre cultivation cost of those crops are as per below in respective order :\n",
      rec_Crop_cost)

total_rec_cost = Data.cost(rec_cost, area)

total_cult_cost = {p: q for p, q in zip(rec_crops, total_rec_cost)}

print("Total cost for your whole farm is as below reapective to your recomanded crop list :\n",
      total_cult_cost)