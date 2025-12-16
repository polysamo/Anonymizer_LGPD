# 🛡️ DataShield Anonymizer

> Ferramenta CLI para anonimização de dados sensíveis e adequação básica à LGPD.

Este projeto é uma ferramenta de linha de comando (CLI) desenvolvida em **Python** que processa arquivos de texto e planilhas para ocultar automaticamente informações pessoais identificáveis (PII), garantindo maior privacidade e segurança no manuseio de dados.

---

## 👥 Autores
* **Antonio Roger Sousa de Morais**
* **Polyana dos Santos Moraes**

---

## ⚙️ Como Funciona

O **DataShield Anonymizer** funciona como um filtro de privacidade. Ao receber um arquivo de entrada, o script executa as seguintes etapas:

1.  **Leitura e Detecção:** O sistema lê o conteúdo do arquivo (suporta `.txt` e `.csv`) e percorre o texto buscando padrões específicos utilizando **Expressões Regulares (Regex)**.
2.  **Mascaramento:**
    * **CPF:** Mantém apenas os dígitos verificadores ou parte do padrão, ocultando o restante (ex: `***.***.789-00`).
    * **E-mail:** Oculta o usuário, mantendo o domínio para contexto (ex: `***@gmail.com`).
    * **Telefone:** Mascara o número principal, mantendo o DDD (ex: `(91) *****-1234`).
3.  **Exportação:** Gera um *novo arquivo* com o prefixo `mascarado_`, preservando o arquivo original intacto.

> **Nota Técnica:** O script força a codificação `UTF-8` para evitar erros comuns de leitura em sistemas Windows.

---

## 🚀 Como Rodar o Projeto

### Pré-requisitos
* Ter o [Python 3.x](https://www.python.org/downloads/) instalado em sua máquina.

### Passo a Passo

1.  **Clone o repositório** (ou baixe os arquivos):
    ```bash
    git clone [https://github.com/seu-usuario/datashield-anonymizer.git](https://github.com/seu-usuario/datashield-anonymizer.git)
    cd datashield-anonymizer
    ```

2.  **Execute o script principal:**
    ```bash
    python datashield.py
    ```

3.  **Utilize o Menu Interativo:**
    * O terminal exibirá um menu. Escolha a **Opção 1**.
    * Digite o nome do arquivo que deseja processar (certifique-se de que o arquivo esteja na mesma pasta do script).
    * Exemplo de entrada: `clientes.csv`

4.  **Verifique o Resultado:**
    * O programa irá gerar o arquivo `mascarado_clientes.csv` no mesmo diretório.