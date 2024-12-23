def gale_shapley(men_preferences, women_preferences):
    # Prepare to track engagements and free men
    free_men = list(men_preferences.keys())  # All men are initially free
    engagements = {}  # woman -> man
    men_next_proposals = {man: 0 for man in men_preferences}  # Track proposal index

    # Reverse the women's preferences for easier comparison
    women_rankings = {
        woman: {man: rank for rank, man in enumerate(preference_list)}
        for woman, preference_list in women_preferences.items()
    }

    # While there are free men who haven't proposed to everyone
    while free_men:
        man = free_men.pop(0)  # Take a free man
        man_preferences = men_preferences[man]
        # Propose to the next woman on his list
        woman_index = men_next_proposals[man]
        woman = man_preferences[woman_index]
        men_next_proposals[man] += 1  # Move to the next preference for the next round

        # If the woman is free, they get engaged
        if woman not in engagements:
            engagements[woman] = man
        else:
            # Check if she prefers the new man over her current partner
            current_partner = engagements[woman]
            if women_rankings[woman][man] < women_rankings[woman][current_partner]:
                # She prefers the new man; break the current engagement
                free_men.append(current_partner)
                engagements[woman] = man
            else:
                # She prefers her current partner; the new man remains free
                free_men.append(man)

    # Return the stable matching
    return engagements


# Example data
men_preferences = {
    "1": ["A", "B", "C","D"],
    "2": ["A", "D", "B","C"],
    "3": ["D", "B", "C","A"],
    "4": ["B", "C", "D","A"],

}

women_preferences = {
    "A": ["1", "3", "4","2"],
    "B": ["2", "1", "3","4"],
    "C": ["4", "2", "1","3"],
    "D": ["4", "3", "2","1"],

}

# Run the algorithm
stable_matching = gale_shapley(men_preferences, women_preferences)
print("Stable Matching:", stable_matching)
