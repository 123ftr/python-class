#if elif else statement
unit1=int (input("enter marks for first unit"))
unit2=int (input("enter marks for second unit"))
unit3=int (input("enter marks for third unit"))
unit4=int (input("enter marks for fourth unit"))
unit5=int (input("enter marks for fifth unit"))
marks=((unit1+unit2+unit3+unit4+unit5) /5)  
if marks>=70 <100:
 print("grAde A")
elif marks>=60 <70:
 print("grAde B")
elif marks>=50 <60:
 print("grAde C")
elif marks>=40 <50:
 print("grAde D")
elif marks>=0 <400:
 print("FAIL")
elif marks>100:
 print("impossible")
elif marks <0:
 print("null") 
else:
  print("")