'''Virtual Enviroment'''
#Step 1 is to create a virtual Enviroment - PC use py -3 -m venv (name of virtual enviroment)

#Step 2 is to activate the vitrual enviroment - PC use myvenv/Scripts/activate

#Step 3 is to install 3rd party library/module starts with pip3 install (library name)

#To ignore files and folders, create a special file (gitignore file)

'''Reading and Writing Files'''
#if csv file, remember to do import csv and to csv.reader(infile) to read

#the code "next(file_name)" skips the row on a csv file, usually used for skipping the header

#writing to a file is different than printing, to write to a csv file use .write

#csv files are iterable, therefore use a for loop to iterate through rows and index to get certain value

#csv files are imported as lists, be sure to conver to an int or a float if doing calculations

'''Dictionaries'''
#{'Key' : Value}

#doing dictionary_name['key'] will return the corresponding value

#dictionaries are able to do code "if variable in dictionary" to find value

#adding values to dictionary: dictionary_name['new key'] = new_value

#to delete value: del dictionary_name['Key']

#.pop removes a key from a dictionary, if it is present, and returns its value.

#.popitem removes the very last key-value pair from a dictionary.

#.values() iterates through the values of the dictionary

#.keys() iterates through the keys of the dictionary

#keys in dictionaries have to be unique, but values do not have to be 

#.items method allows you to get key and value element at the same time and will print a tuple with key and value

#within a for loop, dict_name[for loop variable] loops through the values

#with json files, you must use .load(infile) in order to work with the file
#.load turns the json file into a list

#dictionaries are MUTABLE and ITERABLE
#when you iterate through a dictionary it only iterates through the keys and not the values of the dict

'''General Notes'''
#adding to a list use .append

#with github, you must write a message and commit the changes to local repsitory BEFORE pushing to github