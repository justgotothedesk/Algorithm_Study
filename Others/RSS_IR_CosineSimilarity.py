!pip install feedparser
!pip install newspaper3k
!pip install konlpy
import feedparser
from newspaper import Article
from konlpy.tag import Okt
from collections import Counter

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from newspaper import Article
from bs4 import BeautifulSoup
import requests

def crawl_article_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    content = soup.get_text()
    return content

def search_article(query, list_articles):
    # 기사 내용 크롤링하여 리스트에 저장
    article_contents = [crawl_article_content(article['link']) for article in list_articles]
    # TF-IDF 벡터화
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(article_contents + [query])

    # TF-IDF 벡터들 간의 코사인 유사도 계산
    similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])[0]

    # 가장 높은 유사도를 가진 문서의 인덱스 찾기
    max_indices = np.argsort(similarities)[::-1][:10]

    # 결과 출력
    print("-----")
    print("상위 10개의 기사 내용:")
    for idx in max_indices:
        num_query = np.round(similarities[idx], 2)
        article = list_articles[idx]
        print('[Title]:', article['title'], end=' ')
        print('[URL]:', article['link'])

# 기사 리스트
list_articles = [
    {'title': 'Article 1', 'link': 'https://www.yna.co.kr/view/AKR20240416105900053'},
    {'title': 'Article 2', 'link': 'https://www.yna.co.kr/view/AKR20240416106100062'},
    {'title': 'Article 3', 'link': 'https://www.yna.co.kr/view/AKR20240416106100061'},
    {'title': 'Article 4', 'link': 'https://www.yna.co.kr/view/AKR20240416106100060'},
    {'title': 'Article 5', 'link': 'https://www.yna.co.kr/view/AKR20240416106100059'},
    {'title': 'Article 6', 'link': 'https://www.yna.co.kr/view/AKR20240416106100058'},
    {'title': 'Article 7', 'link': 'https://www.yna.co.kr/view/AKR20240416106100057'},
    {'title': 'Article 8', 'link': 'https://www.yna.co.kr/view/AKR20240416106100056'},
    {'title': 'Article 9', 'link': 'https://www.yna.co.kr/view/AKR20240416106100055'},
    {'title': 'Article 10', 'link': 'https://www.yna.co.kr/view/AKR20240416106100054'},
    {'title': 'Article 11', 'link': 'https://www.yna.co.kr/view/AKR20240416106100053'},
    {'title': 'Article 12', 'link': 'https://www.yna.co.kr/view/AKR20240416106100052'},
    {'title': 'Article 13', 'link': 'https://www.yna.co.kr/view/AKR20240416106100051'},
    {'title': 'Article 14', 'link': 'https://www.yna.co.kr/view/AKR20240416106100050'},
    {'title': 'Article 15', 'link': 'https://www.yna.co.kr/view/AKR20240416106100049'},
    {'title': 'Article 16', 'link': 'https://m.sports.naver.com/wfootball/article/410/0000992160'},
    {'title': 'Article 17', 'link': 'https://m.sports.naver.com/wfootball/article/413/0000175481'},
    {'title': 'Article 18', 'link': 'https://m.sports.naver.com/wfootball/article/109/0005058859'},
    {'title': 'Article 19', 'link': 'https://m.sports.naver.com/wfootball/article/311/0001715157'},
    {'title': 'Article 20', 'link': 'https://m.sports.naver.com/wfootball/article/477/0000484812'},
    {'title': 'Article 21', 'link': 'https://m.sports.naver.com/wfootball/article/139/0002200997'},
    {'title': 'Article 22', 'link': 'https://m.sports.naver.com/wfootball/article/343/0000127036'},
    {'title': 'Article 23', 'link': 'https://m.sports.naver.com/wfootball/article/413/0000175466'},
    {'title': 'Article 24', 'link': 'https://m.sports.naver.com/wfootball/article/139/0002200999'},
    {'title': 'Article 25', 'link': 'https://m.sports.naver.com/wfootball/article/216/0000131273'},
    {'title': 'Article 26', 'link': 'https://m.sports.naver.com/wfootball/article/311/0001715062'},
]

# 예시 쿼리
query = input("쿼리를 입력하세요: ")

# 검색 및 결과 출력
search_article(query, list_articles)
