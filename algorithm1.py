#Fyrir hvern einasta reit þarf að skilgreina
#hvaða áttir hægt er að fara. X og Y notað til þess að 
#skilgreina reiti

locationx = 1
locationy = 1
reitur = [locationx, locationy]
endir = [3,1]
message = "You can travel: "
notvalid = "Not a valid direction!"
var =0
while reitur != endir:
    if reitur == [1, 1] or reitur == [2,1]:
        if var ==0: print(message + "(N)orth.")
        change = input("Direction: ")
        if change.lower()== "n":
            locationy +=1
            var =0
        else:
            print(notvalid)
            var=1
    elif reitur == [1, 2]:
        if var == 0: print (message + "(N)orth or (E)ast or (S)outh.")
        change = input("Direction: ")
        if change.lower() =="n":
            locationy +=1
            var=0
        elif change.lower() == "e":
            locationx +=1
            var=0
        elif change.lower()=="s":
            locationy-= 1
            var=0
        else:
            print(notvalid)
            var=1
    elif reitur == [2, 2] or reitur == [3, 3]:
        if var== 0: print (message + "(S)outh or (W)est.")
        change = input("Direction: ")
        if change.lower() == "w":
            locationx -=1
            var=0
        elif change.lower() == "s":
            locationy -=1
            var=0
        else:
            print(notvalid)
            var=1
    elif reitur == [1, 3]:
        if var ==0: print (message + "(E)ast or (S)outh.")
        change = input("Direction: ")
        if change.lower() == "e":
            locationx +=1
            var=0
        elif change.lower()== "s":
            locationy -=1
            var =0
        else:
            print(notvalid)
            var=1
    elif reitur == [2, 3]:
        if var ==0: print (message + "(E)ast or (W)est.")
        change = input("Direction: ")
        if change.lower() == "w":
            locationx -= 1
            var=0
        elif change.lower() == "e":
            locationx += 1
            var =0
        else:
            print(notvalid)
            var=1
    elif reitur == [3, 2]:
        if var ==0: print (message + "(N)orth or (S)outh.")
        change = input("Direction: ")
        if change.lower() == "n":
            locationy +=1
            var=0
        elif change.lower() == "s":
            print("Victory!")
            break
        else:
            print(notvalid)
            var=1
    reitur = [locationx, locationy]