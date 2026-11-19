import pandas as pd
from analiza import podstawowe_statystyki


def test_podstawowe_statystyki(capsys):
    df = pd.DataFrame({
        "temp_max" : [20, 22],
        "temp_min" : [10, 12],
        "opady" : [10, 12]
    })

    podstawowe_statystyki(df)

    wynik = capsys.readouterr()

    assert "21.00" in wynik.out
    assert "11.00" in wynik.out
    assert "22.00" in wynik.out
    #assert "Średnia temp minimalna: 11.00 ℃" in wynik.out
    #assert "Suma opadów: 22.00 mm" in wynik.out