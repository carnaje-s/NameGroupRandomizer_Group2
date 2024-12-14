import random
 
class RandomizerBase:             
    def __init__(self, items):    
        self.items = items

    def validate_items(self):    
        if not self.items:
            raise ValueError("No names provided!")  
        for item in self.items:
            if ',' not in item:
                raise ValueError("Names must be separated by commas.")

class GroupRandomizer(RandomizerBase): 
    def __init__(self, items):        
        super().__init__(items)

    def create_groups(self, num_groups):   
        self.validate_items()              
        if num_groups <= 0 or num_groups > len(self.items): 
            raise ValueError("Invalid number of groups!")   

        random.shuffle(self.items)

        groups = {f"Group {i + 1}": [] for i in range(num_groups)} 
        for i, name in enumerate(self.items):                      
            groups[f"Group {(i % num_groups) + 1}"].append(name)

        return groups

    def pick_random_name(self):          
        self.validate_items()            
        return random.choice(self.items) 