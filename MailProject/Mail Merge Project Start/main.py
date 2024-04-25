#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open(r"Input/Names/invited_names.txt","r") as o:
    tablica_names = o.readlines()
    # print(tablica_names)

    with open(r"Input/Letters/starting_letter.txt","r") as l:
        #letter_list = l.readlines()
        reading = l.read()
        for line in tablica_names:
            x = line.rstrip('\n')
            repl = reading.replace("[name]", x)
            # print(repl)
            with open(f"Output/ReadyToSend/example_{x}.txt","w") as e:
                e.write(repl)



            # replorigin = lread.replace(letter_list[0],repl)

       #      print(repl)
       #     print(replorigin)
       # print(replorigin)

