import random

wt = ('ドド', 'スコ')
t = (
    # dummy
    (),
    # st.1
    (2, 1), #ドド
    # st.2
    (2, 3), #スコ
    # st.3
    (2, 4), #スコ
    # st.4
    (2, 1), #スコ
)

cur_st = [1]
nxt_st = [1]
[
    [
        [
            cur_st.append(nxt_st.pop()),
            cur_st.pop(0),
            nxt_st.append(t[cur_st[0]][w]),
            print(wt[w], end=''),
            print('❤❤ラブ注入❤❤', end='') if cur_st[0] == 4 and w == 1 else None,
        ]
        for w in (random.choice((0,1)),)
    ]
    for i in range(0,1000)
]

