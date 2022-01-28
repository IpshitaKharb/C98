def countWords ():
    fileName=input("Enter The File Name")
    numberOfWords = 0
    fileOpen=open(fileName,'r')

    # Line is a variable in fileOpen #
    for line in fileOpen:
        words = line.split()
        # len = length of the string array or list #
        numberOfWords = numberOfWords + len(words)

    print('NUMBER OF WORDS: ')
    print(numberOfWords)

countWords()