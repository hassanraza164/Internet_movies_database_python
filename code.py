print("******************************I   M    D    B*****************************")
while True:
    print("-------------------------<  M A I N    P A G E  >-------------------------")
    print("For Administrator Login:1\tFor User Login:2\tTo Close:0")
    login=input("Enter: ")
    if login=="1": #Administrator Login
        while True:
            admin=input("Enter admin name: ")
            code=input("Enter password: ")
            if (admin=="unity" and code=="786") or (admin=="masaid" and code=="190"): #check
                def movies_items(m): #to make a sequence wise declaration(administrator)
                    if m==0:
                        py="enter the movie name: "
                    elif m==1:
                        py="enter the rating of the movie: "
                    elif m==2:
                        py="enter the bussiness of the movie: "
                    elif m==3:
                        py="enter the hero of the movie: "
                    elif m==4:
                        py="enter the 2nd cast of the movie: "
                    elif m==5:
                        py="enter the 3rd cast(supporting character)of the movie: "
                    elif m==6:
                        py="enter the 4th cast(2nd supporting character) of the movie: "
                    value=input(py) #ask for more movies to enter
                    return value #and return to check
                def use(y):
                    while True:     #to make addition in categories
                        x=input("enter the category of movies in which addition has to be made: ")
                        decide=y[x]
                        l=[]
                        k=[]
                        count=0
                        g=True
                        while (g==True):
                            j=movies_items(count)
                            k.append(j)          #k[m]=j
                            count+=1
                            if count==7:
                                l.append(k)
                                k=[]
                                u=input("want to enter 1 more movie?,y/n: ")
                                if u=="y":
                                    count-=7
                                else:
                                    g=False
                        decide.extend(l)
                        puchloo=input("want to add in other category?,y/n: ")
                        if puchloo=="n":
                            break
                        elif puchloo=="y":
                            pass
                        y[x]=decide
                    return y #return with a new dictionary
                def delete(khatko):   #to delete the category
                    ok1=input("enter the name of category which do u want to delete: ")
                    del khatko[ok1]
                    while True:
                        check=input('want to delete more categories,y/n: ')
                        if check=="n":
                            break
                        chalo=input('enter the name of that category: ') #if yes
                        del khatko[chalo]
                    return khatko   #Whole dictionary return
                def listdel(d):   #To delete the movies
                    while True:
                        key=input("enter the category of the movie: ")
                        ab_gya=d[key]
                        while (True):
                            movie_name=input("enter movie name: ")
                            for ra in ab_gya:
                                if ra[0]==movie_name: #matching movie name
                                    ab_gya.remove(ra)  #Whole sub-list(movie will be deleted)
                                    break
                            again=input("want to delete one more movie?,y/n: ")
                            if again=="n":
                                 break
                            elif again=="y":
                                 pass
                        d[key]=ab_gya   #assaigning new value
                        puchoo=input("want to delete movie from other category,y/n: ")
                        if puchoo=="n":
                            break
                        elif puchoo=="y":
                            pass
                    return d
                b={} #starting dictionary (begining)
                f=open("IMDB.txt","r") #firstly,file reading to save it from being re-write
                w=f.read()
                i=w.split("\n")
                for p in i:
                    t=p.split(":")
                    for z in t:
                        g=[]
                        if z!=t[0]:
                            lover=z.split(";")
                            for su in lover:
                                 ui=su.split("!")
                                 g.append(ui)
                    if p!=i[-1]:
                        b[t[0]]=g
                print("                                 Welcome Back!!!!!!\n")
                print("Your Data:",b)
                while True: #bigger outer loop
                        print("\n-------------------------------<<<EDITING SECTION>>>--------------------------------")
                        print("To add new stuff:1\tfor deleting section:2\tlog out:0")
                        start=input("enter: ")
                        if start=="1": #condition 1
                            while True:
                                print("To add new category:1\tto add new movie in a pre-existing category:2\t Back:0")
                                pta_kro=input("enter: ")
                                if (pta_kro=="1"): #to add new categories
                                    while True:
                                        x=input("enter the category name: ")
                                        l=[]
                                        k=[]
                                        m=0
                                        g=True
                                        while (g==True):
                                            film_things=movies_items(m)
                                            k.append(film_things)          #k[m]=j
                                            m+=1
                                            if m==7:
                                                l.append(k)
                                                k=[]
                                                u=input("want to enter 1 more movie?,y/n: ")
                                                if u=="y":
                                                    m-=7
                                                else:
                                                    g=False
                                        
                                        b[x]=l
                                        more=input("want to add more category?,y/n: ")
                                        if more=="n":
                                            break #..........................
                                        elif more=="y":
                                            pass
                                elif pta_kro=="2": #to add new movies in pre-existing categories
                                    b=use(b)
                                else:
                                    break
                        elif start=="2": #condition 2
                            while True: #to make repition in case of error(wrong input)
                                print("To delete category:4\tto delete movies:5\t Back:0")
                                deletes=input("enter: ")
                                if deletes=="4":
                                    b=delete(b)
                                    pass #Do nothing
                                elif deletes=="5":
                                    b=listdel(b);
                                    pass #Do nothing
                                elif deletes=="0":
                                    break
                                else:
                                    print("ERROR:type 4 or 5")
                        else:
                            break
                file=open("IMDB.txt","w") #writing modified dictionary
                for h in b:
                    file.write(h+":")
                    for a in b[h]:
                        for e in a:
                            if (e==a[-1]):
                                file.write(e)
                            else:
                                file.write(e+"!")
                        if a!=b[h][-1]:
                            file.write(";")
                    file.write("\n")
                file.close()
                print("After modifictaion:",b) #just checking the dictionary
                break
            else:
                print("Either Wrong password or username") #end of administrator loop (for error repitition)
    elif login=="2": #user block
        while True:
            user_007=input("Enter username: ")
            user_password=input("Enter Your Password")
            if (user_007=="hassan" and user_password=="164") or (user_007=="haseeb" and user_password=="170"):
                def movies_showing(me): #picking up the things relative to the value of m
                    if me==0:
                        py="movie name:"
                    elif me==1:
                        py="rating of the movie:"
                    elif me==2:
                        py="bussiness of the movie:"
                    elif me==3:
                        py="hero of the movie:"
                    elif me==4:
                        py="other cast of the movie:"
                    elif me==5:
                        py="1st supporting character of the movie: "
                    elif me==6:
                        py="2nd supporting character of the movie: "
                    return py  #it will be printed out


                def categories(temp):   #for displaying categories
                    print("categories:")
                    for cat in temp:
                        print(cat)
                b={}  #again starter(reading)
                f=open("IMDB.txt","r")
                w=f.read()
                i=w.split("\n")
                for p in i:
                    t=p.split(":")
                    for z in t:
                        g=[]
                        if z!=t[0]:
                            lover=z.split(";")
                            for su in lover:
                                 ui=su.split("!")
                                 g.append(ui)
                    if p!=i[-1]:
                        b[t[0]]=g

                categories(b) #displaying categories
                jojo=0 #required to print categories only once
                while True:
                    if jojo!=0: #after 1st repition only one time categories printing
                        categories(b)
                    def movies_name(c): #to show movies names
                        print("              ...............................................       ")
                        for film in b[c]:
                            print(film[0])
                        return c; #key returning
                    print("\nfor searching the category:1\tfor exit:0")
                    wanted=input("enter: ")
                    if wanted=="1":
                        cc=movies_name(input("enter the category name: "))
                        chl=0 #movies ki repitition ko roknye k lye
                        while True:
                            if chl!=0: #same concept of jojo
                                movies_name(cc)
                            def search(ctg,name): #to show the specifictions of the movie
                                print("          *****************************************")
                                global filmi
                                for filmi in b[ctg]:
                                    if filmi[0]==name:
                                        g=0
                                        for charac in filmi:
                                            print(movies_showing(g),charac)
                                            g+=1
                                        break
                                return name  #it is the movie name
                            print('\nfor searching the movie:1\tfor back:0')
                            want=input("enter: ")
                            if want=="1":
                                name_movie=input("enter movie to see its specifications: ")
                                gg=name_movie+".txt" #to make txt file of movie name
                                search(cc,name_movie)
                                filer=open("no_repitition.txt","r") #(to check for repition(it will contain the movie name alongwith the password of user
                                gnn=filer.read()                    #everytime user pass it will create movie name +password and count if it is greater 
                                filer.close()                       #than 1 then no ratings will be taken for the movie from that user)
                                counter0=gnn.count(name_movie+user_password)  #count() function to check whther password is there?
                                if (counter0==0): #if no record found
                                    ratings=eval(input("\nPlease give ratings to this movie out of ten: "))
                                    if filmi[1]=="0": #if rating zero then create the  new file
                                        new_file=open(gg,"w")
                                        new_file.write("0") #actually noyhing #first time create file
                                        new_file.close()
                                    same_file=open(gg,"r")
                                    kk=same_file.read() #to read the file
                                    counter=kk.count("1") #indirectly users or how many time rating has been given
                                    same_file.close()
                                    sum1=eval(filmi[1])*counter #to take sum
                                    final_rating=(sum1+ratings)/(counter+1) #after addition taking average including present user
                                    filmi[1]=str(final_rating) #replacing previous
                                    new=open(gg,"w")
                                    new.write(str(counter)+"1") #making the entry of user
                                    new.close()
                                    print("Your ratings have beeen saved SUCCESSFULLY")
                                    print("         THANK YOU!!!!!!!!")
                                else:
                                    print("\n<-------YOU HAVE ALREADY RATED THE MOVIE------->")
                                filer1=open("no_repitition.txt","w")
                                filer1.write(gnn+name_movie+user_password) #again making the entry
                                filer1.close()
                                print("          *****************************************")
                                while True:   #to exit the loop or go back
                                    furthur=input("for back,type(y)")
                                    if furthur=="y":
                                        chl=1
                                        break
                                    else:
                                        print("error:type y")
                            elif want=="0":
                                break
                            else:
                                print("ERROR: press 1 or 0")
                    elif wanted=="0":
                        break
                    else:
                        print("ERROR:enter 1 or 0")
                        pass
                    jojo=1 #intentionally
                file2=open("IMDB.txt","w")    #writing in a file before closing
                for h in b:
                    file2.write(h+":")
                    for a in b[h]:
                        for e in a:
                            if (e==a[-1]):
                                file2.write(e)
                            else:
                                file2.write(e+"!")
                        if a!=b[h][-1]:
                            file2.write(";")
                    file2.write("\n")
                file2.close()
                break
            else:
                print("Either user_name is wrong or password")

                            
    else:
      print("\nPROJECT CLOSE")
      print("GOOD BYE!!!!!!!!")
      break
                    
