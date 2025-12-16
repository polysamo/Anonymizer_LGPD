import re
import os

def mascarar_texto(texto):
    """
    Função Core: Recebe uma string e aplica as máscaras.
    Cumpre o item: 'Core de Mascaramento' da EAP.
    """
    # 1. Regex de CPF 
    padrao_cpf = r'(\d{3})\.\d{3}\.\d{3}[-](\d{2})'
    
    # 2. Regex de Email
    padrao_email = r'([a-zA-Z0-9])[a-zA-Z0-9._%+-]+(@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
    
    # 3. Regex de Telefone
    padrao_tel = r'(\(\d{2}\) \d)\d{4}-(\d{4})'

    # Aplicação das substituições
    texto_saida = re.sub(padrao_cpf, r'\1.*.*-\2', texto)
    texto_saida = re.sub(padrao_email, r'\1***\2', texto_saida)
    texto_saida = re.sub(padrao_tel, r'\1**-\2', texto_saida)
    
    return texto_saida

def processar_arquivo():
    """
    Função de I/O: Lê um arquivo e salva o resultado.
    """
    nome_input = input("Digite o nome do arquivo (ex: base_clientes.csv): ")
    
    caminhos_tentativa = [
        nome_input,
        os.path.join("data", nome_input),
        os.path.join("..", "data", nome_input)
    ]
    
    arquivo_encontrado = None
    
    # Testa qual caminho existe
    for caminho in caminhos_tentativa:
        if os.path.exists(caminho):
            arquivo_encontrado = caminho
            break
            
    if arquivo_encontrado:
        try:
            print(f"Lendo arquivo de: {arquivo_encontrado}") # Feedback visual
            
            # Leitura
            with open(arquivo_encontrado, 'r', encoding='utf-8') as f:
                conteudo_original = f.read()
            
            # Processamento
            conteudo_mascarado = mascarar_texto(conteudo_original)
            
            # Extrai o diretorio e o nome do arquivo
            diretorio, nome_base = os.path.split(arquivo_encontrado)
            nome_saida = os.path.join(diretorio, f"mascarado_{nome_base}")
            
            with open(nome_saida, 'w', encoding='utf-8') as f:
                f.write(conteudo_mascarado)
            
            print(f"\n[SUCESSO] Arquivo processado!")
            print(f"Salvo como: {nome_saida}\n")
            
        except Exception as e:
            print(f"Erro ao processar arquivo: {e}")
    else:
        print("\n[ERRO] Arquivo não encontrado (Verifique se está na pasta 'data').\n")

def menu():
    """
    Interface CLI simples.
    Cumpre o item: 'Interface CLI' da EAP.
    """
    while True:
        print("=== PROJETO LGPD (CLI) ===")
        print("1. Digitar Texto (Teste Rápido)")
        print("2. Carregar Arquivo (.txt ou .csv)")
        print("3. Sair")
        
        opcao = input("Opção: ")
        
        if opcao == '1':
            texto = input("Digite o texto: ")
            print(f"\nResultado: {mascarar_texto(texto)}\n")
        elif opcao == '2':
            processar_arquivo()
        elif opcao == '3':
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()