from collections import Counter

def analisa_frequencia_letras(texto):
    contador = Counter(texto.lower())
    total_de_caracteres = sum(contador.values())

    proporcoes = {letra: (aparicoes / total_de_caracteres) for letra, aparicoes in contador.items()}
    proporcoes = Counter(proporcoes)
    mais_comuns = proporcoes.most_common(10)
    for caractece, frequencia in mais_comuns:
        print(f'{caractece} => {frequencia * 100:.2f}%')

if __name__ == '__main__':
    meu_texto = '''Imagina que a liderança da empresa em que você trabalha tem uma alta expectativa
    em relação a entrega de um projeto, que pode potencializar vários ganhos para a organização, e para não decepcioná-los você acaba se comprometendo com ela, mesmo sabendo que as chances de cumprir os requisitos é mínima.

Isso já aconteceu com você? Bem, comigo já aconteceu e é sobre isso que vou escrever neste artigo.

Quando resgato essas experiências, que para mim foram um tanto embaraçosas, sempre me questiono: "Por que eu falei que dava para entregar quando eu já sabia que não era possível?", "Como é que eu pude ser tão otimista e simplesmente aceitei sem antes negociar melhor um prazo ou outros pontos do projeto?"

Eis que surge uma palavra mágica: negociação.

Quando comecei a exercer liderança, a negociação passou a fazer parte das competências que queria (para não dizer precisava) desenvolver, pois eu sabia o quanto poderia prejudicar o meu trabalho e o da equipe ao assumir compromissos sem antes ter uma perspectiva mais clara sobre o que precisava ser feito, em quanto tempo e quais recursos seriam envolvidos, independente do tamanho do projeto.

Com isso fui aprendendo que a negociação é um método disponível para tomar decisões. É um processo em que a troca é usada entre várias partes.

Negociar é sinônimo de troca.
A troca é o coração de uma negociação e está presente em todo o processo. Na verdade, você verá que existe uma fase dedicada à troca e aos comportamentos mais eficazes para realizá-la.

E como uma pessoa que atua como líder pode melhorar sua negociação?

Conhecendo as principais competências que uma pessoa que sabe negociar precisa desenvolver.

Vamos lá?

1. Autoavaliação
Uma pessoa com altas habilidades de negociação conhece seu estilo de negociação, tanto individualmente quanto em equipe. Observe quais traços de personalidade ou habilidades você precisa melhorar para aumentar competências para negociar, uma vez que existem traços de personalidade que não podem ser alterados, mas eles podem ser gerenciados e desenvolvidos. Quem é líder se observa e consegue manter a neutralidade na maioria das vezes (lembre-se que se você for muito efusivo (a) pode assustar, se for muito quieto (a) pode criar desconfiança). Manter uma postura equilibrada diante do conflito potencializa a sensação de conforto e confiança com que você negocia.

2. Liderança interna
Como líder, você tem a capacidade de gerenciar sua equipe e o ambiente interno de sua organização, mas nem sempre poderá exercer sua influência externamente. Concentre-se no seu ambiente interno e nas pessoas com quem trabalha, na sua equipe e não no mundo externo. Trabalhe para melhorar o que está mais próximo de você.

3. Recompensas
Os resultados são importantes para quem atua como líder, mas a atitude dos membros da equipe é ainda mais importante. Não aja como se os resultados fossem a única coisa importante, recompense aquelas pessoas que se movem por outra coisa, recompense sua vontade de colaborar, a atitude otimista e a vontade de melhorar. Equipes que trabalham com uma atitude positiva também vão alcançar os resultados esperados.

4. Comunique-se claramente
Uma das competências de liderança mais solicitadas agora e no futuro é a capacidade de se comunicar com eficácia - ou seja, com clareza. Saber ouvir a opinião do restante da equipe é uma importante habilidade de comunicação, já que saber a opinião dos demais é a chave para depois expressar sua opinião e tomar a melhor decisão. Não é fácil, mas, como todas as outras habilidades, você pode melhorar com a prática.

5. Empatia
Grandes líderes são valorizados(as) por sua capacidade de se colocar no lugar das outras pessoas. Essa é uma das principais maneiras de entender verdadeiramente as necessidades e preocupações da equipe. É uma habilidade muito exigida na área de liderança, pois a falta de empatia se traduz em um sentimento de incompreensão que gera desconforto e ruptura na equipe.

6. Gerenciar sucessos
Para ter sucesso, você também precisa saber como lidar com o sucesso. Ao líder é solicitado que entre suas competências de liderança saiba traçar metas de curto prazo, para que aos poucos as vitórias sejam comemoradas. É responsabilidade do líder saber canalizar esses sucessos para chegar ainda mais perto dos grandes objetivos.

7. Adaptação à mudança
Em um mundo cada vez mais competitivo e incerto, a capacidade de se adaptar às mudanças pode fazer a diferença na liderança. Entre as funções que serão exigidas da liderança estarão a procura de pequenas mudanças que nos ajudem a ser mais eficientes, encontrar ideias inovadoras que representem benefícios para a organização, etc. Em suma, adaptar-se às mudanças é necessário para satisfazer as necessidades da própria empresa e dos clientes, pois se trata de um ambiente dinâmico que exige um guia que saiba liderar as equipes.

8. Acompanhamento
De uma perspectiva da liderança, é importante verificar o impacto que suas decisões têm em sua equipe e na organização como um todo. Desta forma, você pode trabalhar em suas áreas de melhoria e obter feedback sobre sua liderança, para que possa refinar seus planos futuros e o relacionamento com seus colegas.

9. Motivação
A capacidade de motivar, talvez seja a competência de liderança mais importante de todas, uma qualidade fundamental em todo bom líder, necessária para atingir objetivos e realizar tarefas. Sem motivação, a equipe não funciona. O líder tem em suas mãos a chave para tirar da equipe a força necessária para fazer o trabalho.

10. Assertividade
Líderes são pessoas solicitadas para defender seus interesses e expressar suas opiniões com calma e sem atropelar os direitos dos outros. Falamos de assertividade, uma das principais competências da liderança presente e futura. É também uma habilidade que garante melhores relacionamentos e aumenta as chances de sucesso. Seja assertivo para que você possa expressar seus próprios critérios e atingir seus objetivos.

11. Prática
Aqui é preciso saber que experiência não é repetir mecanicamente algo aprendido, mas aplicar reflexivamente a novas situações o que tanto nos custou o trabalho de aprender. Saber negociar inclui discussão e preparo, tanto individualmente quanto em grupos.

Atuar como líder requer várias competências e saber negociar requer preparo e estudo. A preparação é uma das formas de mostrar confiança e ganhar a confiança das outras pessoas, isso inclui ter a capacidade de definir suas próprias estratégias e saber aproveitar as oportunidades advindas das negociações. Lembre-se que uma boa negociação gera oportunidades de melhorias para você e sua empresa.

Agora te pergunto: de todas essas competências que vimos, qual você considera ser o aspecto mais difícil para melhorar a sua negociação?

Se você quer se aprofundar no tema, conheça o curso Negociação para líderes: Desenvolva a habilidade e consiga bons acordos.'''
    
    analisa_frequencia_letras(meu_texto)
