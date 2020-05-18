try:
    with open('temper.stat', 'r') as r, open('temper.result', 'w', encoding='utf-8') as w:
        temps =list(map(lambda x: float(x.strip()), r.readlines()))
        w.write("Максимальная температура: " +
                     str(max(temps)) +"\n")
        w.write("Минимальная температура: " +
                     str(min(temps)) + "\n")
        w.write("Средняя температура: " +
                     str("%.2f" % (sum(temps)/len(temps))) + "\n")
        w.write("Медианная температура: " +
                     str(sorted(temps)[len(temps)//2]) + "\n")
        w.write("Количество уникальных температур: " +
                     str(len(set(temps))))

except Exception as err:
    print(err)
