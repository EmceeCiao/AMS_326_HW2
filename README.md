# 📌 Setup Instructions

There are two ways of running the programs I've submmited for my AMS 326 HW.      
    1. Running/Downloading the Jupyter Notebook, the .ipynb file which is found in this repository             
    2. Running/Downloading all the .py files found here, there are 3, 2 for the 2 methods in 2.1 and 1 for problem 2.2           

## 🔧 Requirements For Jupyter Notebook 
To run this Jupyter Notebook, you need:
- Python 3.13.1 installed ([Download Python](https://www.python.org/downloads/))
- Jupyter Notebook or VS Code with the Jupyter extension 
    - Personally I recommend doing it with a VSCODE
- Required Python libraries: `numpy, ipykernal, jupyter`

### 📥 Installation Guide + Setup (Jupyter)

To prevent muddling of dependencies do the following, otherwise skip the next two steps: 

1. Create a Virtual Environment:
    ```bash
    python -m venv env
    ```
2. Activate the Virtual Environment:
    - **On Windows:**
      ```bash
      env\Scripts\activate
      ```
    - **On macOS/Linux:**
      ```bash
      source env/bin/activate
      ```

3. If you don't have the required libraries, install them using:
```bash
pip install numpy ipykernal jupyter
```  
 
4. Now you can open up the .ipynb file and scroll through the sections to run and test each part of the code with the inputs that have already been pre-inputted. If you would like to test your own sorts of values inside the program, you must edit the code and change it as seen fit. 

## 🔧 Requirements For Running Python Files + Run Guide
To run my python files you need the following: 
- Python 3.13.1 installed ([Download Python](https://www.python.org/downloads/))
- Required Python libraries: `numpy`  

Instead of one file there are the following 3:  

- rectangle_method.py (Rectangle Method For Problem 2.1)
- trapezoidal_method.py (Trapezoidal Method For Problem 2.1) 

- gaussian.py (Problem 2.2) 

To prevent muddling of dependencies do the following, otherwise skip the next two steps: 

1. Create a Virtual Environment:
    ```bash
    python -m venv env
    ```
2. Activate the Virtual Environment:
    - **On Windows:**
      ```bash
      env\Scripts\activate
      ```
    - **On macOS/Linux:**
      ```bash
      source env/bin/activate
      ```

3. If you don't have the required libraries, install them using:
```bash
pip install numpy
```  

Now to run these files all you need to do is open them in the editor of your choice and run them, there is no command line inputs needed.  

If you are trying to run them through the terminal you can do the following: 
- **On Windows:**
      ```
      py file_name.py
      ```
- **On macOS/Linux:**
      ```
      python3 file_name.py 
      ```  
    
Replace file_name.py with one of the 3 file names and the output will be printed to the terminal! 


