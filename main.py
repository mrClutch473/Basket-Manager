# -*- coding: utf-8 -*-
import random
import time

import os
from pydoc_data.topics import topics

import pygame
from pygame import USEREVENT


image_path_for_android = '/data/data/org.bsktMngr.bsktMngr/files/app/'

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
screen = pygame.display.set_mode((1024, 1024), flags=pygame.NOFRAME) #, flags=pygame.NOFRAME
#screen = pygame.display.set_mode((1200, 990), flags=pygame.NOFRAME) #

pygame.display.set_caption("BaskeT_ManageR")
iconM = pygame.image.load('imges/bsket_icon.png').convert_alpha()
pygame.display.set_icon(iconM)

#variables
game_mode = -1
game_plot = 1

namesArr = ("Эндрю Смит", "Майкл Джонсон", "Кристофер Уилсон", "Дэвид Браун", "Джеймс Джонс", "Джошуа Мартин", "Роберт Ли", "Итан Тейлор", "Бенжamин Гарбус", "Гарретт Уайт", "Логан Мартинeз", "Майкл Кларк", "Гарретт Хантер", "Чарльз Линч", "Джозеф Сандерс", "Кевин Риверс", "Уильям Паттерсон", "Дональд Фостер", "Лиам Лонг", "Оливер Тейлор", "Антонио Питерсон", "Натан Мур", "Филипп Диксон", "Закари Хейс", "Тимоти Чейз", "Дерек Леман", "Кайл Стоун", "Сет Говард", "Трейси Мэлоун", "Алан Мейсон", "Роберт Фишер", "Честер Бёрнс", "Эммет Гриффин", "Брэндон Хэллоуэлл", "Дилан Мортон", "Эдвард Розен", "Алан Кук", "Гарри Симмс", "Сэм Келли", "Наоми Джером", "Винсент Карпентер", "Роберто Браун", "Стэнли Джереми", "Фрэнк Дрейк", "Джереми Стоун", "Джосс Диксон", "Саймон Армстронг", "Брайан Шиппер", "Тревор Бойл", "Гарет Адамс", "Глаффер Эванс", "Даллас Хопкинс", "Джонни Мартинес", "Сидни Мартин", "Мерфи Стоуни", "Джимми Хаверэн", "Кингсли Браун", "Джексон Озер", "Энн Мур", "Тэри кепонд", "Гейб Хотели", "Блэз Уинтер", "Патрик Оваль", "Ральф Кинг", "Грег Миллер", "Морис Рейн", "Олдрик Грабов", "Эрик Келли", "Томас Браун", "Крис Генри", "Трэвис Мун", "Николь Дики", "Джон Мэссей", "Гарри Линч", "Брэк Мальчик", "Лоренцо Типпет", "Шотт Мартин", "Альберт Монтгомери", "Джонни Блэк", "Майкл Боуер", "Стефан Шеридэн", "Корм Блэк", "Сквозляк Вогл", "Лерой Симон", "Уилберт Вест", "Стэнли Коваль", "Туфал Бах", "Тед Блэтчли", "Керни Паркер", "Ларри Гайтер", "Шепп Сигал", "Коул Норрис", "Линн Манс", "Тони Фостер", "Марио Корбин", "Долорес Бенсон", "Райан Хейл", "Митчелл Кент", "Гарри тээрэм", "Ужлер Испити", "Тим Гетси", "Гленн Габли", "Митч Рэнит", "Эрни Бодьяк", "Донн Ларсен", "Алан Трейси", "Лерoy Смит", "Ли Брэдли", "Хайден О’то", "Роланд Линч", "Ника Кэри", "Тим Ивейл", "Тельма Хосре", "Гас Мееры", "Таня О’Мэри", "Джексон Райт", "Авери Рэй", "Ллойд О’Тис", "Дэлл Браун", "Агостино Ауле", "Кимбер Кармен", "Глин Колитти", "Энтони Кэри", "Бенджамин Хостей", "Майкл Смит", "Оззи Ролважа", "Эмиль Гаваль", "Фред Уотс", "Ларри Верн", "Роберт Скиммей", "Ноah Уонг", "Патрик Бэнжам", "Райан Тейлор", "Эдгар Ноу", "Бен Смит", "Тим Тосер", "Джаред Доу", "Рональд Кортни", "Омар Каппи", "Дервин Монтгомери", "Деннис Хасгард", "Александр Тейлор", "Ченсел Ворени", "Донни Льюис", "Шон Хан", "Джозеф Гамус", "Пол Риккерт", "Кен Ворожи", "Корин Бенет", "Метт Дики", "Эвант Дорнад", "Аарон Бенджамин", "Роберт Хэйс", "Эксперт Эдвардс", "Джейк Дизель", "Уолтер Недо", "Эрик Туппер", "Джорджсон Браун", "Клер Крейг", "Гарри Пэттерсон", "Бенни Уолли", "Тони Мартин", "Эджи Хрущев", "Ник Третьяков", "Ларри Хаббард", "Эдриан Ву", "Бен Саймон", "Майкл Хиер", "Рэй Мэрил", "Роб Диктат", "Аможер Ван", "Бен Джонсон", "Гост Ким", "Леон Кук", "Райан Серчев", "Джордан Мартин", "Терри Срезин", "Лонни Мартинес", "Райан Бороз", "Дмирал Халил", "Майк Чарльз", "Тим Браун", "Богдан Якушен")

random_team_names = ("Летящие Совы", "Огненные Соколы", "Стальные Тигры", "Космические Дельфины", "Золотые Орлы", "Неоновые Молнии", "Супер Крабсы", "Ледяные Драконы", "Мифические Единороги", "Лунные Хищники", "Магические Львы", "Буревестники Небес", "Снежные Химеры", "Пиратские Корабли", "Теневые Призраки", "Дикие Вулканы", "Солнечные Лыжи", "Танцующие Фламинго", "Холодные Актеры", "Бурные Ветра", "Смелые Ракеты", "Дельтапланы Судьбы", "Защитники Мира", "Боевики Картелей", "Светящиеся Кометы", "Исполинские Помидоры", "Звёздные Грифоны", "Гигантские Пингвины", "Танцующие Надежды", "Энергия Солнца", "Алмазные Воины", "Теневые Сверкания", "Безумные Дизайнеры", "Летучие Мыши", "Бравые Мысли", "Волшебные Листья", "Бурные Фьельды", "Шумные Эликсиры", "Странники Звёзд", "НеоноваяЭпопея", "Технические Машины", "Ультра Чудовища", "Ракеты-Гиганты", "Золотые Густоты", "Казино Птиц", "Секретные Ходы", "Лучи Света", "Лунные Небоскрёбы", "Небесные Корабли", "Вихревые Бойцы", "Огненные Вороны", "Цирковые Слоны", "Безумцы Потока", "Сказочные Рыцари", "Карнавальные Жирафы", "Прыгающие Фьельды", "Сиреневые Буревестники", "Эхо Страха", "Снежные Ниндзі", "Гнездовье Алхимиков", "Бурлящие Реки", "Ледяные Гиганты", "Заряженные Щелкуны", "Фантазийные Носороги", "Космические Параллели", "Вдохновленные Венеры", "Царственные Клубы", "Громовая Атака", "Волшебные Ослепления", "Радужные Океаны", "Воробьиные Замыслы", "Саблезубые Бандиты", "Луна и Солнце", "Медные Сферы", "Драгоценные Яйца", "Песни Севера", "Космические Паутины", "Сияющие Звезды", "Завоеватели Вселенной", "Шепчущие Тени", "Тайные Нападения", "Невидимые Рыцари", "Скрепленные Мечты", "Искрометная Сила", "Лавровый Плод", "Скаты-Друзья", "Искорки Надежды", "Морские Львы", "Галактические Полководцы", "Трясущиеся Ручьи", "Эфирные Узоры", "Планетные Защитники", "Всплески Эмоций", "Облачные Ремесленники", "Загадочные Дороги", "Танцующие Тонны", "Светящиеся Растения", "Серебряные Зебры", "Огненные Самолёты", "Морские Вертолеты", "Древесные Друзья", "Тундровые Боги", "Заброшенные Сады", "Тепло Доброты", "Ночные Операции", "Ветры Перемен", "Радужные Барабаны")

random_team_managers = ("Алексей Тимофеев", "Брайан Мартинов", "София Уилкинсон", "Тимур Далбеков", "Роберт Ким", "Олеся Каверина", "Майкл Скоморов", "Виктория Невская", "Алан Ренар", "Николай Чернов", "Эмили Смит", "Дмитрий Кишиневский", "Сара Браун", "Антон Розанов", "Лора Белль", "Игорь Селиванов", "Кристина Ламберти", "Артур Блом", "Анастасия Варламова", "Стивен Гибсон", "Валентина Шмидт", "Кирилл Нестеров", "Люси Левин", "Денис Петров", "Жасмин Фарид", "Михаил Воробьев", "Элизабета Синиця", "Леонардо Мартинез", "Анна Зайцев", "Фёдор Кудрявцев", "Оливия Парк", "Григорий Степанов", "Татьяна Мороз", "Никита Фенюшкин", "Лиам Уотсон", "Полина Мартынюк", "Семан Мельчаков", "Харрисон Уайз", "Екатерина Ремезова", "Тимофей Ильин", "Зои Бёрнс", "Данила Кашаев", "Лука Мчедлишвили", "Эмилия Гонзалес", "Вадим Кифаров", "Людмила Панова", "Марк Бэрд", "Роман Ярушин", "Эйми Кира", "Василий Петренко", "Жюли Верно", "Кирилл Бочаров", "Алиса Горовая", "Николас Тейлор", "Мирослава Прокофьева", "Сэм Розен", "Данила Ларионов", "Ким Тэхён", "Артемий Тихонов", "Агата Низовка", "Остин Браун", "Юлия Коррель", "Геннадий Кузьмич", "Кристофер Хантер", "Евгения Лауренс", "Александр Бенедиктов", "Сидней Грант", "Мария Крепкая", "Эвана Сачков", "Арсений Чекмагушев", "Эмилиас Кочетков", "Захар Глушков", "Дональд Кайл", "Тимур Крутов", "Александра Досаждева", "Ноа Хан", "Вениамин Коновалов", "Мелисса Тиринг", "Дамир Шарипов", "Жанна Чиркова", "Лорен Дженкинс", "Филипп Макаров", "Элеонора Сивкова", "Джек Саймон", "Станислав Синичкин", "Полина Корнеева", "Оскар Краузе", "Азалия Кудрявцева", "Денис Хосайнов", "Ксения Ларина", "Иван Чуднов", "Кристоф Сидоренко", "Дин Фролов", "Олеся Печенкина", "Эндрю Смит", "Майкл Джонсон", "Кристофер Уилсон", "Дэвид Браун", "Джеймс Джонс", "Джошуа Мартин", "Роберт Ли", "Итан Тейлор", "Бенжamин Гарбус", "Гарретт Уайт", "Логан Мартинeз", "Майкл Кларк", "Гарретт Хантер", "Чарльз Линч", "Джозеф Сандерс", "Кевин Риверс", "Уильям Паттерсон", "Дональд Фостер", "Лиам Лонг", "Оливер Тейлор", "Антонио Питерсон", "Натан Мур", "Филипп Диксон", "Закари Хейс", "Тимоти Чейз", "Дерек Леман", "Кайл Стоун", "Сет Говард", "Трейси Мэлоун", "Алан Мейсон", "Роберт Фишер", "Честер Бёрнс", "Эммет Гриффин", "Брэндон Хэллоуэлл", "Дилан Мортон", "Эдвард Розен", "Алан Кук", "Гарри Симмс", "Сэм Келли", "Наоми Джером", "Винсент Карпентер", "Роберто Браун", "Стэнли Джереми", "Фрэнк Дрейк", "Джереми Стоун", "Джосс Диксон", "Саймон Армстронг", "Брайан Шиппер", "Тревор Бойл", "Гарет Адамс", "Глаффер Эванс", "Даллас Хопкинс", "Джонни Мартинес", "Сидни Мартин", "Мерфи Стоуни", "Джимми Хаверэн", "Кингсли Браун", "Джексон Озер", "Энн Мур", "Тэри кепонд", "Гейб Хотели", "Блэз Уинтер", "Патрик Оваль", "Ральф Кинг", "Грег Миллер", "Морис Рейн", "Олдрик Грабов", "Эрик Келли", "Томас Браун", "Крис Генри", "Трэвис Мун", "Николь Дики", "Джон Мэссей", "Гарри Линч", "Брэк Мальчик", "Лоренцо Типпет", "Шотт Мартин", "Альберт Монтгомери", "Джонни Блэк", "Майкл Боуер", "Стефан Шеридэн", "Корм Блэк", "Сквозляк Вогл", "Лерой Симон", "Уилберт Вест", "Стэнли Коваль", "Туфал Бах", "Тед Блэтчли", "Керни Паркер", "Ларри Гайтер", "Шепп Сигал", "Коул Норрис", "Линн Манс", "Тони Фостер", "Марио Корбин", "Долорес Бенсон", "Райан Хейл", "Митчелл Кент", "Гарри тээрэм", "Ужлер Испити", "Тим Гетси", "Гленн Габли", "Митч Рэнит", "Эрни Бодьяк", "Донн Ларсен", "Алан Трейси", "Лерoy Смит", "Ли Брэдли", "Хайден О’то", "Роланд Линч", "Ника Кэри", "Тим Ивейл", "Тельма Хосре", "Гас Мееры", "Таня О’Мэри", "Джексон Райт", "Авери Рэй", "Ллойд О’Тис", "Дэлл Браун", "Агостино Ауле", "Кимбер Кармен", "Глин Колитти", "Энтони Кэри", "Бенджамин Хостей", "Майкл Смит", "Оззи Ролважа", "Эмиль Гаваль", "Фред Уотс", "Ларри Верн", "Роберт Скиммей", "Ноah Уонг", "Патрик Бэнжам", "Райан Тейлор", "Эдгар Ноу", "Бен Смит", "Тим Тосер", "Джаред Доу", "Рональд Кортни", "Омар Каппи", "Дервин Монтгомери", "Деннис Хасгард", "Александр Тейлор", "Ченсел Ворени", "Донни Льюис", "Шон Хан", "Джозеф Гамус", "Пол Риккерт", "Кен Ворожи", "Корин Бенет", "Метт Дики", "Эвант Дорнад", "Аарон Бенджамин", "Роберт Хэйс", "Эксперт Эдвардс", "Джейк Дизель", "Уолтер Недо", "Эрик Туппер", "Джорджсон Браун", "Клер Крейг", "Гарри Пэттерсон", "Бенни Уолли", "Тони Мартин", "Эджи Хрущев", "Ник Третьяков", "Ларри Хаббард", "Эдриан Ву", "Бен Саймон", "Майкл Хиер", "Рэй Мэрил", "Роб Диктат", "Аможер Ван", "Бен Джонсон", "Гост Ким", "Леон Кук", "Райан Серчев", "Джордан Мартин", "Терри Срезин", "Лонни Мартинес", "Райан Бороз", "Дмирал Халил", "Майк Чарльз", "Тим Браун", "Богдан Якушен")

posesArr = ("PG", "SG", "SF", "PF", "C")

end_time_l = 5
end_time_l_gm3 = 4.3

my_teamArr_pos = [0] * 6
my_teamArr = []
id_team = 0
tm_card_x = 170
tm_card_y = 175
cur_add_id = 0

max_team_val = 6

min_height_pl = 160
max_height_pl = 240
min_weight_pl = 60
max_weight_pl = 140


min_stat_pl = 10
max_stat_pl = 70
min_ovrl_pl = 30
max_ovrl_pl = 80
stat_val = 8

if game_plot == 1:
    money = 1000
    min_stat_pl = 10
    max_stat_pl = 70
    min_ovrl_pl = 30
    max_ovrl_pl = 80
elif game_plot == 2:
    money = 2000
    min_stat_pl = 10
    max_stat_pl = 70
    min_ovrl_pl = 35
    max_ovrl_pl = 80
elif game_plot == 3:
    money = 3500
    min_stat_pl = 15
    max_stat_pl = 75
    min_ovrl_pl = 40
    max_ovrl_pl = 80
else:
    print("ERROR №1: UNKNOWN GAME_PLOT")

#GENERATE_STATS_FOR_CARDS_PLAYER
def gen_stat_pl():
    stat_pl_gen_arr = []
    gen_sum_ovrl = 0
    for iii in range(stat_val):
        rnd_gen_stat = random.randint(min_stat_pl, max_stat_pl)
        gen_sum_ovrl += rnd_gen_stat
        stat_pl_gen_arr.append(rnd_gen_stat)

    if min_ovrl_pl < (gen_sum_ovrl/stat_val) < max_ovrl_pl:
        return stat_pl_gen_arr
    else:
        return None


#LOADING_SCREEN
loading1_bg = pygame.image.load('imges/loading_scr/l_bg1.png').convert_alpha()

loading_img = pygame.image.load('imges/loading_scr/loading_icn.png').convert_alpha()
loading_img0 = pygame.image.load('imges/loading_scr/loading_icn0.png').convert_alpha()
loading_img1 = pygame.image.load('imges/loading_scr/loading_icn1.png').convert_alpha()
loading_img2 = pygame.image.load('imges/loading_scr/loading_icn2.png').convert_alpha()
loading_img3 = pygame.image.load('imges/loading_scr/loading_icn3.png').convert_alpha()
loading_arr = [loading_img0,loading_img1,loading_img2,loading_img3,loading_img]
cur_load_id = 0

#LOADING_SCREEN_GM3
loading3_bg = pygame.image.load('imges/loading_scr/l_bg3.png').convert_alpha()

loading_img_3_0 = pygame.image.load('imges/loading_scr/loading_icn_gm3_0.png').convert_alpha()
loading_img_3_1 = pygame.image.load('imges/loading_scr/loading_icn_gm3_1.png').convert_alpha()
loading_img_3_2 = pygame.image.load('imges/loading_scr/loading_icn_gm3_2.png').convert_alpha()
loading_img_3_3 = pygame.image.load('imges/loading_scr/loading_icn_gm3_3.png').convert_alpha()
loading_img_3_4 = pygame.image.load('imges/loading_scr/loading_icn_gm3_4.png').convert_alpha()
loading_img_3_5 = pygame.image.load('imges/loading_scr/loading_icn_gm3_5.png').convert_alpha()
loading_img_3_6 = pygame.image.load('imges/loading_scr/loading_icn_gm3_6.png').convert_alpha()
loading_img_3_7 = pygame.image.load('imges/loading_scr/loading_icn_gm3_7.png').convert_alpha()
loading_arr_gm3 = [loading_img_3_0,loading_img_3_1,loading_img_3_2,loading_img_3_3,loading_img_3_4,loading_img_3_5,loading_img_3_6,loading_img_3_7]

#START_LOADING_SCREEN
start_loading_img = pygame.image.load('imges/start_load/start_load_img.png').convert_alpha()
start_loading_img0 = pygame.image.load('imges/start_load/start_load_img0.png').convert_alpha()
start_loading_img1 = pygame.image.load('imges/start_load/start_load_img1.png').convert_alpha()
start_loading_img2 = pygame.image.load('imges/start_load/start_load_img2.png').convert_alpha()
start_loading_img3 = pygame.image.load('imges/start_load/start_load_img3.png').convert_alpha()
start_loading_img4 = pygame.image.load('imges/start_load/start_load_img4.png').convert_alpha()
start_loading_img5 = pygame.image.load('imges/start_load/start_load_img5.png').convert_alpha()
start_loading_arr = [start_loading_img0,start_loading_img1,start_loading_img2,start_loading_img3,start_loading_img4,start_loading_img5,start_loading_img]
cur_start_load_id = 0

#TEAM_LOGOS_IMAGES
team_logo_1 = [pygame.image.load('imges/team_logos/embl1_0.png').convert_alpha(),pygame.image.load('imges/team_logos/embl1_1.png').convert_alpha(),pygame.image.load('imges/team_logos/embl1_2.png').convert_alpha(),pygame.image.load('imges/team_logos/embl1_3.png').convert_alpha(),pygame.image.load('imges/team_logos/embl1_4.png').convert_alpha()]
team_logo_2 = [pygame.image.load('imges/team_logos/embl2_0.png').convert_alpha(),pygame.image.load('imges/team_logos/embl2_1.png').convert_alpha(),pygame.image.load('imges/team_logos/embl2_2.png').convert_alpha(),pygame.image.load('imges/team_logos/embl2_3.png').convert_alpha(),pygame.image.load('imges/team_logos/embl2_4.png').convert_alpha()]
team_logo_3 = [pygame.image.load('imges/team_logos/embl3_0.png').convert_alpha(),pygame.image.load('imges/team_logos/embl3_1.png').convert_alpha(),pygame.image.load('imges/team_logos/embl3_2.png').convert_alpha(),pygame.image.load('imges/team_logos/embl3_3.png').convert_alpha(),pygame.image.load('imges/team_logos/embl3_4.png').convert_alpha()]
team_logo_4 = [pygame.image.load('imges/team_logos/embl4_0.png').convert_alpha(),pygame.image.load('imges/team_logos/embl4_1.png').convert_alpha(),pygame.image.load('imges/team_logos/embl4_2.png').convert_alpha(),pygame.image.load('imges/team_logos/embl4_3.png').convert_alpha(),pygame.image.load('imges/team_logos/embl4_4.png').convert_alpha()]
team_logo_5 = [pygame.image.load('imges/team_logos/embl5_0.png').convert_alpha(),pygame.image.load('imges/team_logos/embl5_1.png').convert_alpha(),pygame.image.load('imges/team_logos/embl5_2.png').convert_alpha(),pygame.image.load('imges/team_logos/embl5_3.png').convert_alpha(),pygame.image.load('imges/team_logos/embl5_4.png').convert_alpha()]
team_logo_arr = [team_logo_1,team_logo_2,team_logo_3,team_logo_4,team_logo_5]
cur_logo_embl = 0
cur_logo_color = 0


#MAIN MENU
menu_logo = pygame.image.load('imges/main_menu/main_logo.png').convert_alpha()
start_button_img = pygame.image.load('imges/main_menu/start_but1.png').convert_alpha()
start_button_rect = start_button_img.get_rect(topleft=(336, 760))
main_menu_bg = pygame.image.load('imges/main_menu/baground.jpeg').convert_alpha()


#FONTS
mainFont = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 40)
mainBaldFont = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 40)
mainBaldFont.set_bold(True)
cardsFont = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 16)
cardsFontBald = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 18)
cardsFontBald.set_bold(True)
cardsPriseFont = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 26)
valFont = pygame.font.Font('fonts/YujiMai-Regular.ttf', 40)
erorFont = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 28)
playerCardsFont = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 26)
playerCardsSecondFont = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 22)
cardsOvrlFontBald = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 20)
cardsOvrlFontBald.set_bold(True)
cardsOvrlSecFontBald = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 22)
cardsOvrlSecFontBald.set_bold(True)
cardsOvrlCRDFontBald = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 25)
cardsOvrlCRDFontBald.set_bold(True)
cardsOvrlCRDSecFontBald = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 28)
cardsOvrlCRDSecFontBald.set_bold(True)
complTeamFontBald = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 25)
complTeamFontBald.set_bold(True)
complTeamFontSec = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 20)
team_setup1 = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 22)
team_setup1.set_bold(True)
team_setup2 = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 22)
team_setup3 = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 30)
mainBaldFont_team_setup = pygame.font.Font('fonts/ShantellSans-VariableFont_BNCE,INFM,SPAC,wght.ttf', 30)
mainBaldFont_team_setup.set_bold(True)
team_logo_font = pygame.font.Font('fonts/YujiMai-Regular.ttf', 35)
mainBaldFont.set_bold(True)

#DRAFT MENU
square_mon = pygame.Surface((170, 70))
square_mon.fill((210, 143, 82))

my_team_text = mainBaldFont.render("Your Team: ", True, (46, 46, 48))
draft_text = mainBaldFont.render("Draft: ", True, (46, 46, 48))

    #DRAFT_POSIGILITY
draft_teamArr = []
id_gen = 0
pl_card_x = 20
pl_card_y = 485
for i in range(16):
    while True:
        temp_arr_stat = gen_stat_pl()
        if temp_arr_stat is not None:
            break
    temp_ovrl_stat = 0
    for jj in temp_arr_stat:
        temp_ovrl_stat+=jj
    temp_ovrl_stat = int(temp_ovrl_stat / stat_val)
    print(i, ": ", temp_arr_stat, "ovrl: ", temp_ovrl_stat)
    rnd_ic = random.randint(1,20)
    ic_gen = "imges/players/pl" + str(rnd_ic) + ".png"
    icmin_gen = "imges/players/pl_mini" + str(rnd_ic) + ".png"
    draft_teamArr.append({
        "name":namesArr[random.randint(0, len(namesArr)-1)],
        "age":random.randint(18,40),
        "icon":pygame.image.load(ic_gen),
        "prise":random.randint(0,400),
        "stats":temp_arr_stat,
        "ovrl":temp_ovrl_stat,
        "pos":random.choice(posesArr),
        "height": random.randint(min_height_pl, max_height_pl),
        "weight": random.randint(min_weight_pl, max_weight_pl),
        "icon_mini": pygame.image.load(icmin_gen),
        "id":id_gen,
        "rect":(pl_card_x,pl_card_y, 125, 205),
        "x": pl_card_x,
        "y": pl_card_y,
        "rect_colider": pygame.Rect(pl_card_x,pl_card_y, 125, 205)
    })
    pl_card_x += 145
    if id_gen == 7:
        pl_card_x = 20
        pl_card_y = 755
    id_gen+=1


def back_to_draft(dr_card, cr_rec, cr_x, cr_y, cr_rec_col, cr_id):
    global id_team, tm_card_x, tm_card_y
    draft_teamArr.append({
        "name": dr_card.get('name'),
        "age": dr_card.get('age'),
        "icon": dr_card.get('icon'),
        "prise": dr_card.get('prise'),
        "stats": dr_card.get('stats'),
        "ovrl": dr_card.get('ovrl'),
        "pos": dr_card.get('pos'),
        "height": dr_card.get('height'),
        "weight": dr_card.get('weight'),
        "icon_mini": dr_card.get('icon_mini'),
        "id": cr_id,
        "rect": cr_rec,
        "x": cr_x,
        "y": cr_y,
        "rect_colider": cr_rec_col,
    })
    id_team -= 1
    print(my_teamArr_pos)

def blit_pos_draft(t_pos,t_x,t_y):
    t_pos_text = cardsFontBald.render(str(t_pos), True, (0, 0, 0))
    if t_pos == 'PG':
        pygame.draw.rect(screen, (110, 20, 20), (t_x-1, t_y-1, 47, 22), border_radius=10)
        pygame.draw.rect(screen, (219,40,40), (t_x,t_y,45,20), border_radius=10)
        screen.blit(t_pos_text,(t_x+11,t_y-3))
    elif t_pos == 'SG':
        pygame.draw.rect(screen, (120, 60, 20), (t_x-1, t_y-1, 47, 22), border_radius=10)
        pygame.draw.rect(screen, (242, 113, 28), (t_x,t_y,45,20), border_radius=10)
        screen.blit(t_pos_text,(t_x+11,t_y-3))
    elif t_pos == 'SF':
        pygame.draw.rect(screen, (14, 81, 29), (t_x-1, t_y-1, 47, 22), border_radius=10)
        pygame.draw.rect(screen, (33, 186, 69), (t_x,t_y,45,20), border_radius=10)
        screen.blit(t_pos_text,(t_x+13,t_y-3))
    elif t_pos == 'PF':
        pygame.draw.rect(screen, (15, 58, 91), (t_x-1, t_y-1, 47, 22), border_radius=10)
        pygame.draw.rect(screen, (33, 133, 208), (t_x,t_y,45,20), border_radius=10)
        screen.blit(t_pos_text,(t_x+12,t_y-3))
    elif t_pos == 'C':
        pygame.draw.rect(screen, (42, 22, 82), (t_x-1, t_y-1, 47, 22), border_radius=10)
        pygame.draw.rect(screen, (100, 53, 201), (t_x,t_y,45,20), border_radius=10)
        screen.blit(t_pos_text,(t_x+16,t_y-3))
    else:
        print("ERROR №2: UNKNOWN GENERATED_POS")

def blit_ovrl_draft(t_ovrl, t_x, t_y, t_param):

    col = (102, 0, 0)
    if 10 <= t_ovrl < 20:
        col = (153, 0, 0)
    elif 20 <= t_ovrl < 25:
        col = (175, 0, 0)
    elif 25 <= t_ovrl < 30:
        col = (204, 0, 0)
    elif 30 <= t_ovrl < 35:
        col = (225, 0, 0)
    elif 35 <= t_ovrl < 40:
        col = (255, 0, 0)
    elif 40 <= t_ovrl < 45:
        col = (255, 50, 0)
    elif 45 <= t_ovrl < 50:
        col = (255, 90, 0)
    elif 50 <= t_ovrl < 55:
        col = (255, 130, 0)
    elif 55 <= t_ovrl < 60:
        col = (255, 170, 0)
    elif 60 <= t_ovrl < 65:
        col = (255, 210, 0)
    elif 65 <= t_ovrl < 70:
        col = (255, 255, 0)
    elif 70 <= t_ovrl < 75:
        col = (128, 255, 0)
    elif 75 <= t_ovrl < 80:
        col = (0, 255, 0)
    elif 80 <= t_ovrl < 85:
        col = (0, 200, 0)
    elif 85 <= t_ovrl < 90:
        col = (0, 150, 0)
    elif 90 <= t_ovrl < 95:
        col = (0, 100, 0)
    elif 95 <= t_ovrl < 100:
        col = (0, 50, 0)
    else:
        print("ERROR №3: UNKNOWN COLOR_OVRL")

    if t_param == 1:
        pygame.draw.circle(screen, (0,0,0), (t_x, t_y), 23)
        pygame.draw.circle(screen, col, (t_x,t_y), 20)
        t_ovrl_text = cardsOvrlFontBald.render(str(t_ovrl), True, (255, 255, 255))
        t_ovrl_text2 = cardsOvrlFontBald.render(str(t_ovrl), True, (128, 128, 128))
        screen.blit(t_ovrl_text2, (t_x - 13, t_y - 13))
        screen.blit(t_ovrl_text, (t_x - 15, t_y - 15))
    elif t_param == 2:
        pygame.draw.circle(screen, (0, 0, 0), (t_x, t_y), 30)
        pygame.draw.circle(screen, col, (t_x, t_y), 27)
        t_ovrl_text = cardsOvrlCRDFontBald.render(str(t_ovrl), True, (255, 255, 255))
        t_ovrl_text2 = cardsOvrlCRDFontBald.render(str(t_ovrl), True, (128, 128, 128))
        screen.blit(t_ovrl_text2, (t_x - 17, t_y - 17))
        screen.blit(t_ovrl_text, (t_x - 19, t_y - 19))



    #TEAM_POSIBILITY
def add_to_my_team(dr_card, pr_rec, pr_x, pr_y, pr_rec_col, pr_id):
    global id_team, tm_card_x, tm_card_y, cur_add_id
    if id_team<6:
        for j in range(6):
            if my_teamArr_pos[j] == 0:
                print("add_arr indx: " + str(j))
                my_teamArr_pos[j] = 1
                if j == 0:
                    tm_card_x = 170
                    cur_add_id = 0
                elif j == 1:
                    tm_card_x = 315
                    cur_add_id = 1
                elif j == 2:
                    tm_card_x = 460
                    cur_add_id = 2
                elif j == 3:
                    tm_card_x = 605
                    cur_add_id = 3
                elif j == 4:
                    tm_card_x = 750
                    cur_add_id = 4
                elif j == 5:
                    tm_card_x = 895
                    cur_add_id = 5
                break
        print(my_teamArr_pos)
        my_teamArr.append({
            "name": dr_card.get('name'),
            "age": dr_card.get('age'),
            "icon": dr_card.get('icon'),
            "prise": dr_card.get('prise'),
            "stats": dr_card.get('stats'),
            "ovrl": dr_card.get('ovrl'),
            "pos": dr_card.get('pos'),
            "height": dr_card.get('height'),
            "weight": dr_card.get('weight'),
            "icon_mini": dr_card.get('icon_mini'),
            "id": cur_add_id,
            "rect": (tm_card_x, tm_card_y, 125, 200),
            "x": tm_card_x,
            "y": tm_card_y,
            "rect_colider": pygame.Rect(tm_card_x, tm_card_y, 125, 200),
            "prev_rect": pr_rec,
            "prev_x": pr_x,
            "prev_y": pr_y,
            "prev_rect_colider": pr_rec_col,
            "prev_id": pr_id
        })
        id_team+=1
        return True
    else:

        return False

#PLAYER_CARD
back_player_img = pygame.image.load('imges/player_card/back_player_icn_small.png').convert_alpha()
confirm_player_img1 = pygame.image.load('imges/player_card/conf_player_icn1_small.png').convert_alpha()
reject_player_img1 = pygame.image.load('imges/player_card/rejct_player_icn1_small.png').convert_alpha()
back_player_rect = back_player_img.get_rect(topleft=(100, 775))
confirm_player_rect1 = confirm_player_img1.get_rect(topleft=(1020,775))
reject_player_rect1 = reject_player_img1.get_rect(topleft=(920, 775))

player_card_open_check = False

cur_pl_el = 0
cur_pl_ic = pygame.image.load('imges/player_card/conf_player_icn_small.jpg').convert_alpha()
cur_pl_name = ""
cur_pl_age = 0
cur_pl_prise = 0
cur_pl_idx = 0
cur_pl_pos = ""
cur_pl_ovrl = 0
cur_pl_stat = []
cur_pl_height = 0
cur_pl_weight = 0

def set_player_stat(elem, idx):
    global pl_stat8_text2, pl_stat7_text2, pl_stat6_text2, pl_stat5_text2, pl_stat4_text2, pl_stat3_text2, pl_stat2_text2, pl_stat1_text2, cur_pl_el,cur_pl_ic,cur_pl_name,cur_pl_age, pl_ovrl_text2, cur_pl_prise,cur_pl_idx, pl_pos_text2, pl_name_text2, pl_prise_text2, pl_age_text2,cur_pl_pos, cur_pl_ovrl, cur_pl_stat, cur_pl_height, cur_pl_weight, pl_height_text2, pl_weight_text2
    cur_pl_el = elem
    cur_pl_idx = idx
    cur_pl_ic = elem.get('icon')
    cur_pl_name = elem.get('name')
    cur_pl_age = elem.get('age')
    cur_pl_prise = elem.get('prise')
    cur_pl_pos = elem.get('pos')
    cur_pl_ovrl = elem.get('ovrl')
    cur_pl_stat = elem.get('stats')
    cur_pl_height = elem.get('height')
    cur_pl_weight = elem.get('weight')

    pl_name_text2 = playerCardsSecondFont.render(str(cur_pl_name), True, (40, 40, 40))
    pl_prise_text2 = playerCardsSecondFont.render(str(cur_pl_prise)+"$", True, (40, 40, 40))
    pl_age_text2 = playerCardsSecondFont.render(str(cur_pl_age), True, (40, 40, 40))
    pl_pos_text2 = playerCardsSecondFont.render(str(cur_pl_pos), True, (40, 40, 40))
    pl_ovrl_text2 = playerCardsSecondFont.render(str(cur_pl_ovrl), True, (40, 40, 40))
    pl_height_text2 = playerCardsSecondFont.render(str(cur_pl_height) + "sm", True, (40, 40, 40))
    pl_weight_text2 = playerCardsSecondFont.render(str(cur_pl_weight) + "kg", True, (40, 40, 40))

    pl_stat1_text2 = playerCardsSecondFont.render(str(cur_pl_stat[0]), True, (40, 40, 40))
    pl_stat2_text2 = playerCardsSecondFont.render(str(cur_pl_stat[1]), True, (40, 40, 40))
    pl_stat3_text2 = playerCardsSecondFont.render(str(cur_pl_stat[2]), True, (40, 40, 40))
    pl_stat4_text2 = playerCardsSecondFont.render(str(cur_pl_stat[3]), True, (40, 40, 40))
    pl_stat5_text2 = playerCardsSecondFont.render(str(cur_pl_stat[4]), True, (40, 40, 40))
    pl_stat6_text2 = playerCardsSecondFont.render(str(cur_pl_stat[5]), True, (40, 40, 40))
    pl_stat7_text2 = playerCardsSecondFont.render(str(cur_pl_stat[6]), True, (40, 40, 40))
    pl_stat8_text2 = playerCardsSecondFont.render(str(cur_pl_stat[7]), True, (40, 40, 40))



pl_info_text = playerCardsFont.render("PLAYER INFO", True, (0, 0, 0))

pl_name_text1 = playerCardsSecondFont.render("ИМЯ:", True, (40, 40, 40))
pl_name_text2 = playerCardsSecondFont.render(str(cur_pl_name), True, (40, 40, 40))
pl_slash_text1 = playerCardsSecondFont.render("_______________________________________", True, (40, 40, 40))

pl_prise_text1 = playerCardsSecondFont.render("ЦЕНА:", True, (40, 40, 40))
pl_prise_text2 = playerCardsSecondFont.render(str(cur_pl_prise), True, (40, 40, 40))
pl_slash_text2 = playerCardsSecondFont.render("_____________", True, (40, 40, 40))

pl_salary_text1 = playerCardsSecondFont.render("ЗАРПЛАТА:", True, (40, 40, 40))
pl_salary_text2 = playerCardsSecondFont.render(str(0)+"$", True, (40, 40, 40))
pl_slash_text3 = playerCardsSecondFont.render("__________", True, (40, 40, 40))

pl_age_text1 = playerCardsSecondFont.render("ВОЗРАСТ:", True, (40, 40, 40))
pl_age_text2 = playerCardsSecondFont.render(str(cur_pl_age), True, (40, 40, 40))
pl_slash_text4 = playerCardsSecondFont.render("____________", True, (40, 40, 40))

pl_pos_text1 = playerCardsSecondFont.render("ПОЗИЦИЯ:", True, (40, 40, 40))
pl_pos_text2 = playerCardsSecondFont.render(str(cur_pl_pos), True, (40, 40, 40))


pl_stat_text = playerCardsFont.render("PLAYER STAT", True, (0, 0, 0))

pl_ovrl_text1 = playerCardsSecondFont.render("ОБЩИЙ РЕЙТИНГ:", True, (40, 40, 40))
pl_ovrl_text2 = playerCardsSecondFont.render(str(cur_pl_ovrl), True, (40, 40, 40))

pl_height_text1 = playerCardsSecondFont.render("РОСТ:", True, (40, 40, 40))
pl_height_text2 = playerCardsSecondFont.render(str(cur_pl_height)+"sm", True, (40, 40, 40))
pl_slash_text5 = playerCardsSecondFont.render("_________", True, (40, 40, 40))

pl_weight_text1 = playerCardsSecondFont.render("ВЕС:", True, (40, 40, 40))
pl_weight_text2 = playerCardsSecondFont.render(str(cur_pl_weight) + "kg", True, (40, 40, 40))
pl_slash_text6 = playerCardsSecondFont.render("__________", True, (40, 40, 40))


pl_stat1_text1 = playerCardsSecondFont.render("СКОРОСТЬ", True, (40, 40, 40))
pl_stat1_text2 = playerCardsSecondFont.render("", True, (40, 40, 40))
pl_stat2_text1 = playerCardsSecondFont.render("ДРИБЛИНГ", True, (40, 40, 40))
pl_stat2_text2 = playerCardsSecondFont.render("", True, (40, 40, 40))
pl_stat3_text1 = playerCardsSecondFont.render("ЗАЩИТА", True, (40, 40, 40))
pl_stat3_text2 = playerCardsSecondFont.render("", True, (40, 40, 40))
pl_stat4_text1 = playerCardsSecondFont.render("ПОДБОР", True, (40, 40, 40))
pl_stat4_text2 = playerCardsSecondFont.render("", True, (40, 40, 40))
pl_stat5_text1 = playerCardsSecondFont.render("БРОСОК", True, (40, 40, 40))
pl_stat5_text2 = playerCardsSecondFont.render("", True, (40, 40, 40))
pl_stat6_text1 = playerCardsSecondFont.render("ТРЁХОЧКОВЫЕ", True, (40, 40, 40))
pl_stat6_text2 = playerCardsSecondFont.render("", True, (40, 40, 40))
pl_stat7_text1 = playerCardsSecondFont.render("ШТРАФНЫЕ", True, (40, 40, 40))
pl_stat7_text2 = playerCardsSecondFont.render("", True, (40, 40, 40))
pl_stat8_text1 = playerCardsSecondFont.render("ПАСЫ", True, (40, 40, 40))
pl_stat8_text2 = playerCardsSecondFont.render("", True, (40, 40, 40))

def blit_pos_card_sec(t_pos, t_pos_x, t_pos_y, t_w, t_h):
    col = (102, 0, 0)
    if t_pos == 'PG':
        col = (219,40,40)
    elif t_pos == 'SG':
        col = (242, 113, 28)
    elif t_pos == 'SF':
        col = (33, 186, 69)
    elif t_pos == 'PF':
        col = (33, 133, 208)
    elif t_pos == 'C':
        col = (100, 53, 201)
    else:
        print("ERROR №2: UNKNOWN GENERATED_POS")

    pygame.draw.rect(screen, col, (t_pos_x, t_pos_y, t_w, t_h))

#EFFECTS
    #BLUR
# def blur_region(region, amount):
#     SCRRR = pygame.transform.box_blur((100,100,300,300), amount)
#     screen.blit(SCRRR, (100,100,300,300))

    #BLACKED_SCREEN
blacked_screen_img = pygame.image.load('imges/effects/blacked_screen(1200_950).png').convert_alpha()
ef_blacked_screen_check = False

def blit_stat_card(t_stat, t_x, t_y):
    col = (102, 0, 0)
    if 10 <= t_stat < 20:
        col = (153, 0, 0)
    elif 20 <= t_stat < 25:
        col = (175, 0, 0)
    elif 25 <= t_stat < 30:
        col = (204, 0, 0)
    elif 30 <= t_stat < 35:
        col = (225, 0, 0)
    elif 35 <= t_stat < 40:
        col = (255, 0, 0)
    elif 40 <= t_stat < 45:
        col = (255, 50, 0)
    elif 45 <= t_stat < 50:
        col = (255, 90, 0)
    elif 50 <= t_stat < 55:
        col = (255, 130, 0)
    elif 55 <= t_stat < 60:
        col = (255, 170, 0)
    elif 60 <= t_stat < 65:
        col = (255, 210, 0)
    elif 65 <= t_stat < 70:
        col = (255, 255, 0)
    elif 70 <= t_stat < 75:
        col = (128, 255, 0)
    elif 75 <= t_stat < 80:
        col = (0, 255, 0)
    elif 80 <= t_stat < 85:
        col = (0, 200, 0)
    elif 85 <= t_stat < 90:
        col = (0, 150, 0)
    elif 90 <= t_stat < 95:
        col = (0, 100, 0)
    elif 95 <= t_stat < 100:
        col = (0, 50, 0)
    else:
        print("ERROR №4: UNKNOWN COLOR_STAT")

    pygame.draw.circle(screen, (0, 0, 0), (t_x, t_y), 55)
    pygame.draw.circle(screen, col, (t_x, t_y), 50)
    pygame.draw.rect(screen, (120, 120, 125), (t_x-55, t_y, 110, 55))
    pygame.draw.rect(screen, (0, 0, 0), (t_x - 80, t_y, 160, 3))
    t_stat_text = cardsOvrlCRDFontBald.render(str(t_stat), True, (255, 255, 255))
    t_stat_text2 = cardsOvrlCRDFontBald.render(str(t_stat), True, (128, 128, 128))
    screen.blit(t_stat_text2, (t_x - 15, t_y - 37))
    screen.blit(t_stat_text, (t_x - 17, t_y - 39))


#COMPL TEAM VISUAL
complText1 = complTeamFontBald.render("Ваша команда укомплектована! Готовы продолжить?", True, (46, 46, 48))
complText2 = complTeamFontSec.render("Да, меня все устраивает", True, (46, 46, 48))
complText3 = complTeamFontSec.render("Нет, я хочу подумать ещё", True, (46, 46, 48))
confirm_player_img = pygame.image.load('imges/player_card/conf_player_icn_small.jpg').convert_alpha()
reject_player_img = pygame.image.load('imges/player_card/rejct_player_icn_small.jpg').convert_alpha()
confirm_player_rect = confirm_player_img.get_rect(topleft=(385, 660))
reject_player_rect = reject_player_img.get_rect(topleft=(735, 660))

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#TEAM_SETUP_TEXT
yr_team_text = mainBaldFont.render("ВАША КОМАНДА", True, (112, 128, 144))
yr_team_name_text = mainBaldFont_team_setup.render("НАЗВАНИЕ:", True, (112, 128, 144))
yr_team_manager_text = mainBaldFont_team_setup.render("ГЛАВНЫЙ ТРЕНЕР:", True, (112, 128, 144))
team_name = ""
team_name_input_check = False
team_name_input_text = team_setup1.render("ВВОДИТЕ НАЗВАНИЕ ВАШЕЙ КОМАНДЫ:", True, (112, 128, 144))
input_box_team_name = pygame.Rect(590, 100, 560, 50)

team_logo_input_text = team_setup1.render("ВЫБЕРИТЕ ЭМБЛЕММУ И ЦВЕТ:", True, (112, 128, 144))
team_logo_type_text = [team_logo_font.render("1", True, (0, 0, 0)),team_logo_font.render("2", True, (0, 0, 0)),team_logo_font.render("3", True, (0, 0, 0)),team_logo_font.render("4", True, (0, 0, 0)),team_logo_font.render("5", True, (0, 0, 0))]
team_logo_type_rect = []
team_logo_color_text = [(255,154,46), (215,55,47), (58,93,193), (255, 213, 4), (74,203,109)]
team_logo_color_active_text = [(255, 100, 0), (204, 4, 4), (6, 6, 184), (240,237,42), (24, 209, 24)]
team_logo_color_rect = []

manager_name = ""
team_manager_input_check = False
team_manager_input_text = team_setup1.render("ВВОДИТЕ ИМЯ МЕНЕДЖЕРА КОМАНДЫ:", True, (112, 128, 144))
input_box_manager_name = pygame.Rect(590, 240, 560, 50)

#TEAM_SETUP_FUNC
def setup_rect_for_but():
    l_x_2 = 655
    l_y_2 = 460
    for l_i_2 in range(5):
        team_logo_type_rect.append(pygame.Rect(l_x_2 - 23, l_y_2 - 8, 71, 71))
        l_x_2 += 100

    ll_x_2 = 655
    ll_y_2 = 600
    for ll_i_2 in range(5):
        team_logo_color_rect.append(pygame.Rect(ll_x_2 - 23, ll_y_2 - 8, 71, 71))
        ll_x_2 += 100

#TEAM_SETUP_IMAGES
team_setup_next_but_img = pygame.image.load('imges/team_setup/t_s_next_button.png').convert_alpha()
team_setup_back_but_img = pygame.image.load('imges/team_setup/t_s_back_button.png').convert_alpha()
team_setup_rnd_but_img = pygame.image.load('imges/team_setup/t_s_random_button.png').convert_alpha()
team_setup_rnd_but_rect = team_setup_rnd_but_img.get_rect(topleft=(800,780))
team_setup_back_but_rect = team_setup_rnd_but_img.get_rect(topleft=(600, 780))
team_setup_next_but_rect = team_setup_rnd_but_img.get_rect(topleft=(1000, 780))



#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#ERORS
my_team_text_fault_max_1 = erorFont.render("В команде не хватает места!", True, (128, 0, 0))
my_team_text_fault_max_2 = erorFont.render("Максимальный размер команды: " + str(max_team_val), True, (128, 0, 0))

my_team_text_fault_money_1 = erorFont.render("У вас не хватает денег!", True, (128, 0, 0))
my_team_text_fault_money_2 = erorFont.render("Нужно денег для подписания: " + str((-1) * (money - cur_pl_prise)) + "$", True, (128, 0, 0))


#SOUND
tr1 = pygame.mixer.Sound('sounds/main_theme/track2(get_jiggy).mp3')
tr2 = pygame.mixer.Sound('sounds/main_theme/track1(where_is_my_head_at).mp3')
tr3 = pygame.mixer.Sound('sounds/main_theme/track3(drain_you).mp3')
tr4 = pygame.mixer.Sound('sounds/main_theme/track4(not_worth_it).mp3')
tr5 = pygame.mixer.Sound('sounds/main_theme/track5(anora).mp3')
tr6 = pygame.mixer.Sound('sounds/main_theme/track6(obsessed_with_you).mp3')
tr7 = pygame.mixer.Sound('sounds/main_theme/track7(bugs&humans).mp3')
tr8 = pygame.mixer.Sound('sounds/main_theme/track8(everybody_talks).mp3')
tr9 = pygame.mixer.Sound('sounds/main_theme/track9(memories).mp3')


main_tracks_arr = [tr1,tr2,tr3,tr4,tr5, tr6, tr7, tr8, tr9]
cur_track = random.randint(0, len(main_tracks_arr)-1)
print("cur_track: " + str(cur_track))

vol_music = 0.1
prev_vol_music = 0.1
mute_check = False

#MAIN REALIZATION
music_cheked = False
running = True
click_check = False
click_check_pl = False
delay_gm_2_check = True
check_window_gm_2 = False
check_start_load_gm_not1 = True
er_maxVal_check = False
er_money_check = False
tap_card_TorD = 0
compl_team = False
#gm4
t_s_check_click_rnd = True
t_s_check_click_back = True
t_s_from_back = False

delay_gm_3_check = True
cur_load_id_3 = 0

while running: #ГЛАВНЫЙ ЦИКЛ --------------------------------------------------------------------------------------------------------------------------------------
    for jj in main_tracks_arr:
        jj.set_volume(vol_music)
    if game_mode == -1: # СТАРТОВЫЙ ЗАГРУЗОЧНЫЙ ЭКРАН
        if check_start_load_gm_not1:
            start_time_load_st = time.time()
            check_start_load_gm_not1 = False

        screen.blit(start_loading_arr[cur_start_load_id], (70, 250))

        current_time_load_st = float(time.time() - start_time_load_st)

        if 0.2 < current_time_load_st < 0.5:
            cur_start_load_id = 1
        elif 0.5 < current_time_load_st < 0.8:
            cur_start_load_id = 2
        elif 0.8 < current_time_load_st < 1.1:
            cur_start_load_id = 3
        elif 1.1 < current_time_load_st < 1.4:
            cur_start_load_id = 4
        elif 1.4 < current_time_load_st < 1.7:
            cur_start_load_id = 5
        elif 1.7 < current_time_load_st < 5.2:
            cur_start_load_id = 6
        if 5.2 < current_time_load_st < 5.5:
            cur_start_load_id = 5
        elif 5.5 < current_time_load_st < 5.8:
            cur_start_load_id = 4
        elif 5.8 < current_time_load_st < 6.1:
            cur_start_load_id = 3
        elif 6.1 < current_time_load_st < 6.4:
            cur_start_load_id = 2
        elif 6.4 < current_time_load_st < 6.7:
            cur_start_load_id = 1
        elif 6.7 < current_time_load_st < 7.0:
            cur_start_load_id = 0
        elif current_time_load_st > 7.5:
            game_mode = 1

    elif game_mode == 0: # ЗАГРУЗОЧНЫЙ ЭКРАН ПЕРЕД ДРАФТОМ
        screen.fill((247, 204, 161))

        screen.blit(loading1_bg, (0,0))

        #screen.blit(menu_logo, (150, 100))
        screen.blit(loading_arr_gm3[cur_load_id], (230, 700))
        if delay_gm_2_check:
            start_time_l = time.time()
            delay_gm_2_check = False

        current_time_l = float(time.time() - start_time_l)
        if 0.5 <= current_time_l < 1.0:
            cur_load_id = 1
        elif 1.0 <= current_time_l < 1.5:
            cur_load_id = 2
        elif 1.5 <= current_time_l < 2.0:
            cur_load_id = 3
        elif 2.0 <= current_time_l < 2.5:
            cur_load_id = 4
        elif 2.5 <= current_time_l < 3.0:
            cur_load_id = 5
        elif 3.0 <= current_time_l < 3.5:
            cur_load_id = 6
        elif 3.5 <= current_time_l < 4.0:
            cur_load_id = 7

        if current_time_l > end_time_l:
            main_tracks_arr[cur_track].stop()
            cur_track +=1
            if cur_track == len(main_tracks_arr):
                cur_track = 0
            music_cheked = False
            game_mode = 2

    elif game_mode == 1: # ГЛАВНОЕ МЕНЮ
        if not music_cheked:
            main_tracks_arr[cur_track].play()
            music_cheked = True
        screen.fill((210, 143, 82))

        screen.blit(main_menu_bg, (0, 0))

        #screen.blit(menu_logo, (150, 100))
        screen.blit(start_button_img, start_button_rect)


        if start_button_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            game_mode = 0
    elif game_mode == 2: # МЕНЮ ДРАФТА-----------------------------------------------------------------------------------

        #CHECK FOR COMPL TEAM
        compl_team = True
        for ttt in my_teamArr_pos:
            if ttt == 0:
                compl_team = False

        moneyOUT = str(str(money) + ' $')
        money_text = valFont.render(moneyOUT, True, (46, 46, 48))
        if not check_window_gm_2:
            pygame.display.set_mode((1200, 1024), flags=pygame.NOFRAME)
            check_window_gm_2 = True
        if not music_cheked:
            main_tracks_arr[cur_track].play()
            music_cheked = True
        screen.fill((147, 101, 59))

        #screen.blit(square_mon, (730,0))
        screen.blit(money_text, (1040, 0))
        screen.blit(my_team_text, (510, 100))


        if not compl_team:

            screen.blit(draft_text, (560, 390))

            if er_maxVal_check: # ПРОВЕРКА ОШИБОК
                screen.blit(my_team_text_fault_max_1, (420, 10))
                screen.blit(my_team_text_fault_max_2, (370, 40))
            else:
                if er_money_check:
                    screen.blit(my_team_text_fault_money_1, (420, 10))
                    screen.blit(my_team_text_fault_money_2, (350, 40))

            if draft_teamArr:
                for el in draft_teamArr:
                    pygame.draw.rect(screen, (135, 135, 145), el.get('rect'))
                    pygame.draw.rect(screen, (112, 112, 121), (el.get('x')+5,el.get('y')+10,115,185))
                    screen.blit(el.get('icon_mini'), (el.get('x')+12,el.get('y')+10))

                    screen.blit(cardsFontBald.render("Имя:", True, (0,0,0)), (el.get('x')+40,el.get('y')+80))
                    screen.blit(cardsFontBald.render("Возраст:", True, (0, 0, 0)), (el.get('x') + 25, el.get('y') + 140))

                    nsplit = el.get('name').split()
                    n1 = cardsFont.render(nsplit[0], True, (46, 46, 48))
                    n2 = cardsFont.render(nsplit[1], True, (46, 46, 48))
                    screen.blit(n1, (el.get('x')+20,el.get('y')+100))
                    screen.blit(n2, (el.get('x') + 20, el.get('y') + 120))

                    screen.blit(cardsFont.render(str(el.get('age')), True, (46, 46, 48)), (el.get('x') + 52, el.get('y') + 165))

                    if el.get('prise') > 99:
                        screen.blit(cardsPriseFont.render((str(el.get('prise'))+'$'), True, (46, 46, 48)),(el.get('x') + 20, el.get('y') - 35))
                    elif el.get('prise') > 9:
                        screen.blit(cardsPriseFont.render((str(el.get('prise')) + '$'), True, (46, 46, 48)),
                                    (el.get('x') + 30, el.get('y') - 35))
                    else:
                        screen.blit(cardsPriseFont.render((str(el.get('prise')) + '$'), True, (46, 46, 48)),
                                    (el.get('x') + 40, el.get('y') - 35))

                    blit_pos_draft(el.get('pos'), el.get('x')+40,el.get('y')+190)
                    blit_ovrl_draft(el.get('ovrl'), el.get('x')+115,el.get('y')+5, 1)
        else: #ВЫВОД УКОМПЛЕКТОВОНОСТИ КОМАНДЫ
            pygame.draw.rect(screen, (120, 120, 125), (247, 547, 706, 306), border_radius=30)
            pygame.draw.rect(screen, (135, 135, 145), (250, 550, 700, 300), border_radius=30)
            pygame.draw.rect(screen, (120, 120, 125), (255, 555, 690, 290), border_radius=30)
            pygame.draw.rect(screen, (135, 135, 145), (258, 558, 684, 284), border_radius=30)
            screen.blit(complText1, (280, 590))
            pygame.draw.rect(screen, (46, 46, 48), (380, 655, 90, 90), border_radius=5)
            pygame.draw.rect(screen, (46, 46, 48), (730, 655, 90, 90), border_radius=5)
            screen.blit(reject_player_img, (385,660))
            screen.blit(confirm_player_img, (735, 660))

            if reject_player_rect.collidepoint(pygame.mouse.get_pos()) and compl_team:
                screen.blit(complText2, (660, 770))
            if confirm_player_rect.collidepoint(pygame.mouse.get_pos()) and compl_team:
                screen.blit(complText3, (300, 770))

            if pygame.mouse.get_pressed()[0]:
                if confirm_player_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and compl_team:
                    if not click_check:
                        print(my_teamArr)
                        set_player_stat(my_teamArr[5], 5)
                        player_card_open_check = False
                        click_check_pl = True
                        print("del_arr indx: " + str(cur_pl_el.get('id')))
                        my_teamArr_pos[cur_pl_el.get('id')] = 0
                        back_to_draft(cur_pl_el, cur_pl_el.get('prev_rect'), cur_pl_el.get('prev_x'),
                                      cur_pl_el.get('prev_y'),
                                      cur_pl_el.get('prev_rect_colider'), cur_pl_el.get('prev_id'))
                        my_teamArr.pop(cur_pl_idx)
                        money += cur_pl_el.get('prise')
                        tap_card_TorD = 0
                if reject_player_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and compl_team:
                    if not click_check:
                        click_check = True
                        t_s_from_back = False
                        cur_load_id_3 = 0
                        delay_gm_3_check = True
                        game_mode = 3

            else:
                click_check = False

        if my_teamArr:
            for el in my_teamArr:
                pygame.draw.rect(screen, (135, 135, 145), el.get('rect'))
                pygame.draw.rect(screen, (112, 112, 121), (el.get('x')+5,el.get('y')+10,115,185))
                screen.blit(el.get('icon_mini'), (el.get('x')+12,el.get('y')+10))

                screen.blit(cardsFontBald.render("Имя:", True, (0,0,0)), (el.get('x')+40,el.get('y')+80))
                screen.blit(cardsFontBald.render("Возраст:", True, (0, 0, 0)), (el.get('x') + 25, el.get('y') + 140))

                nsplit = el.get('name').split()
                n1 = cardsFont.render(nsplit[0], True, (46, 46, 48))
                n2 = cardsFont.render(nsplit[1], True, (46, 46, 48))
                screen.blit(n1, (el.get('x')+20,el.get('y')+100))
                screen.blit(n2, (el.get('x') + 20, el.get('y') + 120))

                screen.blit(cardsFont.render(str(el.get('age')), True, (46, 46, 48)), (el.get('x') + 52, el.get('y') + 165))

                blit_pos_draft(el.get('pos'), el.get('x') + 40, el.get('y') + 190)
                blit_ovrl_draft(el.get('ovrl'), el.get('x') + 115, el.get('y') + 5, 1)

        if ef_blacked_screen_check:
            screen.blit(blacked_screen_img, (0, 0))

        if player_card_open_check: # КАРТОЧКА ИГРОКА
            screen.blit(blacked_screen_img, (0, 0))
            pygame.draw.rect(screen, (178, 178, 185), (80,80,1040,790))

            screen.blit(confirm_player_img1,(1020,780))
            screen.blit(back_player_img, (100, 780))
            if tap_card_TorD == 2:
                screen.blit(reject_player_img1, (920, 780))

            pygame.draw.rect(screen, (120, 120, 125), (100, 100, 300, 220))
            screen.blit(cur_pl_ic, (100,102))


            pygame.draw.rect(screen, (120, 120, 125), (420, 100, 680, 220))
            screen.blit(pl_info_text, (700,110))

            screen.blit(pl_name_text1, (430,160))
            screen.blit(pl_slash_text1, (495, 165))
            screen.blit(pl_name_text2, (700, 160))

            screen.blit(pl_prise_text1, (430, 210))
            screen.blit(pl_slash_text2, (505, 215))
            screen.blit(pl_prise_text2, (580, 210))

            screen.blit(pl_salary_text1, (430, 260))
            screen.blit(pl_slash_text3, (550, 265))
            screen.blit(pl_salary_text2, (610, 260))

            screen.blit(pl_age_text1, (790, 210))
            screen.blit(pl_slash_text4, (899, 215))
            screen.blit(pl_age_text2, (970, 210))

            screen.blit(pl_pos_text1, (790, 260))
            pygame.draw.rect(screen, (40, 40, 50), (950, 257, 65, 37))

            blit_pos_card_sec(cur_pl_pos, 953, 260, 59, 31)
            if cur_pl_pos == "PG" or cur_pl_pos == "SG":
                screen.blit(pl_pos_text2, (969, 260))
            elif cur_pl_pos == "C":
                screen.blit(pl_pos_text2, (977, 260))
            else:
                screen.blit(pl_pos_text2, (972, 260))

            pygame.draw.rect(screen, (120, 120, 125), (100, 340, 1000, 430))

            screen.blit(pl_stat_text, (550, 350))

            screen.blit(pl_ovrl_text1, (185, 410))
            blit_ovrl_draft(cur_pl_ovrl, 415, 425, 2)


            screen.blit(pl_height_text1, (490, 410))
            screen.blit(pl_slash_text5, (555, 415))
            screen.blit(pl_height_text2, (590, 410))

            screen.blit(pl_weight_text1, (790, 410))
            screen.blit(pl_slash_text6, (835, 415))
            screen.blit(pl_weight_text2, (880, 410))


            screen.blit(pl_stat1_text1, (240, 480))
            blit_stat_card(cur_pl_stat[0], 293, 580)

            screen.blit(pl_stat2_text1, (240, 610))
            blit_stat_card(cur_pl_stat[1], 293, 710)

            screen.blit(pl_stat3_text1, (455, 480))
            blit_stat_card(cur_pl_stat[2], 503, 580)


            screen.blit(pl_stat4_text1, (460, 610))
            blit_stat_card(cur_pl_stat[3], 503, 710)

            screen.blit(pl_stat5_text1, (660, 480))
            blit_stat_card(cur_pl_stat[4], 703, 580)


            screen.blit(pl_stat6_text1, (625, 610))
            blit_stat_card(cur_pl_stat[5], 703, 710)

            screen.blit(pl_stat7_text1, (840, 480))
            blit_stat_card(cur_pl_stat[6], 903, 580)

            screen.blit(pl_stat8_text1, (870, 610))
            blit_stat_card(cur_pl_stat[7], 903, 710)


            if pygame.mouse.get_pressed()[0]: # ОБРАБОТЧИК НАЖАТИЯ МЫШИ В КАРТОЧКЕ ИГРОКА
                if reject_player_rect1.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and tap_card_TorD == 2:
                    if not click_check_pl:
                        player_card_open_check = False
                        click_check_pl = True
                        print("del_arr indx: " + str(cur_pl_el.get('id')))
                        my_teamArr_pos[cur_pl_el.get('id')] = 0
                        back_to_draft(cur_pl_el, cur_pl_el.get('prev_rect'), cur_pl_el.get('prev_x'), cur_pl_el.get('prev_y'),
                                      cur_pl_el.get('prev_rect_colider'), cur_pl_el.get('prev_id'))
                        my_teamArr.pop(cur_pl_idx)
                        money += cur_pl_el.get('prise')
                        tap_card_TorD = 0
                if confirm_player_rect1.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    if not click_check_pl:
                        if tap_card_TorD == 1:
                            if (money - cur_pl_el.get('prise')) >= 0:
                                if add_to_my_team(cur_pl_el, cur_pl_el.get('rect'), cur_pl_el.get('x'), cur_pl_el.get('y'),
                                                  cur_pl_el.get('rect_colider'),
                                                  cur_pl_el.get('id')):
                                    draft_teamArr.pop(cur_pl_idx)
                                    money -= cur_pl_el.get('prise')
                                else:
                                    print("В команде нет места")
                                    er_maxVal_check = True
                            else:
                                my_team_text_fault_money_2 = erorFont.render("Нужно денег для подписания: " + str((-1) * (money - cur_pl_prise)) + "$", True, (128, 0, 0))
                                print("У вас не хватает денег!")
                                er_money_check = True
                            tap_card_TorD = 0
                            player_card_open_check = False
                            click_check_pl = True
                        elif tap_card_TorD == 2:
                            tap_card_TorD = 0
                            player_card_open_check = False
                            click_check_pl = True
                if back_player_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                    if not click_check_pl:
                        player_card_open_check = False
                        click_check_pl = True
                        tap_card_TorD = 0
            else:
                click_check_pl = False
        else: # ОБРАБОТЧИК НАЖАТИЯ МЫШИ В МЕНЮ ДРАФТА
            if pygame.mouse.get_pressed()[0]:
                for (i,el) in enumerate(draft_teamArr):
                    if el.get('rect_colider').collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and not compl_team:
                        if not click_check:
                            er_maxVal_check = False
                            er_money_check = False
                            player_card_open_check = True
                            set_player_stat(el, i)
                            click_check = True
                            tap_card_TorD = 1
                for (i,el) in enumerate(my_teamArr):
                    if el.get('rect_colider').collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and not compl_team:
                        if not click_check:
                            er_maxVal_check = False
                            er_money_check = False
                            player_card_open_check = True
                            set_player_stat(el, i)
                            click_check = True
                            tap_card_TorD = 2
            else:
                click_check = False

    elif game_mode == 3:  # ЗАГРУЗОЧНЫЙ ЭКРАН ПЕРЕД GAMEMODE 4-----------------------------------------------------------------------------------
        screen.fill((112, 128, 144))

        screen.blit(loading3_bg, (0, 0))

        #screen.blit(menu_logo, (300, 100))
        screen.blit(loading_arr_gm3[cur_load_id_3], (318, 700))
        if delay_gm_3_check:
            start_time_l = time.time()
            delay_gm_3_check = False

        current_time_l = float(time.time() - start_time_l)
        if 0.5 <= current_time_l < 1.0:
            cur_load_id_3 = 1
        elif 1.0 <= current_time_l < 1.5:
            cur_load_id_3 = 2
        elif 1.5 <= current_time_l < 2.0:
            cur_load_id_3 = 3
        elif 2.0 <= current_time_l < 2.5:
            cur_load_id_3 = 4
        elif 2.5 <= current_time_l < 3.0:
            cur_load_id_3 = 5
        elif 3.0 <= current_time_l < 3.5:
            cur_load_id_3 = 6
        elif 3.5 <= current_time_l < 4.0:
            cur_load_id_3 = 7

        if current_time_l > end_time_l_gm3:
            main_tracks_arr[cur_track].stop()
            cur_track += 1
            if cur_track == len(main_tracks_arr):
                cur_track = 0
            music_cheked = False
            if t_s_from_back:
                game_mode = 2
            else:
                game_mode = 4

    elif game_mode == 4:  # ЗАГРУЗОЧНЫЙ ЭКРАН ПЕРЕД GAMEMODE 4-----------------------------------------------------------------------------------
        if not music_cheked:
            main_tracks_arr[cur_track].play()
            music_cheked = True
            setup_rect_for_but()
        screen.fill((47, 79, 79))

        pygame.draw.rect(screen, (23, 40, 40), (20,20,520,950))
        pygame.draw.rect(screen, (23, 40, 40), (560, 20, 620, 300))
        pygame.draw.rect(screen, (23, 40, 40), (560, 340, 620, 400))
        #pygame.draw.rect(screen, (112, 128, 144), (40, 80, 480, 500))
        screen.blit(team_logo_arr[cur_logo_embl][cur_logo_color], (20,120))
        screen.blit(yr_team_text, (110,50))
        screen.blit(yr_team_name_text, (185, 650))
        screen.blit(yr_team_manager_text, (140, 800))
        pygame.draw.rect(screen, (112, 128, 144), (60, 750, 420, 5), border_radius=2)
        pygame.draw.rect(screen, (112, 128, 144), (60, 900, 420, 5), border_radius=2)
        name_team_text = team_setup3.render(team_name, True, (215, 215, 215))
        screen.blit(name_team_text, (270 - (8.5 * len(team_name)), 710))
        manager_team_text = team_setup3.render(manager_name, True, (215, 215, 215))
        screen.blit(manager_team_text, (270 - (8 * len(manager_name)), 860))


        screen.blit(team_name_input_text, (645,50))
        if team_name_input_check:
            pygame.draw.rect(screen, (3, 7, 7), input_box_team_name)
        else:
            pygame.draw.rect(screen, (10, 24, 24), input_box_team_name)
        input_name_team = team_setup2.render(team_name, True, (112, 128, 144))
        screen.blit(input_name_team, (890-(7*len(team_name)), 110))

        screen.blit(team_manager_input_text, (650, 190))
        if team_manager_input_check:
            pygame.draw.rect(screen, (3, 7, 7), input_box_manager_name)
        else:
            pygame.draw.rect(screen, (10, 24, 24), input_box_manager_name)
        input_name_manager = team_setup2.render(manager_name, True, (112, 128, 144))
        screen.blit(input_name_manager, (890 - (7 * len(manager_name)), 250))

        screen.blit(team_setup_rnd_but_img, (800,780))
        screen.blit(team_setup_back_but_img, (600, 780))
        screen.blit(team_setup_next_but_img, (1000, 780))

        screen.blit(team_logo_input_text, (695, 370))
        l_x = 655
        l_y = 460
        for l_i in range(5):
            pygame.draw.rect(screen, (112, 128, 144), (l_x - 23, l_y - 8, 71, 71), border_radius=20)
            if l_i == cur_logo_embl:
                pygame.draw.rect(screen, (150, 150, 150), (l_x - 20, l_y - 5, 65, 65), border_radius=20)
            else:
                pygame.draw.rect(screen, (215,215,215), (l_x - 20, l_y - 5, 65, 65), border_radius=20)
            screen.blit(team_logo_type_text[l_i], (l_x, l_y))

            l_x += 100

        ll_x = 655
        ll_y = 600
        for ll_i in range(5):
            pygame.draw.rect(screen, (112, 128, 144), (ll_x - 23, ll_y - 8, 71, 71), border_radius=20)
            if ll_i == cur_logo_color:
                pygame.draw.rect(screen, team_logo_color_active_text[ll_i], (ll_x - 20, ll_y - 5, 65, 65), border_radius=20)
            else:
                pygame.draw.rect(screen, team_logo_color_text[ll_i], (ll_x - 20, ll_y - 5, 65, 65), border_radius=20)

            ll_x += 100



        if pygame.mouse.get_pressed()[0]:
            for (i,el4) in enumerate(team_logo_type_rect):
                if el4.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and game_mode == 4:
                    if i == 0:
                        cur_logo_embl = 0
                    elif i == 1:
                        cur_logo_embl = 1
                    elif i == 2:
                        cur_logo_embl = 2
                    elif i == 3:
                        cur_logo_embl = 3
                    elif i == 4:
                        cur_logo_embl = 4
            for (i_2,el4_2) in enumerate(team_logo_color_rect):
                if el4_2.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and game_mode == 4:
                    if i_2 == 0:
                        cur_logo_color = 0
                    elif i_2 == 1:
                        cur_logo_color = 1
                    elif i_2 == 2:
                        cur_logo_color = 2
                    elif i_2 == 3:
                        cur_logo_color = 3
                    elif i_2 == 4:
                        cur_logo_color = 4
            if team_setup_rnd_but_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and game_mode == 4:
                if t_s_check_click_rnd:
                    cur_logo_embl = random.randint(0,4)
                    cur_logo_color = random.randint(0, 4)
                    team_name = random.choice(random_team_names)
                    manager_name = random.choice(random_team_managers)
                    t_s_check_click_rnd = False
                    t_s_check_click_back = False
            if team_setup_back_but_rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] and game_mode == 4:
                if t_s_check_click_back:
                    t_s_from_back = True
                    cur_load_id_3 = 0
                    delay_gm_3_check = True
                    game_mode = 3



    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            main_tracks_arr[cur_track].stop()
            cur_track+=1
            if cur_track == len(main_tracks_arr):
                cur_track = 0
            main_tracks_arr[cur_track].play()
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            main_tracks_arr[cur_track].stop()
            cur_track -= 1
            if cur_track < 0:
                cur_track = len(main_tracks_arr)-1
            main_tracks_arr[cur_track].play()
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            vol_music += 0.05
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            vol_music -= 0.05
        if event.type == pygame.KEYUP and event.key == pygame.K_m:
            if not mute_check:
                prev_vol_music = vol_music
                vol_music = 0
                mute_check = True
            else:
                vol_music = prev_vol_music
                mute_check = False
        if event.type == pygame.KEYUP and event.key == pygame.K_b:
             ef_blacked_screen_check = True
        if event.type == pygame.KEYUP and event.key == pygame.K_n:
             ef_blacked_screen_check = False
        if game_mode == 4:

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box_team_name.collidepoint(event.pos):
                    team_name_input_check = True
                else:
                    team_name_input_check = False

                if input_box_manager_name.collidepoint(event.pos):
                    team_manager_input_check = True
                else:
                    team_manager_input_check = False

            if event.type == pygame.KEYDOWN:
                if team_name_input_check:
                    if event.key == pygame.K_BACKSPACE:
                        team_name = team_name[:-1]
                    else:
                        team_name += event.unicode

                if team_manager_input_check:
                    if event.key == pygame.K_BACKSPACE:
                        manager_name = manager_name[:-1]
                    else:
                        manager_name += event.unicode

            if event.type == pygame.KEYUP and event.key == pygame.K_p and game_mode == 4:
                if cur_logo_color == 4:
                    cur_logo_color = 0
                else:
                    cur_logo_color+=1
            if event.type == pygame.KEYUP and event.key == pygame.K_o and game_mode == 4:
                if cur_logo_color == 0:
                    cur_logo_color = 4
                else:
                    cur_logo_color-=1
            if event.type == pygame.KEYUP and event.key == pygame.K_l and game_mode == 4:
                if cur_logo_embl == 4:
                    cur_logo_embl = 0
                else:
                    cur_logo_embl+=1
            if event.type == pygame.KEYUP and event.key == pygame.K_k and game_mode == 4:
                if cur_logo_embl == 0:
                    cur_logo_embl = 4
                else:
                    cur_logo_embl -= 1
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    t_s_check_click_rnd = True
                    t_s_check_click_back = True
