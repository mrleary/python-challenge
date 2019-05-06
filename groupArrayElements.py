import numpy as np

def groupArrayElements(array, groupSize):    
    length = len(array)
    remainder = length % groupSize
    numberOfGroups = (int)((length - remainder)/groupSize)
    
    groups = [array[(i*groupSize):((i+1)*groupSize)] for i in np.arange(0, numberOfGroups)]
    
    if (remainder):
        groups.append(array[length-remainder:])
        
    return groups