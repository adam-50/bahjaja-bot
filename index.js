const express = require("express");
const bodyParser = require("body-parser");
const axios = require("axios");

const app = express();
app.use(bodyParser.json());

const TOKEN = process.env.BOT_TOKEN;
const TELEGRAM_API = `https://api.telegram.org/bot${TOKEN}`;

app.get("/", (req, res) => {
  res.send("Bot is running 🚀");
});

app.post("/webhook", async (req, res) => {
  const message = req.body.message;

  if (!message) return res.sendStatus(200);

  const chat_id = message.chat.id;
  const text = message.text;

  if (text === "/start") {
    await axios.post(`${TELEGRAM_API}/sendMessage`, {
      chat_id,
      text: "مرحباً بك 👋 في بهججة",
      reply_markup: {
        inline_keyboard: [
          [{ text: "🌐 الموقع", url: "https://bahjaja.wuiltstore.com/" }],
          [{ text: "📝 شكوى", url: "https://forms.gle/Rk388FAJRhgWRW6r7" }],
          [{ text: "📱 التطبيق", url: "https://apkpure.com/ar/bahjaja-store/co.median.android.krxwerj" }],
          [{ text: "💬 الدعم", callback_data: "support" }]
        ]
      }
    });
  }

  res.sendStatus(200);
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log("Bot running"));
