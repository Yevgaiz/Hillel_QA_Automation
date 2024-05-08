month_order = {
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4,
    'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8,
    'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
}

dates = ['1-Jan', '31-Dec', '12-Jan', '12-Apr', '13-Apr', '14-Dec', '10-Feb', '25-Dec', '05-Mar']

sorted_dates = sorted(dates, key=lambda x: (month_order[x[-3:]], int(x.split("-")[0])))

print(sorted_dates)





