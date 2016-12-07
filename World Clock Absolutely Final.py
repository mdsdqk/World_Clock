#WORLD CLOCK
import math
print("WELCOME TO THE PROGRAM TO FIND THE CURRENT TIME \nIN CITIES ALL AROUND THE WORLD")
city={"islamabad":-1,"kabul":-2,"tehran":-4,"karachi":-1,"samara":-3,"tbilisi":-3,"baghdad":-5,"kuwait":-5,"abu dhabi":-3, "dubai":-3
      ,"muscat":-3,"jeddah":-5,"port louis":-3,"moscow":-5,"ankara":-7,"jerusalem":-7,"cairo":-7, "damascus":-5,"johannesburg":-7
      ,"cape town":-7,"nairobi":-5,"istanbul":-7,"athens":-7,"bucharest":-7,"vienna":-9,"st. petersburg":-5,"stockholm":-9
      ,"copenhagen":-9,"berlin":-9,"bern":-9,"paris":-9,"brussels":-9,"amsterdam":-9,"rome":-9,"barcelona":-9,"milan":-9
      ,"verona":-9,"geneva":-9,"florence":-9,"madrid":-9,"london":-11,"dublin":-11,"canary islands":-11,"uganda":-5,"mid atlantic":-15
      ,"santo damingo":-19,"boston":-19,"montreal":-19,"new york":-19,"philadelphia":-19,"ottawa":-19,"toronto":-19,"colombus":-19
      ,"baltimore":-19, "washington dc":-19, "miami":-19,"panama city":-21,"galapagos islands":-23,"mexico city":-23,"chicago":-21
      ,"las vegas":-25,"san fransisco":-25,"phoenix":-25,"los angeles":-25,"portland":-25,"honolulu":-31,"greenland":-17,"perm":-1
      ,"buenos aires":-17,"oslo":-9,"vatican city":-9,"brasilia":-15,"doha":-5,"riyadh":-5,"addis ababa":-5,"beirut":-7,"kanpur":0
      ,"bangalore":0,"bangkok":3,"singapore":5,"delhi":0,"bombay":0,"kolkata":0,"kuala lumpur":5,"hong kong":5,"kathmandu":0.5
      ,"taipei":5,"beijing":5,"tokyo":7,"ho chi minh city":3,"jakarta":3,"seoul":7,"manila":5,"perth":5,"melbourne":11
      ,"adelaide":10,"sydney":11,"canberra":11,"auckland":15,"wellington":15,"dhaka":1,"astana":1,"omsk":1,"helsinki":-7,"kiev":-7
      ,"colombo":0,"yangon":2,"osaka":7,"shangai":5,"bali":5,"hanoi":3,"reykjavik":-11,"milwaukee":-21,"seattle":-25,"houston":-21,"alaska":-27}
i=1
while i>=1:
    o=0
    place=input("\nEnter the Name of the City\n")
    if place.lower() in city:
        a=int(city.get(place.lower()))
        b=a//2
        import datetime
        maxhr=24
        maxmin=60
        localTime=str(datetime.datetime.now().time())
        timeNow=localTime.split(":")

        localHour=int(timeNow[0])
        localMin=int(timeNow[1])

        print("\n The Local Time is" ,localHour,":",format(str(localMin),'0>2'))

        if(localHour+b) < 24 and (localHour+b)>0:
            Hr=localHour+b
            date=0
        elif  (localHour+b)>24:
            Hr=b-(24-localHour)
            date=1
        elif (localHour+b)<0:
            Hr=24+(localHour+b)
            date=-1

        if a%2!=0:
            if localMin+30< 60:
               Min=localMin+30
               
    
            else:
              Min=str(30-(60-localMin))
              Hr=Hr+1
    
        else: Min=str(localMin)

        print("The Time in",place.title(),"is",Hr,":",format(Min,'0>2'))
        if date== 1:
                print("The Next Day")
        elif date==-1:
                print("The Previous Day")
    else:
        k=list(city.keys())
        l=[]
        correct=list(place.lower())
        for z in range (0,len(city)):
                count=0
                ct=0
                for p in range (0,min(len(correct),len(k[z]))):
                        if correct[p] ==k[z][p]:
                           count+=1
                        if correct[p] in k[z]:
                            ct+=1
                if (count>len(k[z])-math.ceil(len(k[z])/2) or ct>len(k[z])-2) and (o <1):
                            print("\nDo you mean",k[z].title())
                            cor=input("enter Yes or No\n")
                            if cor.lower()=="yes":
                                o=1
                                place=k[z]
                                a=int(city.get(place.lower()))
                                b=a//2
                                import datetime
                                maxhr=24
                                maxmin=60
                                localTime=str(datetime.datetime.now().time())
                                timeNow=localTime.split(":")

                                localHour=int(timeNow[0])
                                localMin=int(timeNow[1])

                                print(" \nThe Local Time is" ,localHour,":",format(str(localMin),'0>2'))

                                if(localHour+b) < 24 and localHour+b>0:
                                    Hr=localHour+b
                                    date=0
                                elif (localHour+b)>24:
                                   Hr=b-(24-localHour)
                                   date=1
                                elif(localHour+b)<0:
                                    Hr=24+localHour+b
                                    date=-1
    
                                if a%2!=0:
                                    if localMin+30< 60:
                                       Min=localMin+30
    
                                    else:
                                      Min=str(30-(60-localMin))
                                      Hr=Hr+1
    
                                else: Min=str(localMin)

                                print("The Time in",place.title(),"is",Hr,":",format(Min,'0>2'))
                                if date== 1:
                                    print("The Next Day")
                                elif date==-1:
                                    print("The Previous Day")
                        
                        
    cont=input("\n\nPress ENTER To Find The Time In Another City\nPress Q to exit")
    if cont.lower()=="q":
        i=0
        print("Thank You For Using Our World Clock")

