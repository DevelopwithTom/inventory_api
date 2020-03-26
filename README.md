This is a very simple inventory api using Django REST framework. 

To register a product http://localhost:8000/inventory/product/

To view (also put and patch update) a product from its SKU http://localhost:8000/inventory/product/[INSERT SKU HERE]

To view all products with a stock > 0 http://localhost:8000/inventory/product/?available=True

To view all products with zero stock http://localhost:8000/inventory/product/?not_in_stock=True
