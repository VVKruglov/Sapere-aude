import numpy as np


class Electre:
    
    def __init__(self, matrix): 
        self.matrix = matrix()
        print(self.matrix)
       
       
    def get_rows(self):
        num_rows = self.matrix.shape[0]
        return num_rows
    
  
    def get_cols(self):
        num_cols = self.matrix.shape[1]
        return num_cols
    
    def get_normalize_matrix(self):
        
        num_cols = self.get_cols()
        new_matrix = np.zeros_like(self.matrix, dtype= float)
        
        # Нормализация матрицы 
        for j in range(num_cols):
            sum_of_squares = np.sum(self.matrix[:, j] ** 2)
            norm_factor = np.sqrt(sum_of_squares)
            new_matrix[:, j] = self.matrix[:, j] / norm_factor
           
        self.new_matrix = new_matrix
        
    
    def apply_weights(self, weights):
        
        num_cols = self.get_cols()
        weights_matrix = np.zeros_like(self.new_matrix, dtype= float)

        # Умножаем значения критериев на их вес
        for j in range(num_cols):
            weights_matrix[:, j] = self.new_matrix[:, j] * weights[j]
        
        self.weights_matrix = weights_matrix
        
    #Вычисляется матрица согласия
    def get_concordance_matrix(self, weights):
        num_rows = self.get_rows()
        num_cols = self.get_cols()
        matrix_concord = np.zeros((num_rows, num_rows))
        
        for i in range(num_rows):
            for j in range(num_rows):
                if i!=j:
                    concord_criteria = []
                    for k in range(num_cols):
                        if self.weights_matrix[i, k] >= self.weights_matrix[j, k]:
                            concord_criteria.append(weights[k])   
                    matrix_concord[i, j] = sum(concord_criteria)
    
        print('Матрица согласия')
        print(matrix_concord)
        self.matrix_concord = matrix_concord
    
    def get_discordance_matrix(self, weight):
        num_rows = self.get_rows()
        num_cols = self.get_cols()
        matrix_discord = np.zeros((num_rows, num_rows))
        
        for i in range(num_rows):
            for j in range(num_rows):
                if i!=j:
                    discord_criteria = []
                    for k in range(num_cols):
                        discord_criteria.append(abs(self.weights_matrix[i, k] - self.weights_matrix[j, k]))
                    matrix_discord[i, j] = max(discord_criteria)
        
        print('Матрица несогласия')
        print(matrix_discord)
        self.matrix_discord = matrix_discord
    
    
    def get_dominance_matrix(self, concord_treshold = 0.5, discord_threshold = 0.3):
        num_rows = self.get_rows()
        matrix_dominance = np.zeros((num_rows, num_rows))
        
        for i in range(num_rows):
            for j in range(num_rows):
                if i!=j:
                    if self.matrix_concord[i, j] >= concord_treshold and self.matrix_discord[i, j] <= discord_threshold:
                        matrix_dominance[i, j] = 1
        
        print(matrix_dominance)
        self.matrix_dominance = matrix_dominance
        
        
    def get_the_best_alt(self, alternatives):
        dominant_values = np.sum(self.matrix_dominance, axis=1)

        best_alternative = np.argmax(dominant_values)
        print(f"\nНаилучшая альтернатива: {best_alternative + 1}")