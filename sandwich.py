import random

import data


def greetUser():
    from data import greetings
    print(random.choice(greetings) + " What would you Like to have?")


def provideMenu():
    from data import fullMenu
    from data import header
    output = "Here is the menu:\n"
    #print(fullMenu)
    count = 1
    for menuItem in fullMenu.keys():
        printMenuItem = str(count) + ") " + menuItem
        menuList = fullMenu[menuItem]
        ingredients = menuList[header.index(data.INGREDIENTS)]
        bread = menuList[header.index(data.BREAD)]
        spread = menuList[header.index(data.SPREAD)]
        if ingredients is not None:
            printMenuItem += " which has " + ' ,'.join(ingredients)
        if bread is not None:
            printMenuItem += ". The bread included is " + bread
        if spread is not None:
            printMenuItem += ". The spread included is " + spread
        output += printMenuItem + '.\n'
        count += 1
    breads="Bread options="+' ,'.join(data.synonyms[data.BREAD])+'\n'
    spreads = "Spread options=" + ' ,'.join(data.synonyms[data.SPREAD]) + '\n'
    addONs="Options ="+' ,'.join(data.synonyms[data.OPTIONS])+'\n'
    removals="Removables="+' ,'.join(data.synonyms[data.EXCEPTIONS])+'\n'
    return output+breads+spreads+addONs+removals




def preprocess(tempStr):
    tempStr = (tempStr.lower()).strip()
    return tempStr


def askedMenu(userInput):
    for keyWord in data.menuPrompt:
        # print("user=",userInput, " menuPrompt=",preprocess(keyWord))
        if preprocess(keyWord) in userInput:
            return True
    return False


def classify(list, userInput):
    # print("in classify=", list)

    output = set()
    for key in list.keys():
        choices = list[key]
        for choice in choices:
            #       print(choice)
            if choice.lower() in userInput.lower() :
                output.add(key)
    if len(output) == 0:
        return None
    return output

#not used
def fillUsual(filledOrder):
    from data import fullMenu
    from data import header
    # use the name of sandwich to fill the usual ingredients

    filledOrder[data.INGREDIENTS] = fullMenu[filledOrder[data.NAMEOFSANDWICH]][header.index(data.INGREDIENTS)]
    bread = fullMenu[filledOrder[data.NAMEOFSANDWICH]][header.index(data.BREAD)]
    spread = fullMenu[filledOrder[data.NAMEOFSANDWICH]][header.index(data.SPREAD)]
    if (bread != ""):
        filledOrder[data.BREAD] = bread
    if (spread != ""):
        filledOrder[data.SPREAD] = spread
    return filledOrder


def satisfied(filledOrder):
    from data import required
    for key in filledOrder.keys():
        if required[key] is True and filledOrder[key] is None:
            return False
    return True


def getList(item):
    output = ""
    list = data.optionsDict[item]
    
    output = " ,".join(list)+"\n"
    return output
    if len(list) <= 1:
        return len[0]
    temp = list[0:-1]
    for tempStr in temp:
        output += tempStr + ","
    output += list[-1]
    output+='\n'
    return output


# this method is used to identify is there is a generic default bread or spread or whatever. and if so return true
# and the prompt will be to agree or disagree if no default value then it will return false and prompt will change to
# choose between one of the options
def createMissingPrompt(itemTofill, filledOrder):
    from data import fullMenu
    if itemTofill is data.NAMEOFSANDWICH:
        tempStr = data.NAMEOFSANDWICH + " is missing, please choose one among the following menu: \n" + provideMenu()
        return [False, tempStr]
    #print('in creating prompt', filledOrder)
    sandwichType = filledOrder[data.NAMEOFSANDWICH]
    #print('in creating prompt,sand= ', itemTofill)
    default=fullMenu[sandwichType][data.header.index(itemTofill)]
    if default is None:

        tempStr = itemTofill + " is missing for " + sandwichType + ". Please Choose among one of the options:\n" + getList(
            itemTofill)
        return [False, tempStr]
    else:
        tempStr = sandwichType + " comes with " + default + " as default. Respond yes to agree, no to choose something else\n"
        return [True, tempStr]


def beautify(filledOrder):
    output="\n\nOrder:"
    for key in filledOrder.keys():
        #print(type(key),type(filledOrder[key]))
        val=filledOrder[key]
        if type(val) is str:
            val=val
        elif val is None:
            val="<Empty>"
        else:
            val=' ,'.join(val)

        output+=(key)+" : "+val+'\n'
    return output


def order(userInput):
    filledOrder = {x: None for x in data.required.keys()}

    from data import synonyms

    for keys in synonyms.keys():
        list = synonyms[keys]
        itemChosen = classify(list, userInput)
        filledOrder[keys] = itemChosen
    while filledOrder[data.NAMEOFSANDWICH] is None:
        userInput = input("Please choose amongst one of the sandwiches:\n" + provideMenu())
        #sandwichType = classify(synonyms[data.NAMEOFSANDWICH], userInput)
        #filledOrder[data.NAMEOFSANDWICH] = sandwichType
        for keys in synonyms.keys():
            list = synonyms[keys]
            itemChosen = classify(list, userInput)
            filledOrder[keys] = itemChosen
    filledOrder[data.NAMEOFSANDWICH]="".join(filledOrder[data.NAMEOFSANDWICH])
    #print(filledOrder)
    if filledOrder[data.NAMEOFSANDWICH] is not None:
        filledOrder[data.INGREDIENTS] = data.fullMenu[filledOrder[data.NAMEOFSANDWICH]][data.header.index(data.INGREDIENTS)]

    while not satisfied(filledOrder):
        for row in filledOrder.keys():
            #print("row=",row,filledOrder[row])
            if data.required[row] is True:
                while filledOrder[row] is None:
                    default, userPrompt = createMissingPrompt(row, filledOrder)
                    userInput = input(userPrompt)
                    ##yes or no
                    if default:
                        #print("Came here")
                        yesOrNo = classify(data.yesOrNo, userInput)
                        #print(yesOrNo)
                        if yesOrNo is not None:
                            yesOrNo=''.join(yesOrNo)
                        #print(yesOrNo, "data.yes", data.YES," no=",data.NO)
                        if yesOrNo is data.YES:
                            defaultVal=data.fullMenu[filledOrder[data.NAMEOFSANDWICH]][data.header.index(row)]
                            #print("row=",row)
                            filledOrder[row] =classify(synonyms[row],defaultVal)
                            #print(filledOrder[row])
                        elif yesOrNo == data.NO:
                            userInput = input("Please choose one of following:"+ getList(row))
                            filledOrder[row] = classify(synonyms[row], userInput)

                    else:
                        # no default is present, the person has to select one of it
                        chosen= classify(synonyms[row], userInput)
                        #print(chosen)
                        filledOrder[row] =chosen

    return beautify(filledOrder)


if __name__ == "__main__":
    greetUser()
    # print(data.synonyms[data.OPTIONS].values())



    # print(data.synonyms[data.EXCEPTIONS])
    while True:
        userInput=""
        boolMenuPrompt = False
        userInput = preprocess(input())
        if askedMenu((userInput)):
            print(provideMenu())
            print('What would you like to have?')
            userInput = preprocess(input())

        output = order(userInput)

        print(output)
        confirmed=""
        while(True):
            exitOrNo=input("Is this what you ordered?\n")
            confirmed = classify(data.yesOrNo, exitOrNo)
            if confirmed is not None:
                confirmed=''.join(confirmed)
                break

        if confirmed== data.YES:
            print("Order confirmed, have a great Day")
            break

        elif confirmed== data.NO:
            print("Ok, you can reorder again\n")
            print(provideMenu())
        # filledOrder=wrapUpOrder(userInput)
