# Guessing Game (Jogo de Adivinhação)

A simple command-line number guessing game in Portuguese. This is a beginner-friendly Python project that uses basic input/output operations, conditionals, and random number generation.

## Purpose

The goal of the game is to guess the hidden number within a limited number of attempts. Difficulty levels vary the range and allowed guesses.

## Technologies Used

- Python 3
- Standard Library (`random`)

## Features

- 5 Difficulty levels with increasing number ranges
- Custom messages and humor in Portuguese
- Input validation and error handling
- Infinite game loop with replay option

## File Structure

```
guessing-game/
├── game.py          # Main game file
└── README.md        # Documentation
```

## How to Run

1. Clone or download the repository:

```bash
git clone https://github.com/your-username/guessing-game.git
cd guessing-game
```

2. Run the script:

```bash
python game.py
```

> Make sure you have Python 3 installed and added to your system's PATH.

## Example (in-game output)

```text
Ta pronto pra um desafio? Escolha a dificuldade:
1 - Mamão com açucar! | 1 - 10 Números
2 - Hummm... ta moleza! | 1 - 50 Números
3 - Assim que é bom!!! | 1 - 100 Números
4 - Eu gosto assim, amostradinho! | 1 - 1.000 Números
5 - For me... IMPOSSIBLE!!! | 1 - 10.000 Números

Eae? Decidiu qual modo vai encarar? Conta pra gente: 2

Sua missão é adivinhar o número que está entre 1 e 50.
Você tem apenas 5 tentativas

(1/5) Qual seu palpite? Me conta ai: 25
Hmmm... você está jogando 'baixo' rsrsrs

(2/5) Qual seu palpite? Me conta ai: 38
Mirou demais nas estrelas...

(3/5) Qual seu palpite? Me conta ai: 33
Aeeee, você acertou em cheio! Parabéns! 
O número era: 33 
Tentativas: 3
```

## Author

Made by [@A1cantar4](https://github.com/A1cantar4)

---

Feel free to fork, improve, or use it as a base for learning or teaching Python!