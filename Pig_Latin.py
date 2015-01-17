#step1
def Pig_Latin():
    word = raw_input("Please input a word.\n")
    #step2
    if word != "":
        #print 'word=%s' % word
        #step3
	new = ""
        for i in range(1, len(word)):
            new = new + word[i]
    
        new = new+ word[0] + "ay"

        #step4
        print 'Your new word is "%s"' % new
    else:
        Pig_Latin()

Pig_Latin()
