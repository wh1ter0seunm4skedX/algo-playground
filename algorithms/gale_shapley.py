def gale_shapley(men_pref, woman_pref):
    
    engagment = {} 
    
    return engagment

# Example data
men_pref = {
    "A": ["X", "Y", "Z"],
    "B": ["Y", "X", "Z"],
    "C": ["Y", "Z", "X"]
}

women_pref = {
    "X": ["B", "A", "C"],
    "Y": ["A", "B", "C"],
    "Z": ["A", "C", "B"]
}

stable_matching = gale_shapley(men_pref, women_pref)
print("Stable Matching:", stable_matching)