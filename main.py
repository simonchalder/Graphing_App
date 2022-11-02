import customtkinter
import itertools
import tkinter
from tkinter import filedialog
import pandas as pd
import numpy

class file:

    def csv1Read(file):
        csvFile1 = pd.read_csv(file) # Place the contents of file 1 into a variable
        return csvFile1

    def csv2Read(file):
        csvFile2 = pd.read_csv(file) # Place the contents of file 1 into a variable
        return csvFile2
    
    def button1SelFile():
        filename1 = filedialog.askopenfilename(initialdir = "C:\\", title = "Select a File", filetypes = (("CSV Files", "*.csv*"), ("all files", "*.*")))
        labelFile1.configure(text=filename1)
        csvFile = file.csv1Read(filename1)
        file.findAxisFile1(csvFile)

    def button2SelFile():
        filename2 = filedialog.askopenfilename(initialdir = "C:\\", title = "Select a File", filetypes = (("CSV Files", "*.csv*"), ("all files", "*.*")))
        labelFile2.configure(text=filename2)
        csvFile = file.csv2Read(filename2)
        file.findAxisFile2(csvFile)

    def findAxisFile1(csvFile):
        axisNames = csvFile.columns
        xaxis1Name = axisNames[0]
        yaxis1Name = axisNames[1]
        plot1XAxisBox.insert(0, xaxis1Name)
        plot1YAxisBox.insert(0, yaxis1Name)
        
    def findAxisFile2(csvFile):
        axisNames = csvFile.columns
        xaxis1Name = axisNames[0]
        yaxis1Name = axisNames[1]
        plot2XAxisBox.insert(0, xaxis1Name)
        plot2YAxisBox.insert(0, yaxis1Name)

    def csvAxisToList1(self, file):
        csvFile1 = pd.read_csv(self, file) # Place the contents of file 1 into a variable
        month = csvFile1['Date'].tolist() # Extract 1st column data into a list
        pop = csvFile1['Population'].tolist()
        return month, pop

    def csvAxisToList2(self, file):
        csvFile1 = pd.read_csv(file) # Place the contents of file 1 into a variable
        month = csvFile1['Date'].tolist() # Extract 1st column data into a list
        pop = csvFile1['Population'].tolist()
        return month, pop


class calc:

    def combobox_callback(choice):
        print("combobox dropdown clicked:", choice)

    def population_change(pop):
        pop_change = numpy.diff(pop)
        pop_change = [float(x) for x in pop_change]
        return pop_change

# Function to Calculate % growth rate in population --------------------------------------------------------------------------------------

    def growth_rate(pop):
        rate = pd.Series(pop)
        change = rate.pct_change()
        return(round(change[1:], 2).tolist())

    def calc_car_cap(r,N,cp):
        # K = (r * N * (1-N) / cp)
        C = []
        for a, b, c in itertools.zip_longest(r, N, cp):
            try:
                K = round((a * b * (1 - b) / c) * -1, 2)
                # K = b / 1 - (c / a * b) * -1
                C.append(K)
            except ZeroDivisionError:           
                K = C[-1]
                C.append(K)
        return(C)   

app = customtkinter.CTk()
app.geometry(f"{1120}x{500}")
app.title("New Graph")

customtkinter.set_appearance_mode("dark")

newFile = file
newCalc = calc

# Frame 1 ------------------------------------------------------------------------------------------------------

frame1 = customtkinter.CTkFrame(app, width=550, height=100, corner_radius=10)
frame1.grid(column=0, row=0, padx=20, pady=10)

file1Button = customtkinter.CTkButton(master=frame1, text="Select File 1", command=newFile.button1SelFile)
file1Button.grid(column=0, row=0, padx=60, pady=20, sticky="w")

entryFile1 = customtkinter.CTkEntry(master=frame1, placeholder_text="Plot Name")
entryFile1.grid(column=1, row=0, padx=60, pady=10, sticky="e")

labelFile1 = customtkinter.CTkLabel(master=frame1, text="")
labelFile1.grid(column=0, row=1, columnspan=2)


file2Button = customtkinter.CTkButton(master=frame1, text="Select File 2", command=newFile.button2SelFile)
file2Button.grid(column=0, row=2)

entryFile2 = customtkinter.CTkEntry(master=frame1, placeholder_text="Plot Name")
entryFile2.grid(column=1, row=2, padx=20, pady=10)

labelFile2 = customtkinter.CTkLabel(master=frame1, text="")
labelFile2.grid(column=0, row=3, columnspan=2)

# -------------------------------------------------------------------------------------------------------------

frame2 = customtkinter.CTkFrame(app, width=550, height=100, corner_radius=10)
frame2.grid(column=0, row=1, padx=20, pady=10)

titleEntry = customtkinter.CTkEntry(master=frame2, placeholder_text="Enter Graph Title")
titleEntry.pack(padx=40, pady=10, ipadx=140)

# ------------------------------------------------------------------------------------------------------------

frame3 = customtkinter.CTkFrame(app, width=550, height=100, corner_radius=10)
frame3.grid(column=0, row=2, padx=20, pady=10, ipadx=40)

# --------------------------------------------------

plot1XAxisLabel = customtkinter.CTkLabel(master=frame3, text="Plot 1 X")
plot1XAxisLabel.grid(column=0, row=1)

plot1XAxisBox = customtkinter.CTkEntry(master=frame3, placeholder_text="")
plot1XAxisBox.grid(column=1, row=1, padx=40, pady=10)

# --------------------------------------------------

plot1YAxisLabel = customtkinter.CTkLabel(master=frame3, text="Plot 1 Y")
plot1YAxisLabel.grid(column=0, row=2)

plot1YAxisBox = customtkinter.CTkEntry(master=frame3, placeholder_text="")
plot1YAxisBox.grid(column=1, row=2, padx=40, pady=10)

# --------------------------------------------------

plot2XAxisLabel = customtkinter.CTkLabel(master=frame3, text="Plot 2 X")
plot2XAxisLabel.grid(column=0, row=3)

plot2XAxisBox = customtkinter.CTkEntry(master=frame3, placeholder_text="")
plot2XAxisBox.grid(column=1, row=3, padx=40, pady=10)

# --------------------------------------------------

plot2YAxisLabel = customtkinter.CTkLabel(master=frame3, text="Plot 2 Y")
plot2YAxisLabel.grid(column=0, row=4)

plot2YAxisBox = customtkinter.CTkEntry(master=frame3, placeholder_text="")
plot2YAxisBox.grid(column=1, row=4, padx=40, pady=10)

# Frame 4 ---------------------------------------------------------------------------------------------

frame4 = customtkinter.CTkFrame(app, width=550, height=100, corner_radius=10)
frame4.grid(column=1, row=0, padx=20, pady=10, ipadx=40, ipady=25)

calcLabel = customtkinter.CTkLabel(master=frame4, text="Select Calculation To Display")
calcLabel.grid(column=0, row=0, padx=10, pady=20)

combobox = customtkinter.CTkComboBox(master=frame4, values=["Carrying Capacity", "Correlation Coefficient", "Standard Deviation + Mean"], command=calc.combobox_callback)
combobox.grid(column=0, row=1, padx=60, pady=10, ipadx=30)
combobox.set("Carrying Capacity")  # set initial value

# Frame 5 --------------------------------------------------------------------------------------------

frame5 = customtkinter.CTkFrame(app, width=550, height=100, corner_radius=10)
frame5.grid(column=1, row=1, padx=20, pady=10, ipady=25)

# genGraphButton = customtkinter.CTkButton(master=frame1, text="Select File 2", command=newGraph.genGraph)
# genGraphButton.grid(column=0, row=2)

app.mainloop()

