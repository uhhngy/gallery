import openai
from django.shortcuts import render
from .forms import ImagePromptForm
from .models import ImagePrompt
from openai.error import InvalidRequestError


def generate_image(api_key, prompt, size):
    openai.api_key = api_key #(Please prepair an OpenAI API key for testing, this key will be revoked after demo) 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

    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size=size,
        response_format="url"
    )

    return response["data"][0]["url"]


def generate(request):
    if request.method == 'POST':
        form = ImagePromptForm(request.POST)
        if form.is_valid():
            api_key = form.cleaned_data['apikey']
            prompt = form.cleaned_data['prompt']
            size = form.cleaned_data['size']
            try:
                image_url = generate_image(api_key, prompt, size)
                return render(request, 'image_generator/generate.html', {'form': form, 'image_url': image_url})
            except InvalidRequestError:
                error_message = "Your request was rejected by our safety system. Your prompt may contain text that is not allowed."
                return render(request, 'image_generator/error.html', {'error_message': error_message})
            except Exception as e:
                error_message = f"An error occurred: {str(e)}"
                return render(request, 'image_generator/error.html', {'error_message': error_message})
    else:
        form = ImagePromptForm()

    return render(request, 'image_generator/generate.html', {'form': form})

