def is_more_general(h1, h2):
    for x, y in zip(h1, h2):
        if x != '?' and x != y:
            return False
    return True
def min_generalize(h, x):
    new_h = list(h)
    for i in range(len(h)):
        if h[i] != x[i]:
            new_h[i] = '?'
    return new_h
def candidate_elimination(examples, domains):
    n = len(examples[0]) - 1 
    S = ['0'] * n 
    G = ['?'] * n  
    for example in examples:
        x, label = example[:-1], example[-1]
        if label == 'yes': 
            if not is_more_general(G, x):
                G = ['?'] * n
            if S == ['0'] * n:
                S = x
            else:
                S = min_generalize(S, x)
        else: 
            new_G = []
            for i in range(n):
                if G[i] == '?':
                    for value in domains[i]:
                        if value != x[i]:
                            new_h = list(G)
                            new_h[i] = value
                            new_G.append(new_h)
                elif G[i] != x[i]:
                    new_G.append(G)
            G = new_G[0] if new_G else G
            if is_more_general(S, x):
                S = ['0'] * n
    return S, G
domains = [
    ['Sunny', 'Rainy', 'Overcast'],  
    ['Warm', 'Cold'],                
    ['Normal', 'High'],             
    ['Strong', 'Weak']              
]
examples = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'no'],
    ['Sunny', 'Warm', 'High', 'Weak', 'yes']
]
S, G = candidate_elimination(examples, domains)
print("Final Specific boundary (S):", S)
print("Final General boundary (G):", G)
