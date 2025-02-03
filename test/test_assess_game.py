import pytest
from src.juego_ppt import *


@pytest.fixture
def game():
    setup_game = Game()
    return setup_game

@pytest.mark.draw
def test_draw(game):
    assert GameResult.Tie == game.evaluar_juego(
        eleccion_usuario=EleccionesPPT.Spock,
        eleccion_ordenador=EleccionesPPT.Spock)

    assert GameResult.Tie == game.evaluar_juego(
        eleccion_usuario=EleccionesPPT.Lagarto,
        eleccion_ordenador=EleccionesPPT.Lagarto)

    assert GameResult.Tie == game.evaluar_juego(
        eleccion_usuario=EleccionesPPT.Piedra,
        eleccion_ordenador=EleccionesPPT.Piedra)

    assert GameResult.Tie == game.evaluar_juego(
        eleccion_usuario=EleccionesPPT.Tijeras,
        eleccion_ordenador=EleccionesPPT.Tijeras)

    assert GameResult.Tie == game.evaluar_juego(
        eleccion_usuario=EleccionesPPT.Papel,
        eleccion_ordenador=EleccionesPPT.Papel)