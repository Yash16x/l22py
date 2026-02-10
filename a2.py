students=["Yash","Ahmed","Peter","Jordan","Mutvel"]
roll=[1,2,3,4,5]
marks=[90,80,70,60,56]
dict1={students:marks for students, roll, marks in
zip(students, roll,marks)}
print(dict1)