class Point:
    instance_count = 0  # 클래스 멤버
    # 클래스 멤버: 클래스 이름 공간 내에 생성, 모든 인스턴스 객체가 공유
    # 인스턴스 멤버: 인스턴스 공간 내에 생성, 개별 인스턴스 객체 내부에서만 활용
    def setX(self, x):  # 인스턴스 메서드의 첫번째 인자는 항상 self이다
        self.x = x  # 파이썬 특성상 생성될 때 할당된다

    def getX(self,):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y