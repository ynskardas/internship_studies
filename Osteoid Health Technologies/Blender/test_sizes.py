import pandas as pd
i = 46
while i < 91:
    filename = "obj_"+ str(i) +"_land.csv"
    data = pd.read_csv(filename)
    if len(data)+1 != 12:
        print(i,": ",len(data)+1)
    i = i + 1