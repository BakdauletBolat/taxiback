from apps.users.smsc_api import SMSC


class SendSmsAction:

    @staticmethod
    def run(phone_number, code):
        smsc = SMSC()
        balance = smsc.get_balance()
        r = smsc.send_sms(phone_number, f"Код для входа в аккаунт: {code}")
        print(r)
