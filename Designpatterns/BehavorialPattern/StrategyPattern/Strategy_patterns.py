# Python Code (Strategy Pattern – Robot Example)
# --- Strategy Interface for Walk ---
class WalkableRobot:
    def walk(self):
        raise NotImplementedError


# --- Concrete Walk Strategies ---
class NormalWalk(WalkableRobot):
    def walk(self):
        print("Walking normally...")


class NoWalk(WalkableRobot):
    def walk(self):
        print("Cannot walk.")


# --- Strategy Interface for Talk ---
class TalkableRobot:
    def talk(self):
        raise NotImplementedError


# --- Concrete Talk Strategies ---
class NormalTalk(TalkableRobot):
    def talk(self):
        print("Talking normally...")


class NoTalk(TalkableRobot):
    def talk(self):
        print("Cannot talk.")


# --- Strategy Interface for Fly ---
class FlyableRobot:
    def fly(self):
        raise NotImplementedError


# --- Concrete Fly Strategies ---
class NormalFly(FlyableRobot):
    def fly(self):
        print("Flying normally...")


class NoFly(FlyableRobot):
    def fly(self):
        print("Cannot fly.")


# --- Robot Base Class ---
class Robot:
    def __init__(self, walk_behavior, talk_behavior, fly_behavior):
        self.walk_behavior = walk_behavior
        self.talk_behavior = talk_behavior
        self.fly_behavior = fly_behavior

    def walk(self):
        self.walk_behavior.walk()

    def talk(self):
        self.talk_behavior.talk()

    def fly(self):
        self.fly_behavior.fly()

    def projection(self):
        raise NotImplementedError


# --- Concrete Robot Types ---
class CompanionRobot(Robot):
    def projection(self):
        print("Displaying friendly companion features...")


class WorkerRobot(Robot):
    def projection(self):
        print("Displaying worker efficiency stats...")


# --- Main / Client Code ---
if __name__ == "__main__":
    robot1 = CompanionRobot(
        NormalWalk(),
        NormalTalk(),
        NoFly()
    )

    robot1.walk()
    robot1.talk()
    robot1.fly()
    robot1.projection()

    print("--------------------")

    robot2 = WorkerRobot(
        NoWalk(),
        NoTalk(),
        NormalFly()
    )

    robot2.walk()
    robot2.talk()
    robot2.fly()
    robot2.projection()

# 🧠 Paragraph Explanation (Simple, Interview-Friendly)

# This code uses the Strategy Design Pattern.
# The main idea of the Strategy Pattern is that behavior should be separated from the main class and selected at runtime. Here, walking, talking, and flying are treated as separate strategies, not hard-coded inside the Robot class. Each behavior has its own interface (WalkableRobot, TalkableRobot, FlyableRobot) and multiple implementations like NormalWalk, NoWalk, NormalTalk, etc.

# The Robot class does not know how walking, talking, or flying happens. It only knows that these behaviors exist and can be called. Different robots (CompanionRobot and WorkerRobot) are created by injecting different behavior objects. This makes the design flexible, easy to extend, and follows Open-Closed Principle because new behaviors can be added without changing existing robot code. In short, behavior changes without modifying the robot class — only the strategy changes.

# 🎯 One-Line Inter An

# “The Strategy Pattern allows us to define a family of behaviors, encapsulate them, and make them interchangeable at runtime without modifying the main class.”