from .core import fetch_data, config_data


DISCORD_API_URL = "https://discord.com/api/v9/"
data = config_data()
int_data = fetch_data()
SeparateStart = data['data']['start_each']
SeparateStop = data['data']['stop_each']
SeparateDm = data['data']['dm_uwu']
apikey = data['data']['captcha_key']  # captcha api key
SolvedCommandsMiningChannelID = data['data']['unci']
solvers = data['data']['server_role_id']  # captcha solvers role id
SolverChannelAndLogs = data['data']['log_channel_id']
SolverChannel = data['data']['mcsci']
first_time_interval = data['data']['start_delay']
second_time_interval = data['data']['end_delay']
OwnerCmd = data['data']['invoke_cmd']
StartCmd = data['data']['startoxyminers']
StopCmd = data['data']['stopoxyminers']
owoid = int_data['data']['owoid']
time_to_sleep_before_response = int_data['data']['time_to_sleep_before_response']
OwoPrefix = int_data['data']['owo_prefix']
DM_captcha_text = int_data['captcha_text']['DM_captcha_text']
Verification_link_captcha = int_data['captcha_text']['Verification_link_captcha']
DM_warning1 = int_data['captcha_text']['DM_warning1']
DM_warning2 = int_data['captcha_text']['DM_warning2']
DM_warning3 = int_data['captcha_text']['DM_warning3']
verified_text = int_data['captcha_text']['verified_text']
guild_captcha_text = int_data['captcha_text']['guild_captcha_text']
