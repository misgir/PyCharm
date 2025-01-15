from lesson4.string_utils import StringUtils

stringUtils = StringUtils()


def test_capitilize_p():
    # позитивные проверки
    assert stringUtils.capitilize('skypro') == ('Skypro')
    assert stringUtils.capitilize('hello, world') == 'Hello, world'
    assert stringUtils.capitilize('текст') == 'Текст'


def test_capitilize_n():
    # негативные проверки
    assert stringUtils.capitilize('') == ''
    assert stringUtils.capitilize('.') == '.'
    assert stringUtils.capitilize('123') == '123'


def test_trim_p():
    # позитивные проверки
    assert stringUtils.trim(' Hello') == 'Hello'
    assert stringUtils.trim(' Привет') == 'Привет'
    assert stringUtils.trim(' 123') == '123'


def  test_trim_n():
    # негативные проверки
    assert stringUtils.trim('') == ''
    assert stringUtils.trim(' ') == ''
    assert stringUtils.trim(' .') == '.'


def test_to_list_p():
   # позитивные проверки
   assert stringUtils.to_list('один,два,три', ',') == ["один","два","три"]
   assert stringUtils.to_list('один:два:три',':') == ["один", "два", "три"]
   assert stringUtils.to_list('1,2,3',',') == ["1", "2", "3"]


def test_to_list_n():
   # негативные проверки
   assert stringUtils.to_list('') == []
   assert stringUtils.to_list('.') == ["."]


def test_contains_p():
   # позитивные проверки
   assert stringUtils.contains('Hello', 'H') == True
   assert stringUtils.contains('Hello', 'P') == False
   assert stringUtils.contains('Привет', 'П') == True
   assert stringUtils.contains('Привет', 'Ч') == False


def test_contains_n():
   # негативные проверки
   assert stringUtils.contains('.', '') == False
   assert stringUtils.contains('Hello', '') == False
   assert stringUtils.contains('', 'П') == False


def test_delete_symbol_p():
    # позитивные проверки
    assert stringUtils.delete_symbol('Hello','H') == 'ello'
    assert stringUtils.delete_symbol('Hello123', '123') == 'Hello'
    assert stringUtils.delete_symbol('Привет', 'т') == 'Приве'


def test_delete_symbol_n():
    # негативные проверки
    assert stringUtils.delete_symbol('Hello', '') == ''
    assert stringUtils.delete_symbol('', '123') == ''
    assert stringUtils.delete_symbol('', '') == ''


def test_starts_with_p():
    # позитивные проверки
    assert stringUtils.starts_with('Hello','H') == True
    assert stringUtils.starts_with('Привет','П') == True
    assert stringUtils.starts_with('Hello', 'Y') == False


def test_starts_with_n():
    # негативыне проверки
    assert stringUtils.starts_with('','') == False
    assert stringUtils.starts_with('123', '') == False
    assert stringUtils.starts_with('Hit', '') == False


def test_end_with_p():
    # позитивные проверки
    assert stringUtils.end_with('Helllo','H') == True
    assert stringUtils.end_with('Привет','П') == False
    assert stringUtils.end_with('hit123', '123') == True


def test_end_with_n():
    # негативные проверки
    assert stringUtils.end_with('', '') == False
    assert stringUtils.end_with('123', '123') == False
    assert stringUtils.end_with('.', '') == False


def test_is_empty_p():
    # позитивные проверки
    assert stringUtils.is_empty("") == True
    assert stringUtils.is_empty(" ") == True
    assert stringUtils.is_empty("Hello") == False
    assert stringUtils.is_empty("123") == False


def test_is_empty_n():
    #  негативные проверки
    assert stringUtils.is_empty("123") == True
    assert stringUtils.is_empty(" ") == False
    assert stringUtils.is_empty("Helllo") == True


def list_to_string_p():
    # позитивные проверки
    assert stringUtils.list_to_string(['Pick','ip'], '!') == 'Pick!ip'
    assert stringUtils.list_to_string(['Sky','Pro']) == 'Sky,Pro'
    assert stringUtils.list_to_string(['Хай','Тэк'] , '-' ) == 'Хай-Тэк'


def  list_to_string_n():
    # негатвные проверки
    assert stringUtils.list_to_string(['',''], '') == ''
    assert stringUtils.list_to_string('.', '') == ''
    assert stringUtils.list_to_string('123', '') == '123'
