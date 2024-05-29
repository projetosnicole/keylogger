from flask import Flask, request, render_template, redirect, url_for, send_file
import pandas as pd
import io

app = Flask(__name__)

# Lista para armazenar os dados submetidos
data_list = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    phone = request.form['phone']
    email = request.form['email']
    address = request.form['address']
    user_ip = request.remote_addr
    
    # Armazenando os dados em uma lista
    data_list.append({
        'Nome': name,
        'Telefone': phone,
        'Email': email,
        'Endereço': address,
        'IP': user_ip
    })
    
    return redirect(url_for('thank_you'))

@app.route('/thank_you')
def thank_you():
    return "<h1>Obrigado!</h1><p>Por favor, não compartilhe suas informações pessoais.</p>"

@app.route('/download')
def download():
    # Convertendo a lista de dados para um DataFrame do pandas
    df = pd.DataFrame(data_list)
    
    # Salvando o DataFrame em um buffer de memória como arquivo Excel
    output = io.BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False, sheet_name='Sheet1')
    writer.save()
    output.seek(0)
    
    # Enviando o arquivo Excel como download
    return send_file(output, as_attachment=True, attachment_filename='dados.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == '__main__':
    app.run(debug=True)
