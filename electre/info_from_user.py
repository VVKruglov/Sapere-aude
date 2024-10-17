import numpy as np

class Info_from_user:
    
    def get_criteria_names(self):
        size_criteria_names = int(input(f'Введите количестов критериев: '))
        criteria_names = []
        
        for i in range(size_criteria_names):
            name = input(f'Введите название критерия {i+1}: ')
            criteria_names.append(name)
        
        self.size_criteria_names = size_criteria_names
        self.criteria_names = criteria_names
    
    
    def get_alternatives(self):
        
        size_goods = int(input(f'Введите количество альтернатив: '))
        alternatives = []
        
        for i in range(size_goods):
            print(f'\nЗаполните критерии для альтернативы {i+1}')
            alt = [int(input(f'{self.criteria_names[j]} = ')) for j in range(self.size_criteria_names)]
            alternatives.append(alt)
        
        self.size_goods = size_goods
        self.alternatives = alternatives
  
    
    def get_weights(self):
         while True:
            print('\nВведите веса для каждого критерия от 0 до 1. Чем больше вес, тем значимее критерий. Сумма весов должна быть равна 1')
            weights = [float(input(f'{name} = ')) for name in self.criteria_names]
            weights = np.array(weights)
            
            if any(w < 0 or w > 1 for w in weights):
                print('Весы введены не корректно. Повторите ввод')
                continue
            if not np.isclose(np.sum(weights), 1.0):
                print('Сумма весов не равна 1. Введите значения снова')
                continue
            
            self.weights = weights
            break
    
    
    
    def criteria_names(self):
        return self.criteria_names
    
    
    def alternatives(self):
        return self.alternatives
    
    
    def weights(self):
        return self.weights
    
    
    def matrix(self):
        np_alternatives = np.array(self.alternatives)
        matrix = np_alternatives.reshape(self.size_goods, self.size_criteria_names)
        return matrix