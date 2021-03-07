class RewardIdStore:
    """
    RewardIdStore
    -------------

    Store
    """

    def __init__(self):
        self.registrationRewardId = ""

    def getRegistrationRewardId(self):
        return self.registrationRewardId

    def setRegistrationRewardId(self, new_registration_reward_id):
        self.registrationRewardId = new_registration_reward_id


reward_id_store = RewardIdStore()
