def reverseVowels(s: str) -> str:
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    pos = []
    st = []

    for j, i in enumerate(s):
        if i in vowels:
            pos.append({"ind": j, "val": i})
        else:
            st.append(i)
    for i in range(len(pos)):
        ind = pos[i]["ind"]
        val = pos[-1 - i]["val"]
        st.insert(ind, val)
    return "".join(st)


print(reverseVowels(" apG0i4maAs::sA0m4i0Gp0"))
