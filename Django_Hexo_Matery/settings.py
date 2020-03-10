import os
import sys

# 基础目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = '_=po3tapr+1rd)bdvu#_!mg4z3%%g^xm4puyb1-!gxlxom7ke8'

DEBUG = False

ALLOWED_HOSTS = ['*']

# APP注册相关
INSTALLED_APPS = [
    'simpleui',
    'import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'mdeditor',
    'pure_pagination',
]

# 中间件相关
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Django_Hexo_Matery.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'blog.views.global_setting',
            ],
        },
    },
]

WSGI_APPLICATION = 'Django_Hexo_Matery.wsgi.application'

# 数据库配置
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django-blog',
        'USER': 'root',
        'PASSWORD': 'P@ssw0rd',
        'HOST': '127.0.0.1'
    }
}

# 密码认证相关
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 语言时区
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# 日志记录
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' :"[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' :"%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'mysite.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'blog': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}

# 静态文件配置
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [(os.path.join(BASE_DIR, 'static'))]

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/media/'

# 网站的基本信息配置
SITE_NAME = '国光'  # 站点名称
SITE_DESCRIPTION = '国光'  # 站点描述
SITE_KEYWORDS = '国光,信息安全,Web安全,极客'  # 站点关键词
SITE_TITLE = '信息安全学习记录'  # 博客标题
SITE_TYPE_CHINESE = '宁静致远'  # 打字效果 中文内容
SITE_TYPE_ENGLISH = 'The quieter you become, the more you are able to hear'  # 打字效果 英文内容
SITE_MAIL = 'admin@sqlsec.com'  # 我的邮箱
SITE_ICP = '苏ICP备19074591号'  # 网站备案号
SITE_ICP_URL = 'http://beian.miit.gov.cn'  # 备案号超链接地址

# Simple Ui 相关设置
SIMPLEUI_LOGIN_PARTICLES = False
SIMPLEUI_ANALYSIS = False
SIMPLEUI_STATIC_OFFLINE = True
SIMPLEUI_LOADING = False
SIMPLEUI_LOGO = 'https://image.3001.net/images/20191031/15724874583730.png'

# 后台MarkDown编辑器配置
X_FRAME_OPTIONS = 'SAMEORIGIN'