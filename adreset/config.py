# SPDX-License-Identifier: GPL-3.0+

from __future__ import unicode_literals

import os.path

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))


class Config(object):
    """The base ADReset application configuration."""

    DEBUG = True
    # We configure logging explicitly, turn off the Flask-supplied log handler
    LOGGER_HANDLER_POLICY = 'never'
    HOST = '0.0.0.0'
    PRODUCTION = False
    TESTING = False
    SHOW_DB_URI = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'replace-me-with-something-random'
    JWT_SECRET_KEY = 'replace-me-with-something-random'
    CORS_URL = '*'
    AD_USE_NTLM = True


class ProdConfig(Config):
    """The production ADReset application configuration."""

    DEBUG = False
    PRODUCTION = True


class DevConfig(Config):
    """The development ADReset application configuration."""

    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(os.path.join(base_dir, 'adreset.db'))
    JSONIFY_PRETTYPRINT_REGULAR = True


class TestConfig(Config):
    """The test ADReset application configuration."""

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
    # ldap3 mocking doesn't support NTLM
    AD_USE_NTLM = False
    AD_DOMAIN = 'adreset.local'
    AD_LDAP_URI = 'ldaps://server.domain.local:636'
