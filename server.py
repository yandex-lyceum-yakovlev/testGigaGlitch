from flask import Flask
from flask import render_template, url_for
import os

from giga import *

app = Flask(__name__)
chat = init_giga()


@app.route('/')
def hello_world():  # put application's code here
    messages = [
        SystemMessage(
            content=f'Ты -добрый писатель, который составляет сказки вместе с ребенком. Ты должен дополнять сказку польователя на'
                    f'одно единственное предложение '

        )
    ]
    user_input = "Расскажи сказку про крокодила."
    messages.append(HumanMessage(content=user_input))
    res = chat(messages).content
    return render_template('index.html', answer=res)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
