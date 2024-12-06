import requests
from lxml import etree
import time
import os

def get_html_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    try:
        # driver = webdriver.Chrome()
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except Exception as e:
        print(f"网络请求异常：{e}")
        return None


def parse_html(html_content):
    tree = etree.HTML(html_content)
    data_list = []
    links = tree.xpath("/html/body/div/section/div/div[@class='view_content']/section/div[@id='imageContent']/section/div/figure/a/img/@data-src")
    for link in links:
        total_link = 'https:' + link + '?x-oss-process=image/format,webp'
        data_list.append(total_link)

    return data_list

def store_data(result_list, save_path):
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    for url in result_list:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            file_name = os.path.join(save_path, url.split('/')[-2].split('?')[0])

            with open(file_name, 'wb') as f:
                f.write(response.content)

            print(f"success download: {file_name}")

        except requests.exceptions.RequestException as e:
            print(f"fail download: {url} : {e}")

        time.sleep(5)



if __name__ == '__main__':
    for page in range(1, 10):
        target_url = f"https://www.vcg.com/creative-image/maogou/?page={page}"
        html_content = get_html_content(target_url)


        if html_content:
            result_list = parse_html(html_content)
            store_data(result_list, 'your save path')
            print("Everyone down")
        else:
            print("fail access web")


