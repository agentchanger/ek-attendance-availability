# ek-attendance-availability
This repository holds a simple Python3 code that helps to filter, group, and create a list of available dates for church volunteers' ministering schedule. It takes in an Excel file (.xlsx) as an input, which is usually the default file output of Google Forms responses, reads the data, and then outputs a .csv file that is much more readable for the attendance admin. 

The file `responses.py` will group available dates into lists, and map each lists with each volunteer's name. The input format has each volunteer's name mapped to their unavailable dates, which is very unreadable for attendance admins. 

Currently, it's still very rigid and very specific to the current church's specific needs. Better optimization is possible in the future and abstractions so that it can serve general purpose needs.

## Setup Guide:


1. Open a new terminal tab (command prompt for Windows users)
2. Run the following commands:
```
    mkdir repo
    cd repo
    git clone https://github.com/agentchanger/ek-attendance-availability.git
    cd ek-attendance-availability
```
3. Install [Python3](https://www.python.org/downloads/) and required libraries by running `pip install requirements.txt`
4. Run `python3 responses.py {excel_filename.xlsx}` where {excel_filename.xlsx} is the name of the file. Make sure the file is in the same folder.
