# SSH Commands GUI Tool

![Python](https://img.shields.io/badge/Made%20with-Python-blue?style=flat-square)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

## 📌 Descrição

Ferramenta gráfica (GUI) feita em Python para executar múltiplos comandos SSH em um equipamento (como Fortigate) e salvar automaticamente os resultados em arquivos `.txt`.

✔️ Interface intuitiva  
✔️ Suporte a múltiplos comandos SSH  
✔️ Salva a saída de cada comando em arquivos separados  
✔️ Barra de progresso com feedback visual  
✔️ Instalador `.exe` disponível para uso sem Python instalado

---

## 🖼️ Interface

![Tela do Programa](https://github.com/heyleao/Fortinet-Backup/blob/main/Tela%20do%20programa.png
)

---

## 🚀 Instalação

### ✅ Método 1: Executável (.exe)

Se você não tem Python instalado, basta baixar e rodar o executável:

👉 **[Download do Executável (.exe)]([https://github.com/seuusuario/seurepositorio/releases])**

Sem necessidade de instalação de dependências!

---

### ✅ Método 2: Rodando via código Python

#### Pré-requisitos:

- Python 3.8+
- Pip
- Instalar dependências:

```bash
pip install paramiko
```

🔐 Funcionalidades
Conecta via SSH utilizando paramiko

Executa os comandos abaixo no equipamento remoto:

```bash
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
```

Salva a saída de cada comando em arquivos separados no diretório selecionado

Exibe progresso visual durante a execução

🧰 Tecnologias Utilizadas
Python 🐍

Paramiko (conexão SSH)

Tkinter (interface gráfica)

🛡️ Segurança
As credenciais são digitadas na interface e não são armazenadas. Use com responsabilidade e apenas em ambientes controlados.

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

📬 Contato
Criado por hey_leao - Entre em contato para dúvidas, melhorias ou sugestões.


