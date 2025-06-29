import wordcount

def main():

    while True:

        filename = input("File name: ")

        try:

            with open(filename, 'r') as fptr:

                wordData = wordcount.wordFreq(fptr)
                wordcount.printWds(wordData)

        except FileNotFoundError:
            print(f"'{filename}' couldnt be found. try again.")
            
        exit = input("do you want to exit (y/n) ")
        
        if exit == 'y':
            break

if __name__ == "__main__":
    main()