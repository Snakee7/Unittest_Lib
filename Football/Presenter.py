import View
import Model
	
class Presenter:
    def __init__(self):
        self._model = Model.Model()
        self._view = View.View(self)

    def GetCoverImage(self, name):
        return self._model.getImage(name)

    def getAlbums(self):
        return self._model.getAlbumsSQL()

    def getTrackList(self, album_title):
        return self._model.getTrackListSQL(album_title)

