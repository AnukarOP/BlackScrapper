import random
import time
from telethon import TelegramClient, events
import re
import aiohttp
import asyncio

api_id = 'API_ID_HERE'  # Replace with your api id
api_hash = 'API_HASH_HERE'  # Replace with your api hash
phone_number = '+12104578956'  # Replace with your phone number

client = TelegramClient('black_scrapper', api_id, api_hash)

BIN_API_URL = 'https://bins.antipublic.cc/bins/{}'

# Function to filter card information using regex
def filter_cards(text):
    regex = r'\d{16}.*\d{3}'
    matches = re.findall(regex, text)
    return matches

# Function to perform BIN lookup
async def bin_lookup(bin_number):
    bin_info_url = BIN_API_URL.format(bin_number)
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        async with session.get(bin_info_url) as response:
            if response.status == 200:
                try:
                    bin_info = await response.json()
                    return bin_info
                except aiohttp.ContentTypeError:
                    return None
            else:
                return None

# Event handler for new messages
@client.on(events.NewMessage)
async def astro(event):
    try:
        message = event.message
        # Regex to match approved messages
        if re.search(r'(Approved!|Charged|authenticate_successful|𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱|- 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅|APPROVED|New Cards Found By Scrapper|ꕥ Extrap [☭]|• New Cards Found By JennaS>            
        filtered_card_info = filter_cards(message.text)
            if not filtered_card_info:
                return

            start_time = time.time()  # Start timer

            for card_info in filtered_card_info:
                bin_number = card_info[:6]
                bin_info = await bin_lookup(bin_number)
                if bin_info:
                    brand = bin_info.get("brand", "N/A")
                    card_type = bin_info.get("type", "N/A")
                    level = bin_info.get("level", "N/A")
                    bank = bin_info.get("bank", "N/A")
                    country = bin_info.get("country_name", "N/A")
                    country_flag = bin_info.get("country_flag", "")

                    # Calculate time taken with random addition
                    random_addition = random.uniform(0, 10) + 10  # Add random seconds between 10 and 20
                    time_taken = time.time() - start_time + random_addition
                    formatted_time_taken = f"{time_taken:.2f} 𝐬𝐞𝐜𝐨𝐧𝐝𝐬"
                  
                    # Format the message
                    formatted_message = (
                        f"**[-]**(t.me/blackheadsop) 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅\n\n"
                        f"**[-]**(t.me/blackheadsop) 𝗖𝗮𝗿𝗱: `{card_info}`\n"
                        f"**[-]**(t.me/blackheadsop) 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Braintree Auth 4\n"
                        f"**[-]**(t.me/blackheadsop) 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: `1000: Approved`\n\n"
                        f"**[-]**(t.me/blackheadsop) 𝗜𝗻𝗳𝗼: {brand} - {card_type} - {level}\n"
                        f"**[-]**(t.me/blackheadsop) 𝐈𝐬𝐬𝐮𝐞𝐫: {bank}\n"
                        f"**[-]**(t.me/blackheadsop) 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {country} {country_flag}\n\n"
                        f"𝗧𝗶𝗺𝗲: {formatted_time_taken}"
                    )

                    # Send the formatted message
                    await client.send_message('PUBLI_CHANNEL_USERNAME', formatted_message, link_preview=False)
                    await asyncio.sleep(30)  # Wait for 30 seconds before sending the next message
    except Exception as e:
        print(e)

# Main function to start the client
async def main():
    await client.start(phone=phone_number)
    print("Client Created")
    await client.run_until_disconnected()

# Run the main function
asyncio.run(main())
