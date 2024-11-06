class Snake:
    def __init__(self):
        self.position = [(1, 1), (1, 2)]

    def move(self, direction):
        self.position.pop()


    




snake = Snake()






class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.board = [[0 for x in range(width)] for y in range(height)]


    def render(self):
        output = '+'
        output += '-'*self.width
        output += '+\n'
        for row in range(self.height):
            output += '|'
            for column in range(self.width):
                if (row, column) == snake.position[0]:
                    output += 'X'
                elif (row, column) in snake.position:
                    output += 'O'
                else:
                    output += ' '
            output += '|\n'
        output += '+'
        output += '-'*self.width
        output += '+'
        print(output)
        

game = Game(15, 40)
game.render()