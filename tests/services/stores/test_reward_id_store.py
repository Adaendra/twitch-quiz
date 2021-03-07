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
