#!/usr/bin/env python3

import random
import string
from tabulate import tabulate

# Define data tables
column_labels = [
    'Band name',
    'Start of range',
    'Range unit',
    'End of range',
    'Range unit'
]

band_ranges = [
    [ 'VLF', '3', 'kHz', '30', 'kHz' ],
    [ 'LF', '30', 'kHz', '300', 'kHz' ],
    [ 'MF', '300', 'kHz', '3', 'MHz' ],
    [ 'HF', '3', 'MHz', '30', 'MHz' ],
    [ 'VHF', '30', 'MHz', '300', 'MHz' ],
    [ 'UHF', '300', 'MHz', '3', 'GHz' ],
    [ 'SHF', '3', 'GHz', '30', 'GHz' ],
    [ 'EHF', '30', 'GHz', '300', 'GHz' ],
]

# Get worksheet difficulty
difficulty = int(input('Difficulty (1 = easy, 2 = medium, 3 = hard, 4 = random): '))

if difficulty is 1:
    entries_to_remove = 5
elif difficulty is 2:
    entries_to_remove = 10
elif difficulty is 3:
    entries_to_remove = 20
elif difficulty is 4:
    entries_to_remove = random.randint(5, 20)
else:
    print("Warning: Unrecognized difficulty, defaulting to easy")
    entries_to_remove = 5

#print('Removing %d entries...' % entries_to_remove)

# Get number of tables to generate
tables_to_generate = int(input('Tables to generate (1-10): '))

if tables_to_generate > 10:
    tables_to_generate = 10

#print('Generating %d tables...' % tables_to_generate)

# Get whether or not to write to file
write_to_file = input('Write to file? (Y/N): ')

if write_to_file is 'Y' or write_to_file is 'y':
    write_to_file = True
elif write_to_file is 'N' or write_to_file is 'n':
    write_to_file = False
else:
    print('Warning: Unrecognized choice, defaulting to no')
    write_to_file = False

if write_to_file:
    filename = 'worksheet_' + ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)) + '.txt'

# Remove entries from band ranges table
band_ranges_array_size = sum(len(band_range) for band_range in band_ranges)

for x in range(0, tables_to_generate):
    band_ranges_copy = band_ranges

    for y in range(0, entries_to_remove):
        entry_to_remove = random.randint(0, band_ranges_array_size)
        row_to_remove = entry_to_remove // len(band_ranges_copy[0]) - 1
        column_to_remove = entry_to_remove % len(band_ranges_copy[0]) - 1
        band_ranges_copy[row_to_remove][column_to_remove] = ''

    # Print table or write to file
    table_string = '\n' + tabulate(band_ranges_copy, headers=column_labels, tablefmt='orgtbl') + '\n\n'

    if write_to_file:
        with open(filename, 'a') as worksheet_file:
            worksheet_file.write(table_string)
    else:
        print(table_string)
