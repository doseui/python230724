# import requests
# from bs4 import BeautifulSoup

# def crawl_blog_info(search_keyword):
#     url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}"
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, "html.parser")

#     blog_info_list = []

#     blog_items = soup.find_all("li", {"class": "bx _svp_item"})
#     for item in blog_items:
#         blog_title = item.find("a", {"class": "total_tit"}).text
#         blog_address = item.find("a", {"class": "total_tit"})["href"]
#         blog_date = item.find("span", {"class": "sub_time"}).text

#         blog_info = {
#             "blog_title": blog_title,
#             "blog_address": blog_address,
#             "blog_date": blog_date
#         }
#         blog_info_list.append(blog_info)

#     return blog_info_list

# if __name__ == "__main__":
#     search_keyword = "%EB%A7%A5%EB%B6%81%EC%97%90%EC%96%B4"
#     results = crawl_blog_info(search_keyword)
#     for result in results:
#         print("Title:", result["blog_title"])
#         print("Address:", result["blog_address"])
#         print("Date:", result["blog_date"])
#         print("----------------------")




##################################################
import os
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

def crawl_blog_info(search_keyword):
    url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    blog_info_list = []

    blog_items = soup.find_all("li", {"class": "bx _svp_item"})
    for item in blog_items:
        blog_title = item.find("a", {"class": "total_tit"}).text
        blog_address = item.find("a", {"class": "total_tit"})["href"]
        blog_date = item.find("span", {"class": "sub_time"}).text

        blog_info = {
            "blog_title": blog_title,
            "blog_address": blog_address,
            "blog_date": blog_date
        }
        blog_info_list.append(blog_info)

    return blog_info_list

def save_to_excel(data, filepath):
    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Blog_Info"

    # Write header row
    worksheet.append(["Title", "Address", "Date"])

    # Write data to the worksheet
    for item in data:
        worksheet.append([item["blog_title"], item["blog_address"], item["blog_date"]])

    workbook.save(filepath)

if __name__ == "__main__":
    search_keyword = "%EB%A7%A5%EB%B6%81%EC%97%90%EC%96%B4"
    results = crawl_blog_info(search_keyword)

    # Set the file path for saving the Excel file
    excel_file_path = os.path.join("c:\\work", "blog_info.xlsx")

    # Save the data to the Excel file
    save_to_excel(results, excel_file_path)

    print(f"Data saved to {excel_file_path}")