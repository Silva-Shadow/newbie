def printBoard(chilli):
    print(chilli['topl'] + '|' + chilli['topm'] + '|' + chilli['topr'])
    print('------')
    print(chilli['midl'] + '|' + chilli['midm'] + '|'+ chilli['midr'])
    print('------')
    print(chilli['lowl'] + '|' + chilli['lowm'] + '|' + chilli['lowr'])
    
    
theBoard = {'topl':' ','topm':' ','topr':' ', 'midl':' ', 'midm':' ', 'midr':' ', 'lowl':' ', 'lowm' :' ', 'lowr':' '} 


printBoard(theBoard)