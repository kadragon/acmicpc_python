def main():
    o_str = "aiyeoubkxznhdcwgpvjqtsrlmfAIYEOUBKXZNHDCWGPVJQTSRLMF"
    t_str = "eouaiypvjqtsrlmfbkxznhdcwgEOUAIYPVJQTSRLMFBKXZNHDCWG"

    while True:
        try:
            t = input()

            for c in t:
                if c in o_str:
                    print(t_str[o_str.index(c)], end="")
                else:
                    print(c, end="")

            print()
        except:
            break


if __name__ == "__main__":
    main()
