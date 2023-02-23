# This is app.py, this is the main file called.
import pandas as pd
from flask import jsonify, render_template, request

from funciones.eda import *
from myproject import app, FiltroForm


@app.route('/', methods=['GET', 'POST'])
def index():
    
    form = FiltroForm()
    
    data = pd.read_excel('data.xlsx')
    text = data['AREA'].str.cat(sep= ' ')
    pie = pie_data(data_frame=data)
    card1 = card1_serie(data_frame=data)
    card2 = card2_serie(data_frame=data)
    
    if form.validate_on_submit():
        pais = form.pais.data
        print(pais)
        sexo = form.sexo.data
        tipo_contratacion = form.tipo_contratacion.data
        
        try:
            data1 = data[(data['PAIS'].isin(pais))]
            try:
                data2 = data1[(data1['SEXO'].isin(sexo))]
                print('paso')
            except:
                pass
            
            try:
                data3 = data2[(data2['TIPO_CONTRATACION'].isin(tipo_contratacion))]
                print('paso2')
            except:
                try:
                    data3 = data1[(data1['SEXO'].isin(sexo))]
                    print('paso')
                except:
                    data3 = data[(data['PAIS'].isin(pais))]
                    
            text = data3['AREA'].str.cat(sep= ' ')
            pie = pie_data(data_frame=data3)
            card1 = card1_serie(data_frame=data3)
            card2 = card2_serie(data_frame=data3)
            
            return render_template('index.html',
                            text = text,
                            pie = pie,
                            card1 = card1,
                            card2 = card2,
                            form = form
                            ) 
        except:
            pass
        
    return render_template('index.html',
                           text = text,
                           pie = pie,
                           card1 = card1,
                           card2 = card2,
                           form = form
                           )

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)