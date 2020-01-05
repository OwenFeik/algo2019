import random

victories = {
    'r': 's',
    's': 'p',
    'p': 'r'
}

class Select_Random():
    rolls = {
        1: 'r',
        2: 'p',
        3: 's'
    }

    def choose(self, prev):
        return rolls[randint(1, 3)]

class Select_Markov():
    def __init__(self):
        self._prev = None
        self.tracking = {
            'r': {
                'r': 1,
                'p': 1,
                's': 1
            },
            'p': {
                'r': 1,
                'p': 1,
                's': 1
            },
            's': {
                'r': 1,
                'p': 1,
                's': 1
            }
        }

    def get_weights(self, prev):
        return [self.tracking[prev]['r'], self.tracking[prev]['p'], self.tracking[prev]['s']]

    def choose(self, prev):
        if self._prev:
            self.tracking[self._prev][prev] += 1
        self._prev = prev

        if prev:
            return random.choices(['p', 's', 'r'], weights = self.get_weights(prev), k = 1)[0]
        else:
            return random.choice(['r', 'p', 's'])

wins = 0
total = 0
prev = None
computer = Select_Markov()
while 1:
    choice = input('Rock Paper or Scissors? > ')

    if choice in victories:
        cpu_choice = computer.choose(prev)

        total += 1

        if victories[cpu_choice] == choice:
            wins += 1
            print(f'Computer wins! {round(wins / total, 2)}')
        elif victories[choice] == cpu_choice:
            print(f'Player wins! {round(wins / total, 2)}')
        else:
            print('Draw!')

        prev = choice
    else:
        print('Please choose r, p or s')
