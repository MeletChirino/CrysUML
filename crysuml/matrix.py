from numpy import zeros
def matrix(lines, rows, link_key):
    matrix = bin_matrix(lines, rows, link_key)
    file_name = F"matrix/{link_key}_matrix.csv"
    write_csv(lines, rows, matrix, file_name)


def write_csv(lines, rows, matrix, file_name):
    # Write csv file
    f = open(file_name, 'w')
    f.write(" ")
    for row in rows:
        f.write(F", {row['description']}")
    f.write("\n")
    f.close()
    f = open(file_name, 'a')
    i=0
    for line in lines:
        f.write(F"{line.name} ")
        j = 0
        for row in rows:
            if(matrix[i, j] == 1):
                f.write(", X")
            else:
                f.write(", ")
            j += 1
        i += 1
        f.write("\n")
    f.close()

def bin_matrix(lines, rows, link_key):
    n_lines = len(lines)
    n_rows = len(rows)
    matrix = zeros([n_lines, n_rows])

    i = 0
    for line in lines:
        j = 0
        for row in rows:
            for link in line.links:
                if (link.get(link_key) and (link[link_key] == row['name'])):
                    matrix[i, j] = 1
            j += 1
        i+=1
    return matrix
