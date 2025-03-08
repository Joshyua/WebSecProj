def handle_line(line: str, delimiter: str) -> list:
    line = line.strip("\n")
    info_list = line.split(":")
    return info_list

def return_sample(count_desired: int, delimiter: str):
    with open("sg.csv", "r") as f:
        line = f.readline()
        info_list = handle_line(line, delimiter)
        size = len(info_list)
        
        count = 0
        sample_list = []
        sample = [ None for _ in range(size) ]
        
        while True:
            for idx, value in enumerate(sample): #iterates over the sample sample_count times 
                if value is None:
                    if info_list[idx] != '':
                        sample[idx] = info_list[idx]
                        if None not in sample:
                            sample_list.append(sample)
                            sample = [ None for _ in range(size) ]
                            count = count + 1
            line = f.readline()
            info_list = handle_line(line, delimiter)
            if count >= count_desired:
                break
        return sample_list
    
if __name__ == "__main__":
    pass
