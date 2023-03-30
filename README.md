# 🌎 OpenAI-Continuous-Translator

[![Continuous Translation test](https://github.com/yunwei37/OpenAI-Continuous-Translator/actions/workflows/translation.yml/badge.svg)](https://github.com/yunwei37/OpenAI-Continuous-Translator/actions/workflows/translation.yml)
[![Integration Test](https://github.com/yunwei37/OpenAI-Continuous-Translator/actions/workflows/integration.yml/badge.svg)](https://github.com/yunwei37/OpenAI-Continuous-Translator/actions/workflows/integration.yml)

OpenAI-Continuous-Translator is an open-source project that enables continuous translation (Or internationalization, i18n) in multiple formats and languages, including code comments, using OpenAI's `ChatGPT/GPT4` API in your `GitHub Action`.

Support file format:

- Markdown
- rst
- txt
- HTML
- jupyter notebook
- cpp/c/python/js (code comments)
- others are comming soon...

## 🔧 Setup the github action

### Repository Settings

#### 1. Settings > Actions > General

- Enable `Read and write permissions`
- Enable `Allow GitHub Actions to create and approve pull requests`
![permissions](https://user-images.githubusercontent.com/69892552/228692074-d8d009a8-9272-4023-97b1-3cbc637d5d84.jpg)

#### 2. Settings > Secrets and variables > Actions

- Set API key(`OPENAI_API_KEY`) to secrets
![secrets](https://user-images.githubusercontent.com/69892552/228692421-22d7db33-4e32-4f28-b166-45b4d3ce2b11.jpg)

### GitHub Actions Workflow Settings

#### Required

- Provide the OPENAI_API_KEY as apiKey.
- Set `on` to trigger when a comment is created (`types: [ created ]`).
- Checkout in advance(`actions/checkout@v3`).

You can translate your repo with Github Actions:

1. Add the following to your github action:

  ```yml
      - uses: actions/checkout@v3
      - uses: yunwei37/OpenAI-Continuous-Translator@master
        with:
            git_repo_url: https://github.com/yourname/reponame
            api_key: ${{ secrets.OPENAI_API_KEY }}
  ```

  The `git_repo_url` does not always need to be the current repo. You can either make a mirror repo from the original one, or you internationalize the original repo.

You can add and commit the result:

```yml
      - name: Add & Commit
        uses: EndBug/add-and-commit@v9.1.1
```

And use [create-pull-request](https://github.com/peter-evans/create-pull-request) to create a PR for your repo:
```yml
    - name: Create Pull Request
      uses: peter-evans/create-pull-request@v4
```

### Example

Here is a complete example:

```yml
name: Continuous Translation

on:
  workflow_dispatch:
  schedule:
    - cron: '0 0 * * 1' # At 00:00 on Monday

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - uses: yunwei37/OpenAI-Continuous-Translator@master
      with:
          git_repo_url: https://github.com/radi-cho/awesome-gpt4
          api_key: ${{ secrets.OPENAI_API_KEY }}
    - name: Add & Commit
      uses: EndBug/add-and-commit@v9.1.1
    - name: Create Pull Request
      uses: peter-evans/create-pull-request@v4
```

The translated repo example maybe:

- https://github.com/yunwei37/Prompt-Engineering-Guide-zh-CN
- https://github.com/yunwei37/awesome-gpt4-zh-CN

The complete workflow is roughly as follows:

1. Spend two minutes configuring the corresponding API key and desired settings in the CI, as well as GitHub permissions.
2. GitHub Actions can periodically check the upstream repository for new changes, and if there are any, it will pull down the corresponding change and translate it.
3. The action will automatically submit the translated changes as a pull request in the current repository, which will be reviewed and proofread by humans before being merged.

## Features

For the translation result of GPT, please refer to [Is-ChatGPT-A-Good-Translator](https://github.com/wxjiao/Is-ChatGPT-A-Good-Translator).

- Translation of multiple file formats, including HTML, rst, txt, and Markdown...

  For example, a Markdown file:

  ```markdown
  - **提示工程技术**:
  - [一个提示模式目录，增强 ChatGPT 的提示工程](https://arxiv.org/abs/2302.11382) [2023] (Arxiv)
  - [让硬提示容易：基于梯度的离散优化方法来进行提示调整和发现](https://arxiv.org/abs/2302.03668) [2023] (Arxiv)。- [合成提示：为大型语言模型生成思路演示](https://arxiv.org/abs/2302.00618) [2023] (Arxiv)
  - [渐进提示：用于语言模型的连续学习](https://arxiv.org/abs/2301.12314) [2023] (Arxiv)
  - [批量提示：使用 LLM API 进行高效推理](https://arxiv.org/abs/2301.08721) [2023] (Arxiv)
  - [连续提示用于解答复杂问题](https://arxiv.org/abs/2212.04092) [2022] (Arxiv)
  - [结构化提示：将上下文学习扩展到 1,000 个示例](https://arxiv.org/abs/2212.06713) [2022] (Arxiv)
  - [大型语言模型是人类级的提示工程师](https://arxiv.org/abs/2211.01910) [2022] (Arxiv)
  - [问我：一个为提示语言模型设计的简单策略](https://paperswithcode.com/paper/ask-me-anything-a-simple-strategy-for) [2022] (Arxiv)
  - [提示 GPT-3 成为可靠的模型](https://arxiv.org/abs/2210.09150) [2022](Arxiv)
  - [分解提示：一种解决复杂任务的模块化方法](https://arxiv.org/abs/2210.02406) [2022] (Arxiv)
  ```

  is translated from English to Chinese:

  ```markdown
  - **Prompt Engineering Techniques**:
  - [A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT](https://arxiv.org/abs/2302.11382) [2023] (Arxiv)
  - [Hard Prompts Made Easy: Gradient-Based Discrete Optimization for Prompt Tuning and Discovery](https://arxiv.org/abs/2302.03668) [2023] (Arxiv)
  - [Synthetic Prompting: Generating Chain-of-Thought Demonstrations for Large Language Models](https://arxiv.org/abs/2302.00618) [2023] (Arxiv) 
  - [Progressive Prompts: Continual Learning for Language Models](https://arxiv.org/abs/2301.12314) [2023] (Arxiv) 
  - [Batch Prompting: Efficient Inference with LLM APIs](https://arxiv.org/abs/2301.08721) [2023] (Arxiv)
  - [Successive Prompting for Decompleting Complex Questions](https://arxiv.org/abs/2212.04092) [2022] (Arxiv) 
  - [Structured Prompting: Scaling In-Context Learning to 1,000 Examples](https://arxiv.org/abs/2212.06713) [2022] (Arxiv) 
  - [Large Language Models Are Human-Level Prompt Engineers](https://arxiv.org/abs/2211.01910) [2022] (Arxiv) 
  - [Ask Me Anything: A simple strategy for prompting language models](https://paperswithcode.com/paper/ask-me-anything-a-simple-strategy-for) [2022] (Arxiv) 
  - [Prompting GPT-3 To Be Reliable](https://arxiv.org/abs/2210.09150) [2022](Arxiv) 
  - [Decomposed Prompting: A Modular Approach for Solving Complex Tasks](https://arxiv.org/abs/2210.02406) [2022] (Arxiv) 
  ```

- Translation of code comments in multiple languages, including Python, Java, and JavaScript...

  For example, a Linux kernel code comment:

  ```c
    /* MEM points to BPF ring buffer reservation. */
    MEM_RINGBUF		= BIT(2 + BPF_BASE_TYPE_BITS),

    /* MEM is in user address space. */
    MEM_USER		= BIT(3 + BPF_BASE_TYPE_BITS),

    /* MEM is a percpu memory. MEM_PERCPU tags PTR_TO_BTF_ID. When tagged
    * with MEM_PERCPU, PTR_TO_BTF_ID _cannot_ be directly accessed. In
    * order to drop this tag, it must be passed into bpf_per_cpu_ptr()
    * or bpf_this_cpu_ptr(), which will return the pointer corresponding
    * to the specified cpu.
    */
    MEM_PERCPU		= BIT(4 + BPF_BASE_TYPE_BITS),
  ```

  will be translated into Chinese:

  ```c
  /* MEM 指向 BPF 环形缓冲区预留。*/
  MEM_RINGBUF		= BIT(2 + BPF_BASE_TYPE_BITS),

  /* MEM 在用户地址空间中。 */
  MEM_USER		= BIT(3 + BPF_BASE_TYPE_BITS),

  /* MEM 是 percpu 内存。MEM_PERCPU 标记 PTR_TO_BTF_ID。
  * 被标记为 MEM_PERCPU 的 PTR_TO_BTF_ID 不能直接访问。
  * 为了去除此标记，必须将其传递到 bpf_per_cpu_ptr() 或 bpf_this_cpu_ptr()，
  * 这将返回与指定 cpu 相对应的指针。
  */
  MEM_PERCPU		= BIT(4 + BPF_BASE_TYPE_BITS),
  ```

- Automatic detection of changes to Git repositories
- Configurable options, such as Git repository URL, source and target languages, and API key

  ```yml
  inputs:
    git_repo_url:
      description: "The git repo url to clone and translate"
    api_key:
      description: "The OpenAI api key to use for translation"
    source_language:
      description: "The source language to translate from. The default is English"
    target_language:
      description: "The target language to translate to. The default is Chinese"
    additional_prompt: 
      description: "Additional prompt to improve performance."
    i18n_surfix:
      description: "The i18n surfix to add to the translated file. The default is empty, so the translated file will overwrite the original file."
    file_types:
      description: "The file types to translate. The default is all file types supported"
    file_path_filter:
      description: "The file path filter to translate. The default is all files"
  ```

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
