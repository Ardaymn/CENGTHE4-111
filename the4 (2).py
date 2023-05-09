def inheritance(Descriptions):
    people=[]
    child={}
    dead=[]
    married={}
    fbi={}
    # DECEASED bulma
    for i in Descriptions:
        if "DECEASED" in i:
            yer=Descriptions.index(i)
            hedefisim=Descriptions[yer].split()[1]
            hedefpara=int(Descriptions[yer].split()[2])
            nonhedefpara=int(Descriptions[yer].split()[2])
            Descriptions.pop(yer)

    # kişiler listesi oluşturma
    for i in Descriptions:
        for a in i.split():
            if a not in people:
                people.append(a)
    if "DEPARTED" in people:
        people.remove("DEPARTED")
    if "MARRIED" in people:
        people.remove("MARRIED")
    if "CHILD" in people:
        people.remove("CHILD")

    # çocuk ve evli listesi oluşturma
    for i in Descriptions:
        if "CHILD" in i:
            a=0
            for a in range(0,(len(i.split())-3)):
                child[i.split()[-1-a]]=i.split()[1:3]
                a=a+1
        if "MARRIED" in i:
            married[i.split()[1]]=i.split()[-1]
            married[i.split()[-1]]=i.split()[1]
        if "DEPARTED" in i:
            dead.append(i.split()[1])
        
    if hedefisim not in dead:
        dead.append(hedefisim)
    # print("married:",married)
    # print("child:",child)
    # print("DEPARTED:",dead)

    for i in people:
        parents=[]
        kids=[]
        if i in dead:
            status="DEAD"
        if i not in dead:
            status="ALIVE"
        if i in married:
            hal="MARRIED"
        if i not in married:
            hal="SINGLE"
        for a in child:
            if i in child[a]:
                kids.append(a)
        if len(kids)==0:
            kids="NONE"
        for a in child:
            if i==a:
                parents.append(child[a][0])
                parents.append(child[a][1])
        if len(parents)==0:
            parents="NONE"
        worth=0
        if i == hedefisim:
            worth=int(hedefpara)
        fbi[i]=[status,hal,parents,kids,worth]
    # print("fbi",fbi[hedefisim])
    kidswhocaninherit=[]
    kidswhocaninheritkidlist=[]
    kidswhocaninheritskid={}
    for i in people:
        if i in fbi[hedefisim][3] and i not in dead:
            kidswhocaninherit.append(i)
        if i in fbi[hedefisim][3] and i in dead:
            if fbi[i][3] == "NONE":
                continue
            for a in fbi[i][3]:
                if "NONE" in fbi[a][3] and a in dead:
                    continue
                if a not in dead:
                    kidswhocaninheritkidlist.append(a)
                if a in dead:
                    for b in fbi[a][3]:
                        if b not in dead:
                            kidswhocaninheritkidlist.append(b)
            if len(kidswhocaninheritkidlist)!=0:
                kidswhocaninheritskid[i]=kidswhocaninheritkidlist
            kidswhocaninheritkidlist=[]
    # print("kidswhocaninherit:",kidswhocaninherit,"kidswhocaninheritskid:",kidswhocaninheritskid)
    aliveparent=[]
    if fbi[hedefisim][2]!="NONE":
        for i in fbi[hedefisim][2]:
            if i not in dead:
                aliveparent.append(i)
    alıcaklılar=[]

    # kardes
    kardes=[]
    if fbi[hedefisim][2]!="NONE":

        for a in child:
            child[a].sort()
            fbi[hedefisim][2].sort()
            if child[a]==fbi[hedefisim][2]:
                if a not in kardes:
                    kardes.append(a)
    if hedefisim in kardes:
        kardes.remove(hedefisim)
    # print("kardes",kardes)
    # kardesol=0
    # for i in kardes:
    #     if i in dead:
    #         kardesol=kardesol+1
    # if kardesol==len(kardes):
    #     kardes=[]

    #alive grandparent and deadgrandparent
    yasdede=[]
    oldede=[]
    grandparents=[]
    if fbi[hedefisim][2] != "NONE":
        for i in fbi[hedefisim][2]:
            if fbi[i][2]!="NONE":
                for a in fbi[i][2]:
                    if a not in dead and a!="NONE":
                        yasdede.append(a)
                    if a in dead and a!="NONE":
                        oldede.append(a)
        for i in fbi[hedefisim][2]:
            if fbi[i][2] != "NONE":
                for a in fbi[i][2]:
                    grandparents.append(a)

    if len(kidswhocaninherit)!=0 or len(kidswhocaninheritskid)!=0:
        def pg1(hedefisim,hedefpara,reuse):
            # print("PG1")
            if fbi[hedefisim][1]=="MARRIED" and married[hedefisim] not in dead and reuse==0:
                fbi[married[hedefisim]][-1]=hedefpara*0.25
                alıcaklılar.append(married[hedefisim])
                hedefpara=hedefpara*0.75
            # print("hedefpara:",hedefpara)
            if len(kidswhocaninherit)!=0 or len(kidswhocaninheritskid)!=0:
                forperson=hedefpara/(len(kidswhocaninherit)+len(kidswhocaninheritskid))
                # print("forperson:",forperson)
                for i in kidswhocaninherit:
                    fbi[i][-1]=forperson
                    alıcaklılar.append(i)
                for i in kidswhocaninheritskid:
                    for j in kidswhocaninheritskid[i]:
                        fbi[j][-1]=forperson/len(kidswhocaninheritskid[i])
                        alıcaklılar.append(j)
        pg1(hedefisim,hedefpara,0)

    pg2=len(kardes)+len(aliveparent)
    if len(kidswhocaninherit)==0 and len(kidswhocaninheritskid)==0 and pg2!=0 and fbi[hedefisim][2]!="NONE" and len(alıcaklılar)==0:
        def pg2(hedefpara):
            kidswhocaninherit=[]
            kidswhocaninheritkidlist=[]
            kidswhocaninheritskid={}
            if fbi[hedefisim][1]=="MARRIED" and married[hedefisim] not in dead:
                fbi[married[hedefisim]][-1]=hedefpara*0.5
                alıcaklılar.append(married[hedefisim])
                hedefpara=hedefpara*0.5
            if len(aliveparent)==2:
                fbi[fbi[hedefisim][2][0]][-1]=hedefpara*0.5
                alıcaklılar.append(fbi[hedefisim][2][0])
                fbi[fbi[hedefisim][2][1]][-1]=hedefpara*0.5
                alıcaklılar.append(fbi[hedefisim][2][1])
            if len(aliveparent)==1:
                for i in fbi[hedefisim][2]:
                    if i in aliveparent:
                        continue
                    deadparent=i
                for i in people:
                    if i in fbi[deadparent][3] and i not in dead:
                        kidswhocaninherit.append(i)
                    if i in fbi[deadparent][3] and i in dead:
                        if fbi[i][3] == "NONE":
                            continue
                        for a in fbi[i][3]:
                            if "NONE" in fbi[a][3] and a in dead:
                                continue
                            if a not in dead:
                                kidswhocaninheritkidlist.append(a)
                            if a in dead:
                                for b in fbi[a][3]:
                                    if b not in dead:
                                        kidswhocaninheritkidlist.append(b)
                        if len(kidswhocaninheritkidlist)!=0:
                            kidswhocaninheritskid[i]=kidswhocaninheritkidlist
                        kidswhocaninheritkidlist=[]
            if len(aliveparent)==0:
                # print("parent yok")
                for i in people:
                    if i in fbi[fbi[hedefisim][2][0]][3] and i not in dead:
                        kidswhocaninherit.append(i)
                    if i in fbi[fbi[hedefisim][2][0]][3] and i in dead:
                        if fbi[i][3] == "NONE":
                            continue
                        for a in fbi[i][3]:
                            if "NONE" in fbi[a][3] and a in dead:
                                continue
                            if a not in dead:
                                kidswhocaninheritkidlist.append(a)
                            if a in dead:
                                for b in fbi[a][3]:
                                    if b not in dead:
                                        kidswhocaninheritkidlist.append(b)
                        if len(kidswhocaninheritkidlist)!=0:
                            kidswhocaninheritskid[i]=kidswhocaninheritkidlist
                        kidswhocaninheritkidlist=[]
                
                for i in people:
                    if i in fbi[fbi[hedefisim][2][1]][3] and i not in dead:
                        if i not in kidswhocaninherit:
                            kidswhocaninherit.append(i)
                    if i in fbi[fbi[hedefisim][2][1]][3] and i in dead:
                        if fbi[i][3] == "NONE":
                            continue
                        for a in fbi[i][3]:
                            if "NONE" in fbi[a][3] and a in dead:
                                continue
                            if a not in dead:
                                kidswhocaninheritkidlist.append(a)
                            if a in dead:
                                for b in fbi[a][3]:
                                    if b not in dead:
                                        kidswhocaninheritkidlist.append(b)
                        if len(kidswhocaninheritkidlist)!=0:
                            kidswhocaninheritskid[i]=kidswhocaninheritkidlist
                        kidswhocaninheritkidlist=[]
        
            if len(kidswhocaninherit)==0 and len(kidswhocaninheritskid)==0 and len(aliveparent)==1:
                fbi[aliveparent[0]][-1]=hedefpara
                alıcaklılar.append(aliveparent[0])

            if len(kidswhocaninherit)!=0 or len(kidswhocaninheritskid)!=0:
                if len(aliveparent)!=0:
                    fbi[aliveparent[0]][-1]=hedefpara*0.5
                    alıcaklılar.append(aliveparent[0])
                    hedefpara=hedefpara*0.5
                forperson=hedefpara/(len(kidswhocaninherit)+len(kidswhocaninheritskid))
                for i in kidswhocaninherit:
                    fbi[i][-1]=forperson
                    alıcaklılar.append(i)
                if len(kidswhocaninheritskid)!=0:
                    for i in kidswhocaninheritskid:
                        for j in kidswhocaninheritskid[i]:
                            fbi[j][-1]=forperson/len(kidswhocaninheritskid[i])
                            alıcaklılar.append(j)


            
        pg2(hedefpara)

    if len(grandparents)!=0 and len(aliveparent)==0 and  len(kardes)==0 and fbi[hedefisim][2]!="NONE" and len(alıcaklılar)==0:
        
        def kidsseeghost(isim):
            kidswhocaninherit=[]
            kidswhocaninheritkidlist=[]
            kidswhocaninheritskid={}
            for i in people:
                if i in fbi[isim][3] and i not in dead:
                    kidswhocaninherit.append(i)
                if i in fbi[isim][3] and i in dead:
                    if fbi[i][3] == "NONE":
                        continue
                    for a in fbi[i][3]:
                        if "NONE" in fbi[a][3] and a in dead:
                            continue
                        if a not in dead:
                            kidswhocaninheritkidlist.append(a)
                        if a in dead:
                            for b in fbi[a][3]:
                                if b not in dead:
                                    kidswhocaninheritkidlist.append(b)
                    if len(kidswhocaninheritkidlist)!=0:
                        kidswhocaninheritskid[i]=kidswhocaninheritkidlist
                    kidswhocaninheritkidlist=[]
            sonuc={}
            sonuc["kidswhocaninherit"]=kidswhocaninherit
            sonuc["kidswhocaninheritskid"]=kidswhocaninheritskid
            return sonuc
        def pg3(hedefpara):
            if fbi[hedefisim][1]=="MARRIED" and married[hedefisim] not in dead:
                fbi[married[hedefisim]][-1]=hedefpara*0.75
                alıcaklılar.append(married[hedefisim])
                hedefpara=hedefpara*0.25
            kisi=0
            kidswhocaninherit=[]
            kidswhocaninheritskid={}
            oluamatorunuvar=[]
            for i in oldede:
                sonuc=kidsseeghost(i)
                if len(sonuc["kidswhocaninherit"])!=0:
                    for g in sonuc["kidswhocaninherit"]:
                        kidswhocaninherit.append(g)
                if len(sonuc["kidswhocaninheritskid"])!=0:
                    for a in sonuc["kidswhocaninheritskid"]:
                        kidswhocaninheritskid[a]=sonuc["kidswhocaninheritskid"][a]
                if len(kidswhocaninherit)!=0 or len(kidswhocaninheritskid)!=0:
                    oluamatorunuvar.append(i)

            kisi=len(yasdede)+len(oluamatorunuvar)
            pay=hedefpara/kisi
            for i in yasdede:
                alıcaklılar.append(i)
                fbi[i][-1]=pay
            for i in oluamatorunuvar:
                sonuc=kidsseeghost(i)
                sonucpay=pay/(len(sonuc["kidswhocaninherit"])+len(sonuc["kidswhocaninheritskid"]))
                for a in sonuc["kidswhocaninherit"]:
                    alıcaklılar.append(a)
                    fbi[a][-1]=sonucpay
                for b in sonuc["kidswhocaninheritskid"]:
                    for c in sonuc["kidswhocaninheritskid"][b]:
                        alıcaklılar.append(c)
                        fbi[c][-1]=sonucpay/len(sonuc["kidswhocaninheritskid"][b])

            
        pg3(hedefpara)
    if len(alıcaklılar)==0 and fbi[hedefisim][1]=="MARRIED" and married[hedefisim] not in dead and len(kardes)==0:
        alıcaklılar.append(married[hedefisim])
        fbi[married[hedefisim]][-1]=hedefpara
    lastlist=[]
    for i in alıcaklılar:
        girilcek=(i,fbi[i][-1])

        lastlist.append((girilcek))
    return lastlist