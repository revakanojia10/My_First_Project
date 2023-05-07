
import pandas
import requests
import time
import math

def crawl_data(url,page_no,Name):
    category_id = url.split("/")[-1]
    page_size = 48

    page_0 = f'''https://www.bedbathandbeyond.com/apis/services/composite/product-listing/v1.0/all?web3feo=1&site=BedBathUS&currencyCode=USD&country=US&rT=xtCompat&tz=-330&displayAdsAt=6&categoryId={category_id}&categoryType=plp_l3&countOnly=false&higherShippingThreshhold=0.1&pageURI=/store/category/storage-cleaning/storage-organization/storage-bins-baskets/12208&solrCat=true&view=grid&web3feo=true&noFacet=false&start=0&perPage=48&sws=&storeOnlyProducts=false&customPriceRange=false&__amp_source_origin=https://www.bedbathandbeyond.com'''

    response = requests.get(page_0)
    data = response.json()
    product_count = data['response']['numFound']

    page_count = math.ceil(product_count // page_size)

    collected_data = []
    print(page_count)
    for page in range(min(page_no,page_count)+1):
        start_value = page * page_size
        page_url = f'''https://www.bedbathandbeyond.com/apis/services/composite/product-listing/v1.0/all?web3feo=1&site=BedBathUS&currencyCode=USD&country=US&rT=xtCompat&tz=-330&displayAdsAt=6&categoryId={category_id}&categoryType=plp_l3&countOnly=false&higherShippingThreshhold=0.1&pageURI=/store/category/storage-cleaning/storage-organization/storage-bins-baskets/12208&solrCat=true&view=grid&web3feo=true&noFacet=false&start={start_value}&perPage=48&sws=&storeOnlyProducts=false&customPriceRange=false&__amp_source_origin=https://www.bedbathandbeyond.com'''
        response = requests.get(page_url)
        response = response.json()
        products = response['response']['docs']

        for i in products:
            try:
                name = i['DISPLAY_NAME']
                rating = i.get("RATINGS", 0)
                review = i.get("REVIEWS", 0)
                normal_price = i['normal']
                discounted_price = i.get('salePrice', normal_price)
                product_id = i['PRODUCT_ID']
                d = {
                    "NAME": name,
                    "RATING": rating,
                    "REVIEW COUNT": review,
                    "PRICE": normal_price,
                    "DISCOUNTED PRICE": discounted_price,
                    "PRODUCT ID": product_id
                }
                collected_data.append(d)
            except Exception as e:
                print(e)
        time.sleep(2)

    pandas_df = pandas.DataFrame(collected_data)
    pandas_df.to_csv(f'{Name}_crawl_data.csv', index=False)
    return len(collected_data)