class Game(object):

    # 类属性记录历史最高分
    top_score = 0

    # 初始化方法中定义实例属性，用实例属性记录当前玩家的姓名
    def __init__(self, player_name):
        self.player_name = player_name

    # 定义静态方法
    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门")

    # 定义类方法
    @classmethod
    def show_top_score(cls):
        print("历史记录%d" % cls.top_score)

    # 定义实例方法
    def start_game(self):
        print("%s开始游戏啦。。" % self.player_name)


# 1. 查看游戏的帮助信息 通过类名.调用静态方法
Game.show_help()
# 2. 查看历史最高分 通过类名.调用类方法
Game.show_top_score()
# 3. 创建游戏对象
game = Game("小明")
# 通过对象的实例调用实例方法
game.start_game()
