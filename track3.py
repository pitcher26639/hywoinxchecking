# tk1 tkinter = tk inter เป็น module graphic
from tkinter import *
tk = Tk()
tk.geometry("400x180") #กำหนดความกว้างจอ


# function section
def trackNo():
    track = {"jaodekpat":"TH040630ANRC6A1",
             "november2000s":"TH020130ANR40M",
             "lilin1712":"TH270130ANQZ5A0",
             "mukob0820":"TH470130ANR84E",
             "ur_mygalaxy":"TH013730ANRW5B",
             "rainbowsripp":"TH390930ANRT0E",
             "konaraipenmhee":"TH013630ANRP9B",
             "godpcha":"TH014930ANQU9E",
             "p_cocoa":"TH014330ANS21A",
             "redgunbonz":"TH030130ANQP7E",
             "suzyhaku":"TH040230ANRH8A1"}
    x = track[entry.get()]
    label3["text"] = "\nYour tracking no. " + x


# main program
tk.title("hywoinx tracking")
label1 = Label(tk, text="\n* * Checking your order status * *")
label1.pack()
label2 = Label(tk, text="\nWhat is your twitter?")
label2.pack()
entry = Entry(tk)
entry.pack()
label3 = Label(tk, text="\nYour tracking no.")
label3.pack()
button = Button(tk, text="Enter", command=trackNo) #command เป็นการเรียก function
button.pack()
tk.mainloop()