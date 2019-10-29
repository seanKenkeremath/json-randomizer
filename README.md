# json_randomizer
Python script to randomize static JSON 

## Running

This script must be run with Python3

`python3 randomize.py {path_to_json_file} {number between 0-1} {optional output file}`

If you are running a version of python greater than 3.0 you can just use `python` instead of `python3`

The second parameter is the percentage of leaves (primitive json nodes) that should be randomized. "0.5" will result in half of all leaves being randomized.

If the third parameter is omitted the script will overwrite the source json file with the modified version

## Results

The file passed in will be overwritten with changes if no third parameter is passed in. If an outputfile is specified as the third parameter the source file will be left in tact and the modified file will be written to the specified file 

The script will produce a `{outputfile}.paths.txt` file that catalogues all changes made to the .json file

## TODO

* Configuration file to specify specific fields to change or exclude
* Ability to pass in multiple files at once
