# Function Calling Demo with OpenAI GPT-4 🚀

This is a simple demo that shows how to use **OpenAI Function Calling** to make AI take real-world actions.

In this example:
👉 The AI calls a `get_current_weather(location)` function  
👉 The function returns weather data (you can connect it to a real API later)  
👉 The AI uses the result to generate a natural response  

---

## 💻 How It Works

1️⃣ User asks: **"What's the weather in Minneapolis?"**  
2️⃣ GPT **decides to call** `get_current_weather(location)`  
3️⃣ The Python app runs the function  
4️⃣ GPT generates final answer using the function result  

---

## 📁 Files

- `functionCallEx.py` → main Python code  
- `.env` → your API key goes here:  
