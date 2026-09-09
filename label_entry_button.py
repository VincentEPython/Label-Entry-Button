import tkinter as tk 

# creating a window
window = tk.Tk()

#creating a label
name_label = tk.Label(window,text = "Enter your name") 
name_label.pack(pady = 20)

# creating an entry
name_entry = tk.Entry(window)
name_entry.pack(pady = 10)

#creating a button
submit_button = tk.Button(window,text = " Submit")
submit_button.pack(pady = 20)


# keeps the window open
window.mainloop()

