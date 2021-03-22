from apps.models.Ranking import Ranking
from apps.models.QuizContestant import QuizContestant
from apps.services.stores.QuizStore import quiz_store


"""
RankingService
--------------

Contains all the services related to the rankings.
"""


def calculateRankings() -> Ranking:
    """
    Calculate the top 10 ranking.
    :return: Ranking
    """
    # The number of lives is multiplied by -1 to sort both elements in an ascending order.
    sorted_list = sorted(quiz_store.listContestants, key=lambda x: (x.number_lives * -1, x.contestant_name))

    ranking = Ranking()

    if len(sorted_list) > 0:
        ranking.first = sorted_list[0].contestant_name

    if len(sorted_list) > 1:
        ranking.second = sorted_list[1].contestant_name

    if len(sorted_list) > 2:
        ranking.third = sorted_list[2].contestant_name

    if len(sorted_list) > 3:
        ranking.fourth = sorted_list[3].contestant_name

    if len(sorted_list) > 4:
        ranking.fifth = sorted_list[4].contestant_name

    if len(sorted_list) > 5:
        ranking.sixth = sorted_list[5].contestant_name

    if len(sorted_list) > 6:
        ranking.seventh = sorted_list[6].contestant_name

    if len(sorted_list) > 7:
        ranking.eighth = sorted_list[7].contestant_name

    if len(sorted_list) > 8:
        ranking.ninth = sorted_list[8].contestant_name

    if len(sorted_list) > 9:
        ranking.tenth = sorted_list[9].contestant_name

    return ranking
