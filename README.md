# 🧙‍♂️ Magic: The Gathering Card and Price Tracker

A Python-based data pipeline for collecting, storing, and analyzing **Magic: The Gathering** card data and price history. This project pulls card metadata from **MTGJSON** ,bulk price data every 12 hours and images from the **Scryfall API**, saving it to a PostgreSQL database for analysis and deck cost tracking.

---

## 📦 Features

- ✅ Load all card metadata from MTGJSON
- ✅ Pull 90-day and current price data from Scryfall
- ✅ Store and update daily price data in PostgreSQL
- ✅ Normalize card printings and price history
- ✅ (Planned) Track and compare MTG deck costs over time

---

## 🛠️ Technologies Used

- **Python** (pandas, requests, sqlalchemy)
- **PostgreSQL**
- **MTGJSON** (https://mtgjson.com/)
- **Scryfall API** (https://scryfall.com/docs/api)
- (Optional) Streamlit or Flask for future 

---

## ⚠️Disclaimer⚠️
Card data provided by [MTGJSON](https://mtgjson.com/) and [Scryfall](https://scryfall.com/).
This project is not affiliated with or endorsed by Wizards of the Coast.
