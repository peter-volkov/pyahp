import itertools 
import numpy

#http://mi.boku.ac.at/ahp/ahptutorial.pdf

class AHP:

    def __init__(self):
        self.PRECISION = 0.015
    
    def get_list_from_user(self):
        user_specified_list = []
        while True:        
            print('Input {0}'.format(len(user_specified_list)))
            user_input = raw_input()

            if not user_input:
                break

            user_specified_list.append(user_input)
                     
        return user_specified_list

    def compare_pairwise(self, data_list):
        
        #Generate criteria importance matrix
        matrix_size = len(data_list) 
        matrix = [[0]*matrix_size for i in range(matrix_size)]
               
        #Fill main diagonal
        for i in range(matrix_size):
            matrix[i][i] = 1

        for elem1, elem2 in itertools.combinations(data_list, 2):
            print('Intput {0} / {1} relative importance'.format(elem1, elem2))
            m, n = criteria_list.index(elem1), criteria_list.index(elem2)
           
            relation = float(raw_input())                
            matrix[m][n] = relation
            matrix[n][m] = 1 / relation                 
            
        return numpy.matrix(matrix)

    def get_eigenvector(self, matrix):                              
        
        rows_sums = [] 
 
        for vector in matrix.tolist():
            rows_sums.append(sum(vector))
                   
        rows_sums_sum = sum(rows_sums)
        normalize = lambda elem: elem / rows_sums_sum
        normalized_vector = map(normalize, rows_sums)
   
        return normalized_vector


    def iterate_normalization(self, matrix):
        matrix *= matrix
        print('Squared criteria importance matrix:')
        print(matrix)
        
        eigenvector = self.get_eigenvector(matrix)
        print('First eigenvector:')
        print(eigenvector)
        
        
        #Iterate until specified precision is satisfied
        while True:                        
            
            matrix *= matrix    
                        
            new_eigenvector = self.get_eigenvector(matrix)            
            eigenvectors_diff = [abs(elem - new_eigenvector[i]) for i, elem in enumerate(eigenvector)]
            print('Eigenvector diff {0}\n'.format(eigenvectors_diff))
            current_precision = max(eigenvectors_diff)            
            print('Iterate  step. Precision = {0}. \nNew eigenvector = {1}'.format(current_precision, new_eigenvector))            
            print(matrix)                      
            
            if current_precision < self.PRECISION:
                break

        return new_eigenvector         
            
       
if __name__ == '__main__':    
    ahp = AHP()
    
    #print('Input criteria:')
    #criteria_list = ahp.get_list_from_user()
    criteria_list = ['style', 'reliability', 'fuel economy']

    #matrix = ahp.compare_pairwise(criteria_list)
    matrix = numpy.matrix([[1, 0.5, 3],[2, 1, 4], [0.3333, 0.25, 1]])    
    print('Criteria importance matrix:')
    print(matrix)
        
    criteria_precise_eigenvector = ahp.iterate_normalization(matrix)              
    print('Criteria weights:')     
    criteria_weights = zip(criteria_list, criteria_precise_eigenvector)
    for elem in criteria_weights:
        print(elem)
        
    #print('Input alternatives:')
    #alternatives_list = ahp.get_list_from_user()
    alternatives_list = ['civic', 'saturn', 'escort', 'cilo']
    
    criteria_alternatives_matrix_dict = {}
    alternatives_eigenvectors = []
    
    #for criterion in criteria_list:
        #matrix = ahp.compare_pairwise(alternatives_list)
        #criteria_alternatives_matrix_dict[criterion] = matrix
    
    criteria_alternatives_matrix_dict['reliability'] = numpy.matrix([[1, 0.25, 4, 0.1666],[4, 1, 4, 0.25], [0.25, 0.25, 1, 0.2], [6, 4, 5, 1]]) 
    criteria_alternatives_matrix_dict['style'] = numpy.matrix([[1, 0.25, 4, 0.1666],[4, 1, 4, 0.25], [0.25, 0.25, 1, 0.2], [6, 4, 5, 1]]) 
    criteria_alternatives_matrix_dict['fuel economy'] = numpy.matrix([[1, 0.25, 4, 0.1666],[4, 1, 4, 0.25], [0.25, 0.25, 1, 0.2], [6, 4, 5, 1]]) 

    for criterion in criteria_list:
        precise_eigenvector = ahp.iterate_normalization(criteria_alternatives_matrix_dict[criterion])
        alternatives_eigenvectors.append(precise_eigenvector)
 
    alternatives_eigenvectors_matrix = numpy.matrix(alternatives_eigenvectors)

    alternatives_eigenvectors_matrix = [
                                         [ 0.1160,  0.2470,  0.0600, 0.5770],
                                         [ 0.3790,  0.2900,  0.0740, 0.2570],
                                         [ 0.3010,  0.2390,  0.2120, 0.2480]
                                       ]

    alternatives_eigenvectors_matrix = numpy.matrix(alternatives_eigenvectors_matrix).transpose()
    print('Alternatives eigenvectors matrix:')
    print(alternatives_eigenvectors_matrix)
    print('Criteria precise eigenvector:')
    print(criteria_precise_eigenvector)

    ranks = alternatives_eigenvectors_matrix * numpy.matrix(criteria_precise_eigenvector).transpose()


    ranks = map(lambda x: x[0], ranks.tolist())
    result = zip(alternatives_list, ranks)


    chart = sorted(result, key=lambda x: x[1], reverse=True)
    print('best choice: {0}'.format(chart[0][0]))
    print('ranks:')
    for elem in chart:    
        print(elem)

