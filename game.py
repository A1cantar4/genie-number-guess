# Guessing Game (Currently Simple)
# Version 1.1.0
import random

# Function to choose difficulty level
def choose_level():
    print("\nTa pronto pra um desafio? Escolha a dificuldade:")
    print("1 - Mamão com açucar! | 1 - 10 Números")
    print("2 - Hummm... ta moleza! | 1 - 50 Números")
    print("3 - Assim que é bom!!! | 1 - 100 Números")
    print("4 - Eu gosto assim, amostradinho! | 1 - 1.000 Números")
    print("5 - For me... IMPOSSIBLE!!! | 1 - 10.000 Números")
    
    # Loop to ensure valid input
    while True:
        choice = input("\nEae? Decidiu qual modo vai encarar? Conta pra gente: ").strip()
        if choice == "1":
            return 1, 10, 3
        elif choice == "2":
            return 1, 50, 5
        elif choice == "3":
            return 1, 100, 7
        elif choice == "4":
            return 1, 1000, 10
        elif choice == "5":
            return 1, 10000, 15
        else:
            print("Opa, as opções são: 1, 2, 3, 4 e 5. Somente essas aventureiro!")

# Function to run a round of the game
def play():
    print("\nSeja bem-vindo ao jogo do Gênio da Lâmpada!")

    lower, upper, max_attempts = choose_level()
    hidden_number = random.randint(lower, upper)
    attempts = 0

    print(f"\nSua missão é adivinhar o número que está entre {lower} e {upper}.\nVocê tem apenas {max_attempts} tentativas")

    while attempts < max_attempts:
        try:
            # Display current attempt / total allowed attempts
            guess = int(input(f"\n({attempts + 1}/{max_attempts}) Qual seu palpite? Me conta ai: "))
            if guess < lower or guess > upper:
                print(f"\nEscolha um número entre {lower} e {upper}!")
                continue

            attempts += 1

            if guess < hidden_number:
                print("Hmmm... você está jogando 'baixo' rsrsrs")
            elif guess > hidden_number:
                print("Mirou demais nas estrelas...")
            else:
                print(f"\nAeeee, você acertou em cheio! Parabéns! \nO número era: {hidden_number} \nTentativas: {attempts}")
                return

        except ValueError:
            print("Meu nobre, acho que cê digitou errado, tenta denovo ai!")

    # If all attempts are used
    print(f"\nÉ... Não foi dessa vez! Tu usou todas as cartas na manga, todas suas {max_attempts} tentativas...")
    print(f"O bendito número secreto era... advinha... isso mesmo... tcharaaaammm: {hidden_number}!")

# Main game loop
while True:
    play()
    repeat = input("\nTa afim de jogar novamente? (S/N): ").strip().lower()
    if repeat != 's':
        print("Valeu pela diversão, tamu junto! Até mais!")
        break