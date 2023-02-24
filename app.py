from flask import Flask, render_template, request, redirect, url_for
from slide_generator import generate_scratch
from datetime import datetime as dt


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
   
    # retrieve inputs from form
    topic = request.form['topic']
    colors = request.form['colors']
    look_n_feel = request.form['look_n_feel']
    num_slides = int(request.form['num_slides'])

    # generate HTML code based on inputs
    html_code = generate_scratch(topic,num_slides, colors,look_n_feel)

    # add tab icon
    html_code = html_code[:html_code.find('</head>')] + '''
        <link rel="icon" href="static/logo.png">
        ''' + html_code[html_code.find('</head>'):]


    # add retry button to go back to main page
    html_code = html_code[:html_code.find('</body>')] + '''
        <div class="retry">
            <button class="retry-button" onclick="window.location.href='/'">Retry</button>
        </div>
        ''' + html_code[html_code.find('</body>'):]

    html_code = html_code[:html_code.find('</style>')] + '''
            .retry {
                position: fixed;
                top: 0;
                right: 0;
                height: 50px;
                width: 100%;
                background-color: #333;
                color: #fff;
                display: flex;
                align-items: center;
                justify-content: flex-end;
                padding: 0 10px;
                }

            .retry-button {
                background-color: #0072C6;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-weight: bold;
                cursor: pointer;
                }

            .retry-button:hover {
                background-color: #d6e6ef;
                color: #333;
                }
        ''' + html_code[html_code.find('</style>'):]

    # log generated HTML
    #with open(f'ChatPPT/log/index{str(dt.now())}.html', 'w') as f:
    #    f.write(html_code)

    # render generated HTML in new page
    return render_template('generated.html', html_code=html_code)
 

@app.route('/back')
def back():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
