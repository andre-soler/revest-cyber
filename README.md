# revest-cyber
🔒 Projeto ReVeste – Tarefa 1 (SAST)
🎯 Objetivo

Implementar SAST (Static Application Security Testing) no repositório para identificar vulnerabilidades no código-fonte ainda na fase de desenvolvimento, garantindo que falhas críticas não cheguem à produção.

🛠️ Passo a passo realizado
1. Criação do repositório

Criado no GitHub com nome revest-cyber.

Estrutura inicial:

revest-cyber/
├── src/
│   └── app.py
├── tests/
└── .github/
    └── workflows/
        └── sast.yml

2. Código de exemplo (src/app.py)

Foi incluído um código vulnerável propositalmente para que o SAST pudesse detectar a falha:

import sqlite3

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    # 🚨 Vulnerável: SQL Injection
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    return cursor.fetchall()

3. Configuração do Workflow (.github/workflows/sast.yml)

Arquivo de pipeline com Semgrep:

name: SAST - Semgrep

on:
  pull_request:
  push:
    branches: [ "main" ]

jobs:
  semgrep:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout código
        uses: actions/checkout@v3

      - name: Instalar Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Instalar Semgrep
        run: pip install semgrep

      - name: Rodar análise SAST
        run: semgrep --config auto src/ --error

4. Execução

Primeiro commit: falhou, pois detectou SQL Injection.

Segundo commit: correção aplicada → pipeline passou ✅

# ✅ Correção com consulta parametrizada
cursor.execute("SELECT * FROM users WHERE username = ?", (username,))

📊 Resultado esperado

Detectar falhas críticas automaticamente.

Bloquear merges até que a vulnerabilidade seja corrigida.

Registro de relatórios na aba Actions do GitHub.

⚖️ Nota Ética

Este exercício usa vulnerabilidades propositais apenas para fins acadêmicos.

Em ambientes reais:

O código deve ser corrigido imediatamente.

O pipeline deve ser monitorado continuamente.

É obrigatório respeitar normas de LGPD e políticas internas de segurança.
