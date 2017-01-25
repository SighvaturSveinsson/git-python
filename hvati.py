#Python verkefni
#Sighvatur Sveinsson

#Dæmi 1
tala1 = int(input("Sláðu inn tölu "))
tala2 = int(input("Sláðu inn tölu "))
summa = tala1 + tala2
margfeldi = tala1 * tala2
print("Summa talnanna er", summa)
print("Margfeldi talnanna er", margfeldi)

#Dæmi 2
fornafn = input("Sláðu inn fornafn ")
eftirnafn = input("Sláðu inn eftirnafn ")
print("Halló", fornafn, eftirnafn)

#Dæmi 3
texti = input("Sláðu inn texta ")
hastafir = 0
lagstafir = 0
for i in texti:
    if i .isupper() and i .isalpha():
        hastafir += 1
    elif i .islower() and i .isalpha():
        lagstafir += 1
print("Í þessum texta eru", hastafir, "hástafir,", lagstafir, "lágstafir")