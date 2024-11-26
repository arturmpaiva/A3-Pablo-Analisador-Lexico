import re

# Definir os padrões de tokens
TOKEN_PATTERNS = [
    ("NUMBER", r'\b\d+(\.\d+)?\b'),         # Números inteiros e reais
    ("IDENTIFIER", r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),  # Identificadores
    ("OPERATOR", r'[+\-*/=]'),              # Operadores
    ("PAREN", r'[()]'),                     # Parênteses
    ("WHITESPACE", r'\s+'),                 # Espaços em branco (ignorar)
    ("UNKNOWN", r'.'),                      # Qualquer outro caractere
]

# Função para realizar a análise léxica
def lexer(input_text):
    tokens = []
    position = 0

    while position < len(input_text):
        match = None
        for token_type, pattern in TOKEN_PATTERNS:
            regex = re.compile(pattern)
            match = regex.match(input_text, position)
            if match:
                text = match.group(0)
                if token_type != "WHITESPACE":  # Ignorar espaços em branco
                    tokens.append((token_type, text))
                position = match.end()
                break
        if not match:
            raise SyntaxError(f"Caractere inválido na posição {position}: '{input_text[position]}'")
    
    return tokens

# Exemplo de uso
if __name__ == "__main__":
    code = "x = 3 + 5 * (10 - 4)"
    result = lexer(code)
    for token in result:
        print(token)
