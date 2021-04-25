#
# This program converts a number from one numerical system into another.
#  Peter Halas

# ----------------------------A testing sample>>>    16K8X;IPG  -------------

#   Konverzna tabulka; obsahuje reprezentacne cisla pre ciselnu hodnotu

KT = {
    
      '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,          
      '8': 8, '9': 9, '10': 'A', '11': 'B', '12': 'C', '13': 'D',
      '14': 'E', '15': 'F', '16': 'G', '17': 'H', '18': 'I','19': 'J',
      '20': 'K', '21': 'L', '22': 'M', '23': 'N', '24': 'O', '25': 'P',
      '26': 'Q', '27': 'R', '28': 'S', '29': 'T', '30': 'U', '31': 'V',
      '32': 'W', '33': 'X', '34': 'Y', '35': 'Z',
      'A': 10, 'B': 11 , 'C': 12, 'D': 13 , 'E': 14,   
      'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20,        
      'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26,        
      'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32,        
      'X': 33, 'Y': 34, 'Z': 35, '36': 36, '37': 37, '38': 38,           
      '39': 39, '40': 40, '41': 41, '42': 42, '43': 43, '44': 44,              
      '45': 45, '46': 46, '47': 47, '48': 48, '49': 49, '50': 50,              
      '51': 51, '52': 52, '53': 53, '54': 54, '55': 55, '56': 56,              
      '57': 57, '58': 58, '59': 59, '60': 60, '61': 61, '62': 62,              
      '63': 63, '64': 64, '65': 65, '66': 66, '67': 67, '68': 68,              
      '69': 69, '70': 70, '71': 71, '72': 72, '73': 73, '74': 74,              
      '75': 75, '76': 76, '77': 77, '78': 78, '79': 79, '80': 80,              
      '81': 81, '82': 82, '83': 83, '84': 84, '85': 85, '86': 86,              
      '87': 87, '88': 88, '89': 89, '90': 90, '91': 91, '92': 92,              
      '93': 93, '94': 94, '95': 95, '96': 96, '97': 97, '98': 98 
      
      }

 


def prevod_Pismen_Cisla(cele, desatine): # prevedie pismena na cisla
    s = []
    t = []
    qq = 0
    #print(type(desatine), desatine)   #class string cele
    if p >= 37:
        pass
        pole = []
        pole = cele.split(":")
        for i in range(len(pole)):
            s.append(int(pole[i]))
            #print(s[i])
            if s[i] >= p:
                print("Nespravne cislo pre danu pociatocnu ciselnu sustavu")
                qq = 1
                return s,t, qq

        #print(pole,"   prevod")
        if type(desatine) != int:
            pole2 = []
            pole2 = desatine.split(":")
            #print(pole2)
            for j in range(len(pole2)):
                t.append(int(pole2[j]))
                #print(t[j])
                if t[j] >= p:
                    print("Nespravne cislo pre danu pociatocnu ciselnu sustavu")
                    qq = 1
                    return s,t, qq
                
            if int(max(pole)) >=  p:
                print("Nespravne cislo pre danu pociatocnu ciselnu sustavu")
                qq = 1
            if int(max(pole2)) >=  p:
                print("Nespravne cislo pre danu pociatocnu ciselnu sustavu")
                qq = 1
            #print(s,t,"Kde si")
            return s,t, qq
        
        elif type(desatine) == int:
            #print(s)
            #print(t,"preco")
            t.append(0)
            return s, t, qq
        
        
    for i in range(len(cele)):
        s.append(KT[cele[i]])

    if type(desatine) == int:
        desatine = "0"
    for j in range(len(desatine)):
        t.append(KT[desatine[j]])

    if max(s) >=  p:
        print("Nespravne cislo pre danu pociatocnu ciselnu sustavu")
        qq = 1
    if max(t) >=  p:
        print("Nespravne cislo pre danu pociatocnu ciselnu sustavu")
        qq = 1
    return s, t, qq
        



 # Na Desiatkovu Cela cast
def NDC(st, p): # st je cislo, p je pociatocna sustava napr. 12kova
    pom = 0   # vysledok v desiatkovej
    dlzka = len(st) # pocet cifier v cisle
    #print(st,st)
    for i in range(len(st)):
        pom  = pom + int(st[i]) * p ** ( dlzka - (i+1))        # pom  = pom + int(st[i]) * p ** ( dlzka - (i+1))
        #print(pom)
    #print(pom,"v desiatkovej")
    return pom


# Na Desiatkovu Desatinna cast
def NDD(stt, pp):
    print()
    pom = 0
    
    dlzka = len(stt)
    for i in range(dlzka):
        c= 0
        #pom = pom + int(stt[i])* pp ** (-i-1)
        pom += int(stt[i]) / (int(pp)**(i+1))
        #c =   (int(stt[i])) / (int(pp)**(i+1))
        #print(int(stt[i]),(int(pp)**(i+1)), c )
        
    #print(pom)
    return pom


# Cele Desiatkove cislo Na Cielovu Sustavu
def CDNCS(cele, q ):
    pom = 0
    k = 0
    celaC = float(cele)
    q = int(q)
    pole = []
    
    while(celaC!=0):
        s = []
        e = ""
        pomo = 0
        
        pom = celaC // q
        pomo = celaC % q
        pomo = int(pomo)
        pomo = str(pomo)
        pole.append(KT[pomo])
        #print(celaC)
        celaC = pom
    pole.reverse()
    #print("Tuuuu soom ", pole)
    if q >= 37:
        
        qw = ""
        for i in range(len(pole)):
            if i == len(pole) -1:
                qw = qw + str(pole[i])
                break
            qw = qw + str(pole[i]) + ":"
            
        return qw

    pole2 = []
    for i in range(len(pole)):
        pole2.append(str(pole[i]))

    strd = ""
    strd = strd + "".join(pole2)
    #print(strd)
    return strd




# Desatinne Desiatkove cislo Na Cielovu Sustavu
def DDNCS(desatine, q):
    #if type(desatine) == float:
        #print("Vazne")
        #return "0"
    
    pom = str(desatine)
    pom = pom.strip("0.")
    strd = ""
    e = int(input("Zadajte pocet desatinnych miest: "))
    
    strd += pom[:dlzkaDesatinnej] # tu sa meni pocet na presnost
    #print(strd,"SSSSSSSS")
    dlzka = len(strd)
    #print(dlzka)
    intee = int(strd)
    #print(intee)
    a = 0
    b = 0
    pole = []
    for i in range(e):
        
        a = (intee * q) % (10 ** dlzka)
        b = (intee * q) // (10 ** dlzka)
        #print(a,b)
        
        pole.append(b)
        intee = a
    #print(pole)
    
    if q >= 11 and q <= 36:
        pole2 = []
        for i in range(len(pole)):
            pole2.append(KT[str(pole[i])])
        
        pole3 = []
        for i in range(len(pole2)):
            pole3.append(str(pole2[i]))
        #pole3.insert(0, "0.")
        strt = ""
        strt = strt + "".join(pole3)
        #print(strt,"2")
        return strt
    
    elif q >= 37:
        ww = ""
        for i in range(len(pole)):
            ww = ww + str(pole[i]) + ":"
            if i == len(pole)-1:
                ww = ww + str(pole[i])
                break
        #print(ww,"1")
        return ww
        
    else:
        pole3 = []
        for i in range(len(pole)):
            pole3.append(str(pole[i]))
        pole3.insert(0, "0.")
        strt = ""
        strt = strt + "".join(pole3)
        #print(strt,"3")
        return strt
    
    

# -----------------------------main program--------------------------------------



#
# p = zaciatocna ciselna sustava; q = cielova ciselna sustava
# cislo = ciselna hodnota na prevod

p = '10';     q = '10';     cislo = "10.0"; # default


while True:
    
    
    print("\n\n\nTento program konvertuje cislo z jednej ciselne sústavy do druhej.\n")
    print("Na ukoncenie programu zadajte >     exit\n")
    print("Vyberte c. sustavy z intervalu   2 - 98\n")
    cislo = input("\nNotacia: Cele.Desatinne >>    ")
    if cislo == "exit":
        break
    p = int(input("Z >>   "))
    q = int(input("Do >>   "))
    
    

    desatine = 0

    cel = cislo.split('.')
    if len(cel) == 2:
        cele = cel[0]; desatine = cel[1]  # rozdelenie na dve casti
        dlzkaDesatinnej = len(desatine)

    else:
        cele = cel[0]
        

    


    pCele = 0    # prevedene do 10 vej sustavy
    pDesatine = 0

    vysledokCele = ""
    vysledokDesatine = ""
    

    quitt = 0
    
    if p != 10:
        mCele = []
        nDesatine = []
        mCele, nDesatine, quitt  =  prevod_Pismen_Cisla(cele, desatine)
        #print(mCele, nDesatine, quitt,"Hlavnom")
        if quitt == 1:
            continue
        pCele = NDC(mCele,p)
        pDesatine = NDD(nDesatine,p)
        #print(pDesatine,"v hlavnom")
        vysledokCele = CDNCS(pCele, q)
        if pDesatine != 0.0 :
            vysledokDesatine = DDNCS(pDesatine,q)
        elif pDesatine == 0.0:
            pass
            
        
        #print(vysledokDesatine,"v hhhh")

    elif p == 10:
        #print("Desiat")
        vysledokCele = CDNCS(cele, q)       # Cele Desiatkove cislo Na Cielovu Sustavu
        #print(desatine[0], len(cel))
        if len(cel) == 2 and  len(cele) > 1 and len(desatine) == 1:
            print("Vysledok je  :   ", vysledokCele )
            continue
        elif len(cel) == 1:
            print("Vysledok je  :   ", vysledokCele )
            continue


        vysledokDesatine = DDNCS(desatine,q)   # Desatinne Desiatkove cislo Na Cielovu Sustavu
        #print(str(vysledokDesatine[0:2]))
        if str(vysledokDesatine[0:2]) == "0.":
            if vysledokCele == "":
                #print(vysledokDesatine)
                print("Vysledok je :   ","0."+ str(vysledokDesatine[2:]))
                continue

            print("Vysledok je :   ",vysledokCele +"."+ str(vysledokDesatine[2:]))
            continue
        elif str(vysledokDesatine[0:2]) != "0." and p < q and vysledokCele == "":
            print("Vysledok je :   ","0."+ str(vysledokDesatine))
            continue
           
        print("Vysledok je :   ",vysledokCele +"."+ str(vysledokDesatine))
        #print(vysledokDesatine)
        continue
        


    if pCele != 0:
        wr = ""
        #print(vysledokDesatine)
        wr = vysledokDesatine.strip("0.")
        if len(cel) == 1:
            print("Vysledok je :   ",vysledokCele )
            continue
        print("Vysledok je( :   ",vysledokCele +"."+ wr )

    elif pCele == 0:
        #print(vysledokCele,"cojest", cele, len(cel))
        
        wr = ""
        #print(vysledokDesatine)
        wr = wr + str(vysledokDesatine[2:])
        #print(wr,"toto je wr")
        if len(cel) == 1:
            print("Vysledok je :   ", vysledokCele )
            continue
        if len(cel) == 2 and vysledokCele == "":
            if q >= 11:
                print("Vysledok je:    ", "0." + vysledokDesatine)
                continue
            
            print("Vysledok1 je :   ", vysledokDesatine )
            continue
        print("Vysledok2 je :   ", "."+ vysledokDesatine )
        
        






