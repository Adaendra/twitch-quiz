class Question:

    question: str = ""
    proposals: list[str] = []
    answer = ""
    theme = ""

    def __init__(self):
        pass

    def __init__(self, question, proposals, answer, theme):
        self.question = question
        self.proposals = proposals
        self.answer = answer
        self.theme = theme

    def toJson(self) -> object:
        return {
            "question": self.question,
            "proposals": self.proposals,
            "answer": self.answer,
            "theme": self.theme
        }
