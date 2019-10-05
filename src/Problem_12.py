#PF-Prac-12
def generate_sentences(subjects,verbs,objects):
    sentence_list=[]
    sentence=""
    for i in subjects:
        for j in verbs:
            for k in objects:
                sentence=i+" "+j+" "+k
                sentence_list.append(sentence)

    
    return sentence_list

subjects=["I","You"]
verbs=["love", "play"]
objects=["Hockey","Football"]
print(generate_sentences(subjects,verbs,objects))