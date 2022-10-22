from flask import render_template, request
from SaleApp.saleapp import app, dao


@app.route('/')
def index():
    categories = dao.load_categories()
    return render_template('index.html',
                           categories=categories)

@app.route('/products')
def products_list():
    categories = dao.load_categories()
    products = dao.load_products()
    cate_id = request.args.get("category_id")
    kw = request.args.get("keyword")
    from_price = request.args.get("from_price")
    to_price = request.args.get(("to_price"))
    products = dao.load_products(cate_id = cate_id,
                                 kw = kw,
                                 from_price = from_price,
                                 to_price = to_price)

    return render_template('products.html',
                           categories=categories,
                           products = products)

@app.route("/products/<int:product_id>")
def product_detail(product_id):
    product = dao.get_product_by_id(product_id)

    return render_template('product_detail.html',
                           product = product)


if __name__ == ('__main__'):
    app.run(debug=True)
