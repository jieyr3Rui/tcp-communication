if __name__ == "__main__":
    msg_id = 0
    while True:
        msg = input("please input")
        if not msg:
            break
        with open("test.txt","w+") as f:
            f.write(str(msg_id) + '\n' + msg)
            f.close()