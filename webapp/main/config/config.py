class Config(object):
    """
    Base configs
    """


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
