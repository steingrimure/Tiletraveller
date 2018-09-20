#Velja upphafsstaðsetningu x og y
locationx, locationy = 1, 1
location = [locationx, locationy]

#Setja inn fall til að athuga í hvaða áttir má fara
def directions(n, e, s, w):
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
#Hér kemur input frá user
def user_input():
    faersla =input("Direction: ")
    faersla = faersla.lower()
    return faersla

def faera(t, f, x, y):
    t= t.lower()
    if t == "n" and n==1:
        y+=1
    elif t == "s" and s ==1:
        y-=1
    elif t == "w" and w == 1:
        x -=1
    elif t == "e" and e == 1:
        x+=1
    else:
        print("Not a valid direction!")
    f = [x, y]
    return f, x, y
