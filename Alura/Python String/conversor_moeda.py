from extrator_url import ExtratorURL


class Conversor(ExtratorURL):
    def __init__(self, url):
        super().__init__(url)
    
    def converter(self):
        # 100 dólares = 493.45 reais = 83.78 euros
        valores_moedas = {
            'dolar': 100,
            'real': 493.45,
            'euro': 83.78
            }
        origem = self.parametros_separados['moedaOrigem']
        destino = self.parametros_separados['moedaDestino']
        quantidade = float(self.parametros_separados['quantidade'])
        resultado = valores_moedas[destino]/valores_moedas[origem] * quantidade

        return resultado


if __name__ == '__main__':
    url_teste = 'bytebank.com/cambio?quantidade=100&moedaOrigem=euro&moedaDestino=real'
    conversor = Conversor(url_teste)
    print(f'{conversor.converter():.2f}')
