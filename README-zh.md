# OpenAI-Continuous-Translator

[![持续翻译测试](https://github.com/yunwei37/OpenAI-Continuous-Translator/actions/workflows/translation.yml/badge.svg)](https://github.com/yunwei37/OpenAI-Continuous-Translator/actions/workflows/translation.yml)
[![集成测试](https://github.com/yunwei37/OpenAI-Continuous-Translator/actions/workflows/integration.yml/badge.svg)](https://github.com/yunwei37/OpenAI-Continuous-Translator/actions/workflows/integration.yml)

OpenAI-Continuous-Translator 是一个开源项目，可以使用 OpenAI 的 API 在您的 `GitHub Action` 中实现多种格式和语言的持续翻译，包括代码注释。

## Github Action

您可以使用 Github Actions 翻译您的 repo：

1. 将以下内容添加到您的 github action：

  ```yml
      - uses: actions/checkout@v3
      - uses: yunwei37/OpenAI-Continuous-Translator@master
        with:
            git_repo_url: https://github.com/yourname/reponame
            api_key: ${{ secrets.OPENAI_API_KEY }}
      - name: Add & Commit
        uses: EndBug/add-and-commit@v9.1.1
  ```

2. 为 GitHub Actions 设置 secrets

要在 GitHub Actions 中使用 secrets，请按照以下步骤操作：

- 首先，创建一个 secret。在 GitHub 仓库页面上，转到“设置”选项卡。
- 在左侧导航栏中，单击“Secrets”。
- 单击“New repository secret”按钮。
- 输入密钥名称和相应的值，然后单击“Add secret”。添加一个密钥名称 `OPENAI_API_KEY`。

## 特点

- 翻译多种文件格式，包括 HTML、rst、txt 和 Markdown...

```

```

- 翻译多种语言的代码注释，包括 Python、Java 和 JavaScript...
- 自动检测 Git 仓库的更改
- 可配置的选项，如 Git 仓库 URL、源语言和目标语言以及 API 密钥
- 详细的日志记录以跟踪翻译进度和调试问题

## 什么是持续翻译？

只返回翻译后的内容，不包括原始文本。持续翻译是自动化翻译新内容的实践，使不同语言和文化之间的交流变得无缝。通过与Git等版本控制系统集成，持续翻译确保翻译始终与最新内容保持同步，减少了手动翻译所需的时间和精力。

## 入门指南

### 使用docker运行

```shell
docker run -e INPUT_GIT_REPO_URL="https://github.com/yourname/reponame" INPUT_API_KEY="your_api_key" -v /path/to/your/repo:/app yunwei37/openai-continuous-translator:latest
```

### 使用python运行

要使用OpenAI-Continuous-Translator，只需按照以下步骤操作：

1. 将此存储库克隆到本地计算机上
2. 在env中设置您的OpenAI API密钥和Git存储库URL
3. 使用`pip install -r requirements.txt`安装所需的依赖项
4. 使用`python main.py`运行程序

OpenAI-Continuous-Translator将自动检测您的Git存储库的更改，并将新内容翻译为您想要的语言。

## 贡献

我们欢迎任何人的贡献！要为OpenAI-Continuous-Translator做出贡献，只需fork此存储库，进行更改，然后提交拉取请求即可。

## 许可证

OpenAI-Continuous-Translator根据MIT许可证获得许可。有关更多信息，请参见`LICENSE`文件。