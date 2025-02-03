import pytest
# from src.juego_ppt import


@pytest.fixture
def game():
    setup_game = Game()
    return setup_game

@pytest.mark.draw
def test_draw(game):
    assert GameResult.Tie == game.assess_game(
        user_action=GameAction.Spock,
        computer_action=GameAction.Spock)

    assert GameResult.Tie == game.assess_game(
        user_action=GameAction.Lizard,
        computer_action=GameAction.Lizard)

    assert GameResult.Tie == game.assess_game(
        user_action=GameAction.Rock,
        computer_action=GameAction.Rock)

    assert GameResult.Tie == game.assess_game(
        user_action=GameAction.Scissors,
        computer_action=GameAction.Scissors)

    assert GameResult.Tie == game.assess_game(
        user_action=GameAction.Paper,
        computer_action=GameAction.Paper)