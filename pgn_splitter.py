from os import chdir, getcwd, path, mkdir

try:
    dir=input('enter directory : ')
    chdir(dir)
    fileName=input('filename : ')
    fileName.endswith('.pgn')
    path.exists(fileName)
    
except:
    print('Directory not Found')
    exit()

counter=0
file_counter=1
pgn=''

def write_pgn(player,name,pgn):
    playerfile=player.replace('.pgn','PGNs')
    try:
        mkdir(playerfile) 
    except OSError as error: 
        print('in Progress')  
    file=open(playerfile+'\\'+name+'.pgn','w')
    file.write(pgn)
    file.close()
    return 0

with open(fileName) as f:
    lines=f.readlines()
    for l in lines:
        if l=='\n':
            counter +=1
        else:
            pgn+=l
        if counter % 2 == 0 and counter != 0:
            write_pgn(fileName,str(file_counter),pgn)
            file_counter+=1
            pgn=''
            counter=0
print('Please make sure to copy last PGN manually as it is a bug in this version.')
            
