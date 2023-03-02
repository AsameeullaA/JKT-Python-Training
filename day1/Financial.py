Year = int(input("Enter The Year: "))
Month = int(input("Enter The Month: "))
if(Month > 4) :
    financial_Year = str(Year) + "-" + str(Year+1)
    assesment_year = str(Year+1) + "-" + str(Year+2)
else:
    financial_Year = str(Year-1) + "-" + str(Year)
    assesment_year = str(Year) + "-" + str(Year+1)

print("The Financial year is", financial_Year)
print("The Assesment yeat is", assesment_year)
