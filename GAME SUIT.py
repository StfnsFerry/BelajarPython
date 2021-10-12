import random

print("Bermain Suit dengan Komputer \nBatu \nGunting \nKertas")
pemain = input("Pilih : ")
komputer = random.choice(["Batu","Gunting","Kertas"])
print("Kamu Memilih : " + pemain)
print("Komputer Memilih : " + komputer)

if (pemain == "Batu" and komputer == "Gunting" or pemain == "Gunting" and komputer == "Kertas" or pemain == "Kertas" and  komputer == "Batu"):
    print("Kamu Menang!")

elif (pemain == "Batu" and komputer == "Batu" or pemain == "Gunting" and komputer == "Gunting" or pemain == "Kertas" and komputer == "Kertas"):
    print("Seri!")

else:
    print("Kamu Kalah!")

