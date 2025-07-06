# Jogo de Advinhação (Atualmente Simples)
# Import da biblioteca Random para gerar números aleatórios
# Variáveis: 'escolha'(Qual nível), 'menor', 'maior', 'max_tentativas', 'numero_oculto', 'tentativas', 'chute', 'repetir'(Loop opcional)
# Versão 1.0.0

import random

# Função para estabelecer a dificuldade
def dificuldade():
    print("\nTa pronto pra um desafio? Escolha a dificuldade:")
    print("1 - Mamão com açucar! | 1 - 10 Números")
    print("2 - Hummm... ta moleza! | 1 - 50 Números")
    print("3 - Assim que é bom!!! | 1 - 100 Números")
    print("4 - Eu gosto assim, amostradinho! | 1 - 1.000 Números")
    print("5 - For me... IMPOSSIBLE!!! | 1 - 10.000 Números")
    
    # Loop para escolha da dificuldade
    while True:
        escolha = input("\nEae? Decidiu qual modo vai encarar? Conta pra gente: ").strip()
        if escolha == "1":
            return 1, 10, 3
        elif escolha == "2":
            return 1, 50, 5
        elif escolha == "3":
            return 1, 100, 7
        elif escolha == "4":
            return 1, 1000, 10
        elif escolha == "5":
            return 1, 10000, 15
        else:
            print("Opa, as opções são: 1, 2, 3, 4 e 5. Somente essas aventureiro!")
            
# Função que estabelece o padrão do jogo
def jogar():
    print("\nSeja bem-vindo ao jogo do Gênio da Lâmpada!")
    
    menor, maior, max_tentativas = dificuldade()
    numero_oculto = random.randint(menor, maior)
    tentativas = 0  
    
    print(f"\nSua missão é adivinhar o número que está entre {menor} e {maior}.\nVocê tem apenas {max_tentativas} tentativas")
    
    while tentativas < max_tentativas:
        # Exceção para evitar erro na hora da seleção
        try:
            # Exibir = (Tentativas usadas / Tentativas Máximas possíveis)
            chute = int(input(f"\n({tentativas + 1}/{max_tentativas}) Qual seu palpite? Me conta ai: "))
            if chute < menor or chute > maior:
                print(f"\nEscolha um número é entre {menor} e {maior}!")
                continue
            
            tentativas += 1 # Armazenar mais 1 na variável anterior
            
            if chute < numero_oculto:
                print("Hmmm... você está jogando 'baixo' rsrsrs")
            elif chute > numero_oculto:
                print("Mirou demais nas estrelas...")
            else:
                print(f"\nAeeee, você acertou em cheio! Parabéns! \nO número era: {numero_oculto} \nTentativas: {tentativas}")                
                return
                
        except ValueError:
            print("Meu nobre, acho que cê digitou errado, tenta denovo ai!")
            
    print(f"É... Não foi dessa vez! Tu usou todas as cartas na manga, todas suas {max_tentativas} tentativas...")
    print(f"O bendito número secreto era... advinha... isso mesmo... tcharaaaammm: {numero_oculto}!")
    
# Loop opcional para jogar denovo
while True:
    jogar()
    repetir = input("\nTa afim de jogar novamente? (S/N): ").strip().lower()
    if repetir != 's':
        print("Valeu pela diversão, tamu junto! Até mais!")
        break
    