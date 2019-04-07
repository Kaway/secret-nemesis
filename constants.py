RESPONSE_RPL_WELCOME = '001'
RESPONSE_RPL_YOUR_HOST = '002'
RESPONSE_RPL_CREATED = '003'
RESPONSE_RPL_MYINFO = '004'
RESPONSE_RPL_BOUNCE = '005'
RESPONSE_RPL_U_MODE_IS = '221'
RESPONSE_RPL_L_USER_CLIENT = '251'
RESPONSE_RPL_L_USER_OP = '252'
RESPONSE_RPL_L_USER_UNKNOWN = '253'
RESPONSE_RPL_L_USER_CHANNELS = '254'
RESPONSE_RPL_L_USER_ME = '255'
RESPONSE_RPL_TOPIC = '332'
RESPONSE_RPL_TOPIC_WHO_TIME = '333'
RESPONSE_RPL_NAM_REPLY = '353'
RESPONSE_RPL_END_OF_NAMES = '366'
RESPONSE_RPL_MOTD = '372'
RESPONSE_RPL_MOTD_START = '375'
RESPONSE_RPL_END_OF_MOTD = '376'

PRIVMSG = 'PRIVMSG'

PING = 'PING'
PONG = 'PONG'

SRV_CMD_JOIN = 'JOIN'
SRV_CMD_NAMES = 'NAMES'
SRV_CMD_NICK = 'NICK'
SRV_CMD_USER = 'USER'

MESSAGES_TO_IGNORE = [RESPONSE_RPL_WELCOME, RESPONSE_RPL_YOUR_HOST, RESPONSE_RPL_CREATED, RESPONSE_RPL_MYINFO,
                      RESPONSE_RPL_BOUNCE, RESPONSE_RPL_U_MODE_IS, RESPONSE_RPL_L_USER_CLIENT, RESPONSE_RPL_L_USER_OP,
                      RESPONSE_RPL_L_USER_UNKNOWN, RESPONSE_RPL_L_USER_CHANNELS, RESPONSE_RPL_L_USER_ME, RESPONSE_RPL_TOPIC,
                      RESPONSE_RPL_END_OF_NAMES, RESPONSE_RPL_MOTD, RESPONSE_RPL_MOTD_START, RESPONSE_RPL_END_OF_MOTD,
                      SRV_CMD_JOIN]