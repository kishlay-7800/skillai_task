from flask import Flask, request
app = Flask(__name__)
import pandas as pd
df = pd.read_csv(r"C:\Users\Kishlay Kumar\Documents\doc1.csv")

app.route('/hello/<int:city_name>')
def hello(city_name):
    return f"hello {city_name}"


@app.route('/population/<string:city_name', methods = ['GET'])
def Population():
    city_name = request.args.get('city')
    population = df[df['My_City'] == city_name]['My_Population'].sum()
    return {'city_name':city_name, 'population':population }

if __name__ == '__main__':
    app.run(debug=True)
