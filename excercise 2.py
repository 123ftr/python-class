john=int(input("enter height for john: "))
mary=int(input("enter height for mary: "))
frank=int(input("enter height for frank: "))
if john> mary and frank:
  print("john",john)
if mary> john and frank:
  print("mary", mary)
if frank> john and mary:
  print("frank",frank)