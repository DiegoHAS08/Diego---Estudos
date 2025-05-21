times = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Fluminense',
         'Bragantino', 'Athletico-PR', 'Atlético-MG', 'Fortaleza', 'São Paulo',
         'Cuiabá', 'Cruzeiro', 'Internacional', 'Corinthians', 'Goiás',
         'Bahia', 'Santos', 'Vasco', 'América-MG', 'Coritiba')
print(f'Os 5 primeiros são: {times[:5]}')
print(f'Os últimos 4 são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O Corinthians está na {times.index("Corinthians")+1}ª posição')