# Approach:
    The most intuitive approach to me was to compare the batsmen along lines of batting style, and attempt to find a bowler fit to a given batsmen by comparing the batsman to other batsmen, and favouring bowlers who performed well against batsmen with a similar style. In doing this, my algorithm implements a kind of heuristic, using comparable batsmen to suggest a bowler.

# Assumptions:
    Given a minimal knowledge of cricket as a whole, I assumed that batsmen who presented similar statistics and handedness could be assumed to have a similar set of strengths and weaknesses with regards to which bowlers they would play well against. 
    Similarly, I assumed that a bowler with the same primary hand and style would perform well against the same set of batsmen as a similar bowler. I also simplified bowling style down to 4 possible combinations, made up of left or right handedness and spin or pace bowling.

# Implementation:
    I used 6 pieces of data from the batsmen to perform comparisons between them. These were their handedness, aggregate runs, fours, sixes, socring rate and the bowlers who dimissed them. I used these values to allow a score to be generated representing how similar each batsman was to the input batsman, and using this score to weight their input to the bowler choice accordingly. Bowlers where compared according to their handedness and bowling style (i.e. pace vs spin bowling), allowing a bowler to be chosen for a batsmen that has some combination of the following characteristics:
        - Success against batsmen similar to the input batsman
        - Bowling style similar to other bowlers who were successful against these batsmen

# Pseudocode:
    individuality_coefficient(bowler, bowlers):
    // Accepts 2 inputs: bowler, the bowler from which to calculae the differences
    //  and bowlers, the population to compare against
    // Returns a value which will be lower the more unique this bowler is
        score = 1
        for other in bowlers:
            if the bowler uses the same hand:
                multiply score by 1.25
            else:
                multiply score by 0.75
            if the bowler uses the same style:
                multiplied score by 1.25
            else:
                multiply score by 0.75
        return score

    choose_bowler(batsman, batsmen, bowlers):
    // Accepts 3 inputs: batsman, the currently batting player, batsmen, the list of all batsmen, and bowlers, the list of all bowlers.
    // Selects the bowler thought to be the best fit for the current batsman and returns this bowler.
    // Can easily be modified to choose the bowler from a list of available bowlers instead of a global list.

        batsmen_scores = dictionary
        for each player in batsmen:
            score = 0
            add the difference multiplied by 10 between the fours and sixes of this player and input batsman to score
            add the difference in scoring rate between this player and input batsman to score
            if this player uses the same hand as input batsman:
                multiply score by 0.75
            else:
                multiply score by 1.25
            set batsmen_scores[player] to score
            
        bowler_scores = dictionary of bowlers as keys with values initialised to 0
        for each player in batsmen:
            for each bowler which dismissed this player:
                increase bowler_scores[bowler] by batsmen_scores[player] multiplied by individuality_coefficient(this bowler, other bowlers)

        return the bowler with the highest score
