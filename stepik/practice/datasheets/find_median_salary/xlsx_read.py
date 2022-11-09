import openpyxl


def reader(f_name: str = 'data.xlsx') -> openpyxl.load_workbook:
    wb = openpyxl.load_workbook(f_name)
    return wb


def analyse_cities_salaries(wb: openpyxl.load_workbook) -> str:
    sheet = wb.active
    rows = sheet.max_row
    columns = sheet.max_column
    cities = {}
    for i in range(2, rows + 1):
        q = sheet.cell(row=i, column=1).value
        cities[q] = cities.setdefault(q, [])
        for j in range(2, columns + 1):
            cities[q].append(sheet.cell(row=i, column=j).value)
        cities[q].sort()
    return max(cities.items(), key=lambda x: x[1][3])[0]


def analyse_prof_salaries(wb: openpyxl.load_workbook) -> str:
    sheet = wb.active
    rows = sheet.max_row
    columns = sheet.max_column
    professions = {}
    for j in range(2, columns + 1):
        q = sheet.cell(row=1, column=j).value
        professions[q] = professions.setdefault(q, [])
        for i in range(2, rows):
            professions[q].append(sheet.cell(row=i, column=j).value)
    return max(professions.items(), key=lambda x: sum(x[1]) / len(x[1]))[0]


def main():
    data = reader()
    print(analyse_prof_salaries(data))
    print(analyse_cities_salaries(data))


if __name__ == '__main__':
    main()
