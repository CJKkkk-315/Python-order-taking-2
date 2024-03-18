def process_salary(person_info):
    l = sorted(person_info.items(),key=lambda x:x[1],reverse=True)
    m = l[0][0]
    avg = sum([i[1] for i in l])/len(l)
    return person_info,avg,m
person_info = {'玛丽': 1800, '汤姆': 1900, '萨拉': 1850, '杰里': 2000, '杰克': 1950}
print(process_salary(person_info))