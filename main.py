from functools import reduce

if __name__ == '__main__':
    #Prompt for how many numbers
    print("How many numbers do you want to print?")
    lastNum = input()
    if not lastNum.isdigit():
        raise Exception("Input must be an integer greater than zero.")
    if not int(lastNum) > 0:
        raise Exception("Input must be greater than zero.")

    #Prompt for which default rules to disable
    defaultRules = {3: True, 5: True, 7: True, 11: True, 13: True, 17: True}
    while True:
        print("Type a number to disable/enable its default rule or \"exit\" to continue")
        rule = input()
        if rule == "exit":
            break
        if not rule.isdigit():
            print("Please enter only a positive integer or \"exit\"")
            continue
        rule = int(rule)
        if not (rule in defaultRules):
            print(str(rule) + " has no default rule associated, only 3, 5, 7, 11, 13 and 17 have default rules")
            continue
        if defaultRules[rule]:
            defaultRules[rule] = False
            print("Rule for " + str(rule) + " disabled.")
        else:
            defaultRules[rule] = True
            print("Rule for " + str(rule) + " enabled.")

    #Prompt for custom rules
    print("To add custom rules. Please input a number and then an associated word.")
    print("The number must be a positive integer which is not associated to any enabled default rule.")
    print("Rules will be executed in increasing order after the default rules (except 13 and 17).")
    customRules = dict()
    while True:
        print("Enter number for a custom rule or \"exit\" to continue")
        rule = input()
        if rule == "exit":
            break
        if not rule.isdigit():
            print("Please enter only a positive integer or \"exit\"")
            continue
        rule = int(rule)
        if rule in defaultRules:
            if defaultRules[rule]:
                print(str(rule) + " already has an enabled default rule associated")
                continue
        if rule in customRules:
            print("Update word for " + str(rule))
            customRules[rule] = input()
        else:
            print("Set word for " + str(rule))
            customRules[rule] = input()

    #print output for each number
    for i in range(1, int(lastNum)+1):
        outputList = []

        #default standard rules with words
        if i % 3 == 0 and defaultRules[3]:
            outputList.append("Fizz")
        if i % 5 == 0 and defaultRules[5]:
            outputList.append("Buzz")
        if i % 7 == 0 and defaultRules[7]:
            outputList.append("Bang")

        #custom rules
        for customRule in customRules:
            if i % customRule == 0:
                outputList.append(customRules[customRule])

        #default rules executed at the end
        if i % 11 == 0 and defaultRules[11]:
            outputList = ["Bong"]
        if i % 13 == 0 and defaultRules[13]:
            startWithB = [word[0] == "B" for word in outputList]
            if any(startWithB):
                outputList.insert(startWithB.index(True), "Fezz")
            else:
                outputList.append("Fezz")
        if i % 17 == 0 and defaultRules[17]:
            outputList.reverse() #What to do if only multiple of 17? Right now will just print the number
            #Also should the Fezz also be reversed or still before the first B?

        if len(outputList) == 0:
            print(i)
        else:
            print(reduce(lambda x, y: x + y, outputList, ""))
            #print(str(i)+": " + reduce(lambda x, y: x + y, outputList, ""))
