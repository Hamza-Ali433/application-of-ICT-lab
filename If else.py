marks=int(input("Enter your marks"))
if marks>=90:
    grade="A"  
elif marks >=75 and marks<90:
    grade="B"
elif marks >=50 and marks<75:
    grade="C" 
else: 
    grade="F"
print (grade)