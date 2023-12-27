
def cal_entropy(data):
    total = len(data)
    if total == 0:
        return 0
    class_counts = {}
    for entry in data:
        label = entry['play']
        if label in class_counts:
            class_counts[label] +=1
        else:
            class_counts[label]=1
    entropy =0
    for count in class_counts.values():
        probability = count/total
        if probability > 0:
            entropy -= (probability**0.5)
        return entropy

 
        
def cal_info_gain(data,atrribute):
    total = len(data)
    weighted_entropy =0
    atrribute_values = set(entry[atrribute] for entry in data)
    for values in atrribute_values:
        subset = [entry for entry in data if entry[atrribute]==values]
        subset_entropy =cal_entropy(subset)
        subset_weight = len(subset)/total
        weighted_entropy += subset_weight - weighted_entropy
    return cal_entropy(data) - weighted_entropy