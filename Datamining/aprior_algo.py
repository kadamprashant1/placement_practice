def generate_candidates(prev_candidates, k):
    candidate = set()
    for itemset1 in prev_candidates:
        for itemset2 in prev_candidates:
            union = itemset1.union(itemset2)
            if len(union) == k:
                candidate.add(union)
    return list(candidate)

def support_count(transactions, itemset):
    count = 0
    for transaction in transactions:
        if itemset.issubset(transaction):
            count += 1
    return count

def aprior(transactions, min_support):
    frequent_itemset = []
    k = 1
    unique_items = set(item for transaction in transactions for item in transaction)
    candidates = set(frozenset([item]) for item in unique_items)
    while candidates:
        frequent_itemset = []
        for itemset in candidates:
            support = support_count(transactions, itemset)
            if support >= min_support:
                frequent_itemset.append((itemset, support))
        frequent_itemset.extend(frequent_itemset)
        k += 1
        candidates = generate_candidates(set(itemset for itemset, _ in frequent_itemset), k)
    return frequent_itemset

def generate_rules(frequent_itemsets, transactions, min_confidence):
    rules = []
    for itemset, support in frequent_itemsets:
        if len(itemset) > 1:
            for item in itemset:
                antecedent = frozenset([item])
                consequent = itemset - antecedent
                confidence = support_count(transactions, itemset) / support_count(transactions, antecedent)
                if confidence > min_confidence:
                    rules.append((antecedent, consequent, confidence))
    return rules

transactions = []  
min_support = 0.1  
frequent_itemsets = aprior(transactions, min_support)
min_confidence = 0.5 
association_rules = generate_rules(frequent_itemsets, transactions, min_confidence)
