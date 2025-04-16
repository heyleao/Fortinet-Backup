SSH Commands Executor
Interface Gráfica para Execução Automatizada de Comandos SSH

Índice
Visão Geral

Funcionalidades

Requisitos

Configuração e Uso

Detalhamento do Código

Considerações de Segurança

Contribuições

Visão Geral
O SSH Commands Executor é uma ferramenta que automatiza a execução de comandos via SSH em hosts remotos. A aplicação utiliza a biblioteca paramiko para gerenciamento de conexões SSH e tkinter para disponibilizar uma interface gráfica interativa, permitindo que o usuário configure os parâmetros de conexão e acompanhe o progresso da execução dos comandos.

Funcionalidades
Conexão SSH:
Estabelece uma conexão segura com o host remoto utilizando as credenciais fornecidas pelo usuário.

Execução Automatizada de Comandos:
Executa uma sequência de comandos pré-definidos e armazena a saída de cada comando em arquivos de texto individuais.

Interface Gráfica Amigável:
Permite a entrada de dados como usuário, senha, host, porta e diretório, além de proporcionar uma barra de progresso e mensagens de status para monitoramento.

Feedback Visual:
Atualiza dinamicamente uma barra de progresso e exibe mensagens de status para garantir que o usuário esteja ciente do andamento do processo.

Requisitos
Python 3.x

Bibliotecas Necessárias:

paramiko:
Instalado via:

bash
Copiar
pip install paramiko
tkinter:
Geralmente incluso nas distribuições padrão do Python. Em sistemas Linux, pode ser necessário instalar o pacote python3-tk.

Sistema Operacional:
Compatível com qualquer sistema que suporte Python e as bibliotecas mencionadas.

Configuração e Uso
Instalação
Clone ou Baixe o Repositório:
Certifique-se de que todos os arquivos do projeto estejam no seu ambiente de trabalho.

Instale as Dependências:
Execute:

bash
Copiar
pip install paramiko
Verifique se o tkinter está instalado.

Execução do Programa
Salve o Script:
Guarde o código em um arquivo com extensão .py.

Execute o Script no Terminal:

bash
Copiar
python nome_do_arquivo.py
Substitua nome_do_arquivo.py pelo nome real do seu arquivo.

Utilizando a Interface Gráfica
Inserção dos Dados de Conexão:

Usuário: Seu nome de usuário para SSH.

Senha: Senha de acesso (campo mascarado).

Host: Endereço IP ou hostname do servidor remoto.

Porta: Porta de conexão (normalmente, 22).

Diretório: Caminho onde os arquivos de saída serão salvos (padrão: diretório atual).

Seleção do Diretório:
Clique no botão “Escolher diretório” para abrir um diálogo e selecionar o local desejado.

Início da Execução:
Após preencher os campos, clique no botão “Executar” para que a conexão seja estabelecida, os comandos sejam executados e os resultados sejam salvos automaticamente.

Detalhamento do Código
Importações e Inicializações:
O script importa as bibliotecas os, paramiko e módulos do tkinter para construir a interface. Variáveis globais, como status_label, auxiliam na atualização visual durante a execução.

Função run_ssh_commands(directory="."):
Responsável por:

Capturar os dados de conexão inseridos pelo usuário.

Conectar via SSH ao host remoto.

Executar uma lista pré-definida de comandos e salvar cada resposta em um arquivo de texto no diretório selecionado.

Atualizar a barra de progresso e mensagens de status durante a execução.

Função choose_directory():
Abre um diálogo para seleção de um diretório e atualiza o campo correspondente na interface.

Interface Gráfica:
A interface utiliza o método grid do tkinter para organizar os elementos visuais (Labels, Entrys e Botões), facilitando a interação do usuário e proporcionando um ambiente responsivo.

Considerações de Segurança
Política de Chaves SSH:
O script utiliza a política AutoAddPolicy, que aceita automaticamente chaves de hosts desconhecidos.
Para ambientes de produção, recomenda-se uma abordagem de verificação de chaves mais robusta.

Proteção de Credenciais:
As senhas são inseridas em campos mascarados, aumentando a segurança na utilização da ferramenta.

Contribuições
Contribuições, sugestões de melhoria e correções são muito bem-vindas. Se você identificou algum problema ou possui ideias para novas funcionalidades, sinta-se à vontade para abrir issues e enviar pull requests no repositório do projeto.


![Tela do Programa](https://github.com/heyleao/Fortinet-Backup/blob/main/Tela%20do%20programa.png
)

