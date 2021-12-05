a_cümlesi = "Şifreleme Algoritması: Bayramınız kutlu olsun."
#from selenium import webdriver

def sifrele(cümle):

    sifre = list()
    for harf in cümle:
        if harf == " ":
            harf_yeni = "{}*&â".format("sP")
            sifre.append(harf_yeni)
        else:
            harf_yeni = "{}*&â".format(harf)
            sifre.append(harf_yeni)
    sifre.reverse()
    yeni_liste = list()
    eklenecek = []
    üc = 3
    baslangıc = 0
    print(5)
    try:

        while True:
            üc = 3

            eklenecek.clear()
            while True:

                eklenecek.append(sifre[baslangıc])
                üc -= 1
                baslangıc += 1
                if üc == 0:
                    yeni_liste.append([eklenecek])
                    print(eklenecek)
                    break
    except:
        #print(yeni_liste)
        a = 0
        print("\n")
        for i in a_cümlesi:

            print(a_cümlesi[a],end="")
            a += 1





sifrele(a_cümlesi)
