from apps.services.stores.QuizStore import quiz_store
from apps.services.RankingService import calculateRankings
from apps.models.QuizContestant import QuizContestant


class TestRankingService:

    # ----- calculateRankings ----- #
    def test_calculateRankings_top0(self):
        quiz_store.listContestants = []

        ranking = calculateRankings()

        assert ranking.first is None
        assert ranking.second is None
        assert ranking.third is None
        assert ranking.fourth is None
        assert ranking.fifth is None
        assert ranking.sixth is None
        assert ranking.seventh is None
        assert ranking.eighth is None
        assert ranking.ninth is None
        assert ranking.tenth is None

    def test_calculateRankings_top1(self):
        quiz_store.listContestants = [
            QuizContestant("player_1", 2)
        ]

        ranking = calculateRankings()

        assert ranking.first == "player_1"
        assert ranking.second is None
        assert ranking.third is None
        assert ranking.fourth is None
        assert ranking.fifth is None
        assert ranking.sixth is None
        assert ranking.seventh is None
        assert ranking.eighth is None
        assert ranking.ninth is None
        assert ranking.tenth is None

    def test_calculateRankings_top2(self):
        quiz_store.listContestants = [
            QuizContestant("player_1", 2),
            QuizContestant("volvic", 3)
        ]

        ranking = calculateRankings()

        assert ranking.first == "volvic"
        assert ranking.second == "player_1"
        assert ranking.third is None
        assert ranking.fourth is None
        assert ranking.fifth is None
        assert ranking.sixth is None
        assert ranking.seventh is None
        assert ranking.eighth is None
        assert ranking.ninth is None
        assert ranking.tenth is None

    def test_calculateRankings_top3(self):
        quiz_store.listContestants = [
            QuizContestant("zorro", 2),
            QuizContestant("player_1", 2),
            QuizContestant("volvic", 3)
        ]

        ranking = calculateRankings()

        assert ranking.first == "volvic"
        assert ranking.second == "player_1"
        assert ranking.third == "zorro"
        assert ranking.fourth is None
        assert ranking.fifth is None
        assert ranking.sixth is None
        assert ranking.seventh is None
        assert ranking.eighth is None
        assert ranking.ninth is None
        assert ranking.tenth is None

    def test_calculateRankings_top4(self):
        quiz_store.listContestants = [
            QuizContestant("zorro", 2),
            QuizContestant("player_1", 2),
            QuizContestant("volvic", 3),
            QuizContestant("A_player", 3)
        ]

        ranking = calculateRankings()

        assert ranking.first == "A_player"
        assert ranking.second == "volvic"
        assert ranking.third == "player_1"
        assert ranking.fourth == "zorro"
        assert ranking.fifth is None
        assert ranking.sixth is None
        assert ranking.seventh is None
        assert ranking.eighth is None
        assert ranking.ninth is None
        assert ranking.tenth is None

    def test_calculateRankings_top5(self):
        quiz_store.listContestants = [
            QuizContestant("zorro", 2),
            QuizContestant("player_1", 2),
            QuizContestant("volvic", 3),
            QuizContestant("A_player", 3),
            QuizContestant("AAA", 1)
        ]

        ranking = calculateRankings()

        assert ranking.first == "A_player"
        assert ranking.second == "volvic"
        assert ranking.third == "player_1"
        assert ranking.fourth == "zorro"
        assert ranking.fifth == "AAA"
        assert ranking.sixth is None
        assert ranking.seventh is None
        assert ranking.eighth is None
        assert ranking.ninth is None
        assert ranking.tenth is None

    def test_calculateRankings_top6(self):
        quiz_store.listContestants = [
            QuizContestant("zorro", 2),
            QuizContestant("VVV", 1),
            QuizContestant("player_1", 2),
            QuizContestant("volvic", 3),
            QuizContestant("A_player", 3),
            QuizContestant("AAA", 1)
        ]

        ranking = calculateRankings()

        assert ranking.first == "A_player"
        assert ranking.second == "volvic"
        assert ranking.third == "player_1"
        assert ranking.fourth == "zorro"
        assert ranking.fifth == "AAA"
        assert ranking.sixth == "VVV"
        assert ranking.seventh is None
        assert ranking.eighth is None
        assert ranking.ninth is None
        assert ranking.tenth is None

    def test_calculateRankings_top7(self):
        quiz_store.listContestants = [
            QuizContestant("zorro", 2),
            QuizContestant("VVV", 1),
            QuizContestant("player_1", 2),
            QuizContestant("player_10", 2),
            QuizContestant("volvic", 3),
            QuizContestant("A_player", 3),
            QuizContestant("AAA", 1)
        ]

        ranking = calculateRankings()

        assert ranking.first == "A_player"
        assert ranking.second == "volvic"
        assert ranking.third == "player_1"
        assert ranking.fourth == "player_10"
        assert ranking.fifth == "zorro"
        assert ranking.sixth == "AAA"
        assert ranking.seventh == "VVV"
        assert ranking.eighth is None
        assert ranking.ninth is None
        assert ranking.tenth is None

    def test_calculateRankings_top8(self):
        quiz_store.listContestants = [
            QuizContestant("zorro", 2),
            QuizContestant("VVV", 1),
            QuizContestant("player_1", 2),
            QuizContestant("player_10", 2),
            QuizContestant("volvic", 3),
            QuizContestant("A_player", 3),
            QuizContestant("AAA", 1),
            QuizContestant("WWW", 1)
        ]

        ranking = calculateRankings()

        assert ranking.first == "A_player"
        assert ranking.second == "volvic"
        assert ranking.third == "player_1"
        assert ranking.fourth == "player_10"
        assert ranking.fifth == "zorro"
        assert ranking.sixth == "AAA"
        assert ranking.seventh == "VVV"
        assert ranking.eighth == "WWW"
        assert ranking.ninth is None
        assert ranking.tenth is None

    def test_calculateRankings_top9(self):
        quiz_store.listContestants = [
            QuizContestant("zorro", 2),
            QuizContestant("VVV", 1),
            QuizContestant("player_1", 2),
            QuizContestant("player_10", 2),
            QuizContestant("volvic", 3),
            QuizContestant("A_player", 3),
            QuizContestant("AAA", 1),
            QuizContestant("WWW", 1),
            QuizContestant("YYY", 1)
        ]

        ranking = calculateRankings()

        assert ranking.first == "A_player"
        assert ranking.second == "volvic"
        assert ranking.third == "player_1"
        assert ranking.fourth == "player_10"
        assert ranking.fifth == "zorro"
        assert ranking.sixth == "AAA"
        assert ranking.seventh == "VVV"
        assert ranking.eighth == "WWW"
        assert ranking.ninth == "YYY"
        assert ranking.tenth is None

    def test_calculateRankings_top9(self):
        quiz_store.listContestants = [
            QuizContestant("zorro", 2),
            QuizContestant("VVV", 1),
            QuizContestant("player_1", 2),
            QuizContestant("player_10", 2),
            QuizContestant("volvic", 3),
            QuizContestant("A_player", 3),
            QuizContestant("AAA", 1),
            QuizContestant("ZZZ", 1),
            QuizContestant("WWW", 1),
            QuizContestant("YYY", 1)
        ]

        ranking = calculateRankings()

        assert ranking.first == "A_player"
        assert ranking.second == "volvic"
        assert ranking.third == "player_1"
        assert ranking.fourth == "player_10"
        assert ranking.fifth == "zorro"
        assert ranking.sixth == "AAA"
        assert ranking.seventh == "VVV"
        assert ranking.eighth == "WWW"
        assert ranking.ninth == "YYY"
        assert ranking.tenth == "ZZZ"
