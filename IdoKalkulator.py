



def Kulonbseg(ido1,ido2):


    ido1 = ido1.replace(":"," ")
    ido2 = ido2.replace(":"," ")


    ora1,perc1,mp1 = ido1.split()
    ora2,perc2,mp2 = ido2.split()

    ora3=int(ora2)-int(ora1)
    perc3=int(perc2)-int(perc1)
    mp3=int(mp2)-int(mp1)

    if mp3<0:
        mp3+=60
        perc3-=1

    if perc3<0:
        perc3+=60
        ora3-=1

    if ora3<0:
        ora3+=24


    print(f"Időkülönbség= {ora3}:{perc3}:{mp3}")



 


