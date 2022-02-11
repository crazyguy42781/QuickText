import json
import os

import twilio.base.exceptions
from twilio.rest import Client

class ContactList(list):
    pass


class Contact:
    contact_list = ContactList()

    account_sid = ""
    auth_token = ""
    try:
        client = Client(account_sid, auth_token)
    except twilio.base.exceptions.TwilioException:
        print("input creds")

    def __init__(self, contact_info, append=True):
        self._info: dict = contact_info
        if append:
            self.contact_list.append(self)

    def __repr__(self):
        return f"{self._info}"

    @property
    def info(self) -> dict:
        return self._info

    @info.setter
    def info(self, value: dict):
        self._name = value

    def text_contact(self, body):
        # todo add max number
        try:
            print(f"f: +19513836718\nt: {self.info['phone']}\nb: {body}")
        except KeyError:
            raise KeyError("No phone in spreadsheet\nPlease ensure phone column is named 'phone'")
        # message = self.client.messages.create(
        #     body='Hi there',
        #     from_='+19513836718',
        #     to=f"+1{self._phone}"
        # )

    def list(self) -> ContactList:
        return self.contact_list

class UserSettings:
    def __init__(self):
        self._settings = {
            "csvLocation": None,
            "csvLastModDate": None
        }
        self._twilio_account_sid = None
        self._twilio_auth_token = None

    def __setitem__(self, key, value):
        self._settings[key] = value

    def __getitem__(self, key):
        return self.settings[key]

    @property
    def settings(self):
        return self._settings

    @settings.setter
    def settings(self, value):
        self._settings = value

    def save(self):
        with open('settings.json', 'w', encoding='utf-8') as file:
            json.dump(self._settings, file)

    def load_twilio_env_variables(self):
        self._twilio_account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        self._twilio_auth_tocken = os.environ["TWILIO_AUTH_TOKEN"]

    def load_all(self):
        with open('settings.json', 'r', encoding='utf-8') as file:
            try:
                contents = json.loads(file.read())
                self._settings = contents
                return contents
            except json.decoder.JSONDecodeError:
                print("No json obj: in class user - temp fix")
        self.load_twilio_env_variables()

    @property
    def twilio_account_sid(self):
        return self._twilio_account_sid

    @twilio_account_sid.setter
    def twilio_account_sid(self, value):
        EMPTY = ""
        if value is None or value is EMPTY:
            raise ValueError("Nonetype cannot be set")
        self._twilio_account_sid = value

    @property
    def twilio_auth_token(self):
        return self._twilio_auth_token

    @twilio_auth_token.setter
    def twilio_auth_token(self, value):
        EMPTY = ""
        if value is None or value is EMPTY:
            raise ValueError("Nonetype cannot be set")
        self._twilio_auth_token = value


