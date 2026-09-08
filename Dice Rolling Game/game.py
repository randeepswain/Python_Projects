
import random

def main():
    count = 0
    while True:
        try:

            choice = input("Roll the Dice (y/n): ").lower()
            if  choice  == 'y':
                print(get_random())
                count += 1
            elif choice == 'n':
                print("Thanks For playing!")
                print(f"You rolled the dice {count} times!")
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid choice!")
            continue
             
def get_random():
    n1 = random.randint(1,6)
    n2 = random.randint(1,6)
    return (n1,n2)


if __name__ == "__main__":
    main()
