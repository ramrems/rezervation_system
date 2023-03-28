liste=[[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]]]
fiyat= { "1":0, "2":0, "3":0, "4":0}

adet={   '1':100, '2':100, '3': 100, '4': 100}

ciro= { '1':0, '2':0, '3': 0, '4': 0 }

dosya = open("C:\\Users\irems\OneDrive\Masaüstü\indirim.txt","r")
b=[]
for line in dosya:
    line=line.rstrip('\n')
    line=line.split("-")
    b.append(line)

for j in range(4):
    fiyat.update({(b[j][0], int(b[j][1]))})

for i in range(4):
    for j in range(3):
        liste[i][j]=b[j+4+(3*i)]   #indirim için gerekli min max bilet değerleri ve indirim oranları

a = [[], [], [], []]

def olustur(a):
    for i in range(4):
        for j in range(100):
            a[i].append("-")
olustur(a)

def rezerveSol(a):
    a[((a.index("-"))-(a.count("x"))+4+(a.index("-")))]="x"
def rezerveSag(a):
    a[a.index("-")]="x"

def rezerve2ve4(a,bilet):
    rezerveList = [[], []]
    for i in range (bilet):
        if ((a.index("-")%10)<5):
            koltuk_no = ((a.index("-"))-(a.count("x"))+4+(a.index("-")))
            sıra = (koltuk_no // 10) + 1
            koltuk = (koltuk_no % 10) + 1
            rezerveList[0].append(sıra)
            rezerveList[1].append(koltuk)
            rezerveSol(a)

        elif ((a.index("-")%10)>=5):
            koltuk_no = a.index("-")
            sıra = (koltuk_no // 10) + 1
            koltuk = (koltuk_no % 10) + 1
            rezerveList[0].append(sıra)
            rezerveList[1].append(koltuk)
            rezerveSag(a)
    print("rezerve edilen koltuklar (sıra-koltuk) : " ,end="  ")
    for i in range(bilet):
        print(rezerveList[0][i], "-", rezerveList[1][i], end=", ")
    print("\n")

def rezerve1ve3(a1_1,bilet):
    rezerveList=[[],[]]
    for a in range(bilet):
        if "x" in a1_1:
            koltuk_no = a1_1.index("-")
            sıra = (koltuk_no // 10) + 1
            koltuk = (koltuk_no % 10)+1
            rezerveList[0].append(sıra)
            rezerveList[1].append(koltuk)
            a1_1.insert(a1_1.index("-"), "x")
        else:
            koltuk_no = a1_1.index("-")
            sıra = (koltuk_no // 10) + 1
            koltuk = (koltuk_no % 10)+1
            rezerveList[0].append(sıra)
            rezerveList[1].append(koltuk)
            a1_1.insert(a, "x")

    print("rezerve edilen koltuklar (sıra-koltuk) :" ,end="  ")
    for i in range(bilet):
        print(rezerveList[0][i],"-",rezerveList[1][i],end=" , ")
    print("\n")

def sat(i,bilet):
    adet.update({(str(i), adet[str(i)] - bilet)})
    #print("kalan bilet ", adet[str(i)])
    print("bilet adedi", bilet,end=", ")
    tutar=((fiyat[str(i)]) * bilet)
    print("toplam tutar:",tutar,end=", ")
    if(int(liste[i-1][0][1])<=bilet<=int(liste[i-1][0][2])):
        oran1=int(liste[i-1][0][3])
        print("yapılan indirim",(tutar*(oran1/100)),end=", ")
        net_tutar=tutar-(tutar*(oran1/100))
        print("net tutar:", tutar-(tutar*(oran1/100)))
        ciro.update({(str(i), ciro[str(i)] + net_tutar)})
    elif (int(liste[i-1][1][1])<=bilet<=int(liste[i-1][1][2])):
        oran2=int(liste[i-1][1][3])
        print("yapılan indirim", (tutar * (oran2 / 100)),end=", ")
        net_tutar = tutar - (tutar * (oran2 / 100))
        print("net tutar: ",net_tutar)
        ciro.update({(str(i), ciro[str(i)] + net_tutar)})
    elif (int(liste[i-1][2][1])<=bilet):
        oran3=int(liste[i-1][2][3])
        print("yapılan indirim", (tutar * (oran3 / 100)),end=", ")
        net_tutar = tutar - (tutar * (oran3 / 100))
        print("net tutar: ", net_tutar)
        ciro.update({(str(i), ciro[str(i)] + net_tutar)})
    else:
        ciro.update({(str(i), ciro[str(i)] + tutar)})

def gosterkategorAll():
    matrix = []
    matrix1 = []
    for i in range(10):
        row=[]
        row1=[]
        for j in range(20):
            row.append(0)
            row1.append(0)
        matrix.append(row)
        matrix1.append(row1)

    for i in range(10):
        for j in range(5):
            matrix[i][j] = a[1][j + (i * 10)]
            matrix1[i][j] = a[3][j + (i * 10)]
        for k in range(5,15):
            matrix[i][k]=a[0][(k-5)+(i*10)]
            matrix1[i][k]=a[2][(k-5)+(i*10)]
        for m in range(15,20):
            matrix[i][m]=a[1][(m-10)+(i*10)]
            matrix1[i][m]=a[3][(m-10)+(i*10)]

    for k in range(10):
        for i in range(20):
            print(matrix[k][i],end=" ")
        print("\n")
    for k in range(10):
        for i in range(20):
            print(matrix1[k][i],end=" ")
        print("\n")

def rezervasyon():
    kategori = int(input("kategoriyi seçiniz (1-4) ?"))
    if (kategori < 1 or kategori > 4):
        print("lütfen geçerli bir kategori giriniz ")
        rezervasyon()
    else:
        print("sectiğiniz kategori ",kategori)
        bilet = int(input("bilet sayısını giriniz (1-30) ?"))
        if bilet>30:
            print("Tek seferde 30 dan fazla bilet alamazsınız ")
            rezervasyon()
        if(adet[str(kategori)]-bilet<0):
            print("bu kategoride istediginiz sayida bilet bulunmamaktadır. Daha az almayı deneyin ")

        else:
            print("Seçtiğiniz bilet sayısı ",bilet)
            if kategori==1 or kategori==3:
                rezerve1ve3(a[kategori-1],bilet)
            if kategori==2 or kategori==4:
                rezerve2ve4(a[kategori-1],bilet)

            sat(kategori,bilet)

def YeniEtkinlik(b):
    for i in range(4):
        b[i].clear()
    olustur(b)

def toplamCiro():
    toplam =0
    for i in range(4):
        print("%i.Kategori icin ciro" %(i+1), (ciro[str(i+1)]))
        toplam=toplam + ciro[str(i+1)]
    print("toplam ciro",toplam)

while True:
    print("\n")
    print("*** Ana Menü ***")
    print("****************")
    print("1.Rezervasyon ve Ucret")
    print("2.Salonu Yazdır")
    print("3.Yeni Etkinlik")
    print("4.Toplam Ciro")
    print("0.Çıkış")
    print("****************")
    print("Seçim Yapınız: ")
    try:
        x = int(input())
        if x==0:
            break
        elif x==1:
            rezervasyon()
        elif x==2:
            gosterkategorAll()
        elif x==3:
            YeniEtkinlik(a)
        elif x==4:
            toplamCiro()

    except ValueError:
        print("Geçersiz sayı")
        continue