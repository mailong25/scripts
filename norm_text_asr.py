def norm_expand(text, special = 'remove', hesitation = 'remove'):
    
    hesitations = set(['uh', 'mhm', 'mm', 'hm', 'ooh', 'hmm', 'hmo', 'heh', 'uhuh', 'ah',
                   'mmm', 'eee', 'hoo', 'noone', 'mnh' 'umm', 'nn', 'hume', 'umhum', 'oh', 
                   'oooh', 'mh', 'hmmm', 'nuh', 'uhh', 'mmmmm', 'hun', 'um', 'yeah', 'eh'
                   'hmh', 'uhhh', 'mn', 'uhm', 'hhmm', 'huhh', 'nm', 'oh', 
                   'ya', 'yup', 'yeah', 'huh', 'yo', 'la', 'yay', 'yah', 'uhhuh', 'ye',
                    'um', 'uh', 'mhm', 'huh', 'mm', 'hum', 'hm', 'eh', 'hmm', 'heh', 'mmm',
                    'mnh', 'umm', 'uhuh', 'umhum', 'mh', 'nuh', 'uhh', 'uuh', 'ooh',
                    'mmmmm', 'nunn', 'meh', 'uhh', 'mmmmm', 'noooo', 'hmh',
                    'uhhh', 'hmh', 'uhhh', 'mn', 'uhm', 'hhmm', 'huhh', 'nm',
                    'yep', 'ya', 'yay', 'yea', 'yap', 'yeee', 'wow'])
    
    if hesitation == 'remove':
        words = text.split()
        words = [w for w in words if w not in hesitations]
        text = ' '.join(words)
    elif hesitation != 'keep':
        raise ValueError("hesitation params must belong [remove,keep]")
    
    text = ' ' + text + ' '
    text = text.replace(" ok ",' okay ')
    text = text.replace(" o k ",' okay ')
    text = text.replace("'ve ",' have ')
    text = text.replace("'re ",' are ')
    text = text.replace("'m ",' am ')
    text = text.replace("n't ",'nooot ')
    text = text.replace("'d ",' would ')
    text = text.replace("'ll ",' will ')
    text = text.replace("'cause ",' because ')
    text = text.replace(" o'"," o")
    text = text.replace("let's",'lets')
    
    expands = ['it','she','he','that','there','this','what',
               'why','how','where','when','here','who']
    for w in expands:
        text = text.replace(w + "'s ", w + " is ")
    
    text = text.replace("' ",' ')
    text = text.replace("'s ",' ')
    
    if special == 'none':
        if not text.replace(' ','').isalpha():
            return None
        else:
            return ' '.join(text.split()).replace('nooot',"n't")
    elif special == 'keep':
        return ' '.join(text.split()).replace('nooot',"n't")
    elif special == 'remove':
        words = text.split()
        words = [w for w in words if w.isalpha()]
        return ' '.join(words).replace('nooot',"n't")
    else:
        raise ValueError("special params must belong [none,keep,ignore]")
        
norm_expand("test it's test", 'none')
