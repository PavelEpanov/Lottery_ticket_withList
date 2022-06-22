import random

def main():
    lottery_num = []

    for i in range (7):
        lottery_num.append(random.randint(0,9))

    for line in lottery_num:
        print(line)

main()
