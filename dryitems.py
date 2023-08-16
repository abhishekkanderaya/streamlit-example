import streamlit as st
import telegram
import asyncio
from telegram import Bot

# Your Telegram Bot API token
TELEGRAM_API_TOKEN = "6028401929:AAE222gMeVVvuBcBh5KLtD_Y6dxBh74YPcE"

# Your Telegram chat ID
CHAT_ID = "21141089"

# List of items for each section
item_data = {
"Bakery Items": [
    "Pav",
    "Burger Bun",
    "Sweet Bun",
    "Veg Roll",
    "Gobi Roll"
],
"Dry Items": [
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
],
    "Frozen Items": [
        "Batata Vada (20 pieces / packet)",
    "Breaded Batata Vada (20 pieces / packet)",
    "Punjabi Samosa (15 pieces / packet)",
    "French Fries 9 mm (2.5 kg / packet)",
    "Sabudhana Vada (20 pieces / packet)",
    "Potato Patty (20 pieces / packet)",
    "Paneer Patty (12 pieces / packet)",
    "Felafel Patty (20 pieces / packet)",
    "Chilly Patty (20 pieces / packet)",
    "Veg Patty (20 pieces / packet)",
    "Bbq Sauce (1 Kg / packet)",
    "Schezwan Sauce (1 Kg / packet)",
    "Tandoori Sauce (1 Kg / packet)",
    "Peri Peri Sauce (1 Kg / packet)",
    "Cheese Sauce (1 Kg / packet)",
    "Mexican Salsa Sauce (1 Kg / packet)",
    "Garlic Mayo Sauce (1 Kg / packet)",
    "Eggless Mayonnaise (1 Kg / packet)",
    "Chipotle Sauce (1 Kg / packet)",
    "Snack Dressing (1 Kg / packet)",
    "Tomato Sachets (100 Packets)",
    "Chilli Garlic Spread (1 Kg / packet)",
    "Cheese Slice ( 50 slices / packet)",
    "Butter ( 500 gms / packet)",
    "Felafel Nuggets (88 pieces)",
    "Thousand Island Sauce (1 Kg / packet)",
    "Gobi Paratha (10 pieces / packet)",
    "Aloo Paratha (10 pieces / packet)",
    "Veg Paratha (10 pieces / packet)",
    "Misal",
    "Poha"
]
}



async def main():
    st.title("Dry Items Order App")

    # Dropdown menu for selecting the location
    selected_location = st.selectbox("Select Location:", ["VV Mohalla", "NIE", "Agrahara", "Kuvempunagar", "Hyd - Pragathi", "Siddartha Layout", "Depot"])

    st.write(f"Ordering from: {selected_location}")

    selected_items = {}

    for section, items in item_data.items():
        st.subheader(section)
        search_query = st.text_input(f"Search {section}:", key=f"{section}_search")
        filtered_items = [item for item in items if search_query.lower() in item.lower()]

        for item in filtered_items:
            quantity = st.number_input(f"{item} - Qty:", value=0, min_value=0, key=f"{item}_input")
            if quantity > 0:
                selected_items[item] = quantity

    if st.button("Submit"):
        st.write("Ordered Items:")
        for item, quantity in selected_items.items():
            st.write(f"{item} - Qty: {quantity}")
            st.empty()  # Insert an empty space for separation

        # Send the order to Telegram and await the response
        response = await send_order_to_telegram(selected_items, selected_location)
        st.success("Thank You For Placing Your Order\n")
        st.subheader("Please clear outstanding dues for order processing.")

async def send_order_to_telegram(ordered_items, selected_location):
    try:
        order_text = f"Order from: {selected_location}\n\nOrdered Items:\n"
        for item, quantity in ordered_items.items():
            if quantity > 0:
                order_text += f"{item}  X {quantity}\n"
        
        bot = Bot(token=TELEGRAM_API_TOKEN)
        response = await bot.send_message(chat_id=CHAT_ID, text=order_text)
        return response
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    asyncio.run(main())
