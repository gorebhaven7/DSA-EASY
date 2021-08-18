
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:        
        count = 0
        while count < len(students) :
            if len(students) == 0:
                break
            
            else:
                if students[0] == sandwiches[0]:
                    count = 0
                    students.pop(0)
                    sandwiches.pop(0)
                else:
                    count += 1
                    students.append(students.pop(0))
                    
        return len(students)
