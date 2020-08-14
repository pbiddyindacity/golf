from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.jinja2')

@app.route('/scorecard', methods=['GET', 'POST'])
def scorecard():
    if request.method == "POST":
        hole_1 = int(request.form.get('hole_1'))
        hole_2 = int(request.form.get('hole_2'))
        hole_3 = int(request.form.get('hole_3'))
        hole_4 = int(request.form.get('hole_4'))
        hole_5 = int(request.form.get('hole_5'))
        hole_6 = int(request.form.get('hole_6'))
        hole_7 = int(request.form.get('hole_7'))
        hole_8 = int(request.form.get('hole_8'))
        hole_9 = int(request.form.get('hole_9'))
        hole_10 = int(request.form.get('hole_10'))
        hole_11 = int(request.form.get('hole_11'))
        hole_12 = int(request.form.get('hole_12'))
        hole_13 = int(request.form.get('hole_13'))
        hole_14 = int(request.form.get('hole_14'))
        hole_15 = int(request.form.get('hole_15'))
        hole_16 = int(request.form.get('hole_16'))
        hole_17 = int(request.form.get('hole_17'))
        hole_18 = int(request.form.get('hole_18'))
        front_9 = (hole_1 + hole_2 + hole_3 +
                      hole_4 + hole_5 + hole_6 +
                      hole_7 + hole_8 + hole_9)
        back_9 = (hole_10 + hole_11 + hole_12 +
                      hole_13 + hole_14 + hole_15 +
                      hole_16 + hole_17 + hole_18)
        total_score = front_9 + back_9
        return render_template('scorecard.jinja2', front_9=front_9, back_9=back_9,
                               total_score=total_score)
    return render_template('scorecard.jinja2')

if __name__ == '__main__':
    app.run(port=5000, debug=True)