import re


def List_for_dates(all):
    month_to_number = {
        'January': 1,
        'February': 2,
        'March': 3,
        'April': 4,
        'May': 5,
        'June': 6,
        'July': 7,
        'August': 8,
        'September': 9,
        'October': 10,
        'November': 11,
        'December': 12}
    for i in range(len(all)):
        all[i] = all[i].replace('-', ' ')

    for i in range(len(all)):
        p = all[i].split(' ')
        month_name = p[0]
        date = p[1]
        year = p[2]
        month_no = [v for k, v in month_to_number.items(
        ) if month_name.lower() in k.lower()][0]
        final_date = "{}/{}/{}".format(month_no, date, year)
        all[i] = final_date
    return all


# TYPE TEXT 1 HERE
text_1 = """   """
# TYPE TEXT 2 HERE
text_2 = """  """
dates_list_1 = re.findall(r"[ADFJMNOS]\w*.[\d]{1,2}.[\d]{4}", text_2)
dates_list_2 = re.findall(r"\d{1,2}/\d{1,2}/\d{4}", text_1)
print(dates_list_2)
print(List_for_dates(dates_list_1) == dates_list_2)
