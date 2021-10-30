'''Matrix creator'''
from numpy import zeros

def matrix(lines, rows, link_key, name):
    try:
        matrix = bin_matrix2(lines, rows, link_key)
    except:
        matrix = bin_matrix(lines, rows, link_key)
    file_name = F"matrix/{name}_matrix.csv"
    write_csv(lines, rows, matrix, file_name)
    return matrix


def write_csv(lines, rows, matrix, file_name):
    # Write csv file
    f = open(file_name, 'w')
    f.write(" ")
    for row in rows:
        f.write(F", {row['verbose_name']}")
    f.write("\n")
    f.close()
    f = open(file_name, 'a')
    i=0
    for line in lines:
        try:
            f.write(F"{line.name} ")
        except:
            pass
        try:
            f.write(F"{line['verbose_name']} ")
        except:
            pass
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

def bin_matrix2(lines, rows, link_key):
    n_lines = len(lines)
    n_rows = len(rows)
    matrix = zeros([n_lines, n_rows])

    i = 0
    for line in lines:
        j = 0
        if line.get('links'):
            for row in rows:
                for link in line['links']:
                    if (link.get(link_key) and (link[link_key] == row['name'])):
                        matrix[i, j] = 1
                j += 1
        i+=1
    return matrix
