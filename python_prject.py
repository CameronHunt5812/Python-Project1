f = open("C:\Users\Cameron\Documents\GitHub\Python_Project\wordsearch3","r")
#Find the height, width and how many words to look for in the file.
height = int(f.readline())
width = int(f.readline()) 
numOfWords = int(f.readline())
#make a list of lists filled with 0 to fill with the letters from the word search
position = [[0 for x in range(width)]for y in range(height)]
#look at each position in the list and replace the 0 with the correct letter from the word search
for y in range (len(position)):
    #store line of charitors in a string to pull each sequentially
    tempLine = f.readline()
    for x in range (len(position[y])):
        #pull reach charitor and incert it into the list
        temp = tempLine[x]
        position[y][x] = temp
print position
#make a list of the words that you are looking for
lookFor = [f.readline() for w in range(numOfWords)]
print lookFor
found = [0 for f in range (len(lookFor))]
def search(placesToCheck,position,y,x,):
    pDi = -1
    #get the values forom the list to see which adjacent places you can check
    for di in (placesToCheck):
        pDi = pDi + 1
        if True == True:
                if pDi == 0:
                    for char in range (len(lookFor[word]) - 1):
                        if y-char != -1 and x-char != -1:
                            letter = lookFor[word][char]
                            if letter == position[y-char][x-char]:
                                if char == len(lookFor[word])-2:
                                    found[word] = 1
                                    print str(x+1) + "," + str(y+1) + " Direction:" +"Up and leaft, " + lookFor[word]
                                placesToCheck[pDi] = 0
                            else:
                                break
                        else:
                            break
                                
                if pDi == 1:
                    for char in range (len(lookFor[word]) - 1):
                        if y-char != -1:
                            letter = lookFor[word][char]  
                            if letter == position[y-char][x]:
                                if char == len(lookFor[word])-2:
                                    found[word] = 1
                                    print str(x+1) + "," + str(y+1) + " Direction:" +"Up, " + lookFor[word]
                                placesToCheck[pDi] = 0
                            else:
                                break
                        else:
                            break
                if pDi == 2:
                    for char in range (len(lookFor[word]) - 1):
                        if y-char != -1 and x+char != width:
                            letter = lookFor[word][char]
                            if letter == position[y-char][x+char]:
                                if char == len(lookFor[word])-2:
                                    found[word] = 1
                                    print str(x+1) + "," + str(y+1) + " Direction:" +"Up and Right, " + lookFor[word]
                                placesToCheck[pDi] = 0
                            else:
                                break
                        else:
                            break
                if pDi == 3:
                    for char in range (len(lookFor[word]) - 1):
                        if x-char != -1:
                            letter = lookFor[word][char]
                            if letter == position[y][x-char]:
                                if char == len(lookFor[word])-2:
                                    found[word] = 1
                                    print str(x+1) + "," + str(y+1) + " Direction:" +"Leaft, " + lookFor[word]
                                placesToCheck[pDi] = 0
                            else:
                                break
                        else:
                            break
                if pDi == 4:
                    for char in range (len(lookFor[word]) - 1):
                        if x+char != width:
                            letter = lookFor[word][char]
                            if letter == position[y][x+char]:
                                if char == len(lookFor[word])-2:
                                    found[word] = 1
                                    print str(x+1) + "," + str(y+1) + " Direction:" +"Right, " + lookFor[word]
                                placesToCheck[pDi] = 0
                            else:
                                break
                        else:
                            break
                if pDi == 5:
                    for char in range (len(lookFor[word]) - 1):
                        if y+char != height and x-char != -1:
                            letter = lookFor[word][char]
                            if letter == position[y+char][x-char]:
                                if char == len(lookFor[word])-2:
                                    found[word] = 1
                                    print str(x+1) + "," + str(y+1) + " Direction:" +"Doun and Leaft, " + lookFor[word]
                                placesToCheck[pDi] = 0
                            else:
                                break
                        else:
                            break
                if pDi == 6:
                    for char in range (len(lookFor[word]) - 1):
                        if y+char != height:
                            letter = lookFor[word][char]
                            if letter == position[y+char][x]:
                                if char == len(lookFor[word])-2:
                                    found[word] = 1
                                    print str(x+1) + "," + str(y+1) + " Direction:" +"Doun, " + lookFor[word]
                                placesToCheck[pDi] = 0
                            else:
                                break
                        else:
                            break
                if pDi == 7:
                    for char in range (len(lookFor[word]) - 1):
                        if y+char != height and x+char != width:
                            letter = lookFor[word][char]
                            if letter == position[y+char][x+char]:
                                if char == len(lookFor[word])-2:
                                    found[word] = 1
                                    print str(x+1) + "," + str(y+1) + " Direction:" +"Doun and Right, " + lookFor[word]
                                placesToCheck[pDi] = 0
                            else:
                                break
                        else:
                            break

for y in range (height):
    for x in range (width):
        for word in range (len(lookFor)):
            if position[y][x] == lookFor[word][0] and found[word] == False:
                placesToCheck = []
                if y == 0 and x == 0:
                    placesToCheck = [0,0,0,0,1,0,1,1]
                elif y == 0 and x == width-1:
                    placesToCheck = [0,0,0,1,0,1,1,0]
                elif y == height-1 and x == 0:
                    placesToCheck = [0,1,1,0,1,0,0,0]
                elif y == height-1 and x == width-1:
                    placesToCheck = [1,1,0,1,0,0,0,0]
                elif y == 0:
                    placesToCheck = [0,0,0,1,1,1,1,1]
                elif y == height-1:
                    placesToCheck = [1,1,1,1,1,0,0,0]
                elif x == 0:
                    placesToCheck = [0,1,1,0,1,0,1,1,]
                elif x == width-1:
                    placesToCheck = [1,1,0,1,0,1,1,0]
                else:
                    placesToCheck = [1,1,1,1,1,1,1,1]
                direction = search(placesToCheck,position,y,x)