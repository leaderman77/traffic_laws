import json
import requests
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

def download_mp4(url, filename):
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(filename, 'wb') as output_file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                output_file.write(chunk)

def fetch_article_alias_uz_la(item, idx):
    url = item['concat']
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        vid_url = data['offense']['report']['video']['download-url']
        print(idx, vid_url)


        download_mp4(vid_url, f"vids/vid_39_1284-2_{idx}.mp4")

        tmp = data['offense'].get('article_alias_uz_la-url', None)
        return tmp
    else:
        print(f"Failed to fetch data from URL: {url}")
        return None

def get_article_alias_uz_la_parallel(json_data, max_workers=3):
    article_aliases = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(fetch_article_alias_uz_la, item, idx): item for idx, item in enumerate(json_data)}

        for future in tqdm(as_completed(futures), total=len(futures)):
            result = future.result()
            article_aliases.append(result)

    return article_aliases

# Read JSON data from a file
with open('link_v3.json', 'r') as file:
    json_data = json.load(file)

json_data_filtered = []
for d in json_data:
    # modda id va number. Etibor qiling Moddalar.pdf da id=Kod, va number=Raqam deyilgan
    if d['id'] == 39 and d['number'] == '128⁴-2':
        json_data_filtered.append(d)

print(len(json_data_filtered))

# vids nomli papka yarating
article_aliases = get_article_alias_uz_la_parallel(json_data_filtered)
