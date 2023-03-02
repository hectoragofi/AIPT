from chatgpt_wrapper import ChatGPT

def callChat(userPrompt):
    print("start")
    bot = ChatGPT()
    #userPrompt = 'Dog'
    prompt = userPrompt

    sampleFile = "[\
        {\
          'title': ,\
          'subtitle': ,\
          'image':,\
          'bullets': []\
        },\
        {\
          'title':,\
          'subtitle':,\
          'image':,\
          'bullets': []\
        },\
        {\
          'title':,\
          'subtitle':,\
          'image':,\
          'bullets': []\
        }\
    ]"
    finalPrompt =  f" {userPrompt} - use this quote to create a structured and engaging powerpoint presentation." \
              "Make it so that it can be directly used in power point. Each slide needs a title subtitle bullet points and an image prompt In a json form." \
              " the image prompt should just be a prompt that can be used as an idea for an image, not a photo neither a link to a photo, it should just be a prompt for a photo. " \
              "The first slide should just have a title subtitle and image. Also generate it in a code snippet. " \
              "Bullet-points in the json file should be labeled bullets and the image should just be labled image." \
              f" Only reply with the json file nothing else. All the above should be in a code snippet. Here is a sample {sampleFile}"

    response = bot.ask(finalPrompt)

    print(response)  # prints the response from chatGPT
    removeChar = "'"
    response = response.replace(removeChar, "")
    removeChar = "`"
    response = response.replace(removeChar, "")
    response = response.replace("json", "")
    f = open("response.json", "a")
    f.write(response)
    f.close()
