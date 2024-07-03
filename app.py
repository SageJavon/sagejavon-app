from flask import Flask, render_template, request
from markupsafe import Markup
from zhipuai import ZhipuAI
import markdown
import markdown.extensions.fenced_code
import markdown.extensions.codehilite
import os
from dotenv import load_dotenv
load_dotenv()

client = ZhipuAI(api_key=os.getenv('ZHIPUAI_API_KEY'))

app = Flask(__name__)
messages = []


@app.route('/')
def home():

    return render_template('index.html')


@app.route('/get_knowledge_concepts_chatglm', methods=['POST'])
def get_bot_response():
    user_input = request.form['user_input']
    # print(user_input)
    messages.append({'role': 'user', 'content': user_input})
    completion = client.chat.completions.create(
        model=os.getenv('LLM_NAME'),
        messages=messages
    )
    print(completion)
    ai_response = completion.choices[0].message.content
    # print(ai_response)
    messages.append({'role': 'assistant', 'content': ai_response})
    print(messages)
    return Markup(markdown.markdown(ai_response, extensions=['fenced_code', 'codehilite']))


@app.route('/reset')
def reset():
    global messages
    messages = []
    return "Conversation history has been reset."


if __name__ == '__main__':
    app.run(debug=True)
