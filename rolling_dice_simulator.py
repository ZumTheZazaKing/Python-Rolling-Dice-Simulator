import randomimport timeimport sysprint("-"*70)print('                         Rolling Dice Simulator')print('-'*70)time.sleep(2)def main():        print('-'*70)        ans = str(input('Would you like to roll a dice? (Y/N)'))        print('-'*70)        if (ans.strip().upper() == 'Y'):                chosenNumber = random.randint(1, 6)                sentence = 'You rolled a {}!'.format(chosenNumber)                time.sleep(1)                print('Rolling...')                print('-'*70)                time.sleep(3)                print(sentence)                print('-'*70)            else:                print('You have decided to leave the simulation')                print('-'*70)                time.sleep(2)                print('Goodbye!')                print('-'*70)                time.sleep(2)                sys.exit(0)            while True:        main()        time.sleep(2)        if str(input("Would you like to roll again?(Y/N)")).strip().upper() != "Y":              print("\nGoodbye!\n")            time.sleep(1)            break        