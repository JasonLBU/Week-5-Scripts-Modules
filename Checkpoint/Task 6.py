# Task 6
import statistics

def Rainfall():
    MonthlyRain = []
    Months = ['January','February','March','April', 'May','June','July','August','September','October','November','December']
    for i in range(0, 12):
        Rainfall = int(input("Enter rainfall for " + "".join(Months[i]) + ": "))
        MonthlyRain.append(Rainfall)
    print(MonthlyRain)
    print()
    return MonthlyRain

def CalculateAverage(List):
    Months = ['January','February','March','April', 'May','June','July','August','September','October','November','December']

    Average = sum(List) / float(len(List))
    Standard_Deviation = statistics.stdev(List)
    Max_Value = max(List)
    MaxMonth = Months[List.index(Max_Value)]
    Min_Value = min(List)
    MinMonth = Months[List.index(Min_Value)]

    print("Max Rainfall: ", str(Max_Value) + "mm in ", MaxMonth)
    print("Min Rainfall: ", str(min(List)) + "mm in ", MinMonth)
    print()
    print("Average: ",  str(Average) + "mm")
    print("Standard DeviationL: ", str(Standard_Deviation) + "mm")

CalculateAverage(Rainfall())