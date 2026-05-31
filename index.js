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

  const update = req.body;

  // =========================
  // MESSAGE HANDLER
  // =========================
  if (update.message) {
    const message = update.message;
    const chat_id = message.chat.id;
    const text = message.text;

    if (text === "/start") {
      await axios.post(`${TELEGRAM_API}/sendMessage`, {
        chat_id,
        text: "مرحباً بك 👋 في بهججة\nاختر الخدمة:",
        reply_markup: {
          inline_keyboard: [
            [{ text: "🌐 الموقع", url: "https://bahjaja.wuiltstore.com/" }],
            [{ text: "📝 شكوى", url: "https://forms.gle/Rk388FAJRhgWRW6r7" }],
            [{ text: "📱 التطبيق", url: "https://apkpure.com/ar/bahjaja-store/co.median.android.krxwerj" }],
            [{ text: "🤖 مساعد ذكي", callback_data: "ai" }],
            [{ text: "👨‍💼 موظف بشري", callback_data: "human" }]
          ]
        }
      });
    } else {
      // أي رسالة عادية
      await axios.post(`${TELEGRAM_API}/sendMessage`, {
        chat_id,
        text: `🤖 استلمت رسالتك:\n\n${text}\n\nاختر الخدمة من /start`
      });
    }
  }

  // =========================
  // CALLBACK HANDLER
  // =========================
  if (update.callback_query) {

    const callback = update.callback_query;
    const chat_id = callback.message.chat.id;
    const data = callback.data;

    // زر المساعد الذكي
    if (data === "ai") {
      await axios.post(`${TELEGRAM_API}/sendMessage`, {
        chat_id,
        text: "🤖 أنت الآن في وضع المساعد الذكي\nاكتب سؤالك وسأحاول مساعدتك."
      });
    }

    // زر الموظف
    if (data === "human") {
      await axios.post(`${TELEGRAM_API}/sendMessage`, {
        chat_id,
        text: "👨‍💼 تم تحويلك للدعم البشري\nسيتم الرد عليك قريبًا من أحد الموظفين."
      });
    }

    // تأكيد الضغط
    await axios.post(`${TELEGRAM_API}/answerCallbackQuery`, {
      callback_query_id: callback.id
    });
  }

  res.sendStatus(200);
});

// =========================
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log("Bot running"));
