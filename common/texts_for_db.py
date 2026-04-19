from aiogram.utils.formatting import Bold, as_list, as_marked_section

categories = ['Food', 'Drinks']

description_for_info_pages = {
    "main": "Welcome!",
    "about": "Such-and-Such Pizzeria.\nWorking hours - 24/7.",
    "payment": as_marked_section(
        Bold("Payment options:"),
        "Card in the bot",
        "Card/Cash on delivery",
        "In the establishment",
        marker="✅ ",
    ).as_html(),
    "shipping": as_list(
        as_marked_section(
            Bold("Delivery/Order options:"),
            "Courier",
            "Takeaway (I'm coming to pick it up)",
            "Dine-in (I'll be there soon)",
            marker="✅ ",
        ),
        as_marked_section(
            Bold("Not allowed:"),
            "Post / Mail",
            "Pigeons",
            marker="❌ "
        ),
        sep="\n----------------------\n",
    ).as_html(),
    'catalog': 'Categories:',
    'cart': 'Your cart is empty!'
}