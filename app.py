from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import os
import logging

# تنظیمات
BOT_TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_ID = int(os.environ.get("ADMIN_ID", 6236509951))

# لاگینگ
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.message.from_user
        user_info = f"👤 کاربر: {user.first_name} ({user.id})"
        
        # پاسخ به کاربر
        await update.message.reply_text("✅ پیام شما به ادمین ارسال شد")
        
        # ارسال به ادمین
        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"{user_info}\n\n📩 پیام: {update.message.text}"
        )
        
        logger.info(f"پیام از {user.first_name} ارسال شد")
        
    except Exception as e:
        logger.error(f"خطا: {e}")
        await update.message.reply_text("❌ خطا در ارسال پیام")

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 سلام! من ربات ارسال پیام ناشناس هستم.\n"
        "هر پیامی بفرستید به صورت ناشناس برای ادمین ارسال میشه."
    )

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    
    # هندلرها
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("✅ ربات فعال شد و در حال اجراست...")
    application.run_polling()

if __name__ == "__main__":
    main()
