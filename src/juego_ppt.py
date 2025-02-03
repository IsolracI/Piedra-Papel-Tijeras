import random

class EleccionesPPT:

    Roca = 0
    Papel = 1
    Tijeras = 2


class ResultadosPPT:

    Victoria = 1
    Derrota = -1
    Empate = 0


Posibles_victorias = {
    EleccionesPPT.Roca: EleccionesPPT.Tijeras,
    EleccionesPPT.Tijeras: EleccionesPPT.Papel,
    EleccionesPPT.Papel: EleccionesPPT.Roca
}

def evaluar_juego(eleccion_usuario, eleccion_ordenador):
    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")

    # You picked Rock
    elif user_action == GameAction.Rock:
        if computer_action == GameAction.Scissors:
            print("Rock smashes scissors. You won!")
        else:
            print("Paper covers rock. You lost!")



    # You picked Paper
    elif user_action == GameAction.Paper:
        if computer_action == GameAction.Rock:
            print("Paper covers rock. You won!")
        else:
            print("Scissors cuts paper. You lost!")

    


    if eleccion_usuario == eleccion_ordenador:
        print("Ambos eligieron ", eleccion_usuario, ". Empate")
        return ResultadosPPT.Empate
    else:
        for eleccion in Posibles_victorias:
            if eleccion_usuario == eleccion.key and eleccion_ordenador == eleccion.values:
                print("El usuario eligió ", )








def assess_game(user_action, computer_action):
    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")

    # You picked Rock
    elif user_action == GameAction.Rock:
        if computer_action == GameAction.Scissors:
            print("Rock smashes scissors. You won!")
        else:
            print("Paper covers rock. You lost!")

    # You picked Paper
    elif user_action == GameAction.Paper:
        if computer_action == GameAction.Rock:
            print("Paper covers rock. You won!")
        else:
            print("Scissors cuts paper. You lost!")

    # You picked Scissors
    elif user_action == GameAction.Scissors:
        if computer_action == GameAction.Rock:
            print("Rock smashes scissors. You lost!")
        else:
            print("Scissors cuts paper. You won!")


def get_computer_action():
    computer_selection = random.randint(0, len(GameAction) - 1)
    computer_action = GameAction(computer_selection)
    print(f"Computer picked {computer_action.name}.")

    return computer_action


def get_user_action():
    # Scalable to more options (beyond rock, paper and scissors...)
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    user_action = GameAction(user_selection)

    return user_action


def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'


def main():

    while True:
        try:
            user_action = get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        computer_action = get_computer_action()
        assess_game(user_action, computer_action)

        if not play_another_round():
            break


if __name__ == "__main__":
    main()