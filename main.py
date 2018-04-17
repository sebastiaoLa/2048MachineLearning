from selenium import webdriver
from popControl import Population
from constants import PLAYERTOTAL

population = Population()


def fill_inputs(fire):
    inputs = []
    for x in range(1, 5):
        for y in range(1, 5):
            num = 0
            try:
                el = fire.find_element_by_class_name(
                    'tile-position-{}-{}'.format(x, y))
                num = int(el.text)
            except Exception as e:
                # print e, 'tile-position-{}-{}'.format(x, y)
                pass
            inputs.append(num)
    return inputs


FIRE = webdriver.Firefox()
FIRE.get('https://gabrielecirulli.github.io/2048/')
while True:
    if population.actualPlayer == 0 and population.genCount > 1:
        try:
            el = FIRE.find_element_by_class_name('best-container')
            print ''
            print 'best of gen: ', el.text
            print ''
            FIRE.close()
            FIRE = webdriver.Firefox()
            FIRE.get('https://gabrielecirulli.github.io/2048/')
        except:
            pass

    el = FIRE.find_element_by_tag_name("body")
    end = False
    inputs = []
    tries = 0
    while not end:
        old_inputs = list(inputs)
        inputs = fill_inputs(FIRE)
        while sum(inputs) == 0:
            print 'get again'
            inputs = fill_inputs(FIRE)
        if old_inputs == inputs and old_inputs != []:
            tries += 1
            if tries > 3:
                end = True
        el.send_keys(population.play(inputs))
        try:
            aux = FIRE.find_element_by_class_name("game-over")
            end = True
        except:
            pass
    while True:
        try:
            score = int(FIRE.find_element_by_class_name(
                'score-container').text)
            break
        except:
            pass

    print ''
    print 'actual player: ', population.actualPlayer+1
    print 'player fitness: ', score*max(inputs)
    print 'actual gen: ', population.genCount
    population.set_fitness(score*max(inputs))
    FIRE.find_element_by_class_name('restart-button').click()
