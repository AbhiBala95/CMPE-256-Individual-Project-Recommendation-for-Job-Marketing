# -*- coding: utf-8 -*-
from scrapy import Spider
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import Request
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class JobsSpider(Spider):
	name = 'jobs'
	allowed_domains = ['indeed.com']

	def start_requests(self):
		self.driver = webdriver.Chrome(executable_path='C:/Users/abhinav/Downloads/chromedriver.exe')
		self.driver.get('https://www.indeed.com/jobs?q=database+developer&start=50')

		sleep(20)
		sel= Selector(text=self.driver.page_source)
		jobs= sel.xpath('//*[@class="title"]/a/@href').extract()
		for job in jobs:
			url='https://indeed.com' + job                             
			yield Request(url, callback=self.parse_job)

	def parse_job(self, response):
		job_title=response.xpath('//*[@class="icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title"]/text()').extract()
		company=response.xpath('//*[@class="icl-u-lg-mr--sm icl-u-xs-mr--xs"]/a/text()').extract()
		location=response.xpath('//*[@class="icl-u-xs-mt--xs  jobsearch-JobInfoHeader-companyLocation jobsearch-DesktopStickyContainer--companylocation"]/text()').extract()
		job_description=response.xpath('//*[@class="jobsearch-jobDescriptionText"]/text()').extract()
		company_info=response.xpath('//*[@id="jobDescriptionText"]/p[1]/text()').extract()
		responsibilities=response.xpath('//*[@id="jobDescriptionText"]/ul[1]/li/text()').extract()
		requirements=response.xpath('//*[@id="jobDescriptionText"]/ul[2]/li/text()').extract()
		job_type=response.xpath('//*[@id="jobDescriptionText"]/p[4]/text()').extract()
		experience=response.xpath('//*[@id="jobDescriptionText"]/ul[3]/li/text()').extract()
		education=response.xpath('//*[@id="jobDescriptionText"]/ul[4]/li/text()').extract()
		yield {'Title of the Job':job_title,'Company':company,'Location':location,"Company Info":company_info,"Responsibilities":responsibilities,"Requirements":requirements,"Job Type":job_type,"Experience":experience,"Education":education}