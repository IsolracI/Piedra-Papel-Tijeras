import random

class EleccionesPPT:

    Piedra = 0
    Papel = 1
    Tijeras = 2
    Lagarto = 3
    Spock = 4

Posibles_victorias = {
    EleccionesPPT.Piedra: EleccionesPPT.Tijeras, 
    EleccionesPPT.Tijeras: EleccionesPPT.Papel,
    EleccionesPPT.Papel: EleccionesPPT.Piedra
}

def evaluar_juego(eleccion_usuario, eleccion_ordenador):

    if eleccion_usuario == eleccion_ordenador:
        print("Ambos eligieron ", eleccion_usuario, ". Empate...")
        return ResultadosPPT.Empate
    elif eleccion_ordenador in Posibles_victorias[eleccion_usuario]:
        print(eleccion_usuario, " le gana a ", eleccion_ordenador, ". Ganaste! ~(^-^)~")
        return ResultadosPPT.Victoria
    else:
        print(eleccion_ordenador, " le gana a ", eleccion_usuario, ". Perdiste :(")
        return ResultadosPPT.Derrota



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