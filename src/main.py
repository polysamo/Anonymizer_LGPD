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