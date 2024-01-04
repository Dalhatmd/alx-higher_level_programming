#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lis = sys.argv[1:]
    nums = [int(items) for items in lis]

    print(sum(nums))
