def main():
    obj1 = Singleton.get_instance()
    print(obj1)
    obj2 = Singleton.get_instance()
    print(obj2)
    print(obj1 == obj2)

class Singleton:
    __instance = None
    def __init__(self):
        print('Start.')
        print('インスタンスを生成しました')
        if Singleton.__instance is not None:
            raise Exception('obj1とob2は同じインスタンスではありません。')
        else:
            print('obj1とobj2は同じインスタンスです。')
            Singleton.__instance = self

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()

        return Singleton.__instance

if __name__ == '__main__':
    main()
