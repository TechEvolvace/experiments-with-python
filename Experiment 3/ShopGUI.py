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

# Places GUI on computer screen that listen for events! 
window.mainloop()