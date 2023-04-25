from tkinter import *
root=Tk()
root.geometry("500x400")
root.title("Entry Form")
def getvals():
    print(namevalue.get())
    print(phonevalue.get())
    print(gendervalue.get())
    print(emailvalue.get())

#using Label widget and packing it using grid method
Label(text="Welcome to TAMANNA Travels", fg="red",pady=30, font="arial 15 bold",bg="light yellow").grid(row=0,column=3)
Label(text="Name").grid(row=1)
Label(text="Phone").grid(row=2)
Label(text="Gender").grid(row=3)
Label(text="Email").grid(row=4)

#tkinter variables for storing variables
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emailvalue=StringVar()
foodservicevalue=IntVar()

#using Entry widget 
e1=Entry(root, textvariable=namevalue)
e2=Entry(root, textvariable=phonevalue)
e3=Entry(root, textvariable=gendervalue)
e4=Entry(root, textvariable=emailvalue)

#packing Entry widget using grid method
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)

#Checkbox
foodservice=Checkbutton(text="Do you like our Services?", variable=foodservicevalue)
foodservice.grid(row=5, column=1)


#using Button widget and packing it using grid method
Button(text="Submit", command=getvals).grid(row=6,column=1)




root.mainloop()