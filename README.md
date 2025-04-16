# SSH Commands Executor  
*Interface Gráfica para Execução Automatizada de Comandos SSH*

---

## Índice

- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Requisitos](#requisitos)
- [Configuração e Uso](#configuração-e-uso)
- [Detalhamento do Código](#detalhamento-do-código)
- [Considerações de Segurança](#considerações-de-segurança)
- [Contribuições](#contribuições)

---

## Visão Geral

O **SSH Commands Executor** é uma ferramenta que automatiza a execução de comandos via SSH em hosts remotos.  
A aplicação utiliza a biblioteca **paramiko** para gerenciamento de conexões SSH e **tkinter** para disponibilizar uma interface gráfica interativa, permitindo que o usuário configure os parâmetros de conexão e acompanhe o progresso da execução dos comandos.

---

## Funcionalidades

- **Conexão SSH:**  
  Estabelece uma conexão segura com o host remoto utilizando as credenciais fornecidas pelo usuário.

- **Execução Automatizada de Comandos:**  
  Executa uma sequência de comandos pré-definidos e armazena a saída de cada comando em arquivos de texto individuais.

- **Interface Gráfica Amigável:**  
  Permite a entrada de dados como usuário, senha, host, porta e diretório, além de proporcionar uma barra de progresso e mensagens de status para monitoramento.

- **Feedback Visual:**  
  Atualiza dinamicamente uma barra de progresso e exibe mensagens de status para garantir que o usuário esteja ciente do andamento do processo.

---

## Requisitos

- **Python 3.x**

- **Bibliotecas Necessárias:**
  - **paramiko:**  
    Instalação via:
    ```bash
    pip install paramiko
    ```
  - **tkinter:**  
    Geralmente incluso nas distribuições padrão do Python. Em sistemas Linux, pode ser necessário instalar o pacote `python3-tk`.

- **Sistema Operacional:**  
  Qualquer sistema que suporte Python e as bibliotecas acima.

---

## Configuração e Uso

### Instalação

1. **Clone ou Baixe o Repositório:**  
   Certifique-se de que todos os arquivos do projeto estejam no seu ambiente de trabalho.

2. **Instale as Dependências:**  
   Execute:
   ```bash
   pip install paramiko


![Tela do Programa](https://github.com/heyleao/Fortinet-Backup/blob/main/Tela%20do%20programa.png
)

