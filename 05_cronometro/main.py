import time

def cronometro(segundos):
    while segundos:
        mins, secs = divmod(segundos, 60)
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        segundos -= 1
    print("00:00\nTempo encerrado!")

if __name__ == "__main__":
    try:
        t = int(input("Digite o tempo em segundos: "))
        cronometro(t)
    except ValueError:
        print("Digite um número válido.")