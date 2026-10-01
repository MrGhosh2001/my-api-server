from flask import Flask, jsonify

app = Flask(__name__)

# Link ka custom route: /pub/rupamlive/api
@app.route('/pub/rupamlive/api', methods=['GET'])
def home():
    return jsonify({
        "status": "success",
        "creator": "Rupam",
        "message": "Welcome to Rupam's Official API!"
    })
    async def num_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if not text.isdigit() or len(text) != 10:
        await update.message.reply_text("❌ ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴀ ᴠᴀʟɪᴅ 10 ᴅɪɢɪᴛ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ")
        return

    msg = await update.message.reply_text("🔍 sᴇᴀʀᴄʜɪɴɢ... ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ")

    try:
        res = requests.get(
            API_URL,
            params={"num": text, "key": API_KEY},
            timeout=30
        )
        data = res.json()
    except Exception as e:
        await msg.edit_text(f"❌ ᴇʀʀᴏʀ: {e}")
        return

    pretty = json.dumps(data, indent=2, ensure_ascii=False)

    LIMIT = 4000
    parts = [pretty[i:i + LIMIT] for i in range(0, len(pretty), LIMIT)]

    try:
        await msg.edit_text(
            f"
            parse_mode="Markdown",
            reply_markup=get_result_keyboard()
        )
        for part in parts[1:]:
            await update.message.reply_text(
                f"
json\n{part}\n```",
                parse_mode="Markdown",
                reply_markup=get_result_keyboard()
            )
    except Exception as e:
        try:
            await msg.edit_text(pretty, reply_markup=get_result_keyboard())
        except Exception:
            await update.message.reply_text(
                f"❌ sᴇɴᴅ ᴇʀʀᴏʀ: {e}",
                reply_markup=get_result_keyboard()
            )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
