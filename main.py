from Parser import *

run = True

data = Parcer()

print("> ", end = "")
while run:
    text = input()
    if text == "-h" or text == "--help":
        print("Программа для получения цен популярных криптовалют.")
        print("Для загрузки используйте load.")
        print("Для отображения загруженных данных используйте read.")
        print("Используйте флаг -q или --quit для завершения работы программы.")
        print("Для вызова справки используйте -h или --help")
    elif text == "-q" or text == "--quit":
        print("Завершение работы.")
        run = False
    elif text == "load":
        print("Загрузка данных.")
        data.load()
        print("Загрузка завершена.")
    elif text == "read":
        for i in range(0, len(data.name)):
            print(i + 1, "\t", data.name[i], "\t", data.price[i], "\t", data.price_ch[i])
    elif text == "url":
        print(data.url)
    else:
        print("Данной команды не обнаружено. Для вызова справки используйте флаг -h")

    if run:
        print("> ", end = "")
        
