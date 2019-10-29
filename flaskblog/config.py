import os


class Config:
    # in command line import secrets, then secrets.token_hex(any number)
    SECRET_KEY = '68742e354d70093e963bd2f800a80061'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # app.config['MAIL_USERNAME'] = os.environ.get('EMAIL')
    # app.config['MAIL_PASSWORD'] = os.environ.get('PASSWORD')
    MAIL_USERNAME = 'a7mtoo133@gmail.com '
    MAIL_PASSWORD = 'aftershake13?aftershake13?'