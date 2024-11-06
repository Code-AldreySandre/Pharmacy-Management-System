# Pharmacy-Management-System
 ## Introdução

 O presente trabalho tem como objetivo o desenvolvimento de um sistema de
 gerenciamento de farmácia, que visa facilitar o cadastro, busca e controle de
 medicamentos e funcionários. Em um cenário onde a eficiência e a precisão na gestão
 de recursos são fundamentais, a implementação de uma solução digital se torna
 imprescindível para otimizar processos e melhorar a organização.
 
 Neste sistema, foram utilizadas estruturas de dados como listas e tuplas, que permitem o
 armazenamento e a manipulação de informações de forma eficiente. O software conta com
 um menu interativo que possibilita ao usuário realizar operações de cadastro, busca, edição,
 exclusão e impressão de registros, promovendo uma experiência intuitiva e acessível.
 
 ## Descrição das Estruturas Utilizadas
 
 **Listas e Tuplas**

Foram utilizadas duas listas principais:

    ● medicamentos: Armazena os medicamentos cadastrados na farmácia;

    ● funcionarios: Armazena os dados dos funcionários;

 Dentro de cada uma dessas listas, os dados são armazenados como tuplas, uma estrutura
 simples e eficiente para representar objetos com múltiplos atributos:

 ● Cada medicamento é representado por uma tupla com os seguintes elementos: nome,
 preço e quantidade.

 ● Cada funcionário é representado por uma tupla contendo: nome, cargo e salário.

 **Estruturas de Controle**

     ● Condicionais (if, elif, else): Para controlar o fluxo do programa baseado nas
 entradas do usuário.

     ● Laços de repetição (for): Utilizados para percorrer as listas e realizar operações
 como busca, edição e exclusão.

 **Funções**

 Cada operação foi organizada em funções específicas para modularidade e clareza do
 código:

     ● Cadastrar: Adiciona medicamentos e       funcionários.

     ● Buscar: Localiza itens cadastrados.

     ● Editar: Permite a modificação dos dados existentes.

     ● Excluir: Remove medicamentos ou funcionários.

     ● Imprimir: Exibe os dados cadastrados ou p parte deles.

 **Interação com o Usuário**

 Ainteração ocorre via um menu com opções de gerenciamento. O programa permanece
 em execução até o usuário optar por sair, garantindo uma experiência contínua.

 **Tratamento de Erros**

 O sistema faz tratamento básico de erros, como a validação de entradas numéricas. Em
 casos de erro, o usuário é notificado e o fluxo do programa segue normalmente.

 ## Acertos e Erros Durante o Desenvolvimento
 **Acertos:**

 A implementação das funções seguiu o   princípio da modularidade, facilitando a manutenção e a leitura do código.

 A utilização de listas e dicionários proporcionou uma forma eficiente de armazenar e manipular os dados.

**Erros:**

 Em alguns momentos, o controle de erros poderia ter sido mais robusto, especialmente na validação de entradas do usuário.

 O sistema apresenta limitações no tratamento de exceções em entradas incorretas, como valores numéricos inválidos ou strings inesperadas.

 Devido à falta de experiência e de tempo hábil, não foi possível implementar todas as funcionalidades desejáveis, como, por exemplo, um banco de dados para armazenar informações ao longo do tempo. Isso faz com que, a cada inicialização do sistema, seja necessário alimentá-lo manualmente. Além disso, o uso de dicionários em determinadas situações, em vez de tuplas, tornaria o programa mais ágil e permitiria um tratamento de erros mais coerente.

 ## Conclusão
 O sistema de gerenciamento de farmácia desenvolvido foi capaz de atender aos
 requisitos propostos, permitindo o cadastro, busca, edição, exclusão e impressão de
 medicamentos e funcionários. A implementação bem-sucedida das funções garantiu a
 funcionalidade esperada, e o menu interativo facilitou a interação do usuário com o
 sistema. Os resultados obtidos mostram que a estrutura modular escolhida foi eficaz,
 permitindo expansões futuras e manutenções simples.


