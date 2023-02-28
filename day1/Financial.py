Year = int(input("Enter The Year: "))
Month = int(input("Enter The Month: "))
if(Month > 4) :
    financial_Year = str(Year) + "-" + str(Year+1)
else:
    financial_Year = str(Year-1) + "-" + str(Year)

print("The Financial year is", financial_Year)
