#memanggil modul yang dibutuhkan
import random
import os

#buat kelas untuk Mini game 1
class Rock_paper_scissors():

#inisialisai variabel yang digunakan
    def __init__(self, user, com):
        self.user = user
        self.com = com

#aturan/cara bermain gamenya
   def rules():
        print('='*17,"Gunting Batu Kertas", '='*17)
        print("Aturan Permainan\n 1. r untuk batu\n 2. p untuk kertas\n 3. s untuk gunting")
        print(" 4. Batu kalah melawan Kertas dan menang melawan Guting\n 5. Kertas kalah melawan Guting dan menang melawan Batu\n 6. Guting kalah melawan Batu dan menang melawan Kertas")

#kosep mini gamenya
    def play():

#user memasukan pilihan (kertas, batu, atau gunting)
        user = input("Pilih! (r/p/s): ").lower()

#computer mimilih secra random (kertas, batu, atau gunting)
        com = random.choice(['r', 's', 'p'])

#jika pilihan user dan komputer sama maka permainan draw
#jika berbeda maka tergantung kondisi bisa menang atau kalah (sesuai aturan bermain)
        if (user == 'r' and com == 's') or (user == 'p' and com == 'r') or(user == 's' and com == 'p'):
            print("you win!")
        elif (user == com):
            print("draw")
        else:
            print("you lost")

#buat kelas untuk Mini game 2
class Guess_number():

#inisialisai variabel yang digunakan
    def __init__(self, com, user, range, try1):
        self.com = com
        self.user = user
        self.range = range
        self.try1 = try1

#aturan/cara bermain gamenya
    def rules():
        print('='*26,"Tebak Angka", '='*26)
        print("Cara Bermain\n 1. Masukan jangkauan angka\n 2. Tebak angka yang dipilih oleh computer")
        print(" 3. Jika angka tebakan lebih besar maka muncul 'lebih kecil lagi'\n 4. Jika angka tebakan lebih kecil maka muncul 'lebih besar lagi'")

#kosep mini gamenya
    def play():

#user memasukan jangkauan bilangan
        range = int(input("Masukan jangkauan bilangan : "))

#komputer mimilih 1 angka random yang tidak lebih besar dari jangkauan
        com = random.randint(1, range)

#Variabel untuk parameter percobaan menebak angka
        try1 = 1

#perulangan hingga kondisi terpenuhi(user menebak angka yang benar)
        while True:

#user menginput angka tebakan
            print("Percobaan ke-", try1)
            user = int(input("Tebak angka : "))
            try1 +=1

#sytem mebersikan display yang ada pada terminal(memulai dari awal)
            os.system('cls')

#uji jawaban user, jika benar maka perulangan akan berhenti
            if user == com:
                break
            elif user<com:
                print("lebih besar lagi")
            else:
                print("lebih kecil lagi")
        print("Yeah Benar, angkanya adalah", com)
#Kelas MiniGame untuk menjalankan Mini gamenya
class MiniGame():
    def play():

#perulangan hingga kondisi terpenuhi(user memilih berhenti bermain)        
	while True: 

#Display Mini game yang tersedia 
            print('='*23)
            print('='*6, "Mini Game", '='*6)
            print('='*23)
            print(" 1. Gunting Batu Kertas\n 2. Tebak Angka")
            print('='*23)

#user memilih Mini game yang tersedia
            choice = int(input("Pilih mini Game(1/2): "))
            os.system('cls')

#menjalankan Mini Game yang dipilh User
            if choice == 1:
                Rock_paper_scissors.rules()
                Rock_paper_scissors.play()

#perulangan hingga kondisi terpenuhi(user memasukan jawaban yang valid)
                while True:
                    loop = input("Apakah anda ingin bermain lagi? (y/n): ").lower()
                    if loop == 'n':

#Kondisi jika user memilih berhenti (Parameter 'Stop' bernilai True)
                        stop = True
                        break

#Kondisi jika user memilih berhenti (Parameter 'Stop' bernilai false)
                    elif loop =='y':
                        stop = False
                        break

#periksa apakah paremeter 'stop' bernilai true, jika iya maka permainan dihentikan, jika tidak maka permainan dilanjutkan(diulang)
                if stop == True:
                    break
            elif choice == 2:
                Guess_number.rules()
                Guess_number.play()
                while True:
                    loop = input("Apakah anda ingin bermain lagi? (y/n): ").lower()
                    if loop == 'n':
                        stop = True
                        break
                    elif loop =='y':
                        stop = False
                        break
                if stop == True:
                    break

#kondisi ketika input user diluar mini game yang tersedia(kembali ke menu awal)
            else:
                print("Pilih mini game yang terseida")
            os.system('cls')

#Melanjankan Mini game          
MiniGame.play()
