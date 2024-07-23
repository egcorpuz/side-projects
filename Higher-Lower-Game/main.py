from game_data import singers
from art import logo_higherlower, logo_vs
from random import choice
from os import system

clear = lambda: system('cls')
clear()
print(logo_higherlower)


def calculate_index(number_of_followers):
    index_of_next = next((index for (index, d) in enumerate(singers) if d["follower_count"] == number_of_followers),
                         None)
    return index_of_next


def compare(current_points, index_of_b):
    if current_points > 0:
        a_pick = singers[index_of_b]
    else:
        a_pick = choice(singers)
    print(f"Compare A: {a_pick["name"]}, a {a_pick["description"]}, from {a_pick["country_of_origin"]}.")
    print(logo_vs)
    while 1:
        b_pick = choice(singers)
        if b_pick == a_pick:
            continue
        else:
            break
    print(f"Compare B: {b_pick["name"]}, a {b_pick["description"]}, from {b_pick["country_of_origin"]}.")

    temp_dict = {'A': a_pick["follower_count"], 'B': b_pick["follower_count"]}
    inverse = [(value, key) for key, value in temp_dict.items()]
    correct_answer = max(inverse)[1]
    b_follower_count = temp_dict['B']
    print(f"PSST. Here is the score sheet: {temp_dict}. Use this ONLY for DEBUGGING.")
    return b_follower_count, correct_answer


def main():
    points = 0
    b_index = 0

    while 1:
        current_b, correct_answer = compare(points, b_index)
        usr_choice = input("Who has more followers? Type 'A' or 'B': ")
        if usr_choice == correct_answer:
            points += 1
            clear()
            print(logo_higherlower)
            print(f"You are right! Current score is {points}.")
            b_index = calculate_index(current_b)   
        else:
            clear()
            print(logo_higherlower)
            print(f"Sorry that is wrong. Final score is {points}.")
            break


if __name__ == "__main__":
    main()

# TODO : Works as intended. Code can be improved for readability
