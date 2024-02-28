# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import xml.etree.ElementTree as ET
from pathlib import Path


def formula_and_number_extractor(file):
    #
    try:
        card = ET.parse(file)
    except:
        f = open("Errors log.txt", "w")
        f.write("Failed to parse " + str(file) + '  Please delete it from the directory')
        f.close()
        print ("Failed to parse " + str(file) + '  Please delete it from the directory')
    else:
        print ('Card with number' + str(file) + "Is ok")

        root = card.getroot()

        for cell_parameters in root.iter('pdf_data'):
            chemical_formula = cell_parameters.find('chemical_formula').text
            pdf_number = cell_parameters.find('pdf_number').text
            formula_number = chemical_formula + ' - ' + pdf_number
        return (formula_number)


def update_phase_list():
    formula_number = list()

    phases_list = open('phases_list.txt', 'w')

    # iteration through the files in directory and writing
    for item in list(Path('.').glob('*.xml')):
        if formula_and_number_extractor(item) != None:
            formula_number.append(formula_and_number_extractor(item))

    formula_number.sort()

    for item in formula_number:
        phases_list.write(item + '\n')

    phases_list.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # function testing with one file
    update_phase_list()

    # .glob testing to check files in the directory
    #print(list(Path('.').glob('*.xml')))