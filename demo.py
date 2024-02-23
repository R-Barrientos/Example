from talker import Talker


def main():
    # this is an addition
    print("This is the modified code.")
    t = Talker()
    t.speak("Hi")
    t.speak("This is speaking very loudly", True)


if __name__ == "__main__":
    main()
