def LowerCaseConverter(word,lang):

    lang=lang

    word=word

    if(lang=='turkey'or lang=='az' or lang=='tr'):       

        for letter in word:

            if(letter=='i'or letter=="I"):

                I=u"\u0131"

                print(I,end='')

            else:

                print(letter.lower(),end='')

   

    if(lang=='Greek' or lang=='el'):

        leng=len(word)-1

        for i in range(leng):

            if(word[i]=="Σ"):

                I=u"\u03C3"

                print(I,end='')

            else:

                print(word[i].lower(),end='')

        if(word[-1]=="Σ"):  

            I=u"\u03C2"

            print(I,end='')

   

    if(lang=='irish' or lang=='ga' or lang=='ga-IE' or lang=='Irish'):

        leng=len(word)

   

        if (word[0]=='n' or word[0]=='t'):

            if(word[1]=='A' or word[1]=='E' or word[1]=='I' or

            word[1]=='O' or word[1]=='U' or word[1]=='Á' or word[1]=='É' or word[1]=='Í' or word[1]=='Ó'

            or word[1]=='Ú'):

                print(word[0].lower()+'-'+word[1].lower(),end='')

                print(word[2:].lower())        

        else:

            print(word.lower())

           

    if(lang=='thai' or lang=='th' or lang=='Thai'):

        for letter in word:

            letter=word.lower()

        print(letter)

   

    if(lang=='english' or lang=='en' or lang=='English' or lang=='en-US' or lang=='en-IE' or lang=='en-Latn'):

        for letter in word:

            letter=word.lower()

        print(letter)

    if(lang=='Chinese' or lang=='chinese' or lang=='zh-Hans'):

        for letter in word:

            letter=word.lower()

        print(letter)
