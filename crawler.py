## Organizador de cursos FIUBA - CSV Crawler
import csv
from models import Curso


def parse_row(row):
    return Curso(row[0], # Codigo
                 row[1],
                 row[2])


if __name__ == '__main__':

    cursos = []

    with open('materias.csv', 'rt', encoding="UTF-8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if str(row[0]).isdigit():
                print(row)
                cursos.append(parse_row(row))

    print(cursos)
