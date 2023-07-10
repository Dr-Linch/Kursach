from utils import utils


def test_get_data():
    assert isinstance(utils.get_data('operations.json'), list)
    assert utils.get_data(0) == 0


def test_get_filtered_data():
    assert len(utils.get_filtered_data([{'state': 'EXECUTED'}])) == 1
    assert len(utils.get_filtered_data([{'state': 'EXECUTED'}, {'state': 'CANCLED'}])) == 1


def test_get_sorted_data():
    print(utils.get_sorted_data([{"date": "2020-08-26T10:50:58.294041"}, {"date": "2019-07-03T18:35:29.512364"}, {"date": "2021-07-03T18:35:29.512364"}])) == [{'date': '2021-07-03T18:35:29.512364'}, {'date': '2020-08-26T10:50:58.294041'}, {'date': '2019-07-03T18:35:29.512364'}]


def test_get_formate_data():
    print(utils.get_formate_data([
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }])) == ('26.08.2019 Перевод организации'
          'Maestro 1596 37** **** 5199 -> Счет **9589'
          '31957.58 руб.')

