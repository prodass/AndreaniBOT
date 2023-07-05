# TOKEN = '6387459776:AAFqGryWIozNRNnk5AEUGbZmyFokmRD-DT0'
# CHAT_ID = '5234302922'

import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = '6387459776:AAFqGryWIozNRNnk5AEUGbZmyFokmRD-DT0'
CHAT_ID = '5234302922'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def obtener_datos():
    url = 'https://apidestinatarios.andreani.com/api/envios/360000874374300/trazas'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            datos = await response.json()
            return datos

async def enviar_mensaje(mensaje):
    await bot.send_message(chat_id=CHAT_ID, text=mensaje)

async def consultar_y_enviar():

    ultimo_estado = "Aún no recibimos tu envío. Suscribite al servicio de notificaciones y te enviaremos las novedades por e-mail"
    while True:
        datos = await obtener_datos()
        ultima_fecha = None
        nuevo_estado = None

        for estado in datos:
            fecha_actual = estado['fecha']['dia']
            if not ultima_fecha or fecha_actual > ultima_fecha:
                ultima_fecha = fecha_actual
                nuevo_estado = estado

        if nuevo_estado and isinstance(nuevo_estado, dict) and nuevo_estado != ultimo_estado:
            mensaje = f"Último estado:\n{nuevo_estado['estado']}"
            ultimo_estado = nuevo_estado
            await enviar_mensaje(mensaje)

        await asyncio.sleep(300)  # Espera 5 minutos (300 segundos)


@dp.message_handler(commands=['start'])
async def send_last_status(message: types.Message):
    await consultar_y_enviar()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
