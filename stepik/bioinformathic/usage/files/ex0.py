#  Вам дается текстовый файл, содержащий некоторое количество непустых строк.
# На основе него сгенерируйте новый текстовый файл, содержащий те же строки в обратном порядке.

with open('dataset_24465_4.txt') as inf:
    data = list(map(str.rstrip, inf.readlines()))

with open('out.txt','w') as ouf:
    for line in data[::-1]:
        print(line,file=ouf)