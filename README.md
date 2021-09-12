# cs166-assignment1
Vincent Moeykens
### Python Standard and Modules Used
Python 3.8, and no modules besides those in the standard library. 


### Running
This program **must** be run as a Python module. To do this, `cd` into the root of this project and run the following 
command: `python -m login_system.main`. This will run the program with the default flags (no debug output and a default
path to the user file). You have additional parameters that can be passed to the program via the command line and those 
are documented below:
```
$ python -m login_system.main -h
usage: main.py [-h] [-d] [-f FILE]

Run the authentication system

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Print Debug output when loading users.
  -f FILE, --file FILE  Path to users file. Default is login_system/data/user_list.csv
  ```
 If you see the help page as displayed above, your directory and environment are set up correctly. You may now run the 
main module with 

### Testing
To test this program, pick a user file that you would like to use (`user_list.csv`, or `large_user_list.csv`, or make 
your own!), and run `python -m login_system.main --file={PATH_TO_FILE}` or simply `python -m login_system.main` if you 
would like to use the default user list. Now, you will be prompted to input a username. The username prompt will stay 
up until you forcibly exit the program or enter a correct username. Once a correct username has been entered, the password
prompt will stay up until you enter a valid password for the selected user. Once you have fully logged in, you will be
presented with a menu to select different areas to go to. Try to select different areas; if you are not allowed in a 
certain area a message will be displayed. When finished, select `1` to exit the program. 

### Program Decisions
The following are some general decisions made when implementing this program
#### General Structure
This program is set up as a module. The main module creates an `AuthenticationSystem` object that holds all the users
and all the possible sub-programs. This object will then run all the appropriate menus for logging in and selecting a 
sub-program to run. When a sub-program is selected, it will validate the user that is trying to access it with the 
sub-program's `AccessPolicy`. This class holds all the appropriate levels that should be allowed to access a sub-program.
#### Access Policies
We default to allowing an `admin` to access *all* sub-programs. The only other levels are `user` and `guest`. 
#### Parsing user file
The user file is a `csv` file that contains four columns: A User's full name, their username, their plaintext password, 
and a string representation of their access level (`admin`, `user`, or `guest`). When parsing the csv file, we strip 
whitespace from all columns except the full name. Any characters are allowed in usernames and passwords.
#### Login Theory
We will prompt for usernames and passwords until valid. For now, there is no limit on the number of login attempts.
We also tell at the prompt if the user is not valid (this may not be the best security practice, but for now it's a 
good debug tool)

### Creation of `large_user_list.csv` file. 
The website: https://mockaroo.com/ was used to create the large list of fake users. 

### Python Coding Standard
PEP-8 Followed throughout with (generally) reStructuredText-style docstrings to outline parameters and return types. 
Python type hints are included throughout as well. 