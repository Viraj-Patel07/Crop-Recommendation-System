import pandas as pd

df3 = pd.read_csv("operation_costs2.csv")

Input_cost = df3["Input_costs"].tolist()
Tillage_Interculture_cost = df3["Tillage_Interculture_cost"].tolist()
Irrigation_Cost = df3["Irrigation_cost"].tolist()
Harvesting_cost = df3["Harvesting_Cost"].tolist()
Other_costs = df3["Other_costs"].tolist()
Yield = df3["Yield"].tolist()
