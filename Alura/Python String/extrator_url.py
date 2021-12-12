from conversor_lista_dicio import lista_para_dicionario
import re

class ExtratorURL:
    def __init__(self, url):
        self.__url = self.__sanitizar_url(url)
        valido = self.__validar_url()
        if valido:
            self.__url_separado = self.__separar_url()

    def __str__(self):
        return (
            f'URL: {self.url}\n'
            f'URL Base: {self.base}\n'
            f'Parâmetros: {self.parametros_separados}'
            )

    def __len__(self):
        return len(self.url)

    # Dunder Method que serve para comparar dois objetos da mesma classe.
    def __eq__(self, other):  # Se utiliza o 'other' por convenção.
        return self.url == other.url  # Nesse caso, estou utilizando o atributo url para comparar 
                                      # se os objetos são iguais ou não.
    # Utilizando dessa maneira, utilizar o '==' para comparar dois objetos, não se estará mais comparando o id(obj), para tal, utiliza-se a palavra-chave 'is'.
    # EXEMPLO: >>> obj1 is obj2 <<<

    @property
    def url(self):
        return self.__url

    @property
    def base(self):
        if type(self.__url_separado) == str:
            return self.__url_separado
        else:
            return self.__url_separado[0]

    @property
    def parametros_juntos(self):
        if type(self.__url_separado) == str:
            return None
        else:
            return self.__url_separado[1]

    @property
    def parametros_separados(self):
        if type(self.__url_separado) == str or not self.__url_separado[2]:
            return None
        else:
            return self.__url_separado[2]

    @url.setter
    def url(self, url):
        self.__url = self.__sanitizar_url(url)
        valido = self.__validar_url()
        if valido:
            self.__url_separado = self.__separar_url()
    
    @staticmethod
    def __sanitizar_url(url):
        if type(url) == str:
            url = url.strip()
            return url
        
        return ''

    def __validar_url(self):
        if not self.url:
            raise ValueError('A URL está vazia')

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('A URL é inválida')
        return True

    def __separar_url(self):
        separador = self.url.find('?')
        if separador == -1:
            return self.url
        else:
            url_base = self.url[:separador]
            url_parametros_juntos = self.url[separador+1:]
            url_parametros_separados = self.__separar_parametros(url_parametros_juntos)
            return url_base, url_parametros_juntos, url_parametros_separados

    @staticmethod
    def __separar_parametros(url_parametros):
        lista_parametros = []
        while True:
            index_sinal_igual = url_parametros.find('=')  # Se tem sinal de igual, tem parâmetro.
            if index_sinal_igual == -1:  # Se NÃO houver parâmetro.
                dicionario_parametros = lista_para_dicionario(lista_parametros)
                return dicionario_parametros  # Único lugar onde vai retornar o valor.
            # Se houver parâmetro, continua.
            # Não é necessário o uso do else, uma vez que caso entre no if, a função irá terminar de rodar com o return.
            index_e_comercial = url_parametros.find('&')  # Se tem &, tem mais de um parâmetro.
            if index_e_comercial == -1:  # Se NÃO houver MAIS DE UM parâmetro.
                lista_parametros.append([url_parametros[:index_sinal_igual],
                                            url_parametros[index_sinal_igual+1:]])
                url_parametros = ''
            else:  # Se houver MAIS DE UM parâmetro.
                lista_parametros.append([url_parametros[:index_sinal_igual],
                                            url_parametros[index_sinal_igual+1:index_e_comercial]])
                url_parametros = url_parametros[index_e_comercial+1:]


if __name__ == '__main__':
    minha_url = ExtratorURL('https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100')
    # minha_url = ExtratorURL('https://bytebank.com/cambio?moedaOrigem=real')
    # minha_url = ExtratorURL('https://bytebank.com/cambio')
    # minha_url = ExtratorURL('palavras?aleatorias')
    # minha_url = ExtratorURL('  ')
    # minha_url = ExtratorURL(None)

    print(minha_url)
