#step1
def Pig_Latin():
    word = raw_input("Please input a word.\n")
    #step2
    if word != "":
        #print 'word=%s' % word
        #step3
	new_word = ""
        for i in range(1, len(word)):
            new_word = new_word + word[i]
    
        new_word = new_word + word[0] + "ay"

        #step4
        print 'Your new word is "%s"' % new_word
    else:
        Pig_Latin()

Pig_Latin()
