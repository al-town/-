per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('Enter the amount you would like to deposit: '))
deposit = [money*per_cent['ТКБ'], money*per_cent['СКБ'], money*per_cent['ВТБ'], money*per_cent['СБЕР']]
print('The maximum amount you can earn is', round(max(deposit), 2))
