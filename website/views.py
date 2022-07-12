from flask import redirect, render_template,Blueprint,request,flash, url_for
from .clima import clima

views = Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
def home():
    global dados
    if request.method == 'POST':
        cidade = str(request.form.get('cidade'))
        try:
            dados = clima(cidade)
            return redirect(url_for('views.result'))
        except:
            flash('Cidade não encontrada','error')
    return render_template('home.html')
@views.route('/result',methods=['GET','POST'])
def result():
    global dados
    cidade = dados['cidade']
    pais = dados['pais']
    temperatura_atual = dados['temperatura']
    sensação = dados['sensação']
    temp_max = dados['temp_max']
    temp_min = dados['temp_min']
    status = dados['desc']
    umidade = dados['umidade']
    vento = dados['vento']
    return render_template('result.html',cidade=cidade,temperatura_atual=temperatura_atual,
    pais=pais,sensação=sensação,temp_max=temp_max,temp_min=temp_min,status=status,
    umidade = umidade,vento=vento
    )