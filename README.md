## About This

This repository allows to covert a git repository into a PDF file. Based on [repository-to-pdf](https://github.com/Alfareiza/repository-to-pdf), this fork adds merging of all pdf files in a repository and a one command execution script. Note: Only works on Ubuntu 22.04. Support for other operating systems requires modification to the launch script.

## How to use

Git, Pip, Python (^3.8) installed and configured as environment variables.

### 1. Clone the Project

Execute the next command on your terminal:

`git clone https://github.com/constracktor/repo-to-pdf.git`

### 2. Run the script

All dependencies and the python environment are setup automatically.
So, for the magic to happen, execute the next command:

`./convert_repo_to_pdf.sh {path_of_the_directory}`

In case you want to change the theme, you can choose it from the next list and aadd it to the script:

- bw
- sas
- xcode
- autumn
- borland
- arduino
- igor
- lovelace
- pastie
- rainbow_dash
- emacs
- tango
- colorful
- rrt
- algol
- abap
