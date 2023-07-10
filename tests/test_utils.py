from utils import utils

def test_get_data():
    """
    Проверка функции get_data
    """
    assert isinstance(utils.get_data('operations.json'), list)


def test_get_filtered_data():
    """
        Проверка функции get_filtered_data
        """
    assert len(utils.get_filtered_data([{'state':'EXECUTED'}])) == 1


def test_get_sorted_data():
     """
     Проверка функции get_sorted_data
     """
     assert utils.get_sorted_data([{'date':"2020-08-26T10:50:58.294041"}, {'date':"2019-08-26T10:50:58.294041"}, {'date':"2021-08-26T10:50:58.294041"}]) == [{'date': '2021-08-26T10:50:58.294041'}, {'date': '2020-08-26T10:50:58.294041'}, {'date': '2019-08-26T10:50:58.294041'}]


def test_get_formate_data():
    """
    Проверка функции get_formate_data
    """
    assert utils.get_formate_data([
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
  }]) == ("26.08.2019 Перевод организации\n"
            "Maestro 1596 37** **** 5199 -> Счет **9589\n"
            "31957.58 руб.\n")
