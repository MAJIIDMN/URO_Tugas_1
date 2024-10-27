import random
import os

class Rock_paper_scissors():
    def __init__(self, user, com):
        self.user = user
        self.com = com
    def rules():
        print('='*3,"Gunting Batu Kertas", '='*3)
        print("Aturan Permainan\n 1. r untuk batu\n 2. p untuk kertas\n 3. s untuk gunting")
    def play():
        user = input("Pilih! (r/p/s): ").lower
        com = random.choice(['r', 's', 'p'])
        if (user == 'r' and com == 's') or (user == 'p' and com == 'r') or(user == 's' and com == 'p'):
            print("you win!")
        elif (user == com):
            print("draw")
        else:
            print("you lost")

class Guess_number():
    def __init__(self, com, user, range, try1):
        self.com = com
        self.user = user
        self.range = range
        self.try1 = try1
    def rules():
        print('='*26,"Tebak Angka", '='*26)
        print("Cara Bermain\n 1. Masukan jangkauan angka\n 2. Tebak angka yang dipilih oleh computer")
        print(" 3. Jika angka tebakan lebih besar maka muncul 'lebih kecil lagi'\n 4. Jika angka tebakan lebih kecil maka muncul 'lebih besar lagi'")
    def play():
        range = int(input("Masukan jangkauan bilangan : "))
        com = random.randint(1, range)
        try1 = 1
        while True:
            print("Percobaan ke-", try1)
            user = int(input("Tebak angka : "))
            try1 +=1
            os.system('cls')
            if user == com:
                break
            elif user<com:
                print("lebih besar lagi")
            else:
                print("lebih kecil lagi")
        print("Yeah Benar, angkanya adalah", com)
class MiniGame():
    def play():
        while True:  
            print('='*23)
            print('='*6, "Mini Game", '='*6)
            print('='*23)
            print(" 1. Gunting Batu Kertas\n 2. Tebak Angka")
            print('='*23)
            choice = int(input("Pilih mini Game(1/2): "))
            os.system('cls')
            if choice == 1:
                Rock_paper_scissors.rules()
                Rock_paper_scissors.play()
                while True:
                    loop = input("Apakah anda ingin bermain lagi? (y/n): ")
                    if loop == 'n' or loop == 'N':
                        stop = True
                        break
                    elif loop =='y' or loop == 'y':
                        stop = False
                        break
                if stop == True:
                    break
            elif choice == 2:
                Guess_number.rules()
                Guess_number.play()
                while True:
                    loop = input("Apakah anda ingin bermain lagi? (y/n): ")
                    if loop == 'n' or loop == 'N':
                        stop = True
                        break
                    elif loop =='y' or loop == 'y':
                        stop = False
                        break
                if stop == True:
                    break
            else:
                print("Pilih mini game yang terseida")
            os.system('cls')
            
MiniGame.play()