[![Python application](https://github.com/valerap97/py-test/actions/workflows/python-app.yml/badge.svg)](https://github.com/valerap97/py-test/actions/workflows/python-app.yml)
[![Coverage Status](https://coveralls.io/repos/github/valerap97/py-test/badge.svg?branch=main)](https://coveralls.io/github/valerap97/py-test?branch=main)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=valerap97_py-test&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=valerap97_py-test)
[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=valerap97_py-test)](https://sonarcloud.io/summary/new_code?id=valerap97_py-test)
[![SonarCloud](https://sonarcloud.io/images/project_badges/sonarcloud-white.svg)](https://sonarcloud.io/summary/new_code?id=valerap97_py-test)

# План тестирования:

Тест А1: Положительный - Поиск комикса по названию

    Начальное состояние: Программа запущена, пользовательский интерфейс ожидает ввода.
    Действие: Пользователь запрашивает поиск комиксов по названию "X-Men" через метод get_comics_by_title класса ComicShop.
    Ожидаемый результат: Возвращается непустой список экземпляров комиксов с названием "X-Men".

Тест А2: Положительный - Применение скидки на комикс

    Начальное состояние: Начальные данные загружены в систему, скидки отсутствуют.
    Действие: Создание экземпляра класса DiscountManager и вызов метода define_discount для установки скидки 25% на комикс с ISBN "11111".
    Ожидаемый результат: Скидка применена успешно, цена комикса снижается с 7.99 до 5.99.

Тест А3: Негативный - Добавление комикса с дублирующим ISBN

    Начальное состояние: В системе уже есть комикс с ISBN "12345".
    Действие: Попытка добавления второго комикса с тем же ISBN "12345" с использованием метода add_comic класса ComicShop.
    Ожидаемый результат: Выдача ошибки с кодом DuplicateISBNError, указывающей на дублирование ISBN.

Тест А4: Негативный - Попытка продать комикс, которого нет в наличии

    Начальное состояние: Комикс с указанным ISBN отсутствует в инвентаре или его количество равно нулю.
    Действие: Попытка продажи комикса с нулевым остатком с использованием метода sell_comic класса ComicShop.
    Ожидаемый результат: Выдача ошибки с кодом ComicNotInStockError, указывающей на отсутствие комикса на складе.


# Блочное тестирование
Блочное тестирование
<ol> 
	<li> 
	<h4>Тест Б1 (положительный)</h4> 
		<ul> 
		<li>Название: Создание объекта ComicBook</li> 
		<li>Действие: Инициализация экземпляра класса ComicBook с валидными параметрами</li> 
		<li>Ожидаемый результат: Создан объект с заданными свойствами</li> 
		</ul> 
	</li> 
	<li> 
	<h4>Тест Б2 (положительный)</h4> 
	<ul> 
		<li>Название: Обновление количества комиксов в инвентаре</li> 
		<li>Действие: Вызов метода update_inventory с положительным числом</li> 
		<li>Ожидаемый результат: Количество в инвентаре обновлено</li> 
	</ul> 
	</li> 
	<li> 
	<h4>Тест Б3 (негативный)</h4> 
	<ul> 
		<li>Название: Попытка установить отрицательное количество комиксов</li> <li>Действие: Инициализация экземпляра класса ComicBook с отрицательным значением количества</li> 
		<li>Ожидаемый результат: Выбрасывается исключение NegativeInventoryError</li> 
	</ul> 
	</li>  
</ol>
Интеграционное тестирование
<ol> 
	<li> 
	<h4>Тест И1 (положительный)</h4> 
	<ul> 
		<li>Название: Проверка взаимодействия классов ComicShop и ComicBook</li> 
		<li>Действие: Добавление экземпляра ComicBook в ComicShop и его последующая продажа</li> 
		<li>Ожидаемый результат: Количество в инвентаре уменьшено, продажа выполнена успешно</li> 
	</ul> </li> 
	<li> 
	<h4>Тест И2 (положительный)</h4> 
		<ul> 
		<li>Название: Взаимодействие классов ComicShop и DiscountManager</li> 
		<li>Действие: Применение скидки через DiscountManager к комиксу в ComicShop</li> 
		<li>Ожидаемый результат: Цена комикса уменьшена согласно скидке</li> 
		</ul> 
	</li> <!-- Дополнительные интеграционные тесты по аналогии --> 
</ol>
