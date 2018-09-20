#Velja upphafsstaðsetningu x og y
locationx, locationy = 1, 1
location = [locationx, locationy]

#Setja inn fall til að athuga í hvaða áttir má fara
message = "You can travel: "
if n==1:
    message += "(N)orth"
if e == 1 and n == 1:
    message += "or (E)ast"
elif e == 1 and n !=1:
    message +="(E)ast"
if s== 1 and (n==1 or e==1):
    message += "or (S)outh"
elif s == 1 and not (n==1 or e==1):
    message += "(S)outh"
if w == 1 and (n==1 or e==1 or s==1):
    message += "or (W)est"
elif w==1 and not (n==1 or e==1 or s==1):
    message += "(W)est"
print (message + ".")
