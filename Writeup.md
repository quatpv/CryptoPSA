#	Tieng_Viet_Lop_1 - 10 point
📍🌏🌏🌏🌏📍📍🌏🌏📍📍🌏📍🌏📍🌏🌏📍📍🌏🌏🌏🌏🌏🌏📍📍🌏🌏🌏🌏🌏📍📍📍📍🌏📍📍🌏📍🌏🌏🌏🌏📍🌏🌏📍📍🌏📍🌏🌏📍🌏📍📍🌏📍📍📍🌏🌏📍🌏🌏🌏🌏🌏🌏🌏📍📍📍🌏🌏📍🌏🌏📍📍📍📍🌏🌏📍🌏📍🌏📍📍📍📍📍🌏📍📍🌏🌏📍📍🌏🌏📍📍🌏📍📍📍📍🌏📍📍📍🌏🌏📍🌏🌏📍📍🌏📍📍🌏📍🌏📍🌏🌏🌏🌏🌏🌏🌏📍📍📍🌏📍🌏🌏🌏📍📍📍📍📍🌏📍

Thay 📍 bằng 1, 🌏 bằng 0 chúng ta thu được:
1000011001101010011000000110000011110110100001001101001011011100100000001110010011110010101111101100110011011110111001001101101010000000111010001111101
```
>s = "1000011001101010011000000110000011110110100001001101001011011100100000001110010011110010101111101100110011011110111001001101101010000000111010001111101"
>hex(int(s, 2))[2:-1].decode('hex')
C500{Bin@ry_form@t}
```

#	Basiz - 20 point
433530307b4833785f656e633064335f736f5f426173697a
```
> "433530307b4833785f656e633064335f736f5f426173697a".decode('hex')
C500{H3x_enc0d3_so_Basiz
```

#   B453 - 30 point
🐛🐛🐛🐛🐛🐛 
SU0yVEFNRDNJSlFYR1pKV0dSUFVFWUxUTVVaVEVYWkJFRVFTQzdJPQ==
Thấy là mã hóa Base64
```
> import base64
> base64.b64decode("SU0yVEFNRDNJSlFYR1pKV0dSUFVFWUxUTVVaVEVYWkJFRVFTQzdJPQ==")
'IM2TAMD3IJQXGZJWGRPUEYLTMUZTEXZBEEQSC7I='
```
Ra được kết quả là mã hóa Base32
```
> base64.b32decode("IM2TAMD3IJQXGZJWGRPUEYLTMUZTEXZBEEQSC7I=")
'C500{Base64_Base32_!!!!}'
```

#   Rivest_Shamir_Adleman - 40 point
Mã hóa RSA cơ bản
Có c, n , d
Tính m bằng cách m = c^d mod n
```
> d = 16966096327321619672310457071395935355526719391481200335334261008715738585025786103565582893941217397221877620796266582618543533735595832669141615932122462966340150400130083229606869228801628652889581304719809448117881469645820003451457895867900897601237672097321873313255118325095923452174969082077176068821157810031149085260531712279971460308440690134813018664972609859242864265615948238687837577978844754848577847362594187077467919801027126121795140858163913731383336464062602497309393694269852594445357211642137208273373240987436424652563448895827201880686239974660121310221682375397376370042999306175406083234433
> c = 0x17e8364b2aefeaf4efe1846242126df6062d450b23d2da8926bc00ca8a1f0f7d489c782e5e8b425d9fde76f9ad4a4962ea98bf0d2c9da3ba5228d87a7077ba602f4007086cb35fd340a714f50717eb02d9d3138fe97c762e6ddc57575947f00fac5fc8dce33a0528a5ccbc85f092834eada87bcdfa1940a6b5ead4b67c7c01e72815de7f153667e659aebef7c1b4c36d235ee53508b783fdac5fe1ca259cf0f2c93287c988b10873d0f45f280c24ca41ac8171b3e2f8148ee067f38f84cbc06cb6a02d8df86b742839e899c09e3cccaea642ab796d917dc7fb7c403d1fae62b093f53e28e968e89578eec135b94c1bfa9f6fd2df37dad4bdc594d5d935ad991c
> n = 18820363151721005221127461494381777511766327162483131793784723488967558558680347729678023123226566766447701314050861933396606086161640895152971125310485948805433893648837597573099955799728712542728918245894078398803344581519602328473226068407153370448414240288459438241888975789976498566100049910834324441813615940761592864056648894843573434302913671041094373670560314850325358723555570168917554920643105097456972439091117433691089762997855483194735949140411807489824919649675086533343897434812096860465112761127100760326967951640978924127675109901824703336929961295489952888347336589919953491795685427780692569794819
> hex(pow(c, d, n))[2:-1].decode('hex')
'C500{RSA_basiz_but_n33d}'
```

#   PSA Feedback - 50 point
Có được file Base64, đem decode thấy header là file png. Vậy chuyển đổi Base64 sang Image. Vào trang [này](http://freeonlinetools24.com/base64-image) để chuyển đổi Base64 sang Image. Có được mã QR Code. Thực hiện scan file ở [đây](https://webqr.com/) để thu được flag
>C500{Image_2_Base64}

#   Dub-key - 100 point
Bruce force thu được string khi băm có 3 byte cuối là \x00\x00\x00 bằng cách sử dụng thư viện của python là Itertools. Thường là với chuỗi kí tự gồm 6 ký tự gồm toàn chữ thường thì mất khoảng 30s là ra kết quả. Điền chuỗi thu được vào file Dub-key thu được Flag

#   Old algorithm - 150 point
Đây là thuật toán mã hóa Feistel (không dùng key luôn). Do không biết chính xác vị trí của chia cắt L và R nên ta thử cho chạy bừa cắt đôi cipher ra, sau đó decode nếu được thì ra flag nếu không, thử tiếp 
```
from base64 import *

(a,b,c,d) = ()

def F(x):
    return (a*x*x + b*x + c)%d

def Decode(R, L):
    rounds = 
    for i in xrange(rounds):
        (R, L) = (L, R^F(L))
    try:
        mL = hex(L)[2:-1].decode('hex')
        mR = hex(R)[2:-1].decode('hex')
        return mL + mR
    except:
        return "Noob"

def GetLR(cipher):
    for i in xrange(2, len(cipher) - 1, 2):
        R = cipher[:i]
        L = cipher[i:]
        R = int(R, 16)
        L = int(L, 16)
        flag = Decode(R, L)
        if "C500" in flag:
            print "[+] Flag:",flag

cipher = r''
cipher = b64decode(cipher).encode('hex')
GetLR(cipher)
```

#   Cafebaby - 200 point
Chúng ta có `psa = pow(2, p - 0xcafebabe, n)` 
>   Đặt c = 0xcafebabe
>   => psa = nk + 2^(p-c)
>   => psa.2^(c-1) = 2^(c-1).n.k + 2^(p-1)
>   => psa.2^(c-1) = 2^(p-1) (modulo p)
>   => psa.2^(c-1) = 1 (modulo p) *Theo định Fermat nhỏ*
>   => psa.2^(c-1) - 1 = pk
>   => p = gcd((psa.2^(c-1) - 1) % n, n)
>   Đặt tmp = pow(2, c-1, n)
>   => p = gcd((psa.tmp - 1) % n, n)

Có `p` thì chúng ta tính toán `q`. Done!

#   ECB - 200 point
Tính chất của AES-ECB mode là kiểu 1-1 tức 2 block giống nhau, nhưng khác vị trí nhưng đều cho cùng cipher. Thế nên nếu 2 bức ảnh được encode theo AES-ECB mode mà mỗi pixel là một block thì cho ta tần số xuất hiện của các pixel có cùng giá trị sẽ lớn. Thử kiểm tra với bức đầu thấy có một số pixel có tần số xuất hiện rất nhiều khác biệt so với các pixel còn lại, tô màu chúng cho thành màu đen còn các pixel khác cho màu trắng, bức thứ 2 cũng vậy. Kết hợp 2 bức hình lại thu được flag

#   Attack in 2017 - 300 point
Là một lỗ hổng của thuật toán RSA tên ROCA phát hiện vào năm 2017(mình nhầm :D). Tool attack [roca](https://github.com/udan11/roca). Lời giải chi tiết trong file Solution.pdf
