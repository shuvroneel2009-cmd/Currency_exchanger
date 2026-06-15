# Currency_exchanger
This is my third project.  I hope you will like this


# Offline-First Currency Converter

A Python command-line application that fetches real-time currency exchange rates and performs conversions. If the user is offline or the API request fails, the application gracefully switches to an offline fallback mode using locally cached historical data.

## 🚀 Features

*   **Real-Time Data**: Fetches up-to-date conversion rates directly from the ExchangeRate-API.
*   **Offline Fallback**: Seamlessly switches to locally stored data when internet connectivity is lost.
*   **Robust Input Validation**: Built-in continuous terminal prompt validation to prevent user entry crashes.
*   **Persistent Tracking**: Local tracking system that saves conversion history directly to a local JSON file.
*   **Error Management**: Dedicated feedback system mapping low-level connection failures and HTTP status codes.

## 📂 Project Structure

*   `main.py`: The entry point managing the operational flow, network requests, and application loops.
*   `functions.py`: core backend logic containing file handlers, string formatters, and mathematical conversion algorithms.
*   `just_clearing_main.py`: Modularized status code and exception handler processing network diagnostics.

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd YOUR_REPOSITORY_NAME
   ```

2. **Install dependencies:**
   This project uses the external Python `requests` library to handle live API connections.
   ```bash
   pip install requests
   ```

3. **Run the application:**
   ```bash
   python main.py
   ```

## 💻 How It Works

1. **Network Initialization**: The app makes an API request to fetch live currency conversion rates.
2. **Error Recovery**: If the connection drops, it assigns a custom internal status code (`1000`) and checks your local storage history.
3. **User Selection**: If valid offline data exists, you will be asked if you want to use the cached exchange rates.
4. **Calculations**: Inputs are converted to uppercase, validated for exact types, and calculated dynamically across any target currency keys.
5. **Persistence**: History logs and the latest currency map data are updated and written back down to `user_history.json`.

## ⚙️ Technologies Used

*   **Python 3**
*   **Requests HTTP Library**
*   **JSON Serialization Backend**
*   **ExchangeRate-API Endpoint Data**
