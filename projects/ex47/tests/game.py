class Room(object):

    def __init(self, name, description):
        self.name = name
        self.description = description
        selt.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        self.paths.update(paths)
