# Effectiveness
    Although the algorithm obviously hasn't been tested in a real world environment, some analysis was performed, with expected outcomes compared to the algorithm's output.

    In these cases, the algorithm proved reliable, suggesting in each case a bowler who had been successful against batsmen with similar characteristics to the input batsman.

# Difficulties
    Some difficulties were encountered in the construction of this algorithm. It was initially unclear how best to model a system of batsmen; whether an approach using some kind of graph was optimal or if it was better to use a numerical approach, which was the solution used. 
    A graphed solution offered the benefits of allowing the use of traditional graph traversal algorithms, while it imposed the disadvantage of having to express the batsman and bowler data on a graph, possibly resulting in oversimplification.
    A numerical solution was therefore chosen, as it allowed for fuller expression of the available data at a lower cost of ingenuity.

# Improvements
    The current implementation (in algorithm.py) isn't capable of evaluating a bowler who hasn't bowled against any of the batsmen in the input population. It could be modified to allow for this.

    A different approach could be considered using some kind of graph traversal technique. However, this approach doesn't seem optimal in this situation because a number of characteristics for each player are considered with the current implementation, such as hand and scoring rate, making it difficult to account for all variables in a rigid structure such as a graph.

# Documentation
    The file provided (algorithm.py) includes 2 classes, Bowler and Batsman. A selection of sample players are provided below this and a statement implements the bowler selection method. 

    Detailed discussion of classes and member methods:
        Bowler:
            The bowler class is designed to model a bowler's style, and so accepts 'name', a string to identify the bowler, 'hand', a string to identify the handedness of the bowler (i.e. 'left' or 'right') and style, a string to identify the bowling style of the play; either 'spin' or 'pace'.
            The class has one function attribute: 
            
            'individuality_coefficient', which accepts one argument 'bowlers'. This function compares the bowler to each of the bowlers in the input list, adjusting 'score' up or down based on how similar this bowler is to the input bowlers. The function will output a higher value the more similar it is to the input set, and is therefore useful for scaling the effect of this bowler on a suggestion.

        Batsman:
            The batsman class is intended to model the playstyle of a player, and accepts 'name' as an identifier, followed by 'hand', 'total', 'fours' and 'sixes', an assortment of play statistics, and 'dismissals' a list of names of bowlers who have bowled out this batsman.

            'score_batsmen' is a function accepting a single argument 'batsmen'. The function compares the Batsman object to each of the batsmen in the input list, assigning each a score. It returns a dictionary containing the names of the input batsmen as keys and their scores as values.

            'choose_bowler' accepts bowlers and batsmen, and chooses an optimal bowler for this Batsman instance based on the effectiveness of the input bowlers against the input batsmen, weighting each bowler based on how well it performed against similar batsmen.
