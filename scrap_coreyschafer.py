from bs4 import BeautifulSoup
import requests
import urllib

"""urllib is an in-built python library that can be used to parse a given link."""


source=requests.get('https://coreyms.com/').text
# print(source)

soup=BeautifulSoup(source,'lxml')
# print(Soup.prettify())


# video_link=video_id.split('/')
# # import ipdb; ipdb.set_trace()


# headline=soup.find_all('h2',class_='entry-title').a.text
# summary=soup.find_all('div',class_='entry-content').p.text
# video_id=soup.find_all('iframe',class_='youtube-player')['src']



for headline in soup.find_all('h2',class_='entry-title'):
    Headline=headline.a.text
    print(f"Headline : {Headline}")
    print("")

for summary in soup.find_all('div',class_='entry-content'):
    Summary=summary.p.text
    print(f"Summary :{Summary}")
    print("")

for video_id in soup.find_all('iframe',class_='youtube-player'):
    Video_id=video_id['src']
    url_parse=urllib.parse.urlparse(Video_id)
    # print(url_parse)
    host_name=url_parse.hostname
    # print(host_name)
    embed_video_link=url_parse.path.split("/")[-1]
    # print(embed_video_link)
    Youtube_link= f"https://{host_name}/watch?v={embed_video_link}"
    # print(Youtube_link)

    print(f"Youtube Link : {Youtube_link}")



# for headline in soup.find_all('h2',class_='entry-title'):
#     Headline=headline.a.text
#     print(f"Headline : {Headline}")
#     print("")

#     for summary in soup.find_all('div',class_='entry-content'):
#         Summary=summary.p.text
#         print(f"Summary :{Summary}")
#         print("")

#         for video_id in soup.find_all('iframe',class_='youtube-player'):
#             Video_id=video_id['src']
#             url_parse=urllib.parse.urlparse(Video_id)
#             # print(url_parse)
#             host_name=url_parse.hostname
#             # print(host_name)
#             embed_video_link=url_parse.path.split("/")[-1]
#             # print(embed_video_link)
#             Youtube_link= f"https://{host_name}/watch?v={embed_video_link}"
#             # print(Youtube_link)

#             print(f"Youtube Link : {Youtube_link}")






