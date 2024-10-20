from pyrogram import Client, filters, idle
import random
import asyncio
from datetime import datetime
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from PIL import Image, ImageDraw, ImageFont
import time
#MDB =
API_ID = "7980140"  
API_HASH = "db84e318c6894f560a4087c20c33ce0a"  
BOT_TOKEN = "7123013710:AAGUUb-cirJUhvUNIFar91zAKTGo7h6WkNs"  
bot = Client("aviator_betting_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

bet_amount = 1000 
session_times = ["09:00", "11:00", "13:00", "15:00", "17:00", "19:00", "21:00", "23:00"] #international
channels_to_post = ["@HowToDownIoadLink"] 
round_intervals = 5  
def edit_image(multiplier, winnings):
    img_path = 'rsgo.jpg'  
    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("font.ttf", 40)  
    multiplier_pos = (230, 86)  
    winnings_pos = (480, 86)  
    draw.text(multiplier_pos, f"{multiplier}x", font=font, fill="white")
    draw.text(winnings_pos, f"₹{winnings}", font=font, fill="white")
    edikd_image_path = "rspg_edd.jpg"
    img.save(edikd_image_path)
    return edikd_image_path
    
def generate_round_result():
    return round(random.uniform(1.0, 3.0), 2) 

def calculate_winnings(bet, multiplier):
    return round(bet * multiplier, 2)

# Use this library at the top if not already included
from PIL import Image, ImageDraw, ImageFont
 
def edit_final_summary_image(total_winnings, round_results):
    img_path = 'summary.jpg'  # Path to the summary image
    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("font.ttf", 40)
    smaller_font = ImageFont.truetype("font.ttf", 30)

    # Positions for text and rectangles
    summary_pos = (50, 50)  
    final_profits_pos = (40, 500)
    rounds_start_pos = 200  
    round_spacing = 10 

    # Draw the title
    draw.text((50, 10), "Aviator Signal Reports", font=font, fill="white")

    # Total winnings text with black background and green rectangle around it
    total_winnings_text = f"₹{total_winnings}"
    total_winnings_box = draw.textbbox((200, 50), total_winnings_text, font=font)
    
    # Draw black background first
    draw.rectangle(total_winnings_box, fill="black")
    # Then draw green rectangle outline
    draw.rounded_rectangle(total_winnings_box, outline="green", width=7, radius=10)
    # Finally, draw the total winnings text on top
    draw.text((200, 50), total_winnings_text, font=font, fill="white")

    # Draw the round results with black background and green rectangle around each multiplier
    for i, result in enumerate(round_results):
        round_text = f"{result}"
        round_pos = (20 + i * 100, rounds_start_pos)  # Spread horizontally
        round_box = draw.textbbox(round_pos, round_text, font=smaller_font)
        
        # Draw black background first
        draw.rectangle(round_box, fill="black")
        # Then draw green rectangle outline
        draw.rounded_rectangle(round_box, outline="green", width=7, radius=10)
        # Finally, draw the round result text on top
        draw.text(round_pos, round_text, font=smaller_font, fill="white")

    # Final message text
    final_message_text = "FINAL PROFITS FROM THIS SESSION"
    draw.text((30, 1600), final_message_text, font=font, fill="white")

    # Save the edited image
    oy_image_path = f"summary_edited.jpg"
    img.save(oy_image_path)
    return oy_image_path

async def run_session():
    total_winnings = {}
    round_results = {}
    for channel in channels_to_post:
        total_winnings[channel] = 0
        round_results[channel] = []

        await bot.send_message(channel, "✅ **Session starting round 1 soon**")
        await asyncio.sleep(1)
        for round_num in range(1, 6):
            await bot.send_message(channel, f" **Hold up! Starting round {round_num}...**")
            await asyncio.sleep(1)
            multiplier = generate_round_result()
            winnings = calculate_winnings(bet_amount, multiplier)
            total_winnings[channel] += winnings
            round_results[channel].append(f"{multiplier}x ")
            await bot.send_message(channel, f" Bet: **{multiplier}x**")
            await asyncio.sleep(1)
            edited_image = edit_image(multiplier, winnings)
            caption = f"Round {round_num} \nMultiplier: **{multiplier}x**\nWinnings: ₹{winnings}"
            markup = InlineKeyboardMarkup([[InlineKeyboardButton(" Check Stats", url="https://rsgo.win")]])
            await bot.send_photo(channel, edited_image, caption=caption, reply_markup=markup)
            await asyncio.sleep(round_intervals)

          
        final_summary_image = edit_final_summary_image(total_winnings[channel], round_results[channel])
        final_summary = "\n".join(round_results[channel])
        final_message = (
            f"📊 **Session Summary**: \n"
            f"{final_summary}\n"
            f"Total winnings after 5 rounds: ₹{total_winnings[channel]}\n"
            f"Session ended."
        )
        await bot.send_photo(channel, final_summary_image, caption=final_message, reply_markup=markup)


    
   #    ''' final_message = (
        #    f" **Session Summary**: \n"
     #       f"Total winnings after 5 rounds: ₹{total_winnings[channel]}\n"
   ###      await bot.send_photo(channel, final_summary_image, caption=final_message, reply_markup=markup)'''


'''async def run_session():
    total_winnings = {} 
    round_results = {}  

    for channel in channels_to_post:
        total_winnings[channel] = 0
        round_results[channel] = []  
        await bot.send_message(channel, "✅ **Session starting round 1 soon**")
        await asyncio.sleep(15)

        for round_num in range(1, 6):
            await bot.send_message(channel, f"🚀 **Hold up! Starting round {round_num}...**")
            await asyncio.sleep(10)

            multiplier = generate_round_result()
            winnings = calculate_winnings(bet_amount, multiplier)
            total_winnings[channel] += winnings

            round_results[channel].append(f"✅**Round {round_num}  ₹{winnings}**")

            await bot.send_message(channel, f"🚀 Bet: **{multiplier}x**")
            await asyncio.sleep(30)

            edited_image = edit_image(multiplier, winnings)
            caption = f"Round {round_num} 🚀\nMultiplier: **{multiplier}x**\nWinnings: ₹{winnings}"
            markup = InlineKeyboardMarkup([[InlineKeyboardButton("📊 Check Stats", url="https://rsgo.win")]])
            await bot.send_photo(channel, edited_image, caption=caption, reply_markup=markup)

            await asyncio.sleep(round_intervals)

        final_summary = "\n".join(round_results[channel])
        final_message = (
            f"📊 **Session Summary**: \n"
            f"{final_summary}\n"
            f"Total winnings after 5 rounds: ₹{total_winnings[channel]}\n"
            f"Session ended."
        )
        await bot.send_message(channel, final_message, reply_markup=markup)'''

         
async def schedule_sessions():
    while True:
        now = datetime.now().strftime("%H:%M")
        print(f"Current") 
        if now in session_times:
            print(f"Starting")  
            await run_session()
        await asyncio.sleep(30)

@bot.on_message(filters.command("start"))
async def start(client, message):
    if message.chat.type == "private":
        await message.reply("Welcome.")
    else:
        await message.reply("Welcome.")
        
async def start_bot():
    await bot.start()
    asyncio.create_task(run_session()) 
    await idle()  

if __name__ == "__main__":
    bot.run(start_bot())
