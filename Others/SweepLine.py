from queue import PriorityQueue
from RedBlackBST import LLRB

class Segment:
    def __init__(self, x1, y1, x2, y2):
        assert(x1==x2 or y1==y2) # Accept either a horizontal or vertical segment  
        assert(not (x1==x2 and y1==y2)) # Two end points cannot be equal              

        # Put smaller values in (x1,y1) and larger values in (x2,y2)
        if x1==x2:            
            if y1<y2: self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
            else: self.x1, self.y1, self.x2, self.y2 = x1, y2, x2, y1
        elif y1==y2:
            if x1<x2: self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
            else: self.x1, self.y1, self.x2, self.y2 = x2, y1, x1, y2
    
    def isHorizontal(self):
        return self.y1 == self.y2

    def isVertical(self):
        return self.x1 == self.x2

    # Create a human-readable string representation
    def __str__(self):
        return f"({self.x1},{self.y1})--({self.x2},{self.y2})"

    def __repr__(self): # Called when a Segment is printed as an element of a list
        return self.__str__()

    # Defines behavior for the equality operator, ==
    # This operator is required for grading
    def __eq__(self, other):
        if other == None: return False
        if not isinstance(other, Segment): return False        
        return self.x1 == other.x1 and self.y1 == other.y1 and self.x2 == other.x2 and self.y2 == other.y2

'''
segments: list of Segment objects
return value: list of Segment pairs that intersect
'''
def sweepLine(segments):
    pq = PriorityQueue()
    result = []
    RB = LLRB()

    for segment in segments:
        #x1과 x2에 따라서 오름차순 정렬을 한 우선순위큐를 생성한다.
        pq.put((segment.x1, segment))
        pq.put((segment.x2, segment))

    while pq.qsize() != 0:
        x, segment = pq.get()
      
        #가로 선의 시작 점일 경우, RB트리에 넣어준다.
        if Segment.isHorizontal(segment) and x == segment.x1:
            RB.put(segment.y1, segment)
          
        #가로 선의 끝 점일 경우, 모두 탐색을 끝낸 것이기 때문에 RB트리에서 제거한다.
        elif Segment.isHorizontal(segment) and x == segment.x2:
            RB.delete(segment.y1)
          
        #세로 선일 경우, 가로 선과 겹치는 점을 탐색해야 한다.
        elif Segment.isVertical(segment):
            #우선순위 큐에 삽입할 때, x좌표를 두 번 넣어주었는데, 세로 선은 두 개가 모두 동일하므로 get()을 한번 더 실행한다.
            pq.get()
          
            #세로 선의 y좌표 사이의 값들이 교차점이므로 이를 찾아준다.
            values = RB.rangeSearch(segment.y1, segment.y2)
            for v in values:
                answer = (RB.get(v), segment)
                result.append(answer)

    return result

def correctnessTest(func, input, expected_output, correct):
    print(f"{func.__name__}({input})")
    output = func(input)
    print(f"output:{output}")
    if output is not None and isinstance(output, list):
        if expected_output == output: print("Pass")
        else:    
            print(f"Fail - the output does not match the expected output {expected_output}")
            correct = False                        
    else:
        print(f"Fail - output is NOT a list")
        correct = False
    print()    

    return correct

#test case
if __name__ == "__main__":
    '''
    Unit Test
    '''    
    print("Correctness test for sweepLine()")
    print("For each test case, if your answer does not appear within 5 seconds, then consider that you failed the case")
    print()
    correct = True

    input = [Segment(0,1,15,1), Segment(1,4,8,4), Segment(3,8,11,8), Segment(9,6,16,6)]
    expected_output = []
    correct = correctnessTest(sweepLine, input, expected_output, correct)

    input = [Segment(-8,0,8,0), Segment(-7,-1,-7,8), Segment(-6,-2,-6,5), Segment(0,1,0,-10), Segment(5,-3,5,10)]
    expected_output = [(Segment(-8,0,8,0), Segment(-7,-1,-7,8)), (Segment(-8,0,8,0), Segment(-6,-2,-6,5)),\
                       (Segment(-8,0,8,0), Segment(0,-10,0,1)), (Segment(-8,0,8,0), Segment(5,-3,5,10))]
    correct = correctnessTest(sweepLine, input, expected_output, correct)

    input = [Segment(3,3,8,3), Segment(4,1,4,8), Segment(7,2,7,10), Segment(1,7,12,7)]
    expected_output = [(Segment(3,3,8,3), Segment(4,1,4,8)), (Segment(1,7,12,7), Segment(4,1,4,8)),\
                       (Segment(3,3,8,3), Segment(7,2,7,10)), (Segment(1,7,12,7), Segment(7,2,7,10))]
    correct = correctnessTest(sweepLine, input, expected_output, correct)

    input = [Segment(0,1,15,1), Segment(14,0,14,2), Segment(1,4,8,4), Segment(6,3,6,7),\
        Segment(2,5,4,5), Segment(3,8,11,8), Segment(9,6,16,6), Segment(13,5.5,13,9.5)]
    expected_output = [(Segment(1,4,8,4), Segment(6,3,6,7)), (Segment(9,6,16,6), Segment(13,5.5,13,9.5)),\
        (Segment(0,1,15,1), Segment(14,0,14,2))]
    correct = correctnessTest(sweepLine, input, expected_output, correct)
   
    input = [Segment(1,3,6,3), Segment(5,0,5,9), Segment(4,7,9,7), Segment(8,6,8,10),\
        Segment(10,4,13,4), Segment(11,2,17,2), Segment(12,1,12,5), Segment(15,5.5,15,7.5), Segment(14,6.5,16,6.5)]
    expected_output = [(Segment(1,3,6,3), Segment(5,0,5,9)), (Segment(4,7,9,7), Segment(5,0,5,9)),\
                       (Segment(4,7,9,7), Segment(8,6,8,10)), (Segment(11,2,17,2), Segment(12,1,12,5)),\
                        (Segment(10,4,13,4), Segment(12,1,12,5)), (Segment(14,6.5,16,6.5), Segment(15,5.5,15,7.5))]
    correct = correctnessTest(sweepLine, input, expected_output, correct)
