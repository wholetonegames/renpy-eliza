define e = Character("Eliza")

label start:
    scene bg whitehouse
    "Talk to the program by typing in plain English, using normal upper- and lower-case letters and punctuation.  Enter \"quit\" when done."
    
    show eileen happy
    e "Hello.  How are you feeling today?"

    python:
        s = ""
        therapist = Eliza()
        while s != "quit":
            try:
                s = renpy.input('')
            except EOFError:
                s = "quit"
            # narrator(s)
            while s[-1] in "!.":
                s = s[:-1]
            e(therapist.respond(s))

    return
