from desconto import calcular_desconto

def test_desconto_simples():
    # Caso 1: Desconto normal 20%
    assert calcular_desconto(100, 20) == 80.0

def test_desconto_sem_desconto():
    # Caso 2: Sem desconto 
    assert calcular_desconto(200, 0) == 200.0
def test_desconto_total():

    # Caso 3: Desconto 100%
    assert calcular_desconto(150, 100) == 0.0