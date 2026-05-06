import random

# Lista de palavras possíveis
palavras = ["python", "computador", "programacao", "jogo", "desenvolvimento"]

# Escolhe uma palavra aleatória
palavra_misteriosa = random.choice(palavras)

tentativas = 10
acertou = False

print("🎮 Bem-vindo ao jogo da palavra misteriosa!")
print(f"Você tem {tentativas} tentativas para adivinhar.\n")

while tentativas > 0:
    palpite = input("Digite seu palpite: ").lower()

    if palpite == palavra_misteriosa:
        print("🎉 Parabéns! Você acertou a palavra!")
        acertou = True
        break
    else:
        tentativas -= 1
        print(f"❌ Errado! Tentativas restantes: {tentativas}\n")

if not acertou:
    print(f"😢 Você perdeu! A palavra era: {palavra_misteriosa}")