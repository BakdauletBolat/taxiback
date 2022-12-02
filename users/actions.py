from users.smsc_api import SMSC


class SendSmsAction:

    @staticmethod
    def run(phone_number, code):
        smsc = SMSC()
        balance = smsc.get_balance()
        print(balance)
        r = smsc.send_sms("87059943864", f"Код для входа в аккаунт: {code}")
        print(r)
