study=float(input("enter the time of study:"))
savings=float(input("enter the amount of time saved:"))
print(study,savings)
if savings>30 and study>4:
    print("excellent day")
elif savings<10 or study<2:
    print("poor day")
else:
    print("normal day")