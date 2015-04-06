def makeInverseIndex(strlist):
    new_index=dict()
    split_list=[listitem.split() for listitem in strlist]
    for lineno,line in enumerate(split_list):
        for word in line:
            #print(word,new_index)
            if word in new_index.keys(): new_index[word].add(lineno) 
            else: new_index[word]={lineno}
    return new_index

def orSearch(inverseIndex,query): 
    new_set=set()    
    # this works
    for item in [inverseIndex[x] for x in query if x in inverseIndex.keys()]:
        new_set.update(item)
    
    return new_set

def andSearch(inverseIndex,query):
    
    y=[set()]
    [y.append(inverseIndex[x]) for x in [x for x in query if x in inverseIndex.keys()]]
    j=[set.intersection(y[0],y[i]) for i in range(1,len(y))]
    return [j[0] if len(j)>0 else set()]


def orSearch1L(inverseIndex,query): 
    new_set=set()    
    
    # trying one liner (this is cool!)
    [new_set.update(inverseIndex[x]) for x in [x for x in query if x in inverseIndex.keys()]]
    return new_set
