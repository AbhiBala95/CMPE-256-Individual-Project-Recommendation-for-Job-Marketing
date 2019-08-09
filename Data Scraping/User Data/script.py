import csv
import paramaters
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def validate_field(field):
    if field:
        pass
    else:
        field = ''
    return field

writer = csv.writer(open(paramaters.file_name, 'w'))
writer.writerow(['Name', 'Job Title','Location', 'URL','Old Positions','Old Companies1','Old Companies2','Number of years1','Number of years2','job description','self description'])

driver = webdriver.Chrome(executable_path='C:/Users/abhinav/Downloads/chromedriver.exe')
driver.get('https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin')

username = driver.find_element_by_id('username')
username.send_keys(paramaters.linkedin_username)
sleep(0.5)

password = driver.find_element_by_id('password')
password.send_keys(paramaters.linkedin_password)
sleep(0.5)

sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')
sign_in_button.click()
sleep(5)

driver.get('https://www.google.com/search?biw=1366&bih=657&ei=3T9LXcnWN5q5tQb5mYTAAw&q=%27site%3Alinkedin.com%2Fin%2F+AND+%22database+developer%22+AND+%22london%22%27&oq=%27site%3Alinkedin.com%2Fin%2F+AND+%22database+developer%22+AND+%22london%22%27&gs_l=psy-ab.3...576997.580414..580977...0.0..0.134.1227.13j3......0....1..gws-wiz.zDg5A8_M_ZA&ved=&uact=5')
sleep(3)

#search_query = driver.find_element_by_name('q')
#search_query.send_keys(paramaters.search_query)
#sleep(0.5)

#search_query.send_keys(Keys.RETURN)
#sleep(3)

linkedin_urls = driver.find_elements_by_tag_name('cite')
linkedin_urls = [url.text for url in linkedin_urls]
sleep(0.5)

for linkedin_url in linkedin_urls:
    driver.get(linkedin_url)
    sleep(5)

    sel = Selector(text=driver.page_source)

    name = sel.xpath('//*[@class="pv-top-card-v3--list inline-flex align-items-center"]/*[@class="inline t-24 t-black t-normal break-words"]/text()').extract_first().strip()

    job_title = sel.xpath('//*[@class="flex-1 mr5"]/*[@class="mt1 t-18 t-black t-normal"]/text()').extract_first().strip()

    location = sel.xpath('//*[@class="display-flex mt2"]/*[@class="flex-1 mr5"]/*[@class="pv-top-card-v3--list pv-top-card-v3--list-bullet mt1"]/*[@class="t-16 t-black t-normal inline-block"]/text()').extract_first().strip()

    linkedin_url = driver.current_url

    old_position = sel.xpath('//*[@class="pv-entity__summary-info pv-entity__summary-info--background-section mb2"]/*[@class="t-16 t-black t-bold"]/text()').extract()

    old_company_1 = sel.xpath('//*[@class="pv-entity__summary-info pv-entity__summary-info--background-section "]/*[@class="pv-entity__secondary-title t-14 t-black t-normal"]/text()').extract()

    old_company_2 = sel.xpath('//*[@class="pv-entity__company-summary-info"]/*[@class="t-16 t-black t-bold"]/span[2]/text()').extract()

    number_of_years_1 = sel.xpath('//*[@class="pv-entity__summary-info pv-entity__summary-info--background-section "]/*[@class="display-flex"]/*[@class="t-14 t-black--light t-normal"]/*[@class="pv-entity__bullet-item-v2"]/text()').extract()

    number_of_years_2 = sel.xpath('//*[@class="pv-entity__company-summary-info"]/*[@class="t-14 t-black t-normal"]/span[2]/text()').extract()

    job_description = sel.xpath('//*[@class="pv-entity__description t-14 t-black t-normal ember-view"]/span/text()').extract()

    self_description = sel.xpath('//*[@class="pv-about__summary-text mt4 t-14 ember-view"]/span/text()').extract()



    name = validate_field(name)
    job_title = validate_field(job_title)
    location = validate_field(location)
    linkedin_url = validate_field(linkedin_url)
    old_position = validate_field(old_position)
    old_company_1 = validate_field(old_company_1)
    old_company_2 = validate_field(old_company_2)
    number_of_years_1 = validate_field(number_of_years_1)
    number_of_years_2 = validate_field(number_of_years_2)
    job_description = validate_field(job_description)
    self_description = validate_field(self_description)

    print('\n')
    print('Name: ' + name)
    print('Job Title: ' + job_title)
    print('Location: ' + location)
    print('URL: ' + linkedin_url)
    print('\n')

    writer.writerow([name,
                     job_title,
                     location,
                     linkedin_url,
                     old_position,
                     old_company_1,
                     old_company_2,
                     number_of_years_1,
                     number_of_years_2,
                     job_description,
                     self_description])

driver.quit()
