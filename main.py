from LC.lru import LRUCache

def main():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))       
    cache.put(3, 3)
    print(cache.get(2))
    print(cache.get(3))

    


if __name__ == "__main__":
    main()
