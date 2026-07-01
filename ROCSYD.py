# Select the number m of attribute for each container n
m = 4

# Open input file (put the folder location instead of "...)"

with open('C://Users/.../input.txt', 'r') as data:

# Read the input file

    raw_data = data.read()
    data.close()

# Crate a list considering the separator

attributes = raw_data.split(';')
attributes_list = list(map(float, attributes))

# Total number of entries

nt = len(attributes_list)

# Open output file (put the folder location instead of "...")

with open('C://Users/.../output.txt', 'w') as output:

# Write into output file with the correct format
    for i in range(0,nt,m):
        output_format = attributes_list[i:i+m]
        attributes_format = "; ".join(map(str, output_format)) + "\n"
        output.write(attributes_format)

output.close()