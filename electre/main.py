import numpy as np
from info_from_user import Info_from_user
from method_electre import Electre

def main():
    
    user_info = Info_from_user()
    
    user_info.get_criteria_names()  
    user_info.get_alternatives()    
    user_info.get_weights()        
    
    
    matrix = user_info.matrix
    electre_method = Electre(matrix)
    electre_method.get_normalize_matrix()
    electre_method.apply_weights(user_info.weights)
    electre_method.get_concordance_matrix(user_info.weights)
    electre_method.get_discordance_matrix(user_info.weights)
    electre_method.get_dominance_matrix()
    electre_method.get_the_best_alt(user_info.alternatives)


if __name__ == '__main__':
    main()
    