SSH Commands Executor com Interface Gráfica
Este programa foi desenvolvido para executar uma série de comandos SSH em um host remoto e salvar as saídas de cada comando em arquivos de texto dentro de um diretório selecionado pelo usuário. A aplicação utiliza a biblioteca paramiko para estabelecer conexões SSH e tkinter para criar uma interface gráfica que facilita a entrada de dados e o acompanhamento do progresso da execução dos comandos.

Funcionalidades
Conexão SSH: Utiliza o módulo paramiko para estabelecer uma conexão SSH com um host remoto, adotando uma política de aceitação automática de chaves de host.

Execução de Comandos: Executa uma série de comandos pré-definidos no host remoto e captura as saídas.

Interface Gráfica: Emprega o tkinter para criar uma interface interativa onde o usuário informa as credenciais de conexão (usuário, senha, host, porta) e escolhe o diretório onde os resultados serão salvos.

Barra de Progresso e Feedback: Atualiza uma barra de progresso e fornece mensagens de status para informar o andamento da execução dos comandos.

Salvamento de Resultados: Cria arquivos de texto para cada comando executado, nomeando-os a partir do comando utilizado (com espaços substituídos por sublinhados).

Requisitos
Python 3.x

Bibliotecas:

paramiko: Para conexões SSH.
Instalação: pip install paramiko

tkinter: Geralmente vem pré-instalado com o Python. Caso não esteja disponível, em distribuições Linux pode ser necessário instalar o pacote python3-tk.

Sistema Operacional: Qualquer sistema que suporte Python e os módulos acima.

Como Usar
Instalação e Dependências:
Certifique-se de que o Python e as bibliotecas necessárias estejam instalados. Se necessário, instale o paramiko executando:

bash
Copiar
pip install paramiko
Executando o Programa:
Execute o script através do terminal:

bash
Copiar
python nome_do_arquivo.py
Substitua nome_do_arquivo.py pelo nome do arquivo onde o código foi salvo.

Usando a Interface Gráfica:

Preenchimento dos Campos:
Insira as informações solicitadas:

Usuário: Nome de usuário para acesso SSH.

Senha: Senha associada ao usuário (campo mascarado).

Host: Endereço IP ou hostname do servidor remoto.

Porta: Porta para conexão SSH (normalmente 22).

Diretório: Local onde os arquivos de saída serão salvos. O diretório atual (".") é o padrão.

Selecionar Diretório:
Clique no botão "Escolher diretório" para abrir um diálogo e selecionar um diretório desejado.

Executar os Comandos:
Após preencher os campos, clique no botão "Executar".
O programa estabelecerá a conexão SSH, executará os comandos listados e atualizará a barra de progresso conforme cada comando é processado.

Comandos SSH Executados
O programa executa os seguintes comandos no host remoto:

show antivirus profile

show full-configuration

sh webfilter profile

sh vpn ipsec phase1-interface

sh vpn ipsec phase2-interface

sh firewall vip

sh router static

sh router bgp

sh firewall policy

sh ips sensor

sh sys interface

sh sys ha

sh user ldap

sh user fsso

sh application list

Cada comando terá sua saída salva em um arquivo de texto, nomeado conforme o comando (com espaços substituídos por sublinhados).

Estrutura de Código
Importações e Inicializações:
São importados módulos essenciais (os, paramiko, tkinter, dentre outros). Variáveis globais, como status_label, são definidas para atualizar a interface.

Função run_ssh_commands(directory="."):
Responsável por:

Obter os dados de conexão a partir dos campos de entrada.

Atualizar a interface com mensagens de status e a barra de progresso.

Estabelecer a conexão SSH e executar os comandos.

Salvar cada saída de comando em um arquivo dentro do diretório escolhido.

Fechar a conexão e atualizar os feedbacks na interface.

Função choose_directory():
Abre um diálogo para seleção do diretório e atualiza o campo de entrada com o diretório escolhido.

Configuração da Interface Gráfica:
A interface é organizada utilizando o método grid do tkinter, onde são posicionados os Labels, Entrys e Botões. Também inclui uma barra de progresso que é dinamicamente atualizada conforme os comandos são executados.

Considerações
Validação do Diretório:
Caso o diretório especificado não exista, o programa notifica o usuário e interrompe a execução.

Segurança:
Embora o script utilize uma política que aceita automaticamente chaves de host desconhecidas (AutoAddPolicy), considere os riscos de segurança associados e ajuste conforme necessário para ambientes de produção.

Feedback Visual:
A aplicação fornece feedback visual, atualizando a barra de progresso e mensagens para que o usuário tenha clareza sobre o andamento da execução dos comandos.

Contribuições
Contribuições e sugestões de melhoria são bem-vindas. Caso identifique algum problema ou tenha ideias para novas funcionalidades, sinta-se à vontade para contribuir para o aprimoramento do projeto.


![Tela do Programa](https://github.com/heyleao/Fortinet-Backup/blob/main/Tela%20do%20programa.png
)

