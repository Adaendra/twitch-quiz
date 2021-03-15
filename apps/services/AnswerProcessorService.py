from apps.services.stores.QuizStore import quiz_store

"""
AnswerProcessorService
----------------------

Service which contains all methods to process contestants answers.
"""


def processContestantAnswers() -> None:
    for contestant in quiz_store.listContestants:
        if contestant.selected_answer != quiz_store.listQuestions[quiz_store.currentQuestionIndex - 1].answer:
            contestant.number_lives = contestant.number_lives - 1

    quiz_store.listContestants = list(filter(lambda player: player.number_lives > 0,
                                             quiz_store.listContestants))
