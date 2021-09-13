# from .settings import *

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = []

# EMAIL_BACKEND = 'django.core.mail.backends.comsole.EmailBackend'

# #ロギング設定
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers':False,

#     #ロガーの設定
#     'loggers':{
#         #Django が利用するロガー
#         'django':{
#             'handlers':['console'],
#             'level': 'INFO',
#         },
#         #diaryアプリケーションが利用するロガー
#         'diary': {
#             'handlers':['console'],
#             'level':'DEBUG',
#         },
#     },

#     'handlers': {
#         'console':{
#             'level':'DEBUG',
#             'class': 'logging.StereamHandler',
#             'formatter': 'dev'
#         },
#     },

#     #ハンドラの設定
#     'handlers': {
#         'console': {
#         'level': 'DEBUG',
#         'class': 'logging.StreamHandler',
#         'formatter': 'dev'
#     },
#    },
#     #フォーマッタの設定
#     'formatters':{
#         'dev': {
#             'format': '\t'.join([
#                 '%(asctime)s',
#                 '[%(levelname)s]',
#                 '%(pathname)s(Line:%(lineo)',
#                 '%(message)s'
#             ])
#         },
#     }
# }


    