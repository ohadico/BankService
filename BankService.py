import Tkinter as tk
import webbrowser


class MainAppView(tk.Frame):
    """Encapsulates of all the GUI logic.
    Attributes:
        master: where to open the Frame, by deafult root window
        title: Main Label
        
        one: Button 
        two: Button 
        three: Button 
    """
    def start_gui(self,ok = True):
        """Starts the GUI, if everything ok, to change"""
        if ok:
            self.mainloop()
        else:
            self.master.destroy()
            
    def createWidgets(self):
        """Create the set of initial widgets"""
        
        # Create the label
        self.title = tk.Label(
                self, text = " What's up ?")
        self.title.grid(
            row=0, column=0,columnspan=4, sticky = tk.E+tk.W )
        
        # Create the three buttons
        self.one = tk.Button(self)
        self.one["text"] = "Task 1"
        self.one.grid(row=1, column=0)
        
        self.two = tk.Button(self)
        self.two["text"] = "Task 2"
        self.two.grid(row=1, column=1)
        
        self.three = tk.Button(self)
        self.three["text"] = "Task 3"
        self.three.grid(row=1, column=2)
        
        self.four = tk.Button(self)
        self.four["text"] = "Task 4"
        self.four.grid(row=1, column=3)
        
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        # option is needed to put the main label in the window
        self.createWidgets()


class MainAppController(object):
    def nothing(self):
        pass
        
    def init_view(self,root):
        """Initializes GUI view
            In addition it bindes the Buttons with the callback methods.
        """
        self.view = MainAppView(master=root)   
        
        # Bind buttons with callback methods
        self.view.one["command"] = self.nothing
        self.view.two["command"] = self.nothing
        self.view.three["command"] = self.nothing
        self.view.four["command"] = self.nothing

        # Start the gui 
        self.view.start_gui()
        

def main():
    controller = MainAppController()
    
    # Build Gui and start it
    root = tk.Tk()
    root.title('Main Application')
    
    controller.init_view(root)

if __name__ == "__main__":
    main()
