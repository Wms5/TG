# An Analysis of the Automatic Bug Fixing Performance of Gemini

## Description
to do


## Features

* **Customizable Parameters:** Adjust parameters to fine-tune the output, such as length, tone, and specific keywords.
* **Modular Design:** Easily extendable with custom modules.
* **Command-Line Interface (CLI):** Simple and intuitive CLI.

## Installation

1.  Clone the repository:

    ```bash
    git clone https://github.com/Wms5/TG.git
    cd TG
    ```

## Usage

To run:

1.  Make it Executable:
    * Open a terminal and navigate to the directory where you saved the script.
    * Run the following command to make the script executable:

    ```bash
    chmod +x run.sh
    ```

2.  Run the Script:
    * Now, you can execute the script by providing two arguments: the program name and the execution number. For example:

    ```bash
    ./run.sh program_name 1
    ```
    * program_name is the name of the program you want to test.
    * 1 is the execution number.
    * Replace program_name and 1 with your desired values.


## Example:

If you want to run the bubblesort.py and it is your first execution, you would run

```bash
./run.sh bubblesort 1
```

This will:

1.  Run pytest QuixBugs/python_testcases/test_bubblesort.py.
2.  Run python3 ast_comp.py bubblesort.
3.  Save the combined output of both commands to TG/Results/python_programs_run1/bubblesort/notes.txt.

### Important Notes

1.  Ensure that the directories specified in the output_file path exist, or the script will fail. You may need to create them manually or add commands within the script to create them.
2.  Make sure that pytest and python3 are installed and that ast_comp.py is in the correct location.
3.  Verify that the QuixBugs/python_testcases/test_*.py files exist in the location the script is referencing.
4.  Be aware of the file paths within the script, as they are absolute paths. If you move the script or the project, you'll need to update them.



