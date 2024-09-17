from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de banco de dados
products = []

@app.route('/product', methods=['POST'])
def add_product():
    data = request.json
    product = {
        'name': data.get('name'),
        'price': data.get('price')
    }
    products.append(product)
    return jsonify({'message': 'Produto adicionado com sucesso!'})

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
