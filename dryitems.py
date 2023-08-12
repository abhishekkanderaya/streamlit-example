import streamlit as st
import telegram
import asyncio
from telegram import Bot

# Your Telegram Bot API token
TELEGRAM_API_TOKEN = "6028401929:AAE222gMeVVvuBcBh5KLtD_Y6dxBh74YPcE"

# Your Telegram chat ID
CHAT_ID = "21141089"

async def main():
    st.title("Mobile-Friendly Order App")

    # List of items from the dry items weekly indent list
    items = [
        "Aachi Bajji Bonda Powder",
        "Aam Panna",
        "Amruttulya Set",
        "Ashwagandha Green Tea",
        "Ashwagandha Tea",
        "Bhaji",
        "Ceramic cups L",
        "Ceramic cups M",
        "Ceramic cups S",
        "Chocolate Powder",
        "Chocolate Sauce",
        "Chocolate Softie Premix",
        "Chocolate Tea",
        "Coffee Extract",
        "Coffee Frappe Powder",
        "Cold Coffee Powder",
        "Gudwali",
        "Gudwali Masala",
        "Hibiscus Tea",
        "Jaljira",
        "Kashmiri Chai",
        "Kit Kat",
        "Kolkata Merchendise",
        "Kullad Cups",
        "Lemon Ice Tea",
        "Lemon Tea",
        "Maggi",
        "Mango Crush",
        "Missal",
        "Nimbu Paani",
        "Oreo Biscuit",
        "Perfekt Badam Powder",
        "Perfekt Chat Masala",
        "Perfekt Chilly Powder",
        "Perfekt Coriander Powder",
        "Perfekt Garam Masala",
        "Poha",
        "Rose Sharbat",
        "Salt",
        "Strawberry Crush",
        "Sugar Masala Sachet",
        "Sugar Sachet",
        "Vadapav Chutney Powder",
        "Vanilla Frappe Powder",
        "Vanilla Softie Premix",
        "Vanilla Waffle Cone Premix",
        "Water Bottle"
    ]

    ordered_items = []

    st.write("Select the quantity of items:")
    for index, item in enumerate(items):
        quantity = st.number_input(f"{item} - Qty:", value=0, min_value=0, key=f"{item}_input_{index}")
        ordered_items.append((item, quantity))

    if st.button("Submit"):
        st.write("Ordered Items:")
        for ordered_item in ordered_items:
            item, quantity = ordered_item
            if quantity > 0:
                st.write(f"{item} - Qty: {quantity}")
                st.empty()  # Insert an empty space for separation

        # Send the order to Telegram and await the response
        response = await send_order_to_telegram(ordered_items)
        st.success("Order sent to Telegram!")
        st.write("Telegram API response:", response)

async def send_order_to_telegram(ordered_items):
    try:
        order_text = "Ordered Items:\n"
        for item, quantity in ordered_items:
            if quantity > 0:
                order_text += f"{item} - Qty: {quantity}\n"
        
        bot = Bot(token=TELEGRAM_API_TOKEN)  # Use the token from the constant
        response = await bot.send_message(chat_id=CHAT_ID, text=order_text)  # Use the chat_id from the constant and await the response
        return response  # Return the response
    except Exception as e:
        return str(e)  # Return the error message

if __name__ == "__main__":
    asyncio.run(main())