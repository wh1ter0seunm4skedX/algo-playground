from colorama import Fore, Style, init
import os

init()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def gale_shapley(men_preferences, women_preferences):
    free_men = list(men_preferences.keys())
    engagements = {}
    men_next_proposals = {man: 0 for man in men_preferences}
    iteration = 1

    women_rankings = {
        woman: {man: rank for rank, man in enumerate(preference_list)}
        for woman, preference_list in women_preferences.items()
    }

    print(f"\n{Fore.CYAN}Initial State:{Style.RESET_ALL}")
    print(f"Free Men: {', '.join(free_men)}")
    print("No engagements yet\n")
    input(f"{Fore.YELLOW}Press Enter to start...{Style.RESET_ALL}")

    while free_men:
        clear_screen()
        man = free_men.pop(0)
        woman_index = men_next_proposals[man]
        woman = men_preferences[man][woman_index]
        men_next_proposals[man] += 1

        print(f"{Fore.YELLOW}Iteration {iteration}{Style.RESET_ALL}")
        print(f"➜ {Fore.GREEN}{man}{Style.RESET_ALL} proposes to {Fore.MAGENTA}{woman}{Style.RESET_ALL}")

        if woman not in engagements:
            engagements[woman] = man
            print(f"✓ {woman} accepts {man}'s proposal")
        else:
            current_partner = engagements[woman]
            if women_rankings[woman][man] < women_rankings[woman][current_partner]:
                print(f"↔ {woman} prefers {man} over current partner {current_partner}")
                free_men.append(current_partner)
                engagements[woman] = man
            else:
                print(f"✗ {woman} rejects {man}, staying with {current_partner}")
                free_men.append(man)

        print(f"\nCurrent State:")
        print(f"Free Men: {', '.join(free_men)}")
        print("Engagements:", ", ".join([f"{w}-{m}" for w, m in engagements.items()]))
        print("-" * 50)
        
        if free_men:  # Only prompt if there are more iterations
            input(f"{Fore.YELLOW}Press Enter for next iteration...{Style.RESET_ALL}")
        iteration += 1

    return engagements