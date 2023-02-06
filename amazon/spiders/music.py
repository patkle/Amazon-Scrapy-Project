from scrapy import Request, Spider


class musicSpider(Spider):
    name = "music"

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.pages = int(kwargs.get("pages", 10))
        self.category = kwargs.get("category", "n%3A5174%2Cn%3A67207")

    def start_requests(self):
        yield Request(
            f"https://www.amazon.com/s?i=popular&rh={self.category}&s=review-rank&dc"
        )
        for i in range(2, self.pages + 1):
            yield Request(
                f"https://www.amazon.com/s?i=popular&rh={self.category}&s=review-rank&dc&page={i}"
            )

    def parse(self, response):
        for sr in response.xpath("//div/div[@data-component-type='s-search-result']"):
            yield {
                "asin": sr.xpath(".//@data-asin").get(),
                "title": sr.xpath(".//h2/a/span/text()").get(),
                "artist": self._get_artist(sr),
                "year": self._get_year(sr),
                "star_rating": self._get_star_rating(sr),
                "review_count": sr.xpath(".//span[@aria-label]/a/span/text()").get(),
                "media": self._get_media(sr),
            }

    def _get_artist(self, selector):
        artist = selector.xpath(".//div/div[@class='a-row']/a/text()").get()
        if artist is None:
            artist = selector.xpath(".//div/div[@class='a-row']/span[2]/text()").get()
        return artist

    def _get_year(self, selector):
        year = selector.xpath(".//div/div[@class='a-row']/span[5]/text()").get()
        if year is None:
            year = selector.xpath(".//div/div[@class='a-row']/span[6]/text()").get()
        return year

    def _get_star_rating(self, selector):
        try:
            return (
                selector.xpath(".//i[contains(@class, 'a-icon-star-small')]/span/text()")
                .get()
                .split("out of")[0]
                .strip()
            )
        except:
            return None

    def _get_media(self, selector):
        return [
            x
            for x in selector.xpath(f".//a[contains(@href, '/dp/')]/text()").getall()
            if x.strip()
        ]
