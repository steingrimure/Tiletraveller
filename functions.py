#Velja upphafsstaðsetningu x og y
locationx, locationy = 1, 1
location = [locationx, locationy]

#Setja inn fall til að athuga í hvaða áttir má fara
def directions(n, e, s, w):
    message = "You can travel: "
    if n==1:
        message += "(N)orth"
    if e == 1 and n == 1:
        message += " or (E)ast"
    elif e == 1 and n !=1:
        message +="(E)ast"
    if s== 1 and (n==1 or e==1):
        message += " or (S)outh"
    elif s == 1 and not (n==1 or e==1):
        message += "(S)outh"
    if w == 1 and (n==1 or e==1 or s==1):
        message += " or (W)est"
    elif w==1 and not (n==1 or e==1 or s==1):
        message += "(W)est"
    print (message + ".")
#Hér kemur input frá user
def user_input():
    faersla =input("Direction: ")
    faersla = faersla.lower()
    return faersla
#Hér eru skipanir frá inputi og peðið færist
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

def heildarfaersla (no, ea, so, we, x, y, xy):
    directions(n, e, s, w)
    location2 = xy
    while location2 == xy:
        att = user_input()
        xy, x, y = faera(att, xy, x, y)
    return xy, x, y
#setja inn alla reitina og hvaða reitur skilar sigri
victory = [3,1]
while location != victory:
    if location == [1,1] or location == [2,1]:
        n, e, s, w = 1, 0, 0, 0
        location, locationx, locationy = heildarfaersla(n, e, s, w, locationx, locationy, location)
    if location == [1,2]:
        n, e, s, w = 1, 1, 1, 0
        location, locationx, locationy = heildarfaersla(n, e, s, w, locationx, locationy, location)
    if location == [2, 2] or location == [3, 3]:
        n, e, s, w = 0, 0, 1, 1
        location, locationx, locationy = heildarfaersla(n, e, s, w, locationx, locationy, location)
    if location == [1, 3]:
        n, e, s, w = 0, 1, 1, 0
        location, locationx, locationy = heildarfaersla(n, e, s, w, locationx, locationy, location)
    if location == [2, 3]:
        n, e, s, w = 0, 1, 0, 1
        location, locationx, locationy = heildarfaersla(n, e, s, w, locationx, locationy, location)
    if location == [3, 2]:
        n, e, s, w = 1, 0, 1, 0
        location, locationx, locationy = heildarfaersla(n, e, s, w, locationx, locationy, location)
print("Victory!")