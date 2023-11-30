#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    content = dir(hidden_4)
    for i in content:
         if not i.startwith(__):
              print(i)
