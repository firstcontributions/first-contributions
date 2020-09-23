contributors = list()
with open('Contributors.md') as file:
    for line in file:
        new_line = line.replace("- ", " ")
        contributors.append(new_line.strip())

contributors.sort()
substring = "#"
file_name = 'contributors.md'
with open (file_name, 'w') as fout:
    for line in contributors:
        if substring in line:
            fout.write(line+"  \n")
        else:
            fout.write("* "+line+"  \n")