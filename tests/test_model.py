from unittest.mock import MagicMock, patch

from model import generate_recipe


def test_prompt_template_applied():
    mock_pipeline = MagicMock()
    mock_pipeline.return_value = [{"generated_text": "Zutaten: Kartoffeln\n\nZubereitung: kochen"}]

    with patch("model.load_model", return_value=mock_pipeline):
        result = generate_recipe("Kartoffeln")

    assert isinstance(result, str)
    call_args = mock_pipeline.call_args
    prompt = call_args[0][0]
    assert "Zutaten: Kartoffeln" in prompt
    assert "Zubereitung:" in prompt


def test_generation_params_passed():
    mock_pipeline = MagicMock()
    mock_pipeline.return_value = [{"generated_text": "test output"}]

    with patch("model.load_model", return_value=mock_pipeline):
        generate_recipe("test", temperature=0.5, max_length=100, top_p=0.8)

    call_kwargs = mock_pipeline.call_args[1]
    assert call_kwargs["temperature"] == 0.5
    assert call_kwargs["max_length"] == 100
    assert call_kwargs["top_p"] == 0.8
    assert call_kwargs["do_sample"] is True
