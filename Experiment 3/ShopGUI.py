from tkinter import * 

# Instantiates an instance of a window 
window = Tk()

# Sets the size of the GUI
window.geometry("640x840")

# Sets the title of the GUI 
window.title("Shop GUI")

# Sets the appearance of the GUI
window.config(background="#8FDAFA")

# Adds a weclome message to the GUI for display
welcomeMessage = Label(window, 
                       text="Welcome to the GUI!",
                       font=('Arial', 40, 'bold'),
                       fg='black',
                       bg='#8FDAFA',
                       padx=20,
                       pady=40)
welcomeMessage.pack()

# Adds place for user to enter a message 
entry = Entry(window, 
              font=("Arial", 20),
              bg='#191970',
              fg='#21fc0d')
entry.pack()

# Add the Product images to the GUI!
product_1_image = PhotoImage(file = "../Assets/Shop-GUI-Product-1.gif")

product_2_image = PhotoImage(file="../Assets/Shop-GUI-Product-2.gif")

product_3_image = PhotoImage(file="../Assets/Shop-GUI-Product-3.gif")

product_1_image.pack()
product_2_image.pack()
product_3_image.pack()

# Places GUI on computer screen that listen for events! 
window.mainloop()