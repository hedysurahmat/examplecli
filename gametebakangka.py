import random

angka_rahasia = random.randint(1, 100)
percobaan = 0

print("🎮 Game Tebak Angka (1 - 100)")
print("Coba tebak angkanya!")

while True:
    tebakan = int(input("Masukkan tebakan kamu: "))
    percobaan += 1

    if tebakan < angka_rahasia:
        print("Terlalu kecil!")
    elif tebakan > angka_rahasia:
        print("Terlalu besar!")
    else:
        print(f"🎉 Benar! Angkanya {angka_rahasia}")
        print(f"Kamu butuh {percobaan} percobaan")
        break