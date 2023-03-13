# ========================== Начало =========================

# Программная ошибка (жарг. баг) — означает ошибку в программе или в системе, из-за которой программа выдает
# неожиданное поведение и, как следствие, результат. Большинство программных ошибок возникают из-за ошибок команды
# разработки.



# Тестирование программного обеспечения — процесс исследования, испытания программного продукта, имеющий своей целью
# проверку соответствия между реальным поведением программы и её ожидаемым поведением на конечном наборе
# тестов, выбранных определённым образом. Тестировщик, в свою очередь, моделирует различные ситуации (тесты), которые
# могут возникнуть в процессе использования программы, чтобы разработчики смогли исправить обнаруженные баги.



# Мы воспользуемся популярной техникой тест-дизайна, позволяющей быстро и качественно проверить что-либо:
#
# - Техника выделения классов эквивалентности и граничных значений позволяет уйти от дублирующих проверок.
# Следовательно, мы сократим количество однотипных тестов.
#
# - Классы эквивалентности — это разбиение функционала на наборы данных, которые ведут себя в пределах этих наборов
# одинаково. Например, дети, взрослые и пенсионеры - это все классы эквивалентности.
#
# - Анализ граничных значений — это метод, который улучшает разделение классов эквивалентности. В нашем случае, самые
# близкие значения — это 17 и 66.



# Чек-лист– это список, содержащий ряд необходимых проверок во время тестирования программного продукта. Отмечая пункты
# списка, команда или один тестировщик могут узнать о текущем состоянии выполненной работы и о качестве продукта.

# ===================================================================



# ========================== Теория ==============================


# ------------------------ Тестирование и качество ------------------------

# Качество программного обеспечения — способность программного продукта при заданных условиях удовлетворять
# установленным или предполагаемым потребностям.



# Quality assurance, Quality control и Testing. Who is who?

# 1. Testing (тестирование) — самый первый уровень. Это проверка программного продукта на соответствие требованиям
# этого продукта.

# То есть ожидаемый результат и фактический результат совпадают, и это тот минимум, без которого нельзя выпускать
# продукт. Возьмем для примера тестирование в интернет—магазине кнопки «Купить».
# В процесс тестирования будет входить проверка функционала и сверка с макетом. Кнопка нажимается, открывается нужное
# окно, кнопка находится в правом нижнем углу, окрашена в зеленый цвет и т.д.


# 2. QC (Quality Control, контроль качества) — второй уровень, включает в себя тестирование и контроль за соответствием
# заранее согласованному уровню качества продукта и готовность к выпуску продукта в продакшн.

# Основная задача контроля качества — предоставить объективную картину того, что происходит с качеством продукта на
# разных этапах разработки. Управление качеством (Quality control) — часть менеджмента качества, направленная на
# выполнение требований к качеству. Это означает, что необходимо выполнять требования, а как это будет
# происходить, зависит от корпоративной культуры.
# Вернемся к интернет-магазину. QC даст отмашку на релиз, если не заполнена страница благодарностей, на которую можно
# перейти из футера (подвала) сайта. Или, например, не даст добро, если страница благодарностей заполнена, а каталог
# пустой.


# 3. QA (Quality Assurance, обеспечение качества) — часть обеспечения согласованного уровня качества продукта. Это уже
# проактивная работа, т.к. основная задача обеспечения качества — это выстроить систему, которая будет работать на
# качество продукта, чтобы при тестировании количество дефектов было минимальным.
#
# В зависимости от специфики проекта сюда может входить тестирование документации, ревью кода на соответствие
# стандартам, внедрение каких-то методик по работе с качеством.
# Обеспечение качества (Quality Assurance) — часть менеджмента качества, направленная на создание уверенности, что
# требования к качеству будут выполнены.

# При более полном понимании можно обратиться к ГОСТ Р ИСО 9000-2015

# -------------------------------------------------------------------------------


# ----------------------------

