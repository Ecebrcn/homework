def shut_down(s):
    if s == "yes":
        result = "Shutting down"
        print(result)
    elif s == "no":
        result = "Shutdown aborted"
        print(result)
    else:
        result = "Sorry"
        print(result)


shut_down("yes")
