import numpy as np

class Topsis:
    
    def __init__(self, matrix):
        self.matrix = matrix()
        print('\nИзначальная матрица')
        print(self.matrix)
    
    
    def get_rows(self):
        num_rows = self.matrix.shape[0]
        return num_rows
    
    def get_col(self):
        num_col = self.matrix.shape[1]
        return num_col
    
    def get_normalize_matrix(self):
        
        num_cols = self.get_col()
        new_matrix = np.zeros_like(self.matrix, dtype= float)
        
        # Нормализация матрицы 
        for j in range(num_cols):
            sum_of_squares = np.sum(self.matrix[:, j] ** 2)
            norm_factor = np.sqrt(sum_of_squares)
            new_matrix[:, j] = self.matrix[:, j] / norm_factor
           
        print('\nНормализованная матрица')
        print(new_matrix)
        self.new_matrix = new_matrix
        
    
    
    def apply_weights(self, weights):
        
        num_cols = self.get_col()
        weights_matrix = np.zeros_like(self.new_matrix, dtype= float)

        # Умножаем значения критериев на их вес
        for j in range(num_cols):
            weights_matrix[:, j] = self.new_matrix[:, j] * weights[j]
        
        print('\nВзвешенная матрица')
        print(weights_matrix)
        self.weights_matrix = weights_matrix
    
    
    def calculate_ideal_and_antiideal(self):
        
        # Определение идеального решения
        num_cols = self.get_col()
        ideal_result = []
        for j in range(num_cols):
            ideal_result.append(max(self.weights_matrix[:, j]))
            
        # Определение антиидеального решения
        anti_ideal_result = []
        for j in range(num_cols):
            anti_ideal_result.append(min(self.weights_matrix[:, j]))
        
        print(f'\nИдеальное решение\n{ideal_result}')
        print(f'\nАнтидеальное решение\n{anti_ideal_result}')
        
        self.ideal_result = ideal_result
        self.anti_ideal_result = anti_ideal_result
    
    
    def calculate_distances(self):
    # Расчет евклидова расстояния до идеального решения
      num_rows = self.get_rows()
      num_cols = self.get_col()
    
      positiv_result = [0] * num_rows
      negativ_result = [0] * num_rows
    
      for i in range(num_rows):
          sum_positiv = 0
          sum_negativ = 0
          for j in range(num_cols):
              sum_positiv += (self.weights_matrix[i, j] - self.ideal_result[j]) ** 2
              sum_negativ += (self.weights_matrix[i, j] - self.anti_ideal_result[j]) ** 2
        
          positiv_result[i] = np.sqrt(sum_positiv)
          negativ_result[i] = np.sqrt(sum_negativ)
    
      self.positiv_result = positiv_result
      self.negativ_result = negativ_result
    
    
    def calculate_relative_closeness(self):
        num_rows = self.get_rows()
        result = np.zeros(num_rows)
        for i in range(num_rows):
            result[i] = self.negativ_result[i] / (self.negativ_result[i] + self.positiv_result[i])
        
        print(f'\nИтоговые значения (относительная близость):\n{result}')
        self.result = result
        
    
    def show_result(self):
        the_best_a = max(self.result)
        for i in range(len(self.result)):
            if self.result[i] == the_best_a:
                print(f"Наиболее подходящий товар для вас - {i+1}")
        
    

           



        