import os 

files = os.listdir('./nodanger')

for file in files:
    if file.endswith('.png'):
        if os.path.exists("./nodanger/png"):
            os.rename("./nodanger/"+file, "./nodanger/png/" + file)
        else:
            os.makedirs("./nodanger/png")
            os.rename("./nodanger/"+file, "./nodanger/png/" + file)
    elif file.endswith('.log'):
        if os.path.exists("./nodanger/log"):
            os.rename("./nodanger/"+file, "./nodanger/log/" + file)
        else:
            os.makedirs("./nodanger/log")
            os.rename("./nodanger/"+file, "./nodanger/log/" + file)
    elif file.endswith('.txt'):
        print(file)
        if os.path.exists("./nodanger/"+file):
            os.remove("./nodanger/"+file)