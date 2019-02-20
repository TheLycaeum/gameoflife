import gameoflife as gol


def test_get_live_neighbours():
    #lastrow
    assert  gol.get_live_neighbours([[True,False,True,False],
                                 [True,False,False,True],
                                 [True,False,False,False],
                                 [True,False,True,True]], [3,2]) == 1
    #bottom right
    assert  gol.get_live_neighbours([[True,False,True,False],
                                 [True,False,False,True],
                                 [True,False,False,False],
                                 [True,False,True,True]], [3,3]) == 1
    #topleft
    assert  gol.get_live_neighbours([[True,False,True,False],
                                 [True,False,False,True],
                                 [True,False,False,False],
                                 [True,False,True,True]], [0,0]) == 1
    #topright
    assert  gol.get_live_neighbours([[True,False,True,False],
                                 [True,False,False,True],
                                 [True,False,False,False],
                                 [True,False,True,True]], [0,3]) == 2
    assert  gol.get_live_neighbours([[True,False,True,False],
                                 [True,False,False,True],
                                 [True,False,False,False],
                                 [True,False,True,True]], [1,1]) == 2

def test_update_state():
    assert  gol.update_state([[False,False,True,False],
                                 [False,False,True,False],
                                 [False,False,True,False],
                                 [False,False,False,False]]) == [[False,False,False,False],
                                                                 [False,True,True,True],
                                                                 [False,False,False,False],
                                                                 [False,False,False,False]]

