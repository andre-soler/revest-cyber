README – Tarefa 1: SAST (Semgrep)
Descrição

Implementação de SAST (Static Application Security Testing) utilizando Semgrep no GitHub Actions.
O objetivo é identificar vulnerabilidades no código-fonte durante o processo de desenvolvimento.

Configuração

Arquivo de workflow: .github/workflows/sast.yml

Gatilhos: push e pull_request para a branch main

Execução

Sempre que houver um commit ou pull request, o pipeline executa o Semgrep para análise estática de código.

Caso vulnerabilidades sejam encontradas, o pipeline falha.

Evidência

Workflow configurado no GitHub Actions com sucesso ✅

Relatórios disponíveis no histórico de execuções.

Entregável

Relatório automático de vulnerabilidades no código-fonte com base em regras de segurança.

📌 README – Tarefa 2: DAST (OWASP ZAP)
Descrição

Implementação de DAST (Dynamic Application Security Testing) utilizando OWASP ZAP no GitHub Actions.
O objetivo é testar a aplicação em execução para identificar vulnerabilidades em tempo real.

Configuração

Arquivo de workflow: .github/workflows/dast.yml

Gatilhos: workflow_dispatch (execução manual) e push na branch main

Ferramenta: zaproxy/action-baseline

Execução

O pipeline inicializa a aplicação (via Docker Compose).

OWASP ZAP executa um baseline scan contra o alvo configurado (http://testphp.vulnweb.com).

Gera um relatório HTML anexado como artefato no GitHub Actions.

Evidência

Execuções registradas no GitHub Actions.

Artefato report.html disponível para download.

Entregável

Relatório HTML com vulnerabilidades dinâmicas encontradas pela varredura OWASP ZAP.

📌 README – Tarefa 3: SCA (Dependency Review)
Descrição

Implementação de SCA (Software Composition Analysis) para analisar bibliotecas e dependências externas utilizadas no projeto.

Configuração

Arquivo de workflow: .github/workflows/cicd.yml (pipeline unificado)

Job: dependency-review

Ferramenta: actions/dependency-review-action@v4

Execução

Executado automaticamente em pull requests para a branch main.

Analisa as dependências do requirements.txt e verifica:

Versões desatualizadas

CVEs conhecidos

Licenças incompatíveis

Evidência

Execuções registradas no GitHub Actions (job SCA - Revisão de Dependências).

Alertas de vulnerabilidades de dependências.

Entregável

Relatório de dependências com riscos associados, sugestões de atualização e plano de ação.

📌 README – Tarefa 4: Integração e Monitoramento (CI/CD)
Descrição

Pipeline unificado de segurança CI/CD consolidando SAST, DAST e SCA no GitHub Actions.
Objetivo: garantir segurança contínua no ciclo de desenvolvimento.

Configuração

Arquivo de workflow: .github/workflows/cicd.yml

Jobs:

sast → análise de código com Semgrep

dast → varredura dinâmica com OWASP ZAP

sca → análise de dependências com Dependency Review

Funcionalidades

Gatilhos automáticos em push e pull_request

Bloqueio de deploy em caso de vulnerabilidades críticas

Relatórios automáticos gerados em cada execução

Monitoramento contínuo via GitHub Actions

Evidência

Pipeline rodando com sucesso no GitHub Actions ✅

Logs e relatórios disponíveis em cada execução

Entregável

Documentação do pipeline CI/CD integrado com logs, alertas e políticas de segurança aplicadas.
