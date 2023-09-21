import os
import paramiko
import tkinter as tk
from tkinter import filedialog
from tkinter import Button
from tkinter import ttk

# Definir variável global para barra de status
status_label = None

def run_ssh_commands(directory="."):
    global status_label # Obter variável global para barra de status

    # Obter informações de conexão
    username = user_entry.get()
    password = password_entry.get()
    host = host_entry.get()
    port = port_entry.get()
    directory = directory or "."
    
    # Configurar a mensagem de status
    status_label.config(text="Aguarde, executando")
    
    # Conectar ao host remoto
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host, port=port, username=username, password=password)

    # Executar comandos e salvar em arquivos
    commands = [
        'show antivirus profile',
        'show full-configuration',
        'sh webfilter profile',
        'sh vpn ipsec phase1-interface',
        'sh vpn ipsec phase2-interface',
        'sh firewall vip',
        'sh router static',
        'sh router bgp',
        'sh firewall policy',
        'sh ips sensor',
        'sh sys interface',
        'sh sys ha',
        'sh user ldap',
        'sh user fsso',
        'sh application list'
    ]

    # Verificar se o diretório existe antes de salvar os arquivos
    if not os.path.exists(directory):
        feedback_label.config(text="O diretório selecionado não existe")
        status_label.config(text="Concluído")
        return
    # Configurar a barra de progresso
    progress_var = tk.DoubleVar()
    progress_var.set(0)
    progress_bar = tk.ttk.Progressbar(root, variable=progress_var, maximum=len(commands))
    progress_bar.config(style="red.Horizontal.TProgressbar")
    style = ttk.Style()
    style.theme_use("default")
    style.configure("red.Horizontal.TProgressbar", foreground='red', background='red', thickness=10, bordercolor='black', troughcolor='white')
    progress_bar.grid(row=7, column=1, pady=10)
        
    # Iterar pelos comandos e salvar os arquivos
    for command in commands:
        # Obter o índice do comando atual
        index = commands.index(command)
        # Atualizar a barra de progresso
        progress_var.set(index + 1)
        status_label.config(text="Aguarde, executando ({} de {})".format(index + 1, len(commands)))
        progress_bar.update()
        
        # Executar o comando
        stdin, stdout, stderr = ssh_client.exec_command(command)
        output = stdout.read().decode()
        
        # Salvar a saída em um arquivo
        filename = os.path.join(directory, "{}.txt".format(command.replace(" ", "_")))
        with open(filename, 'w') as f:
            f.write(output)

    # Fechar a conexão SSH
    ssh_client.close()

    # Atualizar o texto do rótulo de feedback e da barra de status
    feedback_label.config(text="Comandos executados com sucesso e resultados salvos em arquivos")
    progress_bar['value'] = len(commands)
    status_label.config(text="Concluído")
    
    # Remover a barra de progresso
    progress_bar.destroy()
    status_label.config(text="")

def choose_directory():
    directory = filedialog.askdirectory()
    if directory:
        directory_entry.delete(0, tk.END)
        directory_entry.insert(0, directory)

# Configurar a interface gráfica
root = tk.Tk()
root.title("SSH Commands")
root.geometry("450x350")

# Label de status
status_label = tk.Label(root, text="")
status_label.grid(row=8, column=1)

# Labels
user_label = tk.Label(root, text="Usuário:")
user_label.grid(row=0, column=0, sticky=tk.W)
password_label = tk.Label(root, text="Senha:")
password_label.grid(row=1, column=0, sticky=tk.W)
host_label = tk.Label(root, text="Host:")
host_label.grid(row=2, column=0, sticky=tk.W)
port_label = tk.Label(root, text="Porta:")
port_label.grid(row=3, column=0, sticky=tk.W)
directory_label = tk.Label(root, text="Diretório:")
directory_label.grid(row=4, column=0, sticky=tk.W)

# Campos de entrada
user_entry = tk.Entry(root)
user_entry.grid(row=0, column=1)
password_entry = tk.Entry(root, show='*')
password_entry.grid(row=1, column=1)
host_entry = tk.Entry(root)
host_entry.grid(row=2, column=1)
port_entry = tk.Entry(root)
port_entry.grid(row=3, column=1)
directory_entry = tk.Entry(root)
directory_entry.grid(row=4, column=1)
directory_entry.insert(0, ".") # Default to current directory

# Botão para escolher diretório
choose_directory_button = Button(root, text="Escolher diretório", command=choose_directory)
choose_directory_button.grid(row=4, column=2)

# Botão para iniciar a função
run_button = Button(root, text="Executar", command=lambda: run_ssh_commands(directory_entry.get()))
run_button.grid(row=5, column=1)

# Feedback label
feedback_label = tk.Label(root, text="")
feedback_label.grid(row=7, column=1)

# Barra de status
status_label = tk.Label(root, text="Pronto")
status_label.grid(row=7, column=1)

# Executar a interface gráfica
root.mainloop()
