from pyrogram import Client, filters, idle
import random
import asyncio
from datetime import datetime
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from PIL import Image, ImageDraw, ImageFont
import time
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
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


def edit_final_summary_image(total_winnings, round_results):
    img_path = 'summary.jpg'  
    img = Image.open(img_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("font.ttf", 40)
    smaller_font = ImageFont.truetype("font.ttf", 30)

    summary_pos = (50, 50)  
    final_profits_pos = (40, 500)
    rounds_start_pos = 200  
    round_spacing = 10 
    draw.text((50, 10), "cricket Signal Reports", font=font, fill="white")
    total_winnings_text = f"₹{total_winnings}"
    total_winnings_box = draw.textbbox((200, 50), total_winnings_text, font=font)
    draw.rectangle(total_winnings_box, fill="black")
    draw.rounded_rectangle(total_winnings_box, outline="green", width=3, radius=3)
    draw.text((200, 50), total_winnings_text, font=font, fill="white")
    for i, result in enumerate(round_results):
        round_text = f"{result}"
        round_pos = (30 + i * 100, rounds_start_pos)  
        round_box = draw.textbbox(round_pos, round_text, font=smaller_font)
        draw.rectangle(round_box, fill="black")
        draw.rounded_rectangle(round_box, outline="green", width=3, radius=3)
        draw.text(round_pos, round_text, font=smaller_font, fill="white")
    final_message_text = "final profits from this session"
    draw.text((10, 150), final_message_text, font=font, fill="white")
    oy_image_path = f"summary_ed.jpg"
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

post_data = {}

ADMIN_USER_IDS = [1137799257] 

# /send command to start the post creation process
@bot.on_message(filters.command("send") & filters.user(ADMIN_USER_IDS))
async def send_post(client, message):
    chat_id = message.chat.id
    post_data[chat_id] = {"image": None, "caption": None, "buttons": [], "interval": None}  # Initialize empty post data

    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("📝 Create Post", callback_data="create_post")],
        [InlineKeyboardButton("❌ Cancel", callback_data="cancel_post")]
    ])
    await message.reply("Admin Panel: Use this to create and manage posts.", reply_markup=markup)

# Create Post Menu
@bot.on_callback_query(filters.regex("create_post"))
async def create_post_menu(client, callback_query):
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("🖼️ Add Image", callback_data="add_image")],
        [InlineKeyboardButton("✏️ Add Caption", callback_data="add_caption")],
        [InlineKeyboardButton("🔗 Add Button", callback_data="add_button")],
        [InlineKeyboardButton("👁️ Preview", callback_data="preview_post")],
        [InlineKeyboardButton("📅 Schedule Post", callback_data="schedule_post")],
        [InlineKeyboardButton("📤 Send Post", callback_data="send_post")],
        [InlineKeyboardButton("❌ Cancel", callback_data="cancel_post")]
    ])
    await callback_query.message.edit_text("Create and customize your post:", reply_markup=markup)

# Cancel post creation
@bot.on_callback_query(filters.regex("cancel_post"))
async def cancel_post_creation(client, callback_query):
    chat_id = callback_query.message.chat.id
    if chat_id in post_data:
        del post_data[chat_id]  # Remove the post data for this chat
    await callback_query.message.edit_text("❌ Post creation cancelled.")

# Add Image
@bot.on_callback_query(filters.regex("add_image"))
async def add_image(client, callback_query):
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("↩️ Back to Menu", callback_data="back_to_menu")]
    ])
    await callback_query.message.edit_text("Please send the image you want to add to the post.", reply_markup=markup)

@bot.on_message(filters.photo & filters.user(ADMIN_USER_IDS))
async def receive_image(client, message):
    chat_id = message.chat.id
    post_data[chat_id]["image"] = message.photo.file_id
    await message.reply("✅ Image added to the post.")

# Add Caption
@bot.on_callback_query(filters.regex("add_caption"))
async def add_caption(client, callback_query):
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("↩️ Back to Menu", callback_data="back_to_menu")]
    ])
    await callback_query.message.edit_text("Please send the caption you want to add to the post.", reply_markup=markup)

@bot.on_message(filters.text & filters.user(ADMIN_USER_IDS))
async def receive_caption(client, message):
    chat_id = message.chat.id
    post_data[chat_id]["caption"] = message.text
    await message.reply("✅ Caption added to the post.")

# Add Button
@bot.on_callback_query(filters.regex("add_button"))
async def add_button(client, callback_query):
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("↩️ Back to Menu", callback_data="back_to_menu")]
    ])
    await callback_query.message.edit_text("Please send the button text and URL in this format:\n`Text - URL`", reply_markup=markup)

@bot.on_message(filters.text & filters.user(ADMIN_USER_IDS))
async def receive_button(client, message):
    chat_id = message.chat.id
    try:
        text, url = message.text.split(" - ")
        post_data[chat_id]["buttons"].append(InlineKeyboardButton(text, url=url))
        await message.reply("✅ Button added.")
    except ValueError:
        await message.reply("❌ Invalid format. Use: `Text - URL`.")

# Preview Post
@bot.on_callback_query(filters.regex("preview_post"))
async def preview_post(client, callback_query):
    chat_id = callback_query.message.chat.id
    data = post_data.get(chat_id, {})

    if data["image"]:
        await client.send_photo(
            chat_id, 
            data["image"], 
            caption=data["caption"], 
            reply_markup=InlineKeyboardMarkup([[btn] for btn in data["buttons"]])
        )
    else:
        await callback_query.message.edit_text("No image added. Add an image or caption to preview.")

# Schedule Post
@bot.on_callback_query(filters.regex("schedule_post"))
async def schedule_post(client, callback_query):
    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("↩️ Back to Menu", callback_data="back_to_menu")]
    ])
    await callback_query.message.edit_text("Please provide the interval in minutes (e.g., `30` for 30 minutes).", reply_markup=markup)

@bot.on_message(filters.text & filters.user(ADMIN_USER_IDS))
async def set_schedule(client, message):
    chat_id = message.chat.id
    try:
        interval = int(message.text) * 60  # Convert minutes to seconds
        post_data[chat_id]["interval"] = interval
        await message.reply(f"✅ Post will be sent every {message.text} minutes.")
    except ValueError:
        await message.reply("❌ Invalid number. Please send a valid number of minutes.")

# Send Post
@bot.on_callback_query(filters.regex("send_post"))
async def send_post(client, callback_query):
    chat_id = callback_query.message.chat.id
    data = post_data.get(chat_id, {})

    if "interval" in data and data["interval"]:
        asyncio.create_task(send_post_at_intervals(client, chat_id, data))
    else:
        await send_post_now(client, chat_id, data)

    await callback_query.message.edit_text("✅ Post has been sent.")

# Send post immediately
async def send_post_now(client, chat_id, data):
    if data["image"]:
        await client.send_photo(
            chat_id, 
            data["image"], 
            caption=data["caption"], 
            reply_markup=InlineKeyboardMarkup([[btn] for btn in data["buttons"]])
        )
    else:
        await client.send_message(chat_id, data["caption"], reply_markup=InlineKeyboardMarkup([[btn] for btn in data["buttons"]]))

# Send post at intervals
async def send_post_at_intervals(client, chat_id, data):
    interval = data["interval"]
    while True:
        await send_post_now(client, chat_id, data)
        await asyncio.sleep(interval)

# Back to Menu
@bot.on_callback_query(filters.regex("back_to_menu"))
async def back_to_menu(client, callback_query):
    await create_post_menu(client, callback_query)

@bot.on_message(filters.text & filters.user(ADMIN_USER_IDS))
async def set_schedule(client, message):
    chat_id = message.chat.id
    try:
        interval = int(message.text) * 60  # Convert minutes to seconds
        post_data[chat_id]["interval"] = interval
        await message.reply(f"✅ Post will be sent every {message.text} minutes.")
    except ValueError:
        await message.reply("❌ Invalid number. Please send a valid number of minutes.")

# Send Post
@bot.on_callback_query(filters.regex("send_post"))
async def send_post(client, callback_query):
    chat_id = callback_query.message.chat.id
    data = post_data.get(chat_id, {})

    if "interval" in data and data["interval"]:
        asyncio.create_task(send_post_at_intervals(client, chat_id, data))
    else:
        await send_post_now(client, chat_id, data)

    await callback_query.message.edit_text("✅ Post has been sent.")

# Send post immediately
async def send_post_now(client, chat_id, data):
    if data["image"]:
        await client.send_photo(
            chat_id, 
            data["image"], 
            caption=data["caption"], 
            reply_markup=InlineKeyboardMarkup([[btn] for btn in data["buttons"]])
        )
    else:
        await client.send_message(chat_id, data["caption"], reply_markup=InlineKeyboardMarkup([[btn] for btn in data["buttons"]]))

# Send post at intervals
async def send_post_at_intervals(client, chat_id, data):
    interval = data["interval"]
    while True:
        await send_post_now(client, chat_id, data)
        await asyncio.sleep(interval)

bot.run()
        
async def start_bot():
    await bot.start()
    asyncio.create_task(run_session()) 
    await idle()  

if __name__ == "__main__":
    bot.run(start_bot())
