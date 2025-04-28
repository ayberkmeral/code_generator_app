# code_generator_app
Code generator app in Python 
A simple Flask-based web application that uses OpenAI's API to generate code snippets based on user input.

Features
Generate code using OpenAI models

Simple, clean Flask web server

Jinja2 templates for frontend rendering

API error handling (e.g., Rate Limits, Missing Templates)

Common Errors
TemplateNotFound (index.html):
Make sure there is a templates/index.html file inside a folder called templates/ in your project root.

openai.lib._old_api.APIRemovedInV1:
Update your OpenAI library usage. You must use the newer format if your openai-python version is >= 1.0.0.

openai.error.RateLimitError:
You have exceeded your usage quota. Check your OpenAI account billing section.

License
This project is open source and available under the MIT License.

Notes
If you are running into API errors, ensure your billing is active on OpenAI's platform.

For heavy usage, you may need to upgrade your OpenAI plan.

Always keep your API key safe and never expose it in public repositories!

