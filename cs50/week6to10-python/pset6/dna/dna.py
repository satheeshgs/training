import sys
import csv


def main():
    if len(sys.argv) != 3:
        print("missing command-line arguments. Usage: python filename database_name sequence_name")
        exit(1)

    # reading the database as a dictionary and sequence as a string
    with open(sys.argv[1], "r") as db:
        reader = csv.DictReader(db)
        database = list(reader)

    with open(sys.argv[2], "r") as sq:
        sequence = sq.read()

    # print(reader.fieldnames)
    # print(sequence)

    # creating a dictionary to store the values of the highest occurences
    patterns = {}

    for i in range(1, len(reader.fieldnames)):
        patterns['name'] = ''
        pattern = reader.fieldnames[i]
        patterns[pattern] = longest_seq(sequence, pattern)

    # print(patterns)

    # compare the dictionary with the csv file to find out whose dna it is
    keys = reader.fieldnames[1:]
    # print(keys)

    name = ''
    for i in range(len(database)):
        sum = 0
        for key in keys:
            # print(patterns[key], database[i][key])

            if int(patterns[key]) == int(database[i][key]):
                sum += 1

        if sum == len(keys):
            print(database[i]['name'])
            exit(0)

    print("No Match")


def longest_seq(sequence, pattern):
    '''
    returns the longest sequence of a specific pattern
    input: sequence and pattern
    output: longest time the pattern appears in the sequence
    '''
    if pattern not in sequence:
        return 0

    l = len(sequence)
    m = len(pattern)
    max = 0

    for i in range(l):
        count = 0
        if sequence[i: i + m] == pattern:
            j = 0
            while sequence[i + j: i + j + m] == pattern:
                count += 1
                j = j + m

            if count > max:
                max = count

    return max


if __name__ == "__main__":
    main()