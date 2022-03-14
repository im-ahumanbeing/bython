from os.path import exists
from sys import argv
from os import system, remove

def string(read, write, index, character):
    write += read[index]
    index += 1
    
    while (read[index] != character):
        if (read[index] == "\\"):
            write += read[index]
            index += 1
        write += read[index]
        index += 1
        
    write += read[index]
    index += 1
        
    return index, write
    
def open_brace(read, write, index, indentation, count):
    indentation += 1

    if (count == 0xffff):
        count = 1
        write += "{"
        index += 1
        return index, write, indentation, count
        
    if (count > 0):
        count += 1
        write += "{"
        index += 1
        return index, write, indentation, count
    
    while (write[-1] in "\n\t "):
        write = write[:-1]

    write += ":"
    index += 1
    return index, write, indentation, count


def close_brace(read, write, index, indentation, count):
    indentation -= 1

    if (count > 0):
        count -= 1    
        write += "}"
        index += 1
        return index, write, indentation, count
        
    while (write[-1] in "\n\t "):
        write = write[:-1]
        
    index += 1
    return index, write, indentation, count
    
def equals(read, write, index, count):
    start = index + 1
    temporary = ""

    while (read[index] in "\t ="):
        temporary += read[index]
        index += 1

    if (read[index] != "{"):
        index = start
        write += "="
        return index, write, count
        
    write += temporary
    count = 0xffff
    return index, write, count
    
def addition(write, index, string, length):
    index += length
    write += string
    return write, index

def parse(filename):
    contents = open(filename, "r").read().replace("\t", "    ")
    read = "\n".join([line.lstrip() for line in contents.splitlines()])
    index, count, indentation = (0, 0, 0)
    write = ""
    
    while (len(read) > index):
        if (read[index - 1] == "\n"):
            if (read[index] != "}"):
                write += "    " * indentation
            elif (indentation > 1):
                write += "    " * (indentation - 1)
            
        if (read[index] == "\""):
            index, write = string(read, write, index, "\"")
            continue
        elif (read[index] == "'"):
            index, write = string(read, write, index, "'")
            continue
        elif (read[index] == "#"):
            index, write = string(read, write, index, "\n")
            continue
        elif (read[index] == "{"):
            index, write, indentation, count = open_brace(read, write, index, indentation, count)
            continue
        elif (read[index] == "}"):
            index, write, indentation, count = close_brace(read, write, index, indentation, count)
            continue
        elif (read[index:index + 2] == "&&"):
            write, index = addition(write, index, "and", 2)
            continue
        elif (read[index:index + 2] == "||"):
            write, index = addition(write, index, "or", 2)
            continue
        elif (read[index] == "!" and read[index + 1] != "="):
            write, index = addition(write, index, "not ", 1)
            continue
        elif (read[index:index + 4] == "true"):
            write, index = addition(write, index, "True", 4)
            continue
        elif (read[index:index + 5] == "false"):
            write, index = addition(write, index, "False", 5)
            continue
        elif (read[index:index + 4] == "none"):
            write, index = addition(write, index, "None", 4)
            continue
        elif (read[index] == "="):
            index, write, count = equals(read, write, index, count)
            continue
        elif (read[index:index + 2] == "++"):
            write, index = addition(write, index, " += 1", 2)
            continue
        elif (read[index:index + 2] == "--"):
            write, index = addition(write, index, " -= 1", 2)
            continue
        elif (read[index:index + 7] == "else if"):
            write, index = addition(write, index, "elif", 7)
            continue
            
        write += read[index]
        index += 1
        
    file = open(filename.rpartition(".")[0] + ".py", "w")
    file.write(write)
    file.close()
    
def main():
    if (len(argv) == 1):
        return

    keep = False
    argv.pop(0)
    
    if ("-k" in argv):
        keep = True
    
    for filename in argv:
        if (exists(filename)):
            parse(filename)
            
    if (exists(argv[0])):
        system("python " + argv[0].rpartition(".")[0] + ".py")
    
    if (not keep):
        for filename in argv:
            if (exists(filename.rpartition(".")[0] + ".py")):
                remove(filename.rpartition(".")[0] + ".py")
    
    
if (__name__ == "__main__"):
    main()
