import app, requests


class ProductApi:
    def __init__(self):
        # 商品分类
        self.product_classify_url = app.base_url + '/category/all'
        # 分类下商品
        self.classify_product_url = app.base_url + '/product/by_category'
        # 商品信息
        self.product_detail_url = app.base_url + '/product/{}'

    def product_classify_api(self):
        return requests.get(self.product_classify_url)

    def classify_product_api(self, classify_id=2):
        data = {'id': classify_id}
        return requests.get(self.classify_product_url, params=data)

    def product_detail_api(self, product_id=2):
        return requests.get(self.product_detail_url.format(product_id))
