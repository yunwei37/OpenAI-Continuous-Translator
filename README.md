# OpenAI-Continuous-Translator

OpenAI-Continuous-Translator is an open-source project that enables continuous translation in multiple formats and languages, including code comments, using OpenAI's API.

## What is Continuous Translation?

Continuous translation is the practice of automating the translation of new content as it is created, allowing for seamless communication across different languages and cultures. By integrating with version control systems like Git, continuous translation ensures that translations are always up-to-date with the latest content, reducing the time and effort required for manual translation.

## Features

- Continuous translation across multiple formats and languages
- Automatic detection of changes to Git repositories
- Translation of code comments
- Configurable options, such as Git repository URL, source and target languages, and API key
- Detailed logging to track translation progress and debug issues

## Getting Started

To use OpenAI-Continuous-Translator, simply follow these steps:

1. Clone this repository to your local machine
2. Set up your OpenAI API key and Git repository URL in the `config.py` file
3. Install the required dependencies using `pip install -r requirements.txt`
4. Run the program using `python src/main.py`

OpenAI-Continuous-Translator will automatically detect changes to your Git repository and translate the new content into your desired language.

## Contributing

We welcome contributions from anyone! To contribute to OpenAI-Continuous-Translator, simply fork this repository, make your changes, and submit a pull request.

## License

OpenAI-Continuous-Translator is licensed under the MIT License. See the `LICENSE` file for more information.
