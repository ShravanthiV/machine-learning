def find_s_algorithm(examples):
    hypothesis = None
    for example in examples:
        instance, label = example[:-1], example[-1]
        if label == 'yes': 
            if hypothesis is None:
                hypothesis = list(instance)
            else:
                
                for i in range(len(hypothesis)):
                    if hypothesis[i] != instance[i]:
                        hypothesis[i] = '?'
    return hypothesis
examples = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'no'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'yes']
]
hypothesis = find_s_algorithm(examples)
print("Final hypothesis:", hypothesis)
