import os
from pathlib import Path

from aws_secrets_loader import __version__
from aws_secrets_loader.clients import AwsSecretsManagerBotoClient
from aws_secrets_loader.loaders import load_secrets_from_json_config

# Example names of secrets in AWS Secrets Manager and values that could be stored in those secrets
DATABASE_SECRET_NAME = "/us/aws_secrets_loader/nonprod/database"
DATABASE_USER_VALUE = "my_user"
DATABASE_PASSWORD_VALUE = "Password1234"

API_SECRET_NAME = "/us/aws_secrets_loader/nonprod/api"
API_KEY_VALUE = "my_api_key"
API_SECRET_VALUE = "it's a secret to everybody"


def test_version():
    assert __version__ == "0.1.0"


def test_it_loads_json_config_into_the_environment(monkeypatch, mocker):
    # Set environment variables needed to process the example_config.json
    monkeypatch.setenv("DATABASE_SECRET_NAME", DATABASE_SECRET_NAME)
    monkeypatch.setenv("API_SECRET_NAME", API_SECRET_NAME)

    mocker.patch.object(AwsSecretsManagerBotoClient, "get_secret", mock_get_secret)

    config_path = Path(__file__).parent.joinpath("example_config.json")

    load_secrets_from_json_config(config_path)

    assert os.environ["DATABASE_USER"] == DATABASE_USER_VALUE
    assert os.environ["DATABASE_PASSWORD"] == DATABASE_PASSWORD_VALUE
    assert os.environ["API_KEY"] == API_KEY_VALUE
    assert os.environ["API_SECRET"] == API_SECRET_VALUE


def mock_get_secret(secret_name):
    if secret_name == DATABASE_SECRET_NAME:
        return {
            "USER": DATABASE_USER_VALUE,
            "PASSWORD": DATABASE_PASSWORD_VALUE,
        }
    elif secret_name == API_SECRET_NAME:
        return {
            "KEY": API_KEY_VALUE,
            "SECRET": API_SECRET_VALUE,
        }
