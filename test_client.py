import smor.client as sm

sm.config('localhost')
sm.put('A', 1)
sm.put('A', 2)
print('got:', sm.get_one('A'))
sm.put('A', 3)
print('got:', sm.get_all('A'))
sm.put('A', 4)
print('got:', sm.get_all('A'))
print('got:', sm.get_all('A'))