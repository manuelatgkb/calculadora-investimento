# calculadora-investimento
Esta calculadora foi criada para responder a primeira parte do desafio de programação. Ela calcula o alcance de um anúncio postado na internet, gerando um relatório virtual que, tomando em consideração o valor investido e quantidade de dias que o anúncio fica em linha retorna: a quantidade máxima de visualizações, a quantidade máxima de cliques e a quantidade máxima de compartilhamentos.

A calculadora e o cadastro necessitam de uma versão no mínimo 3.8.6

A calculadora foi adicionada ao sistema de cadastro de pessoas, pedido na segunda parte do desafio. 

No cadastro de pessoas, detalhes sobre o anúncio como seu título, o nome de seu criador, a data de seu início e fim e o valor que pretende ser investido devem ser fornecidos. A calculadora retorna um relatório virtual resumido do alcance do anúncio em maximo de visualizações, compartilhamentos e cliques. 

Sua utilização é bastante simples, basta realizar o input das informações solicitadas para receber o relatório virtual.
Entretanto, cada campo foi pensado para receber apenas dados específicos: o campo de data recebe apenas datas no formato dd/mm/yyyy, os campos de título do anúncio e de nome não podem ser deixados em branco e o campo de investimento inicial deve receber um input numérico e maior do que 0. 

Para o bom funcionamento da calculadora, foram criadas as seguintes variáveis, aqui detalhadas: 

# média_visu:  é a média de visualizações a cada 1 real investido
# média_clq:  é o número de cliques para cada 100 visualizações
# média_compart:  é o compartilhamentos de cada 20 pessoas que clicaram no anúncio
# média_seq_compart:  é o número máximo de compartilhamentos em sequ6encia
# média_visu_por_compart:  é o número de novas visualizações geradas pelos compartilhamentos

O comando irá baixar todas as dependências do projeto. Além disso, serão executados os testes unitários, e se algum falhar, o programa exibirá essa informação no console, guiando o usuário e fornecendo uma boa experiência de uso. 
