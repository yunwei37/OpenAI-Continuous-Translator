from unittest.mock import MagicMock
from continuous_translation import translation


def test_translate_text():
    # 使用 MagicMock 模拟 openai.ChatCompletion.create 函数的返回值
    mock_completion = MagicMock()
    mock_completion["choices"][0].get.return_value = {
        "role": "assistant",
        "content": "Ceci est un texte en français."
    }

    # 为了避免真实调用 OpenAI API，使用 MagicMock 替换 translation.openai.ChatCompletion.create
    translation.openai.ChatCompletion.create = MagicMock(
        return_value=mock_completion)

    source_text = "This is a text in English."
    translated_text = translation.translate(source_text, "en", "fr", "")

    assert translated_text == "Ceci est un texte en français."
