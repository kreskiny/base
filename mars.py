from flask import Flask, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['title'] = 'Заготовка'
    return render_template('base.html', **param)
@app.route('/training/<prof>')
def training(prof):
    param = {}
    param['prof'] = prof
    return render_template('train.html', **param)

@app.route('/list_prof/<list1>')
def  list_prof(list1):
    param = {}
    param['title'] = 'Заготовка'
    param['list'] = list1
    param['profs'] = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                      'инженер по терраформированию', 'климатолог', 'специалист по радиационной защите', 'астрогеолог',
                      'гляциолог', 'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                      'штурман', 'пилот дронов']
    return render_template('proffesions.html', **param)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
