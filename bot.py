import telebot, psutil, platform, subprocess

bot = telebot.TeleBot("7944853161:AAFzSU_IK7jrjMZEulUA05xO8cycMOUZtAE")

@bot.message_handler(commands=["my_charasteristics"])
def pc(message):
    ram = psutil.virtual_memory()
    gpu = subprocess.check_output("wmic path win32_VideoController get name", shell=True, text=True).splitlines()[1].strip()
    text = f"""Ваши характеристики
    
    Процессор:
    {platform.processor()}
    Колл-во ядер:
    {psutil.cpu_count()}
    Видеокарта: 
    {gpu}
    ОЗУ:
    {ram.total//1024**3} GB
    OC:
    {platform.system()}
{platform.release()}
    Диски:"""
    for d in psutil.disk_partitions():

        try:
            x = psutil.disk_usage(d.mountpoint)
            text += f"\n{d.device} - {x.free//10243}/{x.total//10243} GB свободно"
        except:
            pass
        bot.send_message(message.chat.id,text)

bot.infinity_polling()