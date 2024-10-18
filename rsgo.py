from pyrogram import Client, filters, idle
import random
import asyncio
from datetime import datetime
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from PIL import Image, ImageDraw, ImageFont
#MDB =
API_ID = "7980140"  
API_HASH = "db84e318c6894f560a4087c20c33ce0a"  
BOT_TOKEN = "6520550784:AAHZPv8eOS2Unc91jIVYSH5PB0z8SO36lUY"  
bot = Client("aviator_betting_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

bet_amount = 1000 
session_times = ["10:00", "11:00", "14:22"] #railwaytime
channels_to_post = ["@anehow", "-1002454896752"] 
round_intervals = 60  
def edit_image(multiplier, winnings):
    img_path = 'rsgo.jpg'  
    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("font.ttf", 30)  
    multiplier_pos = (230, 85)  
    winnings_pos = (490, 85)  
    draw.text(multiplier_pos, f"{multiplier}x", font=font, fill="white")
    draw.text(winnings_pos, f"₹{winnings}", font=font, fill="white")
    edited_image_path = "rspg_edited.jpg"
    img.save(edited_image_path)
    return edited_image_path
    
def generate_round_result():
    return round(random.uniform(1.0, 3.0), 2) 

def calculate_winnings(bet, multiplier):
    return round(bet * multiplier, 2)

async def run_session():
    total_winnings = {} 
    for channel in channels_to_post:
        total_winnings[channel] = 0 
        await bot.send_message(channel, "✅ **Session started starting round 1 soon**")
        await asyncio.sleep(1)
        for round_num in range(1, 6):
            await bot.send_message(channel, f"🚀 **Hold up! Starting round {round_num}...**")
            await asyncio.sleep(2)
            multiplier = generate_round_result()
            winnings = calculate_winnings(bet_amount, multiplier)
            await bot.send_message(channel, f"🚀 Bet: **{multiplier}x**")
            await asyncio.sleep(2)
            total_winnings[channel] += winnings
            edited_image = edit_image(multiplier, winnings)
            caption = f"Round {round_num} 🚀\nMultiplier: **{multiplier}x**\nWinnings: ₹{winnings}"
            markup = InlineKeyboardMarkup(
                [[InlineKeyboardButton("📊 Check Stats", url="https://rsgo.win")]]
            )
            await bot.send_photo(channel, edited_image, caption=caption, reply_markup=markup)
            await asyncio.sleep(round_intervals)
            
            await bot.send_message(channel, f"📊 **Session Summary**: \nTotal winnings after 5 rounds: ₹{total_winnings[channel]}\nSession ended.", reply_markup=markup)

async def schedule_sessions():
    while True:
        now = datetime.now().strftime("%H:%M")
        print(f"Current Time: {now}") 
        if now in session_times:
            print(f"Starting session at {now}")  
            await run_session()
        await asyncio.sleep(10)

@bot.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply("Welcome")
async def start_bot():
    await bot.start()
    asyncio.create_task(schedule_sessions()) 
    await idle()  

if __name__ == "__main__":
    bot.run(start_bot())
