class RewardIdStore:
    """
    RewardIdStore
    -------------

    Store
    """

    def __init__(self):
        self.registrationRewardId = ""
        self.responseARewardId = ""
        self.responseBRewardId = ""
        self.responseCRewardId = ""
        self.responseDRewardId = ""

    # ----- Registration rewards ----- #
    def getRegistrationRewardId(self):
        return self.registrationRewardId

    def setRegistrationRewardId(self, new_registration_reward_id):
        self.registrationRewardId = new_registration_reward_id

    # ----- Response rewards ----- #
    # -- A
    def getResponseARewardId(self):
        return self.responseARewardId

    def setResponseARewardId(self, new_response_award_id):
        self.responseARewardId = new_response_award_id

    # -- B
    def getResponseBRewardId(self):
        return self.responseBRewardId

    def setResponseBRewardId(self, new_response_award_id):
        self.responseBRewardId = new_response_award_id

    # -- C
    def getResponseCRewardId(self):
        return self.responseCRewardId

    def setResponseCRewardId(self, new_response_award_id):
        self.responseCRewardId = new_response_award_id

    # -- D
    def getResponseDRewardId(self):
        return self.responseDRewardId

    def setResponseDRewardId(self, new_response_award_id):
        self.responseDRewardId = new_response_award_id


reward_id_store = RewardIdStore()
