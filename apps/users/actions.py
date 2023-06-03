from apps.users.smsc_api import SMSC
import hashlib
import requests
from .models import User, Payment
import xml.etree.ElementTree as ET
import os

class SendSmsAction:

    @staticmethod
    def run(phone_number, code):
        smsc = SMSC()
        balance = smsc.get_balance()
        r = smsc.send_sms(phone_number, f"Код для входа в аккаунт: {code}")


class FreedomPay:

    def __init__(self) -> None:
        self.merchant_id = '544010'
        self.secret_key = os.getenv('SECRET_KEY_FREEDOM_PAY', 'HbotreoJWjDyuWGB')
        self.data = {}
        self.call_back_url = os.getenv('SITE_URL','https://1226-176-119-229-155.ngrok-free.app')
        self.result_url = self.call_back_url+'/api/users/payment/result/'

    def prepare_data(self, user:User, payment: Payment) -> None:
        self.data = {
            'pg_order_id': payment.gen_id,
            'pg_merchant_id': self.merchant_id,
            'pg_amount': payment.coin,
            'pg_description': 'Покупка бонусов',
            'pg_salt': f'random_text_{payment.gen_id}',
            'pg_testing_mode': 1,
            'pg_result_url': self.result_url,
            'pg_user_phone': user.phone
        }
        if user.user_info and user.user_info.email: # type: ignore
            self.data['pg_user_email'] = user.user_info.email # type: ignore

    def generate_message(self, data:dict):
        message = 'init_payment.php;'
        new_data = dict(sorted(data.items(), key=lambda x: x[0]))
        for value in new_data.values():
            message += f'{value};'
        return message+self.secret_key
    
    def calculate_md5_hash(self):
        message = self.generate_message(self.data)
        md5_hash = hashlib.md5()
        md5_hash.update(message.encode('utf-8'))
        return md5_hash.hexdigest()
    
    def create_payment(self) -> str:
        md5_hash = self.calculate_md5_hash()
        self.data['pg_sig'] = md5_hash
        res = requests.post('https://api.freedompay.money/init_payment.php', data=self.data)
        tree = ET.fromstring(res.text)
        pg_redirect_url = tree.find('pg_redirect_url')
        return pg_redirect_url.text # type: ignore
    

