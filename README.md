# OpenAI-Continuous-Translator

[![Continuous Translation test](https://github.com/yunwei37/OpenAI-Continuous-Translator/actions/workflows/translation.yml/badge.svg)](https://github.com/yunwei37/OpenAI-Continuous-Translator/actions/workflows/translation.yml)
[![Integration Test](https://github.com/yunwei37/OpenAI-Continuous-Translator/actions/workflows/integration.yml/badge.svg)](https://github.com/yunwei37/OpenAI-Continuous-Translator/actions/workflows/integration.yml)

OpenAI-Continuous-Translator is an open-source project that enables continuous translation in multiple formats and languages, including code comments, using OpenAI's API in your `GitHub Action`.

## Github Action

You can translate your repo with Github Actions:

1. Add the following to your github action:

  ```yml
      - uses: actions/checkout@v3
      - uses: yunwei37/OpenAI-Continuous-Translator@master
        with:
            git_repo_url: https://github.com/yourname/reponame
            api_key: ${{ secrets.OPENAI_API_KEY }}
      - name: Add & Commit
        uses: EndBug/add-and-commit@v9.1.1
  ```

2. set the secrets for GitHub Actions

To use secrets in GitHub Actions, follow these steps:

- First, create a secret. on the GitHub repository page, go to the "Settings" tab.
- In the left-hand navigation bar, click on "Secrets".
- Click the "New repository secret" button.
- Enter a key name and the corresponding value, and click "Add secret". Add a secret name `OPENAI_API_KEY`.

## Features

- Translation of multiple file formats, including HTML, rst, txt, and Markdown...

```

```

- Translation of code comments in multiple languages, including Python, Java, and JavaScript...
- Automatic detection of changes to Git repositories
- Configurable options, such as Git repository URL, source and target languages, and API key
- Detailed logging to track translation progress and debug issues

## What is Continuous Translation?

Continuous translation is the practice of automating the translation of new content as it is created, allowing for seamless communication across different languages and cultures. By integrating with version control systems like Git, continuous translation ensures that translations are always up-to-date with the latest content, reducing the time and effort required for manual translation.

## Getting Started

### Run with docker

```shell
docker run -e INPUT_GIT_REPO_URL="https://github.com/yourname/reponame" INPUT_API_KEY="your_api_key" -v /path/to/your/repo:/app yunwei37/openai-continuous-translator:latest
```

### Run with python

To use OpenAI-Continuous-Translator, simply follow these steps:

1. Clone this repository to your local machine
2. Set up your OpenAI API key and Git repository URL in the env
3. Install the required dependencies using `pip install -r requirements.txt`
4. Run the program using `python main.py`

OpenAI-Continuous-Translator will automatically detect changes to your Git repository and translate the new content into your desired language.

## Contributing

We welcome contributions from anyone! To contribute to OpenAI-Continuous-Translator, simply fork this repository, make your changes, and submit a pull request.

## License

OpenAI-Continuous-Translator is licensed under the MIT License. See the `LICENSE` file for more information.
