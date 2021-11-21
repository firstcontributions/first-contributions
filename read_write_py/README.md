# Simple Read Write operations from a file using Python
## Pre-requisites
- Python v3.6 or above

## Instructions to run the program
### Linux / Mac OS
- From termial, navigate to the folder where the .py file is located and run the below command.
- `python3 <file_name>.py`

### Windows
- From Command Prompt, navigate to the folder where the .py file is located and run the below command.
- `python <file_name>.py`

## Execution
- Acceptables input for system prompts - Y or N.
- When the program is executed,
    - System will prompt user if they want to add any data to the text file.
    - System will prompt user if they want to view the contents of the text file.
### Adding data to text file
- If User enters Y to the system prompt for adding text file,
    - System checks if a text file names 'todos.txt' exists.
        - If it exists, then it prompts the user to add input to the file.
        - If it does not exist, then it creates a 'todos.txt'and prompts the user to add input.
    - Once User has added their text, system displays a success message, and then prompts the User if they want to vire the text file's content.

### Viewing data from text file
- If User wants to view the text added to the file, or simply view the existing contents of the file, enter Y.


