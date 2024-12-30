from tkinter import *  # Installed Tkinter by conda and pip!
from PIL import Image, ImageTk  # Installed pillow by Conda!

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

# Read the image files and get all of the product images!
product_1_image = Image.open("./Assets/Shop-GUI-Product-1.gif")

product_2_image = Image.open("./Assets/Shop-GUI-Product-2.gif")

product_3_image = Image.open("./Assets/Shop-GUI-Product-3.gif")

# Resized the product images!
resized_product_1_image = product_1_image.resize((250, 250))

resized_product_2_image = product_2_image.resize((250, 250))

resized_product_3_image = product_3_image.resize((250, 250))

# Reformatted each of the resized images with PhotoImage function!
reformatted_product_1_image = ImageTk.PhotoImage(resized_product_1_image)

reformatted_product_2_image = ImageTk.PhotoImage(resized_product_2_image)

reformatted_product_3_image = ImageTk.PhotoImage(resized_product_3_image)

# Displaying each product image in the GUI!
product_image_gallery = Canvas(window, width=640, height=600)
product_image_gallery.pack()
product_image_gallery.create_image(0, 20, image = reformatted_product_1_image)
product_image_gallery.create_image(0, 90, image = reformatted_product_2_image)
product_image_gallery.create_image(0, 140, image = reformatted_product_3_image)


# Places GUI on computer screen that listen for events! 
window.mainloop()