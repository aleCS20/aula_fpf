import random

numero_secreto = random.randint(1, 100)
tentativas = 7

print("🎮 Jogo: Adivinhe o número!")
print("Estou pensando em um número entre 1 e 100.")
print(f"Você tem {tentativas} tentativas.\n")

while tentativas > 0:
    try:
        palpite = int(input("Digite seu palpite: "))

        if palpite == numero_secreto:
            print("🎉 Você acertou!")
            break
        elif palpite < numero_secreto:
            print("📉 Muito baixo!")
        else:
            print("📈 Muito alto!")

        tentativas -= 1
        print(f"Tentativas restantes: {tentativas}\n")

    except ValueError:
        print("⚠️ Digite um número válido!\n")

if tentativas == 0:
    print(f"😢 Fim de jogo! O número era {numero_secreto}.")