import matplotlib.pyplot as plt
import customtkinter
import itertools
import tkinter
from tkinter import filedialog
import pandas as pd
import numpy as np

########################### Class Definitions #####################################

class file: # - Object instances store all data required for current calculations and graphs

    def __init__(self, filePath1, filePath2, csvFileData1, csvFileData2, xAxisName1, yAxisName1, xAxisName2, yAxisName2, xAxisList1, yAxisList1, xAxisList2, yAxisList2):
        self.filePath1 = filePath1
        self.filePath2 = filePath2
        self.csvFileData1 = csvFileData1
        self.csvFileData2 = csvFileData2
        self.xAxisName1 = xAxisName1
        self.yAxisName1 = yAxisName1
        self.xAxisName2 = xAxisName2
        self.yAxisName2 = yAxisName2
        self.xAxisList1 = xAxisList1
        self.yAxisList1 = yAxisList1
        self.xAxisList2 = xAxisList2
        self.yAxisList2 = yAxisList2

    def getfilePath1(self): # - Getters and Setters
        return self.filePath1

    def setfilePath1(self, newValue):
        self.filePath1 = newValue

    def getfilePath2(self):
        return self.filePath2

    def setfilePath2(self, newValue):
        self.filePath2 = newValue

    def getcsvFileData1(self):
        return self.csvFileData1

    def setcsvFileData1(self, newValue):
        self.csvFileData1 = newValue

    def getcsvFileData2(self):
        return self.csvFileData2

    def setcsvFileData2(self, newValue):
        self.csvFileData2 = newValue
    
    def getXAxisName1(self):
        return self.xAxisName1

    def setXAxisName1(self, newValue):
        self.xAxisName1 = newValue

    def getYAxisName1(self):
        return self.yAxisName1

    def setYAxisName1(self, newValue):
        self.yAxisName1 = newValue

    def getXAxisName2(self):
        return self.xAxisName2

    def setXAxisName2(self, newValue):
        self.xAxisName2 = newValue

    def getYAxisName2(self):
        return self.yAxisName2

    def setYAxisName2(self, newValue):
        self.yAxisName2 = newValue

    def getXAxisList1(self):
        return self.xAxisList1

    def setXAxisList1(self, newValue):
        self.xAxisList1 = newValue

    def getYAxisList1(self):
        return self.yAxisList1

    def setYAxisList1(self, newValue):
        self.yAxisList1 = newValue

    def getXAxisList2(self):
        return self.xAxisList2

    def setXAxisList2(self, newValue):
        self.xAxisList2 = newValue

    def getYAxisList2(self):
        return self.yAxisList2

    def setYAxisList2(self, newValue):
        self.yAxisList2 = newValue  

class calc:

    def population_change(pop): # - Population change calculation for carrying capacity. Takes an array (pop) as an argument
        pop_change = np.diff(pop) # - numpy method to create a new array containing the difference in values of the pop array
        pop_change = [float(x) for x in pop_change]
        return pop_change

    def growth_rate(pop): # - Creates an array with values showing the % change from value to value in an array. Takes an array (pop) as an argument
        rate = pd.Series(pop)
        change = rate.pct_change()
        return(round(change[1:], 2).tolist())

    def calc_car_cap(r,N,cp): # - Iterates through the pop array and using arrays from the growth rate and pop change functions calculates the carrying capacity for every value in the pop array
        # K = (r * N * (1-N) / cp) - alternative formula found for carrying capacity
        C = []
        for a, b, c in itertools.zip_longest(r, N, cp):
            try:
                K = round((a * b * (1 - b) / c) * -1, 2)
                # K = b / 1 - (c / a * b) * -1
                C.append(K)
            except ZeroDivisionError: # - In the case of a zero division error (no change from value to value), the last carrying capacity value is used           
                K = C[-1]
                C.append(K)
        return(C) # - Returns an array of carrying capacity values

    def correlation_coefficient(ylist1, ylist2): # - Correlation coefficient calculation function using numpy method
        cor_coef = np.corrcoef(ylist1, ylist2, rowvar=False)
        cor_coef_rounded = round(cor_coef[0,1], 3)
        cor_coef_str = "Correlation Coefficient = " + str(cor_coef_rounded)
        return cor_coef, cor_coef_rounded, cor_coef_str # Returns the coefficient, a rounded version (2 decimal places) and a concatinated string for display in the graph

    def sd_mean(ylist1, ylist2): # - Function to calculate mean and sd values in an array
        sd1 = round(np.std(ylist1), 2)
        sd2 = round(np.std(ylist2), 2)
        mean1 = round(sum(ylist1) / len(ylist1), 2)
        mean2 = round(sum(ylist2) / len(ylist2), 2)
        sd_mean_str = entryFile1.get() + " SD  = " + str(sd1) + " ***  Mean = " + str(mean1) + "\n " + entryFile2.get() + " SD = " + str(sd2) + " ***  Mean = " + str(mean2)
        return sd1, sd2, mean1, mean2, sd_mean_str # - Returns sd and mean values for each axis as well as a concatinated string to display in a graph

########################### Function Definitions #####################################

def makeNewFilesObject(file1, file2, csv1, csv2, x1, y1, x2, y2, xl1, yl1, xl2, yl2): # - Creates a new object from the file class
    newFiles = file(file1, file2, csv1, csv2, x1, y1, x2, y2, xl1, yl1, xl2, yl2)
    return newFiles

def printCheck(): # - Used in debug
    print(newFiles.getXAxisName1())

def fileButton1(): # - Function called when file selection gui button is pressed
    global newFiles, filePath1, filePath2, csvFileData1, xAxisName1, yAxisName1, xAxisList1, yAxisList1, csvFileData2, xAxisName2, yAxisName2, xAxisList2, yAxisList2
    filePath1 = filedialog.askopenfilename(initialdir = "C:\\", title = "Select File 1", filetypes = (("CSV Files", "*.csv*"), ("all files", "*.*")))   
    csvFileData1 = pd.read_csv(filePath1)
    axisNames1 = csvFileData1.columns

    xAxisName1 = axisNames1[0] # - File path is read from user input, csv file is read and axis names are generated for both files
    yAxisName1 = axisNames1[1]

    xAxisList1 = csvFileData1[xAxisName1]
    yAxisList1 = csvFileData1[yAxisName1]
    
    filePath2 = filedialog.askopenfilename(initialdir = "C:\\", title = "Select File 2", filetypes = (("CSV Files", "*.csv*"), ("all files", "*.*")))   
    csvFileData2 = pd.read_csv(filePath2)
    axisNames2 = csvFileData2.columns
    
    xAxisName2 = axisNames2[0]
    yAxisName2 = axisNames2[1]

    xAxisList2 = csvFileData2[xAxisName2]
    yAxisList2 = csvFileData2[yAxisName2]
    
    newFiles = makeNewFilesObject(filePath1, filePath2, csvFileData1, csvFileData2, xAxisName1, yAxisName1, xAxisName2, yAxisName2, xAxisList1, yAxisList1, xAxisList2, yAxisList2)
    
    labelFile1.configure(text=newFiles.filePath1)
    labelFile2.configure(text=newFiles.filePath2)
    plot1XAxisBox.insert(0, newFiles.xAxisName1)
    plot1YAxisBox.insert(0, newFiles.yAxisName1)
    plot2XAxisBox.insert(0, newFiles.xAxisName2)
    plot2YAxisBox.insert(0, newFiles.yAxisName2)

def genGraph(): # - Calculations and graph generated depending on option selected in GUI combobox by the user
    
    if combobox.get() == "Carrying Capacity":
        
        pop1 = newFiles.getYAxisList1()
        pc1 = calc.population_change(pop1)
        lastpcval1 = pc1[-1] # get the last value in the list
        pc1.append(lastpcval1)
        gr1 = calc.growth_rate(pop1)
        lastgrval1 = gr1[-1] # Get the last value in the list
        gr1.append(lastgrval1)
        cc1 = calc.calc_car_cap(gr1, pop1, pc1)

        pop2 = newFiles.getYAxisList2()
        pc2 = calc.population_change(pop2)
        lastpcval2 = pc2[-1] # get the last value in the list
        pc2.append(lastpcval2)
        gr2 = calc.growth_rate(pop2)
        lastgrval2 = gr2[-1] # Get the last value in the list
        gr2.append(lastgrval2)
        cc2 = calc.calc_car_cap(gr2, pop2, pc2)
        
        if titleEntry.get() == '': # Title is auto generated from plot names if no user input is given
            plt.title(entryFile1.get() + " vs " + entryFile2.get())
        else:
            title = titleEntry.get()
            plt.title(title)

        plt.grid(True)
        
        plt.plot(newFiles.getXAxisList1(),newFiles.getYAxisList1(), label = entryFile1.get(), color = "black") # Plot data from file 1 population numbers       
        
        plt.plot(newFiles.getXAxisList1(), cc1, label = entryFile1.get() + " Carrying Capacity", color = "blue", linestyle = 'dotted') # Plot carrying capacity data for species 1
       
        plt.plot(newFiles.getXAxisList2(),newFiles.getYAxisList2(), label = entryFile2.get(), color = "green") # Plot data from file 2 population numbers       
        
        plt.plot(newFiles.getXAxisList2(), cc2, label = entryFile2.get() + " Carrying Capacity", color = "red", linestyle = 'dotted') # Plot carrying capacity data for species 1
        
        plt.xlabel(newFiles.getXAxisName1()) # Axis labels # Axis labels
        plt.ylabel(newFiles.getYAxisName2())

        plt.legend(loc="upper right") # Display graph legend

        plt.show() 

    elif combobox.get() == "Correlation Coefficient":
        
        cor_coef, coef_rounded, coef_str = calc.correlation_coefficient(newFiles.yAxisList1, newFiles.yAxisList2)

        if titleEntry.get() == '':
            plt.title(entryFile1.get() + " vs " + entryFile2.get())
        else:
            title = titleEntry.get()
            plt.title(title)

        plt.grid(True)
        
        plt.plot(newFiles.xAxisList1,newFiles.yAxisList1, label = entryFile1.get(), color = "black") # Plot data from file 1 population numbers       
       
        plt.plot(newFiles.xAxisList2,newFiles.yAxisList2, label = entryFile2.get(), color = "green") # Plot data from file 2 population numbers       
        
        plt.figtext(0.5, 0.03, coef_str, ha="center", va="center", fontsize=14, bbox={"facecolor":"white", "alpha":0.5})

        plt.xlabel(newFiles.xAxisName1) # Axis labels # Axis labels
        plt.ylabel(newFiles.yAxisName2)

        plt.legend(loc="upper right") # Display graph legend

        plt.show() 

    elif combobox.get() == "Standard Deviation + Mean":

        sd1, sd2, mean1, mean2, sd_mean_str = calc.sd_mean(newFiles.yAxisList1, newFiles.yAxisList2)

        if titleEntry.get() == '':
            plt.title(entryFile1.get() + " vs " + entryFile2.get())
        else:
            title = titleEntry.get()
            plt.title(title)

        plt.grid(True)
        
        plt.plot(newFiles.xAxisList1,newFiles.yAxisList1, label = entryFile1.get(), color = "black") # Plot data from file 1 population numbers       
       
        plt.plot(newFiles.xAxisList2,newFiles.yAxisList2, label = entryFile2.get(), color = "green") # Plot data from file 2 population numbers       
        
        plt.figtext(0.5, 0.03, sd_mean_str, ha="center", va="center", fontsize=14, bbox={"facecolor":"white", "alpha":0.5})

        plt.xlabel(newFiles.xAxisName1) # Axis labels # Axis labels
        plt.ylabel(newFiles.yAxisName2)

        plt.legend(loc="upper right") # Display graph legend

        plt.show() 

########################### Tkinter GUI #####################################

app = customtkinter.CTk()
app.geometry(f"{700}x{860}x{0}x{0}") # - GUI dimensions
app.title("New Graph") # - GUI window title

customtkinter.set_appearance_mode("dark")

# Frame 1 ------------------------------------------------------------------------------------------------------

frame1 = customtkinter.CTkFrame(app, width=550, height=100, corner_radius=10)
frame1.pack(ipadx=40, pady=10)

file1Button = customtkinter.CTkButton(master=frame1, text="Select Files To Compare", command=fileButton1)
file1Button.grid(column=0, row=0, padx=60, pady=20, sticky="w")

entryFile1 = customtkinter.CTkEntry(master=frame1, placeholder_text="Plot 1 Name")
entryFile1.grid(column=1, row=0, padx=60, pady=10, sticky="e")

labelFile1 = customtkinter.CTkLabel(master=frame1, text="")
labelFile1.grid(column=0, row=1, columnspan=2)

entryFile2 = customtkinter.CTkEntry(master=frame1, placeholder_text="Plot 2 Name")
entryFile2.grid(column=1, row=3, padx=20, pady=10)

labelFile2 = customtkinter.CTkLabel(master=frame1, text="")
labelFile2.grid(column=0, row=4, columnspan=2)

# -------------------------------------------------------------------------------------------------------------

frame2 = customtkinter.CTkFrame(app, width=550, height=100, corner_radius=10)
frame2.pack(pady=10, ipadx=140)

titleEntry = customtkinter.CTkEntry(master=frame2, placeholder_text="Enter Graph Title")
titleEntry.pack(pady=20, ipadx=100)

# ------------------------------------------------------------------------------------------------------------

frame3 = customtkinter.CTkFrame(app, width=550, height=100, corner_radius=10)
frame3.pack(pady=10, ipadx=10)

# --------------------------------------------------

plot1XAxisLabel = customtkinter.CTkLabel(master=frame3, text="Plot 1 X")
plot1XAxisLabel.grid(column=0, row=1)

plot1XAxisBox = customtkinter.CTkEntry(master=frame3, placeholder_text="")
plot1XAxisBox.grid(column=1, row=1, padx=130, pady=10)

# --------------------------------------------------

plot1YAxisLabel = customtkinter.CTkLabel(master=frame3, text="Plot 1 Y")
plot1YAxisLabel.grid(column=0, row=2)

plot1YAxisBox = customtkinter.CTkEntry(master=frame3, placeholder_text="")
plot1YAxisBox.grid(column=1, row=2, padx=160, pady=10)

# --------------------------------------------------

plot2XAxisLabel = customtkinter.CTkLabel(master=frame3, text="Plot 2 X")
plot2XAxisLabel.grid(column=0, row=3)

plot2XAxisBox = customtkinter.CTkEntry(master=frame3, placeholder_text="")
plot2XAxisBox.grid(column=1, row=3, padx=160, pady=10)

# --------------------------------------------------

plot2YAxisLabel = customtkinter.CTkLabel(master=frame3, text="Plot 2 Y")
plot2YAxisLabel.grid(column=0, row=4)

plot2YAxisBox = customtkinter.CTkEntry(master=frame3, placeholder_text="")
plot2YAxisBox.grid(column=1, row=4, padx=160, pady=10)

# Frame 4 ---------------------------------------------------------------------------------------------

frame4 = customtkinter.CTkFrame(app, width=550, height=100, corner_radius=10)
frame4.pack(padx=20, pady=10, ipadx=150, ipady=10)

calcLabel = customtkinter.CTkLabel(master=frame4, text="Select Calculation To Display")
calcLabel.pack(padx=10, pady=20)

combobox = customtkinter.CTkComboBox(master=frame4, values=["None", "Carrying Capacity", "Correlation Coefficient", "Standard Deviation + Mean"], command=None)
combobox.pack(padx=60, pady=10, ipadx=30)
combobox.set("None")  # set initial value

# Frame 5 --------------------------------------------------------------------------------------------

frame5 = customtkinter.CTkFrame(app, width=550, height=100, corner_radius=10)
frame5.pack(pady=10, ipadx=150)

genGraphButton = customtkinter.CTkButton(master=frame5, text="Generate Graph", command=genGraph)
genGraphButton.pack(padx=50, pady=20, ipadx=40, ipady=40)

# ----------------------------------------------------------------------------------------------------
frame6 = customtkinter.CTkFrame(app, width=550, height=100, corner_radius=10)
frame6.pack(pady=10, ipadx=125, ipady=10)

footerLabel = customtkinter.CTkLabel(master=frame6, text="Distributed under the MIT Licence, Copyright Simon Chalder 2022")
footerLabel.pack()

app.mainloop()

