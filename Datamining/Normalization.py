def cal_mean(data):
    return sum(data)//len(data)

def cal_mode(data):
    frequency={}
    for item in data:
        frequency[item]= frequency.get(item, 0)+1
    mode =[k for k,v in frequency.items() if v ==max(frequency.values())]
    return mode
    
def cal_median(data):
    sorted_data= sorted(data)
    n = len(data)
    if n%2==0:
        return (sorted_data[n//2  -1] + sorted_data[n//2])/2
    else:
        return sorted_data[n//2]
    
def cal_variance(data):
    mean = cal_mean(data)
    return sum((x-mean)**2 for x in data) / len(data)

def cal_std_deviation(data):
    return cal_variance(data)**0.5

def min_max(data):
    min_val = min(data)
    max_val = max(data)
    scaled_data = [(x - min_val)/(max_val - min_val) for x in data]
    return scaled_data

def z_score(data):
    mean = cal_mean(data)
    std_dev = cal_std_deviation(data)
    normalized_data =[(x - mean)/std_dev for x in data]
    return normalized_data

def decimal_scaling(data):
    max_val = max(abs(x) for x in data)
    num_digit = len(str(max_val))
    scaled_val =[x / (10 ** num_digit) for x in data]
    return scaled_val
