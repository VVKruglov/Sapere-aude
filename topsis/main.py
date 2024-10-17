import numpy as np
from info_user import Info_from_user  
from method_topsis import Topsis               

def main():
    
    user_info = Info_from_user()
    
    user_info.get_criteria_names()  
    user_info.get_alternatives()    
    user_info.get_weights()        
    
    
    matrix = user_info.matrix
    topsis_method = Topsis(matrix)
    topsis_method.get_normalize_matrix()
    topsis_method.apply_weights(user_info.weights)
    topsis_method.calculate_ideal_and_antiideal()
    topsis_method.calculate_distances()
    topsis_method.calculate_relative_closeness()
    topsis_method.show_result()

if __name__ == '__main__':
    main()