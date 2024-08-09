from point import Point

def bound_instance_method():
    """
    bound instance method: 인스턴스 직접 바인딩 된 메서드
    """
    p = Point() # Point 인스턴스 생성
    p.setX(10)
    p.setY(20)

    print(p.getX(), p.getX(), sep=",")
    print(p.getX, p.getY)

def unbound_instance_method():
    """
    unbound instance method:
    클래스 메서드에 인스턴스 참조주소를 전달하고 우회 접근 법
    인스턴스 메서드의 첫번째 인자가 self인 이유이다.
    """
    p = Point()
    Point.setX(p, 10)
    Point.setY(p, 20)
    print(Point.getX(p), Point.getY(p))
    print(Point.getX, Point.getY)

def class_member_test():
    p1 = Point()
    p1.setX(10)
    p1.setY(20)
    print(p1.getX(), p1.getY(), p1.instance_count)
    # p1.instance_count는 클래스 멤버(인스턴스 멤버 아님)

    p2 = Point()
    p1.setX(20)
    p1.setY(30)
    print(p2.getX(), p2.getY(), p2.instance_count)
    # p2.instance_count는 클래스멤버

    print(p1.x is p2.x)
    print(p1.instance_count is p2.instance_count)





if __name__ == "__main__":
    # bound_instance_method()
    # unbound_instance_method()
    class_member_test()