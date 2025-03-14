import os
from dotenv import load_dotenv
from openai import OpenAI
from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler, ContextTypes,
                          MessageHandler, filters)

from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

presentation_content = [
    {"role": "system", "content": "ЛАТОКЕН - ЭТО СУПЕРМАРКЕТ АКТИВОВ НА ТЕХНОЛОГИЯХ WEB3 И AI. #1 по числу активов "
                                  "для трейдинга 3,000+ (Бинанс 400+). Топ 25 Крипто биржа по рейтингам CoinmarketCap "
                                  "and CoinGecko. 4 миллиона Счетов. 1 миллион платящих пользователей в 2022. Мы "
                                  "делаем простым для каждого возможность Узнать, Обменять, Заработать и Потратить "
                                  "любой криптоакти. Помогая людям понимать криптоактивы и прогнозировать их цену, "
                                  "мы превращаем их в участников глобального интеллекта и помогаем стать "
                                  "стейкхолдерами будущего."},
    {"role": "system", "content": "РАБОТА В ЛАТОКЕН  - УНИКАЛЬНАЯ ВОЗМОЖНОСТЬ ДЛЯ 'СПОРТСМЕНОВ' ВЛЮБЛЕННЫХ В "
                                  "ТЕХНОЛОГИИ. Быстрый рост через решение нетривиальных задач. Передовые технологии "
                                  "AIxWEB3. Глобальный рынок, клиенты в 200+ странах. Самая успешная компания из СНГ "
                                  "в WEB3. Удаленная работа, но без дауншифтинга. Оплата в твёрдой валюте, "
                                  "без привязки к банкам. Опционы с 'откешиванием' криптолетом"},
    {"role": "system", "content": "РАБОТА У НАС - ВОЗМОЖНОСТЬ СДВИНУТЬ ПЕРИМЕТР ТЕХНОЛОГИЙ.Распределенный  "
                                  "AGI?Трансформеры AGI? zk Rollups Re-Staking Мультимодальность RAG Layer 3? Web 2 "
                                  "->3? Квантовый  AGI? DePin? RWA? Synthetic? Q learning? Мультиагенты?"},
    {"role": "system", "content": "НАУЧИМ СДВИГАТЬ ГРАНИЦЫ ВОЗМОЖНОГО. «Друзья моего сына, перестали развиваться, "
                                  "идти к целям... Они не желали брать на себя нагрузки высшей спортивной школы. "
                                  "Поэтому я сказал сыну „Они тебе не друзья, сын“. Хабиб пытался парировать, "
                                  "что дружат со школы. Я в тот момент спросил его: — Они готовы делать объемы, "
                                  "которые делаешь ты? — Нет. — Их родители думают о том же, о чем я думаю? — Нет. — "
                                  "Как вам тогда идти по пути вместе? Ведь я с каждым годом буду увеличивать тебе "
                                  "нагрузку. Те, кого ты называешь своими друзьями, — они сами и их семьи готовы к "
                                  "таким нагрузкам? — Нет».Абдулманап Нурмагомедов, тренер 18 чемпионов мира"},
    {"role": "system", "content": "СПОРТИВНЫЙ ТРЕНЕР ПОДХОДИТ ТЕБЕ ЕСЛИ ЛЮБИШЬ: Сверхусилие и ответственность решить "
                                  "проблему, когда большинство сдается. Прямоту в обсуждении проблем и ошибок, "
                                  "недоработок. Стресс и давление для  ускорения и  креативности. Технологии чтобы "
                                  "создать будущее, нежели полировать прошлое"},
    {"role": "system", "content": "СПОРТИВНЫЙ ТРЕНЕР НЕ ПОДХОДИТ ТЕБЕ ЕСЛИ:Хочет 'непыльную' работу. Ищет 'вторые "
                                  "работы'. Меняет работу, когда сталкиваетс с трудностями и ответственностью. Лелеит "
                                  "обиды, чтобы оправдать отлынивание. Прикрывает коллег или сплетничает, "
                                  "вместо прямоты"},
    {"role": "system",
     "content": "КАЖДЫЙ ОТВЕЧАЕТ ЗА ПОЛЬЗУ В ПРОДЕ  ДЛЯ КЛИЕНТОВ. Разберусь и сделаю, расписав проект, "
                "задачи, блокеры и репорты.Каждую неделю улучшаю продукт или процесс, "
                "тестирую.Измеряю какую пользу  приносит моя работа.Дожму задачу сегодня, "
                "чтобы не замусоривать недоделом завтра.Нахожу 10х улучшения на хакатонах по суботам. "
                "Мы не: Это от меня не зависит.Я не QA и не должен это тестировать.Я не аналитик и не "
                "должен смотреть как релиз повлиял на конверсию.Я не менеджер, пусть кто то распишет "
                "мне задачи.Мой рабочий день закончился.Занимаюсь ритуалами обывателей вместо хакатонов "
                "по выходным"},
    {"role": "system",
     "content": "ТЕБЯ ОКРУЖАЮТ ТЕ, КТО ЛЮБЯТ СВЕРХ УСИЛИЯ И РОСТ?ЭТО СТАНЕТ ПОНЯТНО В ПЕРВУЮ ЖЕ НЕДЕЛЮ ПО ТВОЕМУ "
                "УЧАСТИЮ В ХАКАТОНАХ ПО  ВЫХОДНЫМ"},
    {"role": "system",
     "content": "НОВЫЕ КОМПАНИИ НЕ НУЖНЫ ЕСЛИ ОНИ НЕ СДЕЛАЛИ РЕВОЛЮЦИЮ В КУЛЬТУРЕ. Новым компаниям проще сделать "
                "культуру, где команда еще прозрачнее и ответственнее. Благодаря меньшему размеру, опционам и "
                "поддерживающим процессам. Это привлекает тех, кто растет чтобы изменить мир и отпугивает "
                "безбилетников."},
    {"role": "system",
     "content": "КУЛЬТУРА СТАРТАПОВ  ОПРЕДЕЛЯЕТСЯ УГРОЗОЙ ГИБЕЛИ В ПОПЫТКЕ СОЗДАТЬ БУДУЩЕЕ. Wartime CEOсоздает и "
                "захватывает рынок при постоянной угрозе гибели ругается и кричит нетерпим к дефокусу тренирует "
                "команду так, чтобы ей не прострелили зад"},
    {"role": "system",
     "content": "КУЛЬТУРА.ПОЛНЫЙ КОММИТМЕНТ РАСТИ, ЧТОБЫ БЫТЬ ПОЛЕЗНЕЕ, 'БАЛАНС' И 'СЧАСТЬЕ' НЕ ДЛЯ ЧЕМПИОНОВ. "
                "Счастья не надо, хотим удовлетворенность, что полезны миру. Баланса нет, есть жизнь где ты учишься "
                "быть полезнее. Выбор Свидание или Хакатон в сб определяется тем, где ты больше разовьешься. Стресс "
                "это друг помочь преодолеть препятствие. Никаких сайд, пет, пед проектов. Полный коммитмент."},
    {"role": "system",
     "content": "АКТУАЛЬНЫЕ ВАКАНСИИ: Продакт Разработчик (2 из 4 от 1 года: Python,  React/Node, Python,Java,C#, "
                "Kotlin, IOS): Супермаркет активов(Python, Java, Kotlin, IOS),Growth платформа(React/Node.js), "
                "Трейдинг деск (C#). Data Engineer(SQL 2+ года, DWH, PBI, Python): Data (SQL, DWH, PBI, "
                "Python).Операционный Менеджер-Разработчик(Меняющим профессию на разработчика или фанаты "
                "автоматизации: HR, Sales CRM"},
    {"role": "system",
     "content": "Как попасть: Отбор на вакансии в Латокен проходит в несколько этапов. Первый шаг - это участие в "
                "нашем хакатоне, где ты можешь продемонстрировать свои навыки и креативность. Победители хакатона "
                "получают предложения о работе и могут пройти финальное интервью."},
    {"role": "system",
     "content": "О хакатоне:ХАКАТОН AIxWEB3 каждую пятницу 18:00 по МСК. Получи опыт внедрения AI и приглашение "
                "работать в Латокен на “периметре технологий”"},
    {"role": "system",
     "content": "Расписание: 18:00 Презентация компании и обсуждение задачи. Суббота: 17:00 Чекпоинт. "
                "18:00 Демо результатов, 19:00 Объявление победителей, интервью и офферы"},
    {"role": "system", "content": "Регистрация https://t.me/gpt_web3_hackathon/5280"},
]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Я MegaMind бот! Чем могу Вам помочь?")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = await request_chat_gpt(user_message)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)


async def request_chat_gpt(user_message):
    messages = presentation_content + [{"role": "user", "content": user_message}]
    try:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.5
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error: {e}")
        return "Извините, не смог обработать запрос."


def main():
    application = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()
    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)

    application.add_handler(start_handler)
    application.add_handler(message_handler)
    application.run_polling()


if __name__ == '__main__':
    main()