from tkinter import *
import wikipedia

def disp(x, textbox):
    textbox.delete("1.0", "end")
    textbox.insert(INSERT, x)

def main(a=None):
    prev = listbox.size()
    if prev == 0:
        if a==None:
            l = wikipedia.search(my_entry.get())
        else:
            l = wikipedia.search(a)
    
        for i in range(len(l)):
            listbox.insert(i+1, l[i])
    else:
        listbox.delete(0, prev)
        main(a)
    
def sectionsbutton():
    i = listbox.curselection()
    i = listbox.get(i)
    try:
        global m
        m = wikipedia.page(title=i, auto_suggest=False)
        l = m.sections
        prev = sectionlist.size()
        if prev == 0:
            for n in range(len(l)):
                sectionlist.insert(n+1, l[n])
        else:
            sectionlist.delete(0, prev)
            sectionsbutton()

    except:
        print("Disambuguation error, be more specific")
        
def extractbutton():
    i = sectionlist.curselection()
    i = sectionlist.get(i)
    sect = m.section(i)
    disp(sect, text)

root = Tk()
root.geometry("800x480")
frame = Frame(root)
frame.pack()

#frames
topframe = Frame(root)
topframe.pack(side=TOP, pady = (15, 0))
leftframe = Frame(root)
leftframe.pack(side=LEFT, pady = 15, padx = (15, 0))
midframe = Frame(root)
midframe.pack(pady = 15, padx = 15)

#search bar #search button
my_entry = Entry(topframe, width = 20,font = ('Verdana',13), relief="groove")
my_entry.insert(0,' ')
my_entry.pack(side = LEFT) 
button1 = Button(topframe, text = "Search", command=main)
button1.pack(side = RIGHT)

#search results #label #section button
res = StringVar()
label = Label(leftframe, textvariable=res)
res.set("Search Results")
label.pack(pady = 0)
listbox = Listbox(leftframe)
listbox.pack(side = TOP)
button4 = Button(leftframe, text = "Sections: ", command=sectionsbutton, bd = 0)
button4.pack(side = TOP,)

#sections #label #extract button
sectionlist = Listbox(leftframe)
sectionlist.pack(pady = (0, 3))
button3 = Button(leftframe, text = "Extract content: ", command=extractbutton, bd = 0)
button3.pack(side = BOTTOM,)

#text display #label
out = StringVar()
label = Label(midframe, textvariable=out)
out.set("Content Requested")
label.pack(pady = 0)
text = Text(midframe)
text.pack()

root.title("Test")
root.mainloop()

