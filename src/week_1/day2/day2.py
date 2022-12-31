def find_nemo(phase):
    try:
        word_find = "Nemo"
        phase = phase.split(" ")
        index = phase.index(word_find)
        position_Nemo = index + 1
    except:
        return 'Nemo is not in list'
        
    return f'I found Nemo at {position_Nemo}!'
