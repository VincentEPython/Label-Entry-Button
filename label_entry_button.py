import tkinter as tk 

# creating a window
window = tk.Tk()

# setting window dimentions
window.geometry("700x500")

def display_info():
    #getting data from entry widget
    data = name_entry.get()
    print(f" Hey {data} Welcome to your first App.")


#creating a label
name_label = tk.Label(window,text = "Enter your name") 
name_label.pack(pady = 20)

# creating an entry
name_entry = tk.Entry(window)
name_entry.pack(pady = 10)

#creating a button
submit_button = tk.Button(window,text = " Submit", command = display_info)
submit_button.pack(pady = 20)

close_button = tk.Button(window,text = " Close", command = window.destroy)
close_button.pack(pady = 20)
 
# keeps the window open
window.mainloop()

