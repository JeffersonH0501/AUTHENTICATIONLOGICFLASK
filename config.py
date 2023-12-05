class Config:
    DEBUG = True
    ALLOWED_HOSTS = ['*']

    SQLALCHEMY_DATABASE_URI = 'postgresql://admin_user:isis2503@10.115.48.18/users_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'svm_)tpa-o^gkn@81sel&lapq2jc7^^-n9c+4y&f9rymz$kum_'
    SIMETRIC_KEY = 'SebastianRamirezLeMeteMuyDuroAArquisoftQ_LM='