class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        c = 0
        while len(students)>0 and c<n*n:
            if students[0] == sandwiches[0]:
                del students[0]
                del sandwiches[0]
            else: 
                
                fi = students.pop(0)
                students.append(fi)
            c+=1

        return len(students)

        
        