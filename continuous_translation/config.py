import os

class ConfigurationError(Exception):
    pass

def load_config():
    config = {
        "GIT_REPO_URL": os.environ.get("GIT_REPO_URL", ""),
        "SOURCE_LANGUAGE": os.environ.get("SOURCE_LANGUAGE", "en"),
        "TARGET_LANGUAGE": os.environ.get("TARGET_LANGUAGE", "zh"),
        "API_KEY": os.environ.get("API_KEY", "")
    }

    missing_keys = [key for key, value in config.items() if not value]

    if missing_keys:
        raise ConfigurationError(f"Missing required environment variables: {', '.join(missing_keys)}")

    return config
