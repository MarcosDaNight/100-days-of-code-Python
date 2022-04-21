from data_game import data
from art import logo, vs
import random
from os import system


def get_random():
    """Get a random object from data"""
    return random.choice(data)


def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess 
    and returns True if they got it right.
    Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    game_Continue = True

    chose_a = get_random()
    chose_b = get_random()
    score = 0
    while game_Continue:
        chose_a = chose_b
        chose_b = get_random()

        while chose_a == chose_b:
            chose_a = get_random()

        print(f"Compare A: {format_data(chose_a)}.\n")

        print(vs)

        print(f"Compare B: {format_data(chose_b)}.\n")
    
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        follower_a_count = chose_a['follower_count']
        follower_b_count = chose_b['follower_count']

        player_status = check_answer(guess, follower_a_count, follower_b_count)

        if player_status:
            system('clear')
            print(logo)
            score += 1
            print(f"You're right! Your score is: {score}")
            

        else:
            print(f"You're Wrong! You lose and the final score is: {score}")
            game_Continue = False

game()
