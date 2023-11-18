import json
import time
import os


def vote(name):
    print("Daftar Pasangan Calon Ketua Osis Imperium 2023-2024\n\nPASANGAN CALON 1\nKetua: Keira Angeline Lasut\nWakil Ketua: Valiant Christopher Budiman\n\nPASANGAN CALON 2\nKetua: Kenneth Maximilian Budijaya\nWakil Ketua: Clara Putri Kosasih")
    vote_success = False
    while not vote_success:
        vote = input("Masukkan pilihan pasangan calon yang diinginkan (1/2): ")

        if vote.isdigit() :
            if int(vote) == 1 or int(vote) == 2 :
                vote_success = True
                with open("login_data.json", "r") as file:
                    data = json.load(file)


                with open("login_data.json", "w") as file:
                    for student_data in data['students']:
                        if student_data['name'] == name:
                            student_data['has_voted'] = True

                    file.write(json.dumps(data, indent=4))

                if int(vote) == 1:
                    with open("result_data.json", "r") as file:
                        data = json.load(file)

                    with open("result_data.json", "w") as file:
                        data['paslon1'] += 1

                        file.write(json.dumps(data, indent=4))

                elif int(vote) == 2:
                    with open("result_data.json", "r") as file:
                        data = json.load(file)

                    with open("result_data.json", "w") as file:
                        data['paslon2'] += 1

                        file.write(json.dumps(data, indent=4))

                print("Terimakasih telah ikut serta dalam pemilihan calon ketua dan wakil ketua OSIS Imperium 2023/2024!")
                print("Layar ini akan terhapus dalam waktu 10 Detik, jangan melakukan apa-apa sebelum layar ini dihapus kembali")
                time.sleep(10)
                os.system('cls')
                login()

def login():
    name = input("Masukkan nama lengkap anda, (sertakan koma jika terdapat pada nama anda): ")
    password_success = False

    while not password_success:
        password_input = input("Masukkan 4 digit kode unik yang telah diberikan oleh usher: ")

        if password_input.isdigit():
            password_success = True


    with open("login_data.json") as file:
        data = json.load(file)

        for student_data in data['students']:
            if student_data['name'] == name:
                if student_data['password'] == int(password_input):
                    if student_data['has_voted'] == False:
                        vote(name)
                        correct_name = True
                        correct_password = True
                    else:
                        print("Anda sudah memilih calon pasangan pemimpin osis. Satu siswa hanya berhak melakukan voting 1x saja.")
                        login()
                    break;
                else:
                    correct_password = False
                    break;
            else:
                correct_name = False

    try:
        if (not correct_name):
            print("Nama atau password anda salah, coba periksa kembali penulisan nama anda, baik kapital dan koma jika ada, atau 4 digit kode unik yang telah diberikan.")
        if (not correct_name or not correct_password):
            login()
    except Exception:
        pass;


name = input("Masukkan nama lengkap anda, (sertakan koma jika terdapat pada nama anda): ")
password_success = False

while not password_success:
    password_input = input("Masukkan 4 digit kode unik yang telah diberikan oleh usher: ")

    if password_input.isdigit() :
        password_success = True


with open("login_data.json") as file:
    data = json.load(file)

    for student_data in data['students']:
        if student_data['name'] == name:
            if student_data['password'] == int(password_input):
                if student_data['has_voted'] == False:
                    vote(name)
                    correct_name = True
                    correct_password = True
                else:
                    print(
                        "Anda sudah memilih calon pasangan pemimpin osis. Satu siswa hanya berhak melakukan voting 1x saja.")
                    login()
                    break;
            else:
                correct_password = False
                break;
        else:
            correct_name = False

try:
    if (not correct_name): print("Nama atau password anda salah, coba periksa kembali penulisan nama anda, baik kapital dan koma jika ada, atau 4 digit kode unik yang telah diberikan.")

    if (not correct_name or not correct_password):
        login()
except Exception:
    pass;








