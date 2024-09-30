from django.http import HttpResponse

# from django.http import Http404
# from django.template import loader
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.db.models import F

import requests
from bs4 import BeautifulSoup
import pyautogui

class IndexView(generic.ListView):
    template_name = "crawling/index.html"
    context_object_name = "latest_question_list"
    
    def get_queryset(self):
        print('test')
        self.pyautogui_prompt()
        return
    
    def crawling_test(self):
        response = requests.get('https://naver.com')
        html = response.text
        # print(html)
        
    def beautifulsoup4_test(self):
        response = requests.get('https://naver.com')
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        word = soup.select_one('#topSearchWrap')
        print(word.text)
        
    def css_test(self):
        # tag: h1, a
        # id: #test
        # class: .test
        # children: .test > span
        print('test')
        response = requests.get('https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90')
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        links = soup.select('.news_tit')
        for link in links:
            title = link.text
            url = link.attrs['href']
            print(title, url)
            
    def input_test(self):
        keyword = input('검색어')
        print('test')
        response = requests.get('https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=' + keyword)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        links = soup.select('.news_tit')
        for link in links:
            title = link.text
            url = link.attrs['href']
            print(title, url)
            
    def pyautogui_prompt(self):
        keyword= pyautogui.prompt('검색어')
        response = requests.get(f'https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query={keyword}')
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        
        links = soup.select('.news_tit')
        for link in links:
            title = link.text
            url = link.attrs['href']
            print(title, url)
            
    def for_prompt(self):
        keyword = '삼성'
        lastPage = 30
        pageNum = 1
        for i in range(1, int(lastPage) * 10, 10):
            response = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}')
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            
            links = soup.select('.news_tit')
            for link in links:
                title = link.text
                url = link.attrs['href']
                print(title, url)
            pageNum = pageNum + 1