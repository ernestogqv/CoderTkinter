import tkinter
import math

input_letters = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
code = ["h", "d", "o", "m", "c", "w", "z", "a"," ", "l", "s", "f", "q", "e", "g", "b", "n", "i", "k", "v", "r", "j", "u", "p", "t", "y", "x"]

#This is the home screen
def feedBack():
        username = entry.get()
        if username == 'e':
            correctLabel=tkinter.Label(root, text='Correct thats your username')
            correctLabel.pack()
            root.destroy()
            return
        else:
            print("They got it wrong heres what they put: " + username)



#Login window
root=tkinter.Tk()
label = tkinter.Label(root, text='Username')
label.pack()
entry = tkinter.Entry(root)
entry.pack()
button = tkinter.Button(root, text='Submit', command=feedBack)
button.pack()

root.mainloop()

#This is where each button press is guided to the next
variable = 0
def coderHome():
    home.destroy()
    global variable
    variable=1
    print(variable)
    return

def decoderHome():
    home.destroy()
    global variable
    variable = 2
    print(variable)
    return

#Home window
home = tkinter.Tk()
homeLabel = tkinter.Label(home, text='Code or Decode')
homeLabel.pack()
buttonCoder=tkinter.Button(home, text='Code', command=coderHome)
buttonDecoder=tkinter.Button(home, text='Decode', command=decoderHome)
buttonCoder.pack()
buttonDecoder.pack()
home.mainloop()

#Coder
def coder():
    #***used lower() so that everything is in lowercase
    user_input=(coderEntry.get()).lower()
    final_result = ""
    try:
        user_input_l = list(user_input)
        for i in user_input_l:
            for i2 in range(0, 26):
                if i == input_letters[i2]:
                    final_result += code[i2]
                    break
        print(final_result)
        return
    except:
        return



#Code home
if variable==1:
    codeHome = tkinter.Tk()
    coderLabel = tkinter.Label(codeHome, text='What do you want to code')
    coderEntry = tkinter.Entry(codeHome)
    coderButton = tkinter.Button(codeHome, text = "Submit", command=coder)
    coderLabel.pack()
    coderEntry.pack()
    coderButton.pack()
    codeHome.mainloop()

#Decode homeee
elif variable==2:
    decodeHome=tkinter.Tk()
    decoderLabel = tkinter.Label(decodeHome, text='What do you want to decode')
    decoderEntry = tkinter.Entry(decodeHome)
    decoderButton = tkinter.Button(decodeHome, text = "Submit")
    decoderLabel.pack()
    decoderEntry.pack()
    decodeHome.mainloop()
