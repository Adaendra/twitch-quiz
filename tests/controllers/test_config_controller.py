from apps.controllers.ConfigController import configController


class TestConfigController:

    # ----- isAllRequiredConfigDefined ----- #
    def test_isAllRequiredConfigDefined_ok(self, mocker):
        mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getClientId',
            return_value="client_id"
        )
        mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getClientSecret',
            return_value="client_secret"
        )
        mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getRewardCost',
            return_value=5000
        )

        assert configController.isAllRequiredConfigDefined() is True

    def test_isAllRequiredConfigDefined_nok_clientId(self, mocker):
        mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getClientId',
            return_value=""
        )
        mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getClientSecret',
            return_value="client_secret"
        )
        mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getRewardCost',
            return_value=5000
        )

        assert configController.isAllRequiredConfigDefined() is False

    def test_isAllRequiredConfigDefined_nok_clientSecret(self, mocker):
        mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getClientId',
            return_value="client_id"
        )
        mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getClientSecret',
            return_value=""
        )
        mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getRewardCost',
            return_value=5000
        )

        assert configController.isAllRequiredConfigDefined() is False

    def test_isAllRequiredConfigDefined_nok_rewardCost(self, mocker):
        mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getClientId',
            return_value="client_id"
        )
        mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getClientSecret',
            return_value="client_secret"
        )
        mocker.patch(
            'apps.controllers.ConfigController.user_config_store.getRewardCost',
            return_value=0
        )

        assert configController.isAllRequiredConfigDefined() is False
