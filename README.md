# Graphing_App
 
## Purpose

This application is intended to provide a way of comparing statistical data in a graphical manner. It is intended to be used with wildlife and ecological data but can be used to display any data in an appropriate format. 

## Usage

The user is able to select two data files to compare. The application will pull column data from a csv file to populate axis data but this can be customised if needed. A title can be given to the project but a title will be automatically generated based on axis data if no title is given by the user. Various calculations or methods of comparison can then be chosen from and the data displayed graphically. Currently the user may choose from displaying Population / Carrying Capacity, Correlation Coefficient Data, or Standard Deviation and Mean Data. CSV files should contain x axis data in column 1 and y axis data in column 2. Column headings in row 1 will be used by the application to autofill axis names.

## Screenshots

![1](https://user-images.githubusercontent.com/66743889/200188676-51f03932-7dbe-468e-8d9b-7ac58c7fa702.png)
![2](https://user-images.githubusercontent.com/66743889/200188683-c48c73d9-5cf5-49fb-8e48-875c4af57110.png)
![3](https://user-images.githubusercontent.com/66743889/200188691-c6af8a2f-9072-4835-9fce-0438ae1bbaed.png)
![4](https://user-images.githubusercontent.com/66743889/200188697-10e916bb-eb2a-4a1e-af23-66f120d695d2.png)
![5](https://user-images.githubusercontent.com/66743889/200188699-ad1a3231-a333-48d4-9122-bbc2284b2f79.png)


## TO-DO

- [ ]  Improvements to error handling and testing
- [ ]  Test with more real life datasets
- [ ]  Add more statistical calculations (R-Squared etc)
- [ ]  Improvements to GUI and graph apprearance

## Notes

This application is written in Python and utilises the following libraries:

- NumPy - https://github.com/numpy/numpy
- Matplotlib - https://github.com/matplotlib/matplotlib
- Pandas - https://github.com/pandas-dev/pandas
- Tkinter - https://github.com/ParthJadhav/Tkinter-Designer
- CustomTkinter - https://github.com/TomSchimansky/CustomTkinter/wiki


Carrying capacity calculations are made using the formula:

K = r * N * (1-N) / CP

found at https://www.calculatorapp.org/carrying-capacity-calculator/index.html
