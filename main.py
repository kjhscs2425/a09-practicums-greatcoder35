p1 = str("Costumes")
p2 = str("Scenery")
p3 = str("Lighting")
p4 = str("Sound")

def choose_practicum():
    option = str(input("Which practicum are you signing up for? "))
    if option == p1 or option == p2 or option == p3 or option == p4:
        return print(f"success, you chose {option}")
    else:
        return choose_practicum()
def main_function():
    name = str(input("What is your name? "))
    option = str(input("Which practicum are you signing up for? "))
    if option == p1 or option == p2 or option == p3 or option == p4:
        return print(f"Congratulations, {name}, you are signed up for {option}")
    else:
        return choose_practicum()

main_function()