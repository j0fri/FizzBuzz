from functools import reduce

if __name__ == '__main__':
    for i in range(1, 501):
        outputList = []
        if i % 3 == 0:
            outputList.append("Fizz")
        if i % 5 == 0:
            outputList.append("Buzz")
        if i % 7 == 0:
            outputList.append("Bang")
        if i % 11 == 0:
            outputList = ["Bong"]
        if i % 13 == 0:
            startWithB = [word[0] == "B" for word in outputList]
            if any(startWithB):
                outputList.insert(startWithB.index(True), "Fezz")
            else:
                outputList.append("Fezz")
        if i % 17 == 0:
            outputList.reverse() #What to do if only multiple of 17? Right now will just print the number
        if len(outputList) == 0:
            print(i)
        else:
            print(reduce(lambda x, y: x + y, outputList, ""))
            #print(str(i)+": " + reduce(lambda x, y: x + y, outputList, ""))
