# 📚 Dashboard de Livros

Projeto da segunda parte da disciplina **Introdução à Programação em Python**.
A cada aula uma nova pasta (`aula01/`, `aula02/`, ...) aparece aqui com o ponto de partida do dia.

## Primeira vez (aula 1)

1. Clique em **Fork** (canto superior direito) para criar a sua cópia deste repositório.
2. No VS Code: `Ctrl+Shift+P` → **Git: Clone** → cole o link do **seu** fork.
3. No terminal do VS Code (PowerShell), dentro da pasta do repositório:

```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass   # libera o script de ativação só nesta janela
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```

## Toda aula (setup rápido)

1. No GitHub, no **seu** fork: **Sync fork** → **Update branch** (traz a pasta da aula nova).
2. Se o computador do laboratório foi apagado: clone de novo e refaça o passo 3 acima.
   Se não foi: no VS Code, **Source Control** → `...` → **Pull**.
3. Configure seu nome no git (só uma vez por máquina):

```powershell
git config --global user.name "Seu Nome"
git config --global user.email "seu-email@exemplo.com"
```

## Importante!

- Trabalhe **somente dentro da pasta da aula do dia** (ex.: `aula03/`). Assim o *Sync fork* nunca dá conflito.
- Ao final: **commit** + **push** e entregue o link do seu repositório.
- Computador compartilhado: ao sair, **deslogue do GitHub** no navegador e no VS Code.
