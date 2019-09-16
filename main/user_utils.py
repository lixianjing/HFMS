import hashlib
import random
import time
import base64
import hmac

from passport.models import User

user_id = -1

def get_id():
    global user_id
    if user_id == -1:
        users = User.objects.order_by("-id")[0:1]
        if users:
            user_id = users[0].id
    user_id += 1
    return user_id
