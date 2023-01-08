def infer_breach(value, lower_limit, upper_limit):
    if value < lower_limit:
        return 'TOO_LOW'
    if value > upper_limit:
        return 'TOO_HIGH'
    return 'NORMAL'

limits = {
    'PASSIVE_COOLING': (0, 35),
    'HI_ACTIVE_COOLING': (0, 45),
    'MED_ACTIVE_COOLING': (0, 40),
}

def check_and_alert(alert_target, battery_char, temperature_in_c):
    lower_limit, upper_limit = limits[battery_char['coolingType']]
    breach_type = infer_breach(temperature_in_c, lower_limit, upper_limit)
    if alert_target == 'TO_CONTROLLER':
        send_to_controller(breach_type)
    elif alert_target == 'TO_EMAIL':
        send_to_email(breach_type)
		
def send_to_controller(breach_type):
    header = 0xfeed
    print(f'{header}, {breach_type}')

def send_to_email(breach_type):
    recepient = "a.b@c.com"
    if breach_type == 'TOO_LOW':
        print(f'To: {recepient}')
        print('Hi, the temperature is too low')
    elif breach_type == 'TOO_HIGH':
        print(f'To: {recepient}')
        print('Hi, the temperature is too high')
