from apps.services.stores.RewardIdStore import reward_id_store


class TestRewardIdStore:

    # ----- RegistrationRewardId ----- #
    def test_RegistrationRewardId(self):
        # Test default value
        assert reward_id_store.getRegistrationRewardId() == ""

        # Test Getter and Setter
        reward_id_store.setRegistrationRewardId("coucou_hibou")

        assert reward_id_store.getRegistrationRewardId() == "coucou_hibou"
