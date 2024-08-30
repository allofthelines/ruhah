import os
from django.core.management.base import BaseCommand
import shopify
from studio.models import Item, EcommerceStore

class Command(BaseCommand):
    help = 'Update item name and price based on Shopify product data'

    def handle(self, *args, **kwargs):
        # Filter items that are connected to a Shopify store and have relevant categories
        items = Item.objects.filter(
            ecommerce_store__platform='shopify',
            ecommerce_product_id__isnull=False,
            cat__in=['dress', 'top', 'bottom', 'accessory']
        )

        # Print the number of items found
        print(f"Found {items.count()} items to process.")

        if not items.exists():
            print("No items found matching the criteria.")
            return

        for item in items:
            ecommerce_store = item.ecommerce_store
            print(f"Processing Item ID: {item.id} - {item.name}")

            # Get Shopify credentials
            api_key = ecommerce_store.api_key
            api_secret = ecommerce_store.api_secret
            api_access_token = ecommerce_store.api_access_token
            shop_url = f"https://{ecommerce_store.shop_url}/admin"

            # Print Shopify credentials (masked for security)
            print(f"Connecting to Shopify store: {shop_url}")

            # Connect to Shopify
            shopify.ShopifyResource.set_site(shop_url)
            session = shopify.Session(shop_url, version="2023-04", token=api_access_token)
            shopify.ShopifyResource.activate_session(session)

            try:
                # Fetch product from Shopify
                print(f"Fetching product {item.ecommerce_product_id} for Item ID: {item.id}")
                product = shopify.Product.find(item.ecommerce_product_id)

                if not product:
                    print(f"No product found for Item ID: {item.id}")
                    continue

                # Update item name and price
                item.name = product.title
                print(f"Product title from Shopify: {product.title}")

                max_price = max(float(variant.price) for variant in product.variants)
                print(f"Highest variant price from Shopify: {max_price}")

                item.price = max_price
                item.save()

                print(f"Updated Item ID: {item.id} - Name: {item.name}, Price: {item.price}")

            except Exception as e:
                print(f"Error updating item {item.id}: {e}")
