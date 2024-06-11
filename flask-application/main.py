import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect
import google.generativeai as genai

app = Flask(__name__)
app.secret_key = "secret"

load_dotenv()   
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
# print("API Key:", GEMINI_API_KEY)

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(model_name='gemini-pro')

all_responses = []

@app.route('/')
def index():
    return render_template('index.html', all_responses=all_responses)

@app.route('/process_prompt', methods=['POST'])
def process_prompt():
    if request.method == 'POST':
        user_input = request.form['input_text']
        genai_response = model.generate_content({user_input})
        # print("Response:", genai_response.text)
        all_responses.append(genai_response.text)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)