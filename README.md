# AWS Secrets Loader
![Build & CI Checker](https://github.com/rewards-lifecycle/aws-secrets-loader/workflows/Build%20&%20CI%20Checker/badge.svg)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

```
╔═╗╦ ╦╔═╗
╠═╣║║║╚═╗
╩ ╩╚╩╝╚═╝
  ╔═╗┌─┐┌─┐┬─┐┌─┐┌┬┐┌─┐
  ╚═╗├┤ │  ├┬┘├┤  │ └─┐
  ╚═╝└─┘└─┘┴└─└─┘ ┴ └─┘
   ╦  ┌─┐┌─┐┌┬┐┌─┐┬─┐
   ║  │ │├─┤ ││├┤ ├┬┘
   ╩═╝└─┘┴ ┴─┴┘└─┘┴└─
```
## Requirements
1) The package manager being used must be configured to use our internal repository.
2) Secrets are stored in the JSON format (key -> value pairs).
1) Machine where application is running must have an AWS profile configured.
3) Machine where the application is running must have access to the requested secrets.

## Installation
https://confluence.corp.ebates.com/display/GUILDS/Internal+PyPI#InternalPyPI-InstallingPackages

## Usage
```
from pathlib import Path

from aws_secrets_loader.loaders import load_secrets_from_json_config

# This uses a file "secrets_config.json" one directory up from the current file's path
BASE_DIR = Path(__file__).resolve().parent.parent
secrets_config_path = BASE_DIR.joinpath("secrets_config.json")

load_aws_secrets_from_json_config(secrets_config_path)
```

In order to load secrets using the secrets loader you must pass in the path of the secrets_config.json file. See
tests/example_config.json for an example of the JSON format.

**ENV_VAR_FOR_AWS_SECRET_NAME**: This is the name of the Environment variable that correlates with the full secret name. This allows you to use environment based secrets (non-prod/prod)

**SECRET_KEYS**: These are the keys of the secret values you would like to load

**PREFIX_FOR_ENV_VAR_NAME**: This is the prefix that will be used when generating the new environment variable name.

The example above would result in two new environment variables being set:
1) 'DB_USER' would be loaded with the value stored on the 'USER' key of the secret
2) 'DB_PASSWORD' would be loaded with the value stored on the 'PASSWORD' key of the secret

# Development
### Pre-commit
A script runner before you commit changes, this will save many red alerts happening over a CI and can warn you on problems you skipped.

As an example We:
* Don't let developers commit directly on master,staging or QA branches.
* Search for ipdb/pdb debug statements in code
* Detect if there is a private key saved in the code base
* If there are merge conflicts not resolved

And many more checks!

#### Installation

```
pre-commit install
pre-commit install-hooks
```

#### upgrade

```
pre-commit autoupdate
```
