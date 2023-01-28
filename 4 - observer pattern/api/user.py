from lib.email import send_email # (remove)
from lib.db import create_user, find_user
from lib.log import log # (remove)
from lib.slack import post_slack_message # (remove)
from lib.stringtools import get_random_string

# add the post event listener.

def register_new_user(name: str, password: str, email: str):
    # create an entry in the database
    user = create_user(name, password, email)
    
    # post a Slack message to sales department (replaced with event call)
    post_slack_message("sales",
        f"{user.name} has registered with email address {user.email}. Please spam this person incessantly.")

    # send a welcome email (replaced with event call)
    send_email(user.name, user.email,
        "Welcome",
        f"Thanks for registering, {user.name}!\nRegards, The DevNotes team")

    # write server log (replaced with event call)
    log(f"User registered with email address {user.email}")

def password_forgotten(email: str):
    # retrieve the user
    user = find_user(email)

    # generate a password reset code
    user.reset_code = get_random_string(16)

    # send a password reset message (replaced with event call)
    send_email(user.name, user.email, "Reset your password",
        f"To reset your password, use this very secure code: {user.reset_code}.\nRegards, The DevNotes team")

    # write server log (replaced with event call)
    log(f"User with email address {user.email} requested a password reset")
