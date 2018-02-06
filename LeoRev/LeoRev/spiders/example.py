# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/Leonisa-Posture-Corrector-Wireless-Support/product-reviews/B01DVCHQQ4/ref=cm_cr_arp_d_paging_btm_3?ie=UTF8&reviewerType=all_reviews&pageNumber={}'.format(i) for i in range(1,81)]

    def parse(self, response):
        author = response.xpath('//a[contains(@data-hook, "review-author")]/text()').extract()
        title = response.xpath('//a[contains(@data-hook, "review-title")]/text()').extract()
        rating = response.xpath('//i[contains(@data-hook, "review-star-rating")]/span[contains(@class, "a-icon-alt")]/text()').extract()
        review_date = response.xpath('//span[contains(@data-hook, "review-date")]/text()').extract()
        found_helpful = response.xpath('//span[contains(@data-hook, "helpful-vote-statement")]/text()').extract()
        review_body = response.xpath('//span[contains(@data-hook, "review-body")]/text()').extract()

        yield {
            'author' : author,
            'title' : title,
            'rating' : rating,
            'review_date' : review_date,
            'found_helpful' : found_helpful,
            'review_body' : review_body
        }
