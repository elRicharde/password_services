# Passwort Service Klasse
# Richarde - Januar 2022

import uuid
import hashlib
import getpass
import time
from os import system

# https://stackoverflow.com/questions/62514742/how-to-store-hashed-passwords-on-sqlite3-database


class Password_service:

    def __init__(self):
        pass # nothing to do so far

    def hash_password(self, password):

        # uuid is used to generate a random number
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode("utf-8")).hexdigest() + ':' + salt

    def check_password(self, hashed_password, user_password):
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode("utf-8")).hexdigest()        # True / False

    def get_new_password(self):
        first = "first"
        second = "kontrolle"
        msg = "nix"
        
        print("Psswort eingeben - Achtung, aus Sicherheitsgründen gibt es kein Cursor")
                
        while first != second:
            system('cls')       # clear screen
            
            if msg != "nix":
                print(msg)
            first = getpass.getpass(prompt="Password: ", stream=None)
            second = getpass.getpass(prompt="Password wiederholen: ", stream=None)
            msg = "Eingabe nicht identisch, bitte neu Beginnen"
        
        return self.__hash_password(first)    # return hashed pw

    def authorize(self, hashed_password):
        wait = 2
        try:
            print("Anmelden abbrechen mit 'Ctrl + C'")
            print("aus Sicherheitsgründen gibt es kein Cursor")
            while self.check_password(hashed_password, getpass.getpass(prompt="Password: ", stream=None) ) == False:
                wait = wait * 2
                for sec in range(wait, 0, -1):
                    system('cls')       # clear screen
                    print("Passwort falsch, neuer Versuch in ", str(sec), " Sekunden")
                    time.sleep(1)
                system('cls')       # clear screen
                print("Anmelden abbrechen mit 'Ctrl + C'")
                print("aus Sicherheitsgründen gibt es kein Cursor")
                    
        except KeyboardInterrupt:
            return False    # nicht Authorisiert

        return True # Authorisiert

