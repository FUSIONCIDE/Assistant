'''
Created on Dec 26, 2017

@author: FUSIONCIDE
'''


from tkinter import *
import platform

def openWindow():
    
    def centerWindow(self):
        self.update()
        cW = self.winfo_width()
        cH = self.winfo_height()
        cSW = self.winfo_screenwidth()
        cSH = self.winfo_screenheight()
        cX = (cSW / 2) - (cW / 2)
        cY = (cSH / 2) - (cH / 2)
        self.geometry("+%d+%d" % (cX, cY))
    
    def updateGIF(self):
        frame = framesGIF[self]
        self += 1
        canvas1.create_image(240, 240, image=frame)
        window.after(49, updateGIF, self)
    
    sysOS = platform.system()  #Get the OS of the computer
    
    'Initiate the window'
    rootWindow = Tk()
    screenHeight = rootWindow.winfo_screenheight()
    screenWidth = rootWindow.winfo_screenwidth()
    
    'Get rid of the border window while keeping the icon and other window things'
    rootWindow.attributes('-alpha', 0.0)
    rootWindow.iconify()
    window = Toplevel(rootWindow,
                      bg="white")  #Create new window to put things in (this is now main window cuz the other
    # rootWindow is invisible
    window.overrideredirect(1)  #Take out everything the Window Manager does, so no x button or minimize, etc.
    #Keep this window above every other application running on the computer
    if sysOS == "Windows":
        window.wm_attributes("-topmost", 1)
    elif sysOS == "Linux":
        window.wm_attributes("-topmost", 1)
    elif sysOS == "macOS":
        window.wm_attributes("-topmost", 1)
    'Body'
    #close = Button(window, bd=0, highlightbackground="red", activebackground="#f44242", activeforeground="#f4f4f4",
    #text="     X     ", fg="#6c6c6c", bg="#f4f4f4", command=lambda: rootWindow.destroy(), font="comicsans")
    #close.pack(side=TOP)
    #THE CLOSE BUTTON IS FOR TESTING PURPOSES ONLY; DELETE AFTER DONE
    #The canvas
    canvas1WH = screenWidth / 4  #Change constant here if want to change size of canvas
    canvas1 = Canvas(window, bg='white', highlightthickness=0, width=canvas1WH, height=canvas1WH)
    canvas1.pack()
    centerWindow(window)  #Center the window before displaying things such as the oval
    #The circle in canvas
    x = 50
    y = canvas1WH - 50
    oval1 = canvas1.create_oval(x, x, y, y, width=10)
    canvas1.itemconfig(oval1, fill="white")
    #Sets everything that is white to transparent
    if sysOS == "Windows":
        window.wm_attributes("-transparentcolor", "white")
    elif sysOS == "Linux":
        window.wm_attributes("-transparentcolor", "white")
    elif sysOS == "macOS":
        window.wm_attributes("-transparentcolor", "white")
    print("height: %d" % canvas1WH)
    print("width: %d" % canvas1WH)
    print(sysOS)
    print(x)
    
    'Keep at end'
    
    rootWindow.mainloop()
