def sortWords(inputFileName, outputFileName):
        try:
                print("Function started");
                print("Function started in featuer1");
                print("Function started in featuer1");
                print("Function started in featuer1");
                print("Function started in featuer1");
                file = open(inputFileName,"r")
                l = file.read().split(" ")
                newList = []
                for j in range(0, len(l) + 1, 2):
                        charToAppend = l[j]
                        if(charToAppend.isdigit()):
                                continue
                        if(len(charToAppend.split('\n')[1]) == 1):
                                charToAppend = charToAppend[:-1]
                        else:
                                charToAppend = charToAppend[:-2]
                        newList.append(charToAppend)
                sortedList = sorted(newList)
                for i in sortedList:
                        newFile = open(outputFileName, "a")
                        newFile.write(i)
                newFile.close()
                file.close()
        except (FileNotFoundError, IOError):
                print("Wrong file or file path given")


if __name__ == "__main__":
        inputFileName = input('Enter Input file path with extension: ')
        outputFileName = input('Enter Output file name with extension: ')
        sortWords(inputFileName, outputFileName)