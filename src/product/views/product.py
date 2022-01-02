import json
from django.views import generic
from django.shortcuts import render, redirect
from product.models import Variant, Product, ProductVariantPrice, ProductImage, ProductVariant


class CreateProductView(generic.View):

    def get(self, request, *args, **kwargs):

        variants = Variant.objects.filter(active=True).values('id', 'title')
        variants = list(variants)
        context = {
            'variants': variants
        }
        return render(request, 'products/create.html', context)

    def post(self, request, *args, **kwargs):
        product_obj = json.loads(request.body.decode('utf-8'))
        print(product_obj)
        product_variant = product_obj['product_variant']
        product_variant_prices= product_obj['product_variant_prices']

        newProduct = Product.objects.create(
            title=product_obj['title'],
            sku=product_obj['sku'],
            description=product_obj['description']
        )
        newImage = ProductImage(
            product=newProduct,
            file_path=product_obj['product_image']
        )
        newImage.save(force_insert=True)
        print(product_variant)
        print(product_variant_prices)
        return redirect('product:list.product')


class ProductListView(generic.ListView):
    template_name = 'products/list.html'
    paginate_by = 2
    model = Product
    context_object_name = 'items'
