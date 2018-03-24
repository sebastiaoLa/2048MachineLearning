from selenium import webdriver
from popControl import Population
from constants import PLAYERTOTAL

fire = webdriver.Firefox()

population  = Population()

while True:
    fire.get('https://gabrielecirulli.github.io/2048/')
    el = fire.find_element_by_tag_name("body")
    end = False
    while not end:
        el.send_keys(population.play())
        try:
            aux = fire.find_element_by_class_name("game-over")
            end = True
        except:
            pass
    while True:
        try:
            score = int(fire.find_element_by_class_name('score-container').text)
            break
        except:
            pass
    score2 = 0
    modifier = 1
    for i in fire.find_elements_by_class_name('tile-inner'):
        try:
            score2 = int(i.text)
            if score2>=128:
                modifier = modifier * {128:2,256:4,512:6,1024:8,2048:10}[score2]
                print modifier
                if score2 == 2048:
                    raise Exception('done')
            else:
                modifier *= 1
        except:
            pass
    
    print ''
    print 'actual player: ',population.actualPlayer+1
    print 'player fitness: ',score
    print 'player modifier: ',modifier
    print 'actual gen: ',population.genCount
    population.set_fitness(score,modifier)
    