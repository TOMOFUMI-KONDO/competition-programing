def main():
    h1, m1, h2, m2, k = map(int, input().split())

    h_diff = h2 - h1
    m_diff = m2 - m1

    if h_diff == 0:
        if m_diff >= 0:
            ans = m_diff - k
        else:
            ans = 24 * 60 + m_diff - k
    elif h_diff > 0:
        ans = h_diff * 60 + m_diff - k
    else:
        ans = 24 + h_diff + m_diff - k

    print(ans)

if __name__ == '__main__':
    main()