#模拟会员打折
vip_judge=input('是否是会员（yes/no):')
price_str=input("请输入消费金额:")
price=float(price_str)
'''
if vip_judge=='yes':
    if price<=200:
        price_vip=price*0.9
    else:
        price_vip=price-50
    print(f'尊贵的会员您好，您的支付金额为{price_vip:.2f}')
'''
if vip_judge=='yes':
    price_vip=price*0.9 if price<=200 else price-50
    print(f'尊贵的会员您好，您的支付金额为{price_vip:.2f}')
else:
    print(f'您的实际支付金额为{price:.2f}')