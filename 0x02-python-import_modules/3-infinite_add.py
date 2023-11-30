#!/usr/bin/python3
if __name__ == "__main__":
    import sys
  
    all_arg = 0
    for i in range(0, len(sys.argv) +1):
      if i != 0:
      all_arg += int(sys.argv[i]) 
    print(all_arg)
