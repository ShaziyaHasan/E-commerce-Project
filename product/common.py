from product.models import Shopping_cart

class Common:
    def __init__(self,request):
        self.request = request

    def check_login(self):
        if self.request.session.has_key('id'):
            return 'Y'
        else:
            return 'N'

    def get_shopping_cart(self):
        user_id = self.request.session['id']

        sca = Shopping_cart.objects.raw('select *, (price * qnt) as tot from '
        '(select psc.id , case when psc.quantity <= pp.quantity then psc.quantity else pp.quantity end qnt, '
        'pp.id as pid, pp.quantity as stock, pp.product_name as product_name, '
        'pp.price as price, pp.color as color, pp.size as size, pp.image as image, mu.id as userid, '
        'mu.first_name as first_name, mu.last_name as last_name from product_shopping_cart as psc '
        'join product_product as pp on psc.product_id_id = pp.id '
        'join myapp_userdetails as mu on psc.user_id_id = mu.id) as abc '
        'where userid= %d;' % user_id)

        sum = 0
        count = 0
        for x in sca:
            sum += x.tot
            count += 1

        ship = 0
        if sum < 1000:
            ship = 100

        tax = sum*0.1

        gros = sum + ship + tax

        dic = {'sca':sca,'sum':sum,'ship':ship,'tax':tax,'gros':gros, 'count':count}

        return dic