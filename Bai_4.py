# nhập độ dài cạnh đáy và chiều cao 
a,h=map(float,input("nhập các số đo:").split())

# tính diện tích xung quanh hình chóp tứ giác đều 
Sxq=a*2*h
dien_tich_xq=round(Sxq,2)
print("diện tích xung quanh hình chóp tứ giác đều là:", dien_tich_xq)

# tính diện tích toàn phần 
Stp=Sxq+a**2
dien_tich_tp=round(Stp,2)
print("diện tích toàn phần hình chóp tứ giác đều là:", dien_tich_tp)

# tính thể tích 
V=1/3 * a**2 *h
the_tich=round(V,2)
print("thể tích hình chóp tứ giác đều là:", the_tich)
