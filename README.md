# Amazon Scrapy Project

This project is configured to be hosted on [Scrapy Cloud](https://www.zyte.com/scrapy-cloud/).  
It uses [Zyte Smart Proxy Manager](https://scrapinghub.com/?rfsn=4170080.0597ad) as proxy service.  
The dataset can be found [here](https://www.kaggle.com/datasets/patkle/metal-music-ratings-and-review-counts-from-amazon).  
A Jupyter Notebook with some EDA on that data can be found [here](https://www.kaggle.com/code/patkle/metal-ratings-from-amazon).

## music

The spider can be ran with
```zsh
python3 -m scrapy crawl music -a pages=5 -a category=n%3A5174%2Cn%3A67207 -O music.csv
```

### Arguments

With `-a` you can specify arguments for the spider.  

|argument   |type  |description   | 
|---|---|---|
|pages   |int   |number of pages to scrape   |
|category   |string   |category as provided in the Amazon url   |

#### Category = rh
The category in Amazon urls is specified via the `rh` parameter.  
In this example, the category would be **n%3A5174%2Cn%3A67207**:
https://www.amazon.com/s?i=popular&rh=n%3A5174%2Cn%3A67207&s=review-rank&dc&page=401&qid=1675625847&ref=sr_pg_3


## Setting up locally
  
When setting up this project locally you must create a **.env** file with the following data:  

|setting   |description   |  
|---|---|
|ZYTE_SMARTPROXY_APIKEY   |your smart proxy manager api key   |
  

## Deploy to Scrapy Cloud
There's a shortcut in the Makefile, just running `make deploy` will deploy the project to Scrapy Cloud (given that you provided the project ID in `scrapinghub.yml`).Don't forget to add the following settings in your cloud project's settings:
|setting   |description   | 
|---|---|
|ZYTE_SMARTPROXY_APIKEY   |your smart proxy manager api key   |
  
## Also, 
you could [buy me a coffe](https://www.buymeacoffee.com/kleinp) if you wanted to. I'd really appreciate that.  
