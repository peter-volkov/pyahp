import unittest 
import numpy

import ahp

#http://mi.boku.ac.at/ahp/ahptutorial.pdf

class TestAHP(unittest.TestCase):

    ahp = ahp.AHP()
    
    def test_get_eigenvector(self):            

        matrix = numpy.matrix([[1, 0.5, 3],[2, 1, 4], [0.3333, 0.25, 1]])    
        matrix *= matrix
        correct_eigenvector = [0.3194162778317101, 0.5595014561738639, 0.12108226599442581]
       
        self.assertEqual(self.ahp.get_eigenvector(matrix), correct_eigenvector)

    def test_iterate_normalization(self):

        matrix = numpy.matrix([[1, 0.5, 3],[2, 1, 4], [0.3333, 0.25, 1]])    
        correct_eigenvector = [0.3196209815589706, 0.5584197045119852, 0.12195931392904427]
       
        self.assertEqual(self.ahp.iterate_normalization(matrix), correct_eigenvector)

    def test_result(self):

        criteria_list = ['style', 'reliability', 'fuel economy']

        alternatives_list = ['civic', 'saturn', 'escort', 'cilo']
        criteria_alternatives_matrix_dict = {}
        criteria_alternatives_matrix_dict['reliability'] = numpy.matrix([[1, 0.25, 4, 0.1666],[4, 1, 4, 0.25], [0.25, 0.25, 1, 0.2], [6, 4, 5, 1]]) 
        criteria_alternatives_matrix_dict['style'] = numpy.matrix([[1, 0.25, 4, 0.1666],[4, 1, 4, 0.25], [0.25, 0.25, 1, 0.2], [6, 4, 5, 1]]) 
        criteria_alternatives_matrix_dict['fuel economy'] = numpy.matrix([[1, 0.25, 4, 0.1666],[4, 1, 4, 0.25], [0.25, 0.25, 1, 0.2], [6, 4, 5, 1]]) 

        alternatives_eigenvectors_matrix = [
                                            [ 0.1160,  0.2470,  0.0600, 0.5770],
                                            [ 0.3790,  0.2900,  0.0740, 0.2570],
                                            [ 0.3010,  0.2390,  0.2120, 0.2480]
                                           ]

        self.assertTrue(True)
                   
if __name__ == '__main__':    
    unittest.main()
