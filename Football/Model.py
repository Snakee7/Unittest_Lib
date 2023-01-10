import sqlite3

class Model:
    _connect = None
    _cursor = None
	
    def __init__(self):
        self._connect = sqlite3.connect('DataFootball.db')
        self._cursor = self._connect.cursor()

    def getTrackListSQL(self, album_title):
        table = [["ID", "Имя", "Фамилия"]]
        sql = '''
SELECT 
    Players.ID,
    Players.Name,
    Players.Surname
FROM Players INNER JOIN Commands
ON Players.ID_Commands = Commands.ID
WHERE Commands.Title = ?;
'''
        for row in self._cursor.execute(sql, [album_title]):
            line = []
            for colum in row:
                line.append(colum)
            table.append(line)
        
        return table

    def getAlbumsSQL(self):
        table = []
        for row in self._cursor.execute("SELECT Title FROM Commands;"):
            line = ''
            for colum in row:
                line += colum
            table.append(line)
        	
        return table

    def getImage(self, name):
        return 'image//' + name + '.jpg'
