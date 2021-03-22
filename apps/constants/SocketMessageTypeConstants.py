# ----- REQUESTS
SOCKET_REQUEST_QUIZ_INIT = "request:quiz:init"
SOCKET_REQUEST_START_QUIZ = "request:quiz:start"

# ----- EVENTS
# Notification
SOCKET_EVENT_NOTIFICATION_MESSAGE = "event:notification:send"
# Stats
SOCKET_EVENT_STATS_CONSTESTANTS_CHECK_IN = "event:stats:contestants_check_in"
SOCKET_EVENT_STATS_ANSWERS_ONGOING = "event:stats:answers_ongoing"
SOCKET_EVENT_STATS_ANSWERS_QUESTION = "event:stats:answers_question"
# Ranking
SOCKET_EVENT_RANKING = "event:ranking:send"
# Quiz
SOCKET_EVENT_REVEAL_ANSWER = "event:quiz:reveal_answer"
SOCKET_EVENT_QUIZ_NEXT_QUESTION = "event:quiz:next_question"
SOCKET_EVENT_QUIZ_STOP = "event:quiz:stop"
SOCKET_EVENT_QUIZ_STOP_NO_WINNER = "event:quiz:stop_no_winner"
SOCKET_EVENT_QUIZ_STOP_WINNER = "event:quiz:stop_winner"
SOCKET_EVENT_QUIZ_STOP_NO_QUESTIONS = "event:quiz:stop_no_questions"
SOCKET_EVENT_QUIZ_CONTINUE = "event:quiz:continue"
