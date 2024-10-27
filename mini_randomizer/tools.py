import random2


def random_int():

    max_number = int(input("Enter the maximum number: "))
    random_number = random2.randint(1, max_number)

    print(f'Победителем становится, участник под номером: {random_number}!!!')
