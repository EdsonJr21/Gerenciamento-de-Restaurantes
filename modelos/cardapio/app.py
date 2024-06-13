from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_lasanha = Restaurante('lasanha', 'comida boa')
bebidas_suco = Bebida('suco  de uva', 3.0, 'grande')
bebidas_suco.aplicar_desconto()
pratos_pastel = Prato('Pastel de frango', 5.0, 'O melhor pastel do brasil')
pratos_pastel.aplicar_desconto()
restaurante_lasanha.adicionar_no_cardapio(bebidas_suco)
restaurante_lasanha.adicionar_no_cardapio(pratos_pastel)                 

def main():
    restaurante_lasanha.exibir_cardapio

if __name__ == '__main__':
    main()