from art import logo, vs
from game_data import data
import random

def format_data(account):
    """Format akun data kedalam format print lalu return"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Ambil data tebakan user dan followers tiap data dan returns jika benar"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

#tampilkan logo pada display
print(logo)
score = 0
account_b = random.choice(data)
game_should_continue = True


#Buat permainan baru jika salah tanpa harus keluar program
while game_should_continue:
    #Generate module random untuk list game_data

    account_a = account_b
    account_b = random.choice(data)


    #pengkondisian untuk menghindari kesamaan pilihan pada random
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    #Beritahu user untuk menebak jawaban
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()


    ##Dapatkan jumlah follower pada tiap akun
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    #Cek jika tebakan user benar.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"Yeay!! anda benar. Current score: {score}")
    else:
        game_should_continue = False
        print(f"Upss salah, Final score: {score}")




