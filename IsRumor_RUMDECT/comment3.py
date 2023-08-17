import jieba


def dosomething(start, end):
    counts = {}
    k = start
    while k < end:
        words = jieba.lcut(ls[k][1])
        for word in words:
            if len(word) < 2 or word in ex or word.isdigit():
                continue
            else:
                counts[word] = counts.get(word, 0) + 1
        k += 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    for m in range(15):
        word, count = items[m]
        print('{}: {}'.format(word, count))


with open('comment.csv', 'r', encoding='GBK') as f:
    ls = [i.strip().split(',', maxsplit=1) for i in f.readlines()[1:]]
ex = ['不错', '比较', '可以', '感觉', '没有', '我们', '就是', '还是', '非常', '但是', '不过', '有点', '一个', '一般',
      '下次',
      '携程', '不是', '晚上', '而且', '他们', '什么', '不好', '时候', '知道', '这样', '这个', '还有', '总体', '位置',
      '客人',
      '因为', '如果', '这里', '很多', '选择', '居然', '不能', '实在', '不会',
      '这家', '结果', '发现', '竟然', '已经', '自己', '问题', '不要', '地方', '只有', '第二天', '酒店', '房间', '虽然']

n = input()
good = 0
total = len(ls)
sums = 0

if n in ["好评", "差评", "总评", "平均"]:
    for i in ls:
        if i[0] == '1':
            good += 1
    if n == "总评":
        print("总评论:", total)
        print("好评:", good)
        print("差评:", total - good)
    elif n == "平均":
        for i in ls:
            sums += len(i[1])
        print(sums // total)
    elif n == "好评":
        dosomething(0, good)
    elif n == "差评":
        dosomething(good, total)
else:
    print("无数据")