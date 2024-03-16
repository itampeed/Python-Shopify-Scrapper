import requests
import pandas as pd

all_variants = []
variable_skus = {}  # To store variable SKU for each product handle

d = [1, 2, 3]

for i in d:
    url = f"https://www.shopbogaboga.com/products.json?limit=250&page={i}"
    r = requests.get(url)
    data = r.json()
    
    for product in data['products']:
        title = product['title']
        handle = product['handle']
        
        first_variant = True

        for variant in product['variants']:
            variant_title = variant['title']
            variant_price = str(variant['price'])
            variant_sku = str(variant['sku'])
            variant_available = variant['available']
            try:
                variant_image = variant['featured_image']['src']
            except:
                variant_image = None
            variant_color = variant['option1']
            variant_size = variant['option2']

            if first_variant:
                variant_type = 'variable'
                first_variant = False
                description = product['body_html']
                category = product['product_type']
                tags = ', '.join(product['tags'])
                
                # Store variable SKU in the dictionary
                variable_skus[handle] = variant_sku  
                parent_sku = ''  # No parent SKU for variable
            else:
                variant_type = 'variation'
                description = ''
                category = ''
                tags = ''
                
                # Assign parent SKU for variations
                parent_sku = variable_skus.get(handle, '')

            all_variants.append({
                'title': title,
                'handle': handle,
                'short_description': description,
                'category': category,
                'tags': tags,
                'variant_title': variant_title,
                'color': variant_color,
                'size': variant_size,
                'variant_price': variant_price,
                'variant_sku': variant_sku,
                'parent': parent_sku,  # Adding parent SKU column
                'variant_available': variant_available,
                'variant_image_src': variant_image,
                'type': variant_type
            })

variants_df = pd.DataFrame(all_variants)
variants_df.to_csv('Variants.csv', index=False)
