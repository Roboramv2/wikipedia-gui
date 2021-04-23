from tkinter import *
import wikipedia

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
        listbox.delete(1, prev)
        main(a)
    
def trying():
    i = listbox.curselection()
    i = listbox.get(i)
    try:
        m = wikipedia.page(title=i, auto_suggest=False)
        print(m.content)
    except:
        try:
            main(i)
        except:
            m = wikipedia.page(title=i, auto_suggest=True)
            print(m.content)


root = Tk()
root.geometry("200x150")
frame = Frame(root)
frame.pack()
 
leftframe = Frame(root)
leftframe.pack(side=LEFT)
 
rightframe = Frame(root)
rightframe.pack(side=RIGHT)

my_entry = Entry(leftframe, width = 20)
my_entry.insert(0,'enter search term')
my_entry.pack(padx = 5, pady = 5)

button1 = Button(leftframe, text = "Search", command=main)
button1.pack(padx = 3, pady = 3)

listbox = Listbox(rightframe)
listbox.pack(side = TOP)  
print(listbox.size())
button3 = Button(rightframe, text = "extract", command=trying)
button3.pack(side = BOTTOM, padx = 3, pady = 3)

root.title("Test")
root.mainloop()

