class Bowler():
    def __init__(self, name, hand, style):
        self.name = name # Name of the bowler
        self.hand = hand # Primary hand used for bowling: l, r, a
        self.style = style # Bowling style: spin, pace

    def individuality_coefficient(self, bowlers):
        score = 1
        for bowler in bowlers:
            score *= 1.25 if bowler.hand == self.hand else 0.75
            score *= 1.25 if bowler.style == self.style else 0.75            

        return score # This number is higher the more similar this bowler is to the rest of the set

class Batsman():
    def __init__(self, name, hand, total, fours, sixes, rate, dismissals):
        self.name = name # Name of the batsman
        self.hand = hand # Primary hand for batting: l, r, a
        self.fours = fours * 4 / total # Percentage of runs from fours
        self.sixes = sixes * 6 / total # Percentage of runs from sixes
        self.rate = rate # Scoring rate (avg runs per 100 bowls)
        self.dismissals = dismissals # List of bowlers who have bowled out this batsman

    def score_batsmen(self, batsmen):
        scores = {}
        for batsman in batsmen: # For each batsman, create a score indicating their similarity to this batsman.
            score = 0 # Measure of how different this batsman is
            score += abs(batsman.fours - self.fours) * 10 # Number is quite small, so 10x
            score += abs(batsman.sixes - self.sixes) * 10 # ^
            score += abs(batsman.rate - self.rate) # Often reasonably sized
            if batsman.hand == self.hand:
                score *= 0.75 # lower scores are better
            else:
                score *= 1.25
            scores[batsman.name] = 10 / score if score > 0 else 100

        return scores

    def choose_bowler(self, bowlers, batsmen):
        batsmen = batsmen + [self] # Add self to batsmen to consider this batsman's former dismissals
        batsmen_scores = self.score_batsmen(batsmen) # Coefficient that tells us how similar each batsman is
        bowlers = {b.name:b for b in bowlers} # Access bowler by their name
        bowler_scores = {b:0 for b in bowlers} # Store a score for each bowler
        hand = 0
        style = 0

        for batsman in batsmen:
            for bowler in batsman.dismissals:
                if bowler in bowlers:
                    modifier = batsmen_scores[batsman.name] * bowlers[bowler].individuality_coefficient([bowlers[b] for b in batsman.dismissals if b != bowler])
                    
                    # if bowlers[bowler].hand == 'right':
                    #     hand += modifier
                    # elif bowlers[bowler].hand == 'left':      
                    #     hand -= modifier

                    # if bowlers[bowler].style == 'pace':
                    #     style += modifier
                    # elif bowlers[bowler].style == 'spin':
                    #     style -= modifier

                    bowler_scores[bowler] += modifier

                else:
                    print(f'Bowler not found: {bowler}')

        return max(bowler_scores, key = lambda k:bowler_scores[k])
                    

