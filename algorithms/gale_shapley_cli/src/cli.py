from data import men_preferences, women_preferences
from gale_shapley import gale_shapley
from colorama import Fore, Style, init

def main():
    init()
    print(f"{Fore.CYAN}Welcome to the Gale-Shapley Algorithm Visualizer!{Style.RESET_ALL}")
    print("\nInitial Preferences:")
    print(f"{Fore.GREEN}Men's Preferences:{Style.RESET_ALL}")
    for man, prefs in men_preferences.items():
        print(f"  {man}: {' > '.join(prefs)}")
    
    print(f"\n{Fore.MAGENTA}Women's Preferences:{Style.RESET_ALL}")
    for woman, prefs in women_preferences.items():
        print(f"  {woman}: {' > '.join(prefs)}")

    print("\nStarting Gale-Shapley Algorithm...")
    engagements = gale_shapley(men_preferences, women_preferences)

    print(f"\n{Fore.CYAN}Final Stable Matching:{Style.RESET_ALL}")
    for woman, man in engagements.items():
        print(f"  {Fore.MAGENTA}{woman}{Style.RESET_ALL} ⚭ {Fore.GREEN}{man}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()