import json
import requests
from bs4 import BeautifulSoup as bs


def get_html(url):
    """
    获取网页源码
    :param url: 网页请求链接 :return: 返回网页源码"""
    try:
        print(url)
        headers={"user-agent":"Mozilla/5.0"}
        r = requests.get(url,headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        print("产生了异常:{}".format(str(e)))


def parse_movie_by_bs4(html):
    page_movies = []
    soup = bs(html, "html")
    div_info_list = soup.find_all("div", {"class": "info"})
    for div_info in div_info_list:
        movie = {}
        div_hd = div_info.find("div", {"class": "hd"})
        div_bd = div_info.find("div", {"class": "bd"})
        movie["url"] = div_hd.a.attrs["href"]
        title = ""
        for span in div_hd.a.contents:
            title += str(span.string)
        print(title)
        movie["title"] = "".join(title.split())
        p1 = div_bd.find("p", {"class": ""})
        movie["info"] = (
            ",".join(p1.get_text(",", strip=True).split())
            .replace(":", ",")
            .replace(",,", ",")
            .replace("/", "")
        )
        div_star = div_bd.find("div")
        movie["rating_num"] = div_star.find_all("span")[1].string
        movie["valutaion_num"] = str(div_star.find_all("span")[3].string).replace(
            "人评价", ""
        )
        p2 = div_bd.find("p", {"class": "quote"})
        if p2 is not None:
            movie["quote"] = p2.span.string
        else:
            movie["quote"] = ""

        page_movies.append(movie)
    return page_movies


def main():
    bash_url = "https://movie.douban.com/top250?start="
    offset = 0
    all_movies = []
    page_id = 0
    while offset < 250:
        print("正在爬取第{}页".format(str(page_id + 1)))
        url = bash_url + str(offset)
        html_text = get_html(url)
        page_movies = parse_movie_by_bs4(html_text)
        all_movies.append(page_movies)
        offset += 25
        page_id += 1
    with open("douban_250.json", "w", encoding="utf-8") as filename:
        filename.write(json.dumps(all_movies, ensure_ascii=False))
        print("所有数据爬取完毕")


print(__name__)
if __name__ == "__main__":
    main()
