import os

TOKEN = "504179513:AAEJT5PbCxOXwRJOjgHrTAAc9n4fQ54Tl-A"
PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)

def help_message(arguments, message):
    response = {'chat_id': message['chat']['id']}
    result = ["Hey, %s!" % message["from"].get("first_name"),
              "\rI can accept only these commands:"]
    for command in CMD:
        result.append(command)
    response['text'] = "\n\t".join(result)
    return response

def base64_decode(arguments, message):
    response = {'chat_id': message['chat']['id']}
    try:
        response['text'] = b64decode(" ".join(arguments).encode("utf8"))
    except:
        response['text'] = "Can't decode it"
    finally:
        return response

updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
updater.bot.set_webhook("https://serene-reaches-88586.herokuapp.com/" + TOKEN)
updater.idle()
