from apps.services.stores.RewardIdStore import RewardIdStore


class TestRewardIdStore:

    # ----- RegistrationRewardId ----- #
    def test_RegistrationRewardId(self):
        reward_id_store = RewardIdStore()

        # Test default value
        assert reward_id_store.getRegistrationRewardId() == ""

        # Test Getter and Setter
        reward_id_store.setRegistrationRewardId("coucou_hibou")

        assert reward_id_store.getRegistrationRewardId() == "coucou_hibou"

    # ----- getResponseARewardId ----- #
    def test_ResponseARewardId(self):
        reward_id_store = RewardIdStore()

        # Test default value
        assert reward_id_store.getResponseARewardId() == ""

        # Test Getter and Setter
        reward_id_store.setResponseARewardId("coucou_hibou")

        assert reward_id_store.getResponseARewardId() == "coucou_hibou"

    # ----- getResponseBRewardId ----- #
    def test_ResponseBRewardId(self):
        reward_id_store = RewardIdStore()

        # Test default value
        assert reward_id_store.getResponseBRewardId() == ""

        # Test Getter and Setter
        reward_id_store.setResponseBRewardId("coucou_hibou")

        assert reward_id_store.getResponseBRewardId() == "coucou_hibou"

    # ----- getResponseARewardId ----- #
    def test_ResponseCRewardId(self):
        reward_id_store = RewardIdStore()

        # Test default value
        assert reward_id_store.getResponseCRewardId() == ""

        # Test Getter and Setter
        reward_id_store.setResponseCRewardId("coucou_hibou")

        assert reward_id_store.getResponseCRewardId() == "coucou_hibou"

    # ----- getResponseDRewardId ----- #
    def test_ResponseDRewardId(self):
        reward_id_store = RewardIdStore()

        # Test default value
        assert reward_id_store.getResponseDRewardId() == ""

        # Test Getter and Setter
        reward_id_store.setResponseDRewardId("coucou_hibou")

        assert reward_id_store.getResponseDRewardId() == "coucou_hibou"