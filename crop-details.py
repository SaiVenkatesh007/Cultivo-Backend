import pandas as pd 

# Picking the recommended conditions for the asked crop
df = pd.read_csv("data\Crop_recommendation.csv")

x = input("Give input: ").lower()
dfMean = df[df['label']==x].describe().loc['mean']

nValue = dfMean.loc['N']
pValue = dfMean.loc['P']
kValue = dfMean.loc['K']
temp = dfMean.loc['temperature']
humid = dfMean.loc['humidity']
phValue = dfMean.loc['ph']
rain = dfMean.loc['rainfall']

print(f"For {x} the recommended conditions are: \nN = {nValue}\nP = {pValue}\nK = {kValue}\nTemperature = {temp}\nHumidity = {humid}\npH = {phValue}\nRainfall = {rain}")
