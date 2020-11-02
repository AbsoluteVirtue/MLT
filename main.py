import data
import xlwt


if __name__ == '__main__':

    book = xlwt.Workbook()
    sheet = book.add_sheet("Composers")

    sheet.write(0, 0, "file")
    sheet.write(0, 1, "composer")
    sheet.write(0, 2, "title")
    sheet.write(0, 3, "genre")
    sheet.write(0, 4, "period")

    i = 1
    for comp in data.composers_data():
        for track in comp['tracks']:
            sheet.row(i).write(0, track['filename'])
            sheet.row(i).write(1, comp['name'])
            sheet.row(i).write(2, track['title'])
            sheet.row(i).write(3, track['genre'])
            sheet.row(i).write(4, track['period'])

            i += 1

    book.save("composers.xls")
