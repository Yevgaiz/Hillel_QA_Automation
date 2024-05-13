def list_item_generator(lst, iter_num=None):
    if iter_num is None:
        while True:
            for item in lst:
                yield item
    else:
        for _ in range(iter_num):
            for item in lst:
                yield item


lst = ['a', 'b']
for i in list_item_generator(lst, iter_num=2):
    print(i)
