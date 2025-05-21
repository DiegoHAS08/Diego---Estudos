palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso',
            'grátis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for palavra in palavras:
    vogais = [letra for letra in palavra if letra.lower() in 'aeiou']
    print(f'Na palavra {palavra.upper()} temos {" ".join(vogais)}')