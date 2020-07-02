print("A 기업의 달력 제품 광고비에 따른 판매액")

base = 2
print('%c = %d%c + %d' % ('y', base, 'x', base * 2))

ad = "광고비"
sell = "판매액"
unit = "만원"
seed = 2
income = 2 * seed + 4
print(f"\t{ad}를 {seed}{unit} 사용하면 {sell}은 {income}{unit}이다.")

seed = 4
income = 2 * seed + 4
print(f"\t{ad}를 {seed}{unit} 사용하면 판매액은 \'{income}{unit} 이상\'이라고 예측할 수 있다.")
print("\t{1}이 {income}{2}인 경우 {0}를 {seed}{2} 사용했다고 말할 수 있다.".format(ad, sell, unit, seed = 8, income = 20))

explain = """A 기업에서 판매하는 달력의 월 광고비와 판매금은 다음과 같은 관계를 갖습니다.
판매금(Y) = 2 * 광고비(X) + 4
예를 들어 광고비가 3만원이면 판매금은 10만원이 될 것이고,
반대로 판매금이 16만원이면 광고비는 6만원임을 유추할 수 있습니다."""

print(explain.count('광고비'))
print(explain.find('달력'))
print(explain.index('달력'))
print(explain.replace('판매금', '판매액'))