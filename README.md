# Books Scraper

BeautifulSoup ve requests kullanarak books.toscrape.com sitesinden kitap verisi çeken bir web scraper.

## Ne yapar
Sitedeki kitap listesini tarar, her kitap için başlık, fiyat ve stok durumu bilgisini alır ve `books.csv` dosyasına kaydeder.

## Kullanılan kütüphaneler
- requests — sayfa içeriğini indirmek için
- BeautifulSoup4 — HTML içinden veri ayıklamak için
- pandas — sonucu CSV'ye yazmak için

## Çalıştırma
pip install requests beautifulsoup4 pandas
python scraper.py