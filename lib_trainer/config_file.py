#!/usr/bin/env python3

###############################################################################
# This file contains the functionality creating the config file for rulesets
#
# Note, in the past I tried to make this generic so that when a new grammar
# rule was added to the trainer, no changes would have to be made to the
# config file generation code. This didn't work out as well as I wanted,
# so to save time and reduce complexity this config file code needs to be
# updated when the grammar generated by the trainer is modified
#
###############################################################################


from configparser import ConfigParser
import os
import json


## Adds the program details to the config file
#
#
# Variables:
#
#     config: the config file being created
#
#     program_info: Info about the program and config info about the current run
#
def add_program_details(config, program_info):

    section = "TRAINING_PROGRAM_DETAILS"
    config.add_section(section)
    
    config.set(section, "contact", program_info['contact'])
    config.set(section, "author", program_info['author'])
    config.set(section, "contact", program_info['contact'])
    config.set(section, "program", program_info['name'])
    config.set(section, "version", program_info['version'])
    
    
## Adds the details from the training dataset to the config file
#
#
# Variables:
#
#     config: the config file being created
#
#     program_info: Info about the program and config info about the current run
#
#     file_input: Info from the input dataset after parsing
#
def add_dataset_details(config, program_info, file_input):

    section = "DATASET_DETAILS"
    config.add_section(section)
    
    config.set(section, "comments", program_info['comments'])
    config.set(section, "filename", program_info['training_file'])
    config.set(section, "encoding", program_info['encoding'])
    config.set(section, "number_of_passwords_in_set", str(file_input.num_passwords))
    config.set(section, "number_of_encoding_errors", str(file_input.num_encoding_errors))
    
    
## Creates the configuration for the base structure
#
# Note, if any new terminal/non-terminal replacements get added this will 
# likely need to be updated.
#
# For example, if you add a new replacement for "sports teams" being a "T"
#
#
# Variables:
#
#     config: the config file being created
#
def add_start(config):

    replacements = [
        {"Config_id": "BASE_A", "Transition_id": "A"}, # Alpha
        {"Config_id": "BASE_D", "Transition_id": "D"}, # Digits
        {"Config_id": "BASE_O", "Transition_id": "O"}, # Other
        {"Config_id": "BASE_K", "Transition_id": "K"}, # Keyboard combos
        {"Config_id": "BASE_X", "Transition_id": "X"}, # ConteXt Sensitive replacements
        {"Config_id": "BASE_Y", "Transition_id": "Y"}, # Years
        
        ]

    section = "START"
    config.add_section(section)
    
    config.set(section, "name", "Base Structure")
    config.set(section, "function", "Transparent")
    config.set(section, "directory", "Grammar")
    config.set(section, "comments", "Base structures as defined by the original PCFG Paper, with some renaming to prevent naming collisions. Examples are A4D2 from the training word pass12")
    config.set(section, "file_type", "Flat")
    config.set(section, "inject_type", "Wordlist")
    config.set(section, "is_terminal", str(False))
    config.set(section, "replacements", json.dumps(replacements))
    config.set(section, "filenames", "Grammar.txt")
        
        
## Creates the configuration for the Alpha Replacements
#
#
# Variables:
#
#     config: the config file being created
#
#     filenames: A list of filenames associated with this replacement
#
def add_alpha(config, filenames):

    section = "BASE_A"
    config.add_section(section)
    
    config.set(section, "name", "A")
    config.set(section, "function", "Shadow")
    config.set(section, "directory", "Alpha")
    config.set(section, "comments", "(A)lpha letter replacements for base structure. Aka pass12 = A4D2, so this is the A4. Note, this is encoding specific so non-ASCII characters may be considered alpha. For example Cyrillic characters will be considered alpha characters")
    config.set(section, "file_type", "Length")
    config.set(section, "inject_type", "Wordlist")
    config.set(section, "is_terminal", str(False))
    config.set(section, "filenames", json.dumps(filenames))     
    

## Creates the configuration for the Digit Replacements
#
#
# Variables:
#
#     config: the config file being created
#
#     filenames: A list of filenames associated with this replacement
#
def add_digits(config, filenames):

    section = "BASE_D"
    config.add_section(section)
    
    config.set(section, "name", "D")
    config.set(section, "function", "Copy")
    config.set(section, "directory", "Digits")
    config.set(section, "comments", "(D)igit replacement for base structure. Aka pass12 = L4D2, so this is the D2")
    config.set(section, "file_type", "Length")
    config.set(section, "inject_type", "Copy")
    config.set(section, "is_terminal", str(True))
    config.set(section, "filenames", json.dumps(filenames))   


## Creates the configuration for the Other Replacements
#
#
# Variables:
#
#     config: the config file being created
#
#     filenames: A list of filenames associated with this replacement
#
def add_other(config, filenames):

    section = "BASE_O"
    config.add_section(section)
    
    config.set(section, "name", "O")
    config.set(section, "function", "Copy")
    config.set(section, "directory", "Other")
    config.set(section, "comments", "(O)ther character replacement for base structure. Aka pass$$ = L4S2, so this is the S2")
    config.set(section, "file_type", "Length")
    config.set(section, "inject_type", "Copy")
    config.set(section, "is_terminal", str(True))
    config.set(section, "filenames", json.dumps(filenames))  


## Creates the configuration for Keyboard Replacements
#
#
# Variables:
#
#     config: the config file being created
#
#     filenames: A list of filenames associated with this replacement
#
def add_keyboard(config, filenames):

    section = "BASE_K"
    config.add_section(section)
    
    config.set(section, "name", "K")
    config.set(section, "function", "Copy")
    config.set(section, "directory", "Keyboard")
    config.set(section, "comments", "(K)eyboard replacement for base structure. Aka test1qaz2wsx = L4K4K4, so this is the K4s")
    config.set(section, "file_type", "Length")
    config.set(section, "inject_type", "Copy")
    config.set(section, "is_terminal", str(True))
    config.set(section, "filenames", json.dumps(filenames)) 


## Creates the configuration for Conte(X)t Sensitive Replacements
#
#
# Variables:
#
#     config: the config file being created
#
#     filenames: A list of filenames associated with this replacement
#
def add_context_sensitive(config, filenames):

    section = "BASE_X"
    config.add_section(section)
    
    config.set(section, "name", "X")
    config.set(section, "function", "Copy")
    config.set(section, "directory", "Context")
    config.set(section, "comments", "conte(X)t sensitive replacements to the base structure. This is mostly a grab bag of things like #1 or ;p")
    config.set(section, "file_type", "Length")
    config.set(section, "inject_type", "Copy")
    config.set(section, "is_terminal", str(True))
    config.set(section, "filenames", json.dumps(filenames))


## Creates the configuration for Year Replacements
#
#
# Variables:
#
#     config: the config file being created
#
#     filenames: A list of filenames associated with this replacement
#
def add_years(config, filenames):

    section = "BASE_Y"
    config.add_section(section)
    
    config.set(section, "name", "Y")
    config.set(section, "function", "Copy")
    config.set(section, "directory", "Years")
    config.set(section, "comments", "Years to replace with")
    config.set(section, "file_type", "Flat")
    config.set(section, "inject_type", "Copy")
    config.set(section, "is_terminal", str(True))
    config.set(section, "filenames", json.dumps(filenames))    


## Creates the configuration for Capitalization Replacements
#
#
# Variables:
#
#     config: the config file being created
#
#     filenames: A list of filenames associated with this replacement
#
def add_capitalization(config, filenames):

    section = "CAPITALIZATION"
    config.add_section(section)
    
    config.set(section, "name", "Capitalization")
    config.set(section, "function", "Capitalization")
    config.set(section, "directory", "Capitalization")
    config.set(section, "comments", "apitalization Masks for words. Aka LLLLUUUU for passWORD")
    config.set(section, "file_type", "Length")
    config.set(section, "inject_type", "Copy")
    config.set(section, "is_terminal", str(True))
    config.set(section, "filenames", json.dumps(filenames))


## Creates the config file and returns it
#
#
# Variables:
#
#     program_info: Info about the program and config info about the current run
#     
#     file_input: Contains info about the passwords just parsed
#
# Returns:
#
#    config: The Python ConfigParser configuration to save for this rulesets
#
def create_config_file(program_info, file_input):

    # Using Python's ConfigParser since it's the most standard built in
    # function to do this
    config = ConfigParser()
    
    add_program_details(config, program_info)
    
    add_dataset_details(config, program_info, file_input)
    
    add_start(config)
    
    add_alpha(config,["file1.txt","file2.txt"])
    
    add_digits(config,["file1.txt","file2.txt"])
    
    add_other(config,["file1.txt","file2.txt"])
    
    add_keyboard(config,["file1.txt","file2.txt"])
    
    add_context_sensitive(config,["file1.txt","file2.txt"])
    
    add_years(config,["file1.txt","file2.txt"])
    
    add_capitalization(config,["file1.txt","file2.txt"])
    
    # print({section: dict(config[section]) for section in config.sections()})
    
    return config
    
    
## Creates the config file and then saves it to disk
#
#
# Variables:
#
#     directory_name: The full name of the rules directory
#
#     program_info: Info about the program and config info about the current run
#     
#     file_input: Contains info about the passwords just parsed
#
# Returns:
#
#    True: If everything worked correctly
#
#    False: If any errors were encountered
#
def save_config_file(directory_name, program_info, file_input):

    # Create the configuration file
    try:
        config = create_config_file(program_info, file_input)
    except Exception as msg:
        print("Exception Encountered: " + str(msg))
        return False
    
    # Save the configuration file
    try:
        with open(os.path.join(directory_name,"config.ini"), 'w') as configfile:
            config.write(configfile)
            
    except IOError as error:
        print (error)
        print ("Error opening file " + os.path.join(directory_name,"config.ini"))
        return False
    
    return True    