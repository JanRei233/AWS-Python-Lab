# AWS re/Start Program Python Laboratories

This repository contains completed Python laboratory exercises from the AWS re/Start program. The labs utilize Python 3.x and cover fundamental programming concepts, data structures, flow control, and practical scientific computing applications.

## 🛠 General Environment Setup (For All Labs)

For every lab in this repository, follow these standard initialization steps:
1. **Access the IDE:** Start your AWS lab environment and wait for the "Lab status: ready" message. Choose AWS to open the Management Console, then copy the `LabIDEURL` and `LabIDEPassword` to open the VS Code IDE in a new browser tab.
2. **Create the File:** In VS Code, choose **File > New File**, then **File > Save As...** to save your `.py` exercise file under the `/home/ec2-user/environment` directory.
3. **Open Terminal:** Choose **Terminal > New Terminal** from the menu bar. Type `pwd` to confirm you are in the `/home/ec2-user/environment` directory.
4. **Execute Code:** Run your scripts using `python3 <filename>.py`.

---

## 📚 Laboratory Instructions & Exercises

### Lab 1: Creating a Hello, World Program
* **Exercise 1 (Introducing Python):** Check your installed Python versions by running `python --version`, `python2 --version`, and `python3 --version` in the terminal.
* **Exercise 2 (First Program):** Inside your Python file, write `print("Hello, World")`, save it, and run it to verify your environment is working.

### Lab 2: Working with Numeric Data Types
* **Exercise 1 (Python Shell):** Open the shell by typing `python3`. Practice basic math: `2 + 2`, `4 - 2`, `2 * 2`, and `4 / 2`. Exit using `quit()`.
* **Exercise 2 (int):** Create a variable `myValue=1`. Print the value, print its type using `type()`, and print a concatenated string using `str()` to convert the integer.
* **Exercise 3 (float):** Update the variable to a float `myValue=3.14` and print its value, type, and concatenated string.
* **Exercise 4 (complex):** Update the variable to a complex number `myValue=5j` and print its value, type, and concatenated string.
* **Exercise 5 (bool):** Update the variable to `myValue=True`, print its details, and then repeat the process for `myValue=False`.

### Lab 3: Working with the String Data Type
* **Exercise 1 (Strings):** Define `myString = "This is a string."` and print its value and data type.
* **Exercise 2 (Concatenation):** Create `firstString = "water"` and `secondString = "fall"`, then concatenate them using the `+` operator into `thirdString` and print it.
* **Exercise 3 (Input):** Use `name = input("What is your name? ")` to pause the script and gather user input, then print the result.
* **Exercise 4 (Formatting):** Gather `color` and `animal` inputs from the user. Use the `.format()` function to print: `print("{}, you like a {} {}!".format(name,color,animal))`.

### Lab 4: Working with Lists, Tuples, and Dictionaries
* **Exercise 1 (Lists):** Define a mutable list `myFruitList = ["apple", "banana", "cherry"]`. Print the whole list and its type, then access items individually by position (0, 1, 2). Change the third item by assigning `myFruitList[2] = "orange"` and reprint the list.
* **Exercise 2 (Tuples):** Define an immutable tuple `myFinalAnswerTuple = ("apple", "banana", "pineapple")`. Print the tuple, its type, and access its items by position.
* **Exercise 3 (Dictionaries):** Define a dictionary with key-value pairs: `myFavoriteFruitDictionary = {"Akua" : "apple", "Saanvi" : "banana", "Paulo" : "pineapple"}`. Access the values using their specific names (e.g., `myFavoriteFruitDictionary["Akua"]`).

### Lab 5: Categorizing Values
* **Exercise 1 (Mixed-type List):** Define a list containing multiple data types: `myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]`. Use a `for` loop to traverse the list and print the data type of each item using `.format(item, type(item))`.

### Lab 6: Working with Composite Data Types
* **Exercise 1 (CSV to Memory):** Create a `car_fleet.csv` file with vehicle data. Import the `csv` and `copy` modules. Define a `myVehicle` dictionary with empty keys. Use `with open('car_fleet.csv') as csvFile:` to read the data, skipping the header line. For each row, create a deep copy of the dictionary using `copy.deepcopy(myVehicle)`, assign the row values to the dictionary keys, and append it to an empty `myInventoryList`. Finally, use nested `for` loops to iterate through the list and print the keys and values.

### Lab 7: Working with Conditionals
* **Exercise 1 (if):** Ask the user `input("Do you need to ship a package? (Enter yes or no) ")`. Use `if userReply == "yes":` to print a confirmation.
* **Exercise 2 (else):** Add an `else:` statement to handle situations where the user does not want to ship a package.
* **Exercise 3 (elif):** Expand the script to offer stamps, envelopes, or copies using `elif userReply == "stamps":` and similar conditions. For copies, use a nested input to ask for the number of copies.

### Lab 8: Working with Loops
* **Exercise 1 (while loop):** Import the `random` module and generate a number using `number = random.randint(1,10)`. Set `isGuessRight = False` and create a `while isGuessRight != True:` loop that continually asks the user for a guess, checking if `int(guess) == number`.
* **Exercise 2 (for loop):** Create a new script that uses `for x in range (0, 11): print(x)` to count to 10.

### Lab 9: Creating a Git Repository
* **Exercises 1-5:** Download your completed lab files, create an account on `github.com`, create a private repository named `aws_restart` initialized with a README, upload your files via the web interface, and download the repository as a ZIP file to your local machine.

### Lab 10: Preparing to Analyze Insulin with Python
* **Exercise 1 (Retrieval):** Search NCBI for "human insulin", copy the sequence starting with `ORIGIN` to a file named `preproinsulin-seq.txt`.
* **Exercise 2 (Cleaning):** Manually or programmatically remove numbers, spaces, slashes, and headers to create a 110-character clean sequence in `preproinsulin-seq-clean.txt`. Create separate files for the signal sequence (amino acids 1–24), b-chain (25–54), c-chain (55–89), and a-chain (90–110).

### Lab 11: String Sequence and Numeric Weight of Insulin
* **Exercises 1-4:** Assign the cleaned sequence chunks to variables (`lsInsulin`, `bInsulin`, `aInsulin`, `cInsulin`). Concatenate the chains using `insulin = bInsulin + aInsulin`. Print the sequences. Implement provided code that uses a dictionary of amino acid weights (`aaWeights`) and the `.count()` method to calculate the rough molecular weight. Calculate the error percentage against the actual weight (5807.63).

### Lab 12: Calculating the Net Charge of Insulin
* **Exercises 1-3:** Create a dictionary `pKR` holding the pKa values of specific amino acids (Y, C, K, H, R, D, E). Use list comprehension and `.count()` to identify the frequency of these amino acids in the sequence. Implement a `while (pH <= 14):` loop containing a mathematical formula to calculate and print the net charge of insulin as the pH increments by 1.

### Lab 13: Using Functions to Implement a Caesar Cipher
* **Exercises 1-6:** Create individual user-defined functions: `getDoubleAlphabet()` to concatenate the alphabet to itself, `getMessage()` for user input, and `getCipherKey()` for the shift amount. Write the `encryptMessage()` function using a `for` loop to find each letter's position and shift it by the key. Write a `decryptMessage()` function that calls the encryption function using a negative key. Finally, write a `runCaesarCipherProgram()` main function that executes them all.

### Lab 14: Creating File Handlers and Modules
* **Exercises 1-3:** Create a file `insulin.json` storing the sequence and weight data. Create a module `jsonFileHandler.py` with a function `readJsonFile()` that utilizes `json.load()` within a `try/except` block to parse the JSON file. In your main script, import the handler, extract the values, and calculate the molecular weight dynamically.

### Lab 15: Introducing System Administration with Python
* **Exercises 1-6:** Import the `os` module and run `os.system("ls")`. Import the `subprocess` module and use `subprocess.run(["ls"])`. Expand the arguments by running `subprocess.run(["ls","-l"])` and `subprocess.run(["ls","-l","README.md"])`. Retrieve system and disk info by running the `uname -a` and `ps -x` commands through subprocesses.

### Lab 16: Using the Debugger
* **Exercises 1-2:** Write a simple script assigning variables. Use the VS Code "Run and Debug" panel. Set red breakpoints by clicking the left gutter, add watch expressions (`name`, `age`), and use the "Step Over" and "Continue" toolbar icons to interactively monitor variable states during execution.

### Lab 17: Debugging the Caesar Cipher Program
* **Exercises 1-4:** Run four provided buggy versions of the Caesar cipher program. Use the interactive Python Debugger (pdb) to analyze tracebacks, identify logical errors (like `TypeError: unsupported operand type(s) for +: 'int' and 'str'`), string casing issues (`.upper()`), and incorrect variable assignments, then fix the code until the program successfully encrypts and decrypts messages.
