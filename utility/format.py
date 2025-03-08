from sample import handle_line

def rename_file(fields: list[str], delimiter: str):
    with open("sg.csv", "r") as f:
        with open("formatted.csv", "w") as fwrite:
            line = f.readline()
            info_list = handle_line(line, delimiter)
            for idx,_ in enumerate(len(fields)):
                if info_list[idx] != '':
                    formatted_line += f"""\"{fields[idx]}:{info_list[idx]} """
                
        
    
    line = line.strip("\n")
    info_list = line.split(":")
    return info_list

if __name__ == "__main__":
    pass
