print("Student Details");
print("----------------")
name=input("Name:")
print("upper:",name.upper())
phoneno=int(input("Phone"))
age=int(input("Age:"))
age_after5_years=age+5
marks=float(input("marks:"))
marks_rounded=int(marks)
if marks>=40:
    result="pass"
else:
    result="fail"
print("Age after 5 years:",age_after5_years)
print("Marks:",marks)
print("Marks_Rounded:",marks_rounded)
print("Result:",result)



