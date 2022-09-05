output = []

# Read file2 into a list
# strips new line character from each line
with open( < path to file 2 > ) as f:
    matches = [i.strip() for i in f]

# Iterate over file1 and place any matches into the output.
with open( < path to file 1 > ) as f:
    for i in f:
        match = i.split(',')[-1].strip()
        if any(match == j for j in matches):
            output.append(i)

# print the output list to a file
with open( < path to output file >, 'w') as output_file:
    output_file.write("\n".join(output))
