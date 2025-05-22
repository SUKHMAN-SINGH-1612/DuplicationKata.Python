from kata.Song import Song


class Lesson2Variable(Song):
    def sing_beer_song(self):
        def beer():
            for i in range (100,98,-1):
                self.sing(f"{i} bottles of beer on the wall")
                self.sing(f"{i} bottles of beer")
                self.sing("Take one down, pass it around")
                self.sing(f"{i-1} bottles of beer on the wall")
        beer()