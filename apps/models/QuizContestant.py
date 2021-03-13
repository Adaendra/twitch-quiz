class QuizContestant:
    """
    QuizContestant
    --------------

    Represents a quiz contestant.
    """
    contestant_name: str = ""
    number_lives: int = 0
    selected_answer: str = ""

    def __init__(self, contestant_name, number_lives):
        self.contestant_name = contestant_name
        self.number_lives = number_lives
